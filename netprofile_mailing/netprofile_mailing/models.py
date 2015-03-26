#!/usr/bin/env python
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-
#
# NetProfile: Mailing module - Models
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

__all__ = [
	'MailingTemplate',
	'MailingLog'
	'MailingSubscription',
]

from sqlalchemy import (
	Column,
	DateTime,
	FetchedValue,
	ForeignKey,
	Index,
	Sequence,
	TIMESTAMP,
	Unicode,
	UnicodeText
)

from sqlalchemy.orm import (
	backref,
	relationship
)

from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.ext.hybrid import hybrid_property

from netprofile.db.connection import (
	Base,
	DBSession
)
from netprofile.db.fields import (
	ASCIIString,
	NPBoolean,
	UInt8,
	UInt16,
	UInt32,
	npbool,
	IPv4Address,
	IPv6Address,
	IPv6Offset
)
from netprofile.db.ddl import (
	Comment,
	Trigger
)
from netprofile.tpl import TemplateObject
from netprofile.ext.columns import MarkupColumn
from netprofile.common.hooks import register_hook
from netprofile.ext.data import (
	ExtModel,
	_name_to_class
)
from netprofile.ext.wizards import (
	ExternalWizardField,
	SimpleWizard,
	Step,
	Wizard
)
from pyramid.i18n import (
	TranslationStringFactory,
	get_localizer
)

_ = TranslationStringFactory('netprofile_mailing')

@register_hook('np.wizard.init.mailing.MailingLog')
#def _wizcb_aent_init(wizard, model, req):
def _wizcb_maillog_submit(wiz, step, act, val, req):
	sess = DBSession()
	em = ExtModel(MailingLog)
	obj = MailingLog()
	print("OLOLO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		# Work around field name clash
	if 'state' in val:
		del val['state']
		### Calculate letter hash here
		### and send mail to user
		### and add new log to database if successful sent
	print(val)
	#{'body': '<p>ууцййцуцйу</p>', 'userid': '75', 'user': 'Doge'}
	#Column 'letteruid' cannot be null
	em.set_values(obj, val, req, True)
	sess.add(obj)
	return {
		'do'     : 'close',
		'reload' : True
		}

	#wizard.steps.append(Step(
	#	ExternalWizardField('AccessEntity', 'password'),
	#	ExternalWizardField('AccessEntity', 'stash'),
	#	ExternalWizardField('AccessEntity', 'rate'),
	#	id='ent_access1', title=_('Access entity properties'),
	#	on_prev='generic',
	#	on_submit=_wizcb_aent_submit
	#))

class MailingTemplate(Base):
	"""
	Mailing Template object
	"""
	__tablename__ = 'mailing_templates'
	__table_args__ = (
		Comment('Mailing Templates'),
		Index('mailing_templates_u_name', 'name', unique=True),
		Index('mailing_templates_u_text', 'body', unique=True),
		#Trigger('after', 'insert', 't_nets_def_ai'),
		#Trigger('after', 'update', 't_nets_def_au'),
		#Trigger('after', 'delete', 't_nets_def_ad'),
		{
			'mysql_engine'  : 'InnoDB',
			'mysql_charset' : 'utf8',
			'info'          : {
				#CORRECT PRIVLIEGES
				'cap_menu'      : 'BASE_NETS',
				'cap_read'      : 'NETS_LIST',
				'cap_create'    : 'NETS_CREATE',
				'cap_edit'      : 'NETS_EDIT',
				'cap_delete'    : 'NETS_DELETE',
				'menu_name'     : _('Mail Templates'),
				'show_in_menu'  : 'admin',
				'menu_order'    : 10,
				'menu_main'     : False,
				'default_sort'  : ({ 'property': 'name', 'direction': 'ASC' },),
				'grid_view'     : (
					'name', 'body'
				),
				'form_view'     : (
					'name', 'body'
				),
				'easy_search'   : ('name',),
				'detail_pane'   : ('netprofile_core.views', 'dpane_simple'),
				'create_wizard' : SimpleWizard(title=_('Add new mailing template'))
			}
		}
	)
	id = Column(
		'templid',
		UInt32(),
		Sequence('mailing_templates_templ_seq'),
		Comment('Template ID'),
		primary_key=True,
		nullable=False,
		info={
			'header_string' : _('ID')
		}
	)
	name = Column(
		Unicode(255),
		Comment('Template Name'),
		nullable=False,
		info={
			'header_string' : _('Name')
		}
	)
	#ADD HTML EDITOR HERE LIKE IN DOCUMENTS
	body = Column(
		UnicodeText(),
		Comment('Template body'),
		nullable=False,
		info={
			'header_string' : _('Template Body'),
			'editor_xtype'  : 'tinymce_field',
			'editor_config' : {
				'tinyMCEConfig' : {
					'theme'                             : 'advanced',
					'skin'                              : 'extjs',
					'inlinepopups_skin'                 : 'extjs',
					'theme_advanced_row_height'         : 27,
					'delta_height'                      : 1,
					'schema'                            : 'html5',
					'plugins'                           : 'lists,pagebreak,style,layer,table,save,advhr,advimage,advlink,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,visualblocks,nonbreaking,xhtmlxtras,template,wordcount,advlist',

					'theme_advanced_buttons1'           : 'bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect',
					'theme_advanced_buttons2'           : 'cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor',
					'theme_advanced_buttons3'           : 'tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen',
					'theme_advanced_buttons4'           : 'insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,visualblocks,nonbreaking,template,pagebreak,restoredraft',

					'theme_advanced_toolbar_location'   : 'top',
					'theme_advanced_toolbar_align'      : 'left',
					'theme_advanced_statusbar_location' : 'bottom',

					'extended_valid_elements'           : '+tpl[if|elsif|else|for|foreach|switch|case|default]',
					'custom_elements'                   : '~tpl',
					'valid_children'                    : '+*[tpl],+tpl[*],+tbody[tpl],+body[tpl],+table[tpl],+tpl[table|tr|tpl|#text]'

					}
				}
			}
	)
	#..... 
	def __str__(self):
		return self.name


class MailingLog(Base):
	__tablename__ = 'mailing_log'
	__table_args__ = (
		Comment('Mailing Logs'),
		Index('mailing_log_u_letteruid', 'letteruid', unique=True),
		#Trigger('after', 'insert', 't_nets_def_ai'),
		#Trigger('after', 'update', 't_nets_def_au'),
		#Trigger('after', 'delete', 't_nets_def_ad'),
		{
			'mysql_engine'  : 'InnoDB',
			'mysql_charset' : 'utf8',
			'info'          : {
				#REVIEW PRIVILEGES
				'cap_menu'      : 'BASE_NETS',
				'cap_read'      : 'NETS_LIST',
				'cap_create'    : 'NETS_CREATE',
				'cap_edit'      : 'NETS_EDIT',
				'cap_delete'    : 'NETS_DELETE',
				'menu_name'     : _('Mailing Logs'),
				'show_in_menu'  : 'admin',
				'menu_order'    : 20,
				'menu_main'     : False,
				'default_sort'  : ({ 'property': 'senttime', 'direction': 'ASC' },),
				'grid_view'     : (
					'senttime', 'user', 'isread', 'letteruid'
				),
				'form_view'     : (
					'senttime', 'readtime', 'user', 'isread', 'letteruid'
				),
				'easy_search'   : ('user'),
				'detail_pane'   : ('netprofile_core.views', 'dpane_simple'),
				#TO REMOVE, SHOULD NOT BE CREATED MANUALLY
				#look at Entities and Access modules
				#еще можно посмотреть в tickets как сделано on_submit. 
				#нам надо брать данные из визарда, вычислять все что нужно и возвраащать соотв поля для создания новой записи и еще отправлять письмо т.е. 
				#искать емейл и туда слать
				#и еще чтобы можно было выбирать шаблон
				#и вставлять его в письмо
				'create_wizard' : Wizard(
					Step(
						'user', 
						ExternalWizardField('MailingTemplate', 'body'),
						title=_('Send new mail'),
						id='generic',
						on_prev='generic',
						on_submit=_wizcb_maillog_submit
						),
					title=_('Send new mail')
					)
				
				}
			}
		)
	id = Column(
		'logid',
		UInt32(),
		Sequence('mailing_log_logid_seq'),
		Comment('Log ID'),
		primary_key=True,
		nullable=False,
		info={
			'header_string' : _('ID')
		}
	)
	senttime = Column(
		'senttime',
		TIMESTAMP(),
		Comment('Sending timestamp'),
		nullable=True,
		default=None,
		server_default=FetchedValue(),
		info={
			'header_string' : _('Sent at'),
			'read_only'     : True
		}
	)
	readtime = Column(
		'readtime',
		TIMESTAMP(),
		Comment('Read timestamp'),
		nullable=True,
		default=None,
		server_default=FetchedValue(),
		info={
			'header_string' : _('Read at'),
			'read_only'     : True
		}
	)
	userid = Column(
		'userid',
		UInt32(),
		ForeignKey('entities_access.entityid', name='mailing_log_fk_userid', ondelete='CASCADE', onupdate='CASCADE'),
		Comment('Access Entity ID'),
		primary_key=True,
		nullable=False,
		info={
			'header_string' : _('User ID')
		}
	)
	letteruid = Column(
		Unicode(255),
		Comment('Letter UID'),
		nullable=False,
		info={
			'header_string' : _('Letter Body'),
			'editor_xtype'  : 'tinymce_field',
			'editor_config' : {
				'tinyMCEConfig' : {
					'theme'                             : 'advanced',
					'skin'                              : 'extjs',
					'inlinepopups_skin'                 : 'extjs',
					'theme_advanced_row_height'         : 27,
					'delta_height'                      : 1,
					'schema'                            : 'html5',
					'plugins'                           : 'lists,pagebreak,style,layer,table,save,advhr,advimage,advlink,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,visualblocks,nonbreaking,xhtmlxtras,template,wordcount,advlist',

					'theme_advanced_buttons1'           : 'bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect',
					'theme_advanced_buttons2'           : 'cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor',
					'theme_advanced_buttons3'           : 'tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen',
					'theme_advanced_buttons4'           : 'insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,visualblocks,nonbreaking,template,pagebreak,restoredraft',

					'theme_advanced_toolbar_location'   : 'top',
					'theme_advanced_toolbar_align'      : 'left',
					'theme_advanced_statusbar_location' : 'bottom',

					'extended_valid_elements'           : '+tpl[if|elsif|else|for|foreach|switch|case|default]',
					'custom_elements'                   : '~tpl',
					'valid_children'                    : '+*[tpl],+tpl[*],+tbody[tpl],+body[tpl],+table[tpl],+tpl[table|tr|tpl|#text]'

					}
				}
			}
		)
	isread = Column(
		'isread',
		NPBoolean(),
		Comment('Is letter read?'),
		nullable=False,
		default=False,
		server_default=npbool(False),
		info={
			'header_string' : _('Is letter read?')
		}
	)

	#CHECK IF WORKS
	user = relationship(
		'AccessEntity',
		backref='mailinglog_entities',
		primaryjoin='MailingLog.userid == AccessEntity.id'
	)

class MailingSubscription(Base):
	"""
	Mailing subscription settings
	"""
	__tablename__ = 'mailing_settings'
	__table_args__ = (
		Comment('Mailing Settings'),
		Index('mailing_settings_u_userid', 'userid', unique=True),
		#Trigger('after', 'insert', 't_nets_def_ai'),
		#Trigger('after', 'update', 't_nets_def_au'),
		#Trigger('after', 'delete', 't_nets_def_ad'),
		{
			'mysql_engine'  : 'InnoDB',
			'mysql_charset' : 'utf8',
			'info'          : {
				#REVIEW PRIVILEGES
				'cap_menu'      : 'BASE_NETS',
				'cap_read'      : 'NETS_LIST',
				'cap_create'    : 'NETS_CREATE',
				'cap_edit'      : 'NETS_EDIT',
				'cap_delete'    : 'NETS_DELETE',
				'menu_name'     : _('Mailing Settings'),
				'show_in_menu'  : 'admin',
				'menu_order'    : 30,
				'menu_main'     : False,
				'default_sort'  : ({ 'property': 'user', 'direction': 'ASC' },),
				'grid_view'     : (
					'user', 'issubscribed'
				),
				'form_view'     : (
					'user', 'issubscribed'
				),
				'easy_search'   : ('user'),
				'detail_pane'   : ('netprofile_core.views', 'dpane_simple'),
				#TO REMOVE, SHOULD NOT BE CREATED MANUALLY
				'create_wizard' : SimpleWizard(title=_('Add new user subscription'))
			}
		}
	)
	userid = Column(
		'userid',
		UInt32(),
		ForeignKey('entities_access.entityid', name='mailing_settings_fk_userid', ondelete='CASCADE', onupdate='CASCADE'),
		Comment('Access Entity ID'),
		primary_key=True,
		nullable=False,
		info={
			'header_string' : _('User ID')
		}
	)
	issubscribed = Column(
		'issubscribed',
		NPBoolean(),
		Comment('Is letter read?'),
		nullable=False,
		default=True,
		server_default=npbool(True),
		info={
			'header_string' : _('Is user subscripted?')
		}
	)
	#CHECK IF WORKS
	user = relationship(
		'AccessEntity',
		backref='subscription_entities',
		primaryjoin='MailingSubscription.userid == AccessEntity.id'
	)
