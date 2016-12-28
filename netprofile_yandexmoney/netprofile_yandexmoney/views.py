#!/usr/bin/env python
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-
#
# NetProfile: Yandex.Money module - Views
# © Copyright 2013-2014 Alex 'Unik' Unigovsky
#
# This file is part of NetProfile.
# NetProfile is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later
# version.
#
# NetProfile is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General
# Public License along with NetProfile. If not, see
# <http://www.gnu.org/licenses/>.

from __future__ import (
	unicode_literals,
	print_function,
	absolute_import,
	division
)

from pyramid.i18n import (
	TranslationStringFactory,
	get_localizer
)

import math
import datetime as dt
from dateutil.parser import parse as dparse
from dateutil.relativedelta import relativedelta

from pyramid.view import view_config
from pyramid.settings import asbool
from pyramid.httpexceptions import (
	HTTPForbidden,
	HTTPSeeOther
)
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
from netprofile import locale_neg

from netprofile_core import global_setting
from netprofile.common.factory import RootFactory
from netprofile.common.hooks import register_hook
from netprofile.db.connection import DBSession
from netprofile_xop.models import (
	ExternalOperation,
	ExternalOperationProvider,
	ExternalOperationState
)
from netprofile_stashes.models import Stash

_ = TranslationStringFactory('netprofile_yandexmoney')


def calc_md5_hash(postdata, shop_pass):
	concat = ';'.join((
			postdata.get('action', ''),
			postdata.get('orderSumAmount', ''),
			postdata.get('orderSumCurrencyPaycash', ''),
			postdata.get('orderSumBankPaycash', ''),
			postdata.get('shopId', ''),
			postdata.get('invoiceId', ''),
			postdata.get('customerNumber', ''),
			shop_pass
			))
	calculated_md5 = hashlib.md5(concat.encode()).hexdigest()
	goal_md5 = postdata.get('md5')
	
	if(goal_md5 is not None and calculated_sha1 == goal_sha1):
		return True
	return False

@view_config(route_name='yandexmoney.cl.neworder', renderer='string')
def ym_new_order(request):
	sess = DBSession()
	providerid = sess.query(ExternalOperationProvider).filter(ExternalOperationProvider.uri=='yandexmoney').first().id
	xop = ExternalOperation(stash_id=request.POST.get('stash', ''), entity=request.user.parent, provider_id=providerid, difference = request.POST.get('diff', ''))
	sess.add(xop)
	sess.flush()
	return xop.id

@view_config(route_name='yandexmoney.cl.checkorder', renderer='netprofile_yandexmoney:templates/ym_checkorder.mak')
def ym_check_order(request):
	"""
	обработчик POST-запросов от YM, которые поступают на
	этот адрес после введения всех данных в платежную форму
	и после ее отправки. здесь же обрабатывается успешный платеж.
	при успешном платеже добавляется запись в базу и происходит пополнение
	счета. в конце редирект на страницу счетов с сообщением о зачислении средств. 
	"""
	loc = get_localizer(request)
	sess = DBSession()
	tpl = {}
	cur_locale = locale_neg(request)
	cfg = request.registry.settings
	shop_pass = global_setting('ym_shoppass')
	sharedsecret = global_setting('ym_sharedsecret')
	errors = {}
	if request.POST:
		request.response.content_type = "text/xml"

		if not calc_md5_hash(request.POST, shop_pass):
			code = 1
		else:
			code = 0

		csrf = request.POST.get('csrf', '')
		diff = request.POST.get('sum', '')
		stashid = request.POST.get('customerNumber', '')
		action = request.POST.get('action', '')
		external_id = request.POST.get('operation_id', '')
		invoiceId = request.POST.get('invoiceId', '')
		shopId = request.POST.get('shopId', '')
		if any(x == '' for x in [csrf, diff, stashid, action, external_id, invoiceId, shopId]):
			code = 4
		if 'xopid' in request.POST:
			xopid = request.POST.get('xopid', '')
			xop = sess.query(ExternalOperation).get(xopid)
		else:
			code = 4
		#проверка заказа
		if action == 'checkOrder':
			if code == 0:
				# OK
				#EXAMPLE <checkOrderResponse performedDatetime="2011-05-04T20:38:01.000+04:00" code="0" invoiceId="1234567" shopId="13"/>
				xop.state = ExternalOperationState.checked
				xop.state = ExternalOperationState.confirmed
				tpl.update({"responseName":'checkOrderResponse',
							"operationDate":datetime.datetime.now(),
							"code":code,
							"invoiceID":invoiceId,
							"shopId":shopId
							})
			if code == 1:
				# WRONG MD5	
				# EXAMPLE <checkOrderResponse performedDatetime="2011-05-04T20:38:01.000+04:00" code="1" invoiceId="1234567" shopId="13" message="Wrong md5" techMessage="Not authorized" />
				tpl.update({"responseName":'checkOrderResponse',
							"operationDate":datetime.datetime.now(),
							"code":code,
							"invoiceID":invoiceId,
							"shopId":shopId,
							"message":'Wrong MD5 value',
							"techMessage":"Not authorized"
							})
				xop.state = ExternalOperationState.cancelled
				
			if code == 3:
				#Something wrong with params
				# EXAMPLE <checkOrderResponse performedDatetime="2011-05-04T20:38:01.000+04:00" code="100" invoiceId="1234567" shopId="13" message="Wrong params, can't accept payment" techMessage="Wrong params" />
				tpl.update({"responseName":'checkOrderResponse',
							"operationDate":datetime.datetime.now(),
							"code":code,
							"invoiceID":invoiceId,
							"shopId":shopId,
							"message":"Wrong parameters, can't accept payment",
							"techMessage":"Parameters error"
							})
				xop.state = ExternalOperationState.cancelled
			else:
				# EXAMPLE <checkOrderResponse performedDatetime="2011-05-04T20:38:01.000+04:00" code="200" invoiceId="1234567" shopId="13" message="Error parsing request" techMessage="Error" />
				code = 4
				tpl.update({"responseName":'checkOrderResponse',
							"operationDate":datetime.datetime.now(),
							"code":code,
							"invoiceID":invoiceId,
							"shopId":shopId,
							"message":"Error parsing request",
							"techMessage":"Error"
							})
				xop.state = ExternalOperationState.cancelled

		#уведомление о переводе
		if action == 'paymentAviso':
			#говорим ок, спасибо
			#1
			#ok
			#достаем соотв xop и меняем статус на оплачено CONFIRMED
			xop.state = ExternalOperationState.cleared
			#<paymentAvisoResponse performedDatetime="2011-05-04T20:38:11.000+04:00" code="0" invoiceId="1234567" shopId="13"/>
			#not ok
			#<paymentAvisoResponse performedDatetime="2011-05-04T20:38:11.000+04:00" code="1" message="Значение параметра md5 не совпадает с результатом расчета хэш-функции"/>
			#totally wrong
			#<paymentAvisoResponse performedDatetime="2011-05-04T20:38:11.000+04:00" code="200" message="Все не так"/>
		if action == 'cancelOrder':
			#отменяем заказ
			#<cancelOrderResponse performedDatetime="2011-05-04T20:38:11.000+04:00" code="0" invoiceId="1234567" shopId="13"/>
			xop.state = ExternalOperationState.cancelled
			#если соотв xop создан, меняем на CANCELLED
		else:
			request.session.flash({
					'text' : loc.translate(_('Something went wrong, sorry.')),
					'class' : 'danger'
					})
			return HTTPSeeOther(location=request.route_url('stashes.cl.accounts', traverse=()))

	request.session.flash({
		'text' : loc.translate(_('Wrong request type')),
		'class' : 'danger'
	})


	return HTTPSeeOther(location=request.route_url('stashes.cl.accounts', traverse=()))
