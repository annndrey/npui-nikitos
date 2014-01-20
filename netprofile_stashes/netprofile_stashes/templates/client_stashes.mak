## -*- coding: utf-8 -*-
<%inherit file="netprofile_access:templates/client_layout.mak"/>\
<%namespace module="netprofile.common.hooks" import="gen_block" />\
<%namespace module="netprofile.tpl.filters" import="date_fmt, curr_fmt" />\
<%block name="title">${_('My Accounts')}</%block>

<h1>${_('My Accounts')}</h1>

% for stash in req.user.parent.stashes:
<h3 title="${_('Account name')}">${stash.name}</h3>
<div class="row">
	<div class="col-sm-4">
		<h4 class="money">
			<span class="balance${' negative' if (stash.amount < 0) else ''}" title="${_('Current account balance')}">
				<span class="fa fa-rub"></span>
				${stash.amount | n,curr_fmt}
			</span>
% if stash.credit != 0:
			<small class="single-line">
				${'Credit:'}
				<span class="balance${' negative' if (stash.credit < 0) else ''}" title="${_('Current credit limit for this account')}">
					<span class="fa fa-rub"></span>
					${stash.credit | n,curr_fmt}
				</span>
			</small>
% endif
		</h4>
	</div>
	<div class="col-sm-8" style="padding-bottom: 0.6em;"><ul class="nav nav-tabs">
		<li class="active"><a href="#tab-users-${stash.id}" data-toggle="tab">${_('Users')}</a></li>
  	    <li><a href="#tab-replenish-${stash.id}" data-toggle="tab">${_('Replenish')}</a></li>
		<li class="dropdown pull-right">
			<a class="dropdown-toggle" data-toggle="dropdown" id="menu-reports-${stash.id}" href="#">
				${_('Actions')}
				<span class="caret"></span>
			</a>
			<ul class="dropdown-menu pull-right" role="menu" aria-labelledby="menu-reports-${stash.id}" aria-expanded="false" aria-hidden="true">
				<li role="presentation"><a role="menuitem" tabindex="-1" href="#">${_('Create User')}</a></li>
				<li role="presentation"><a role="menuitem" tabindex="-1" href="#">${_('Transfer Funds')}</a></li>
				<li role="presentation" class="divider"></li>
				<li role="presentation"><a role="menuitem" tabindex="-1" href="${req.route_url('stashes.cl.stats', stash_id=stash.id)}">${_('Operations Report')}</a></li>
				<li role="presentation"><a role="menuitem" tabindex="-1" href="#">${_('Promised Payments Report')}</a></li>
			</ul>
		</li>
	</ul></div>
</div>
<div class="tab-content">
% if len(stash.access_entities):
	<ul class="list-group tab-pane fade in active" id="tab-users-${stash.id}">
% for a in stash.access_entities:
% if a.alias_of_id == None:
		<li class="list-group-item">
			<h4 class="list-group-item-heading">
				${a.nick}
% if a.access_state:
				<span class="label label-danger pull-right">${a.access_state_string(req)}</span>
% endif
			</h4>
% if a.quota_period_end:
			<div class="row">
				<label for="fld-qpend-${stash.id}" class="col-sm-4">${_('Paid Till')}</label>
				<div id="fld-qpend-${stash.id}" class="col-sm-8">${a.quota_period_end | n,date_fmt}</div>
			</div>
% endif
			<div class="row">
				<label for="fld-rate-${stash.id}" class="col-sm-4">${_('Current Rate')}</label>
				<div id="fld-rate-${stash.id}" class="col-sm-8">${a.rate}</div>
			</div>
% if a.next_rate:
			<div class="row">
				<label for="fld-nextrate-${stash.id}" class="col-sm-4">${_('Next Rate')}</label>
				<div id="fld-nextrate-${stash.id}" class="col-sm-8">${a.next_rate}</div>
			</div>
% endif
			<form class="row" role="form" method="post" action="${req.route_url('stashes.cl.chrate')}">
				<label for="fld-chrate-${a.id}" class="col-sm-4">${_('New Next Rate')}</label>
				<div class="col-sm-8 form-inline">
					<input type="hidden" name="csrf" value="${req.get_csrf()}" />
					<input type="hidden" name="entityid" value="${a.id}" />
					<select class="form-control chosen-select padded-wrap" id="fld-chrate-${a.id}" name="rateid" title="${_('Next Rate')}">
% for rate in rates:
						<option label="${rate}" value="${rate.id}"\
% if (a.next_rate_id and (rate.id == a.next_rate_id)) or ((not a.next_rate_id) and (rate.id == a.rate_id)):
 selected="selected"\
% endif
>${rate}</option>
% endfor
					</select>
					<span class="btn-group">
						<button class="btn btn-default" type="submit" name="submit" title="${_('Select different next rate')}">${_('Set')}</button>
% if a.next_rate_id:
						<button class="btn btn-default" type="submit" name="clear" title="${_('Cancel scheduled rate change')}">${_('Clear')}</button>
% endif
					</span>
				</div>
			</form>
${gen_block('stashes.cl.block.info')}
		</li>
% endif
% endfor
	</ul>
% else:
	<div class="well tab-pane fade in active" id="tab-users-${stash.id}">${_('This account has no users.')}</div>
% endif
	<ul class="list-group tab-pane fade" id="tab-replenish-${stash.id}">
${gen_block('stashes.cl.block.payment')}
		<li class="list-group-item">
			<form class="row" role="form" method="post" action="${req.route_url('stashes.cl.dofuture')}">
				<label for="" class="col-sm-4">${_('Promise Payment')}</label>
				<div class="col-sm-8 form-inline">
					<input type="hidden" name="csrf" value="${req.get_csrf()}" />
					<input type="hidden" name="stashid" value="${stash.id}" />
					<input type="text" placeholder="${_('Enter sum')}" class="form-control" required="required" name="diff" title="${_('Enter the sum you promise to pay at a later date.')}" value="" tabindex="-1" autocomplete="off" />
					<button class="btn btn-default" type="submit" name="submit" title="${_('Press to promise payment')}">${_('Promise')}</button>
				</div>
			</form>
		</li>
	</ul>
</div>
% endfor

