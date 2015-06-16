## -*- coding: utf-8 -*-

## Hidden modal domain creation form
<div class="modal fade" id="formModalDomain" tabindex="-1" role="dialog" aria-labelledby="formModalDomainLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
	
	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
	<h4 class="modal-title" id="formModalDomainLabel">${loc.translate(_("New domain"))}</h4>
	
      </div>
      <div class="modal-body">
	<form method="POST" action="${req.route_url("pdns.cl.create")}" class="form-inline" role="form" id="hostForm">
	  
	  <div class="form-group">
	    <input type="text" name="hostName" class="form-control" id="hostName" placeholder="${loc.translate(_("Enter host name"))}"/>
	  </div>
	  
	  ##<div class="form-group">
	  ##  <select name="hostType" class="form-control" id="hosttype" placeholder=${loc.translate(_("Host type"))}>
	  ##    % for i in ["NATIVE", "MASTER", "SLAVE", "SUPERSLAVE"]:
	  ##	<option>${i}</option>
	  ##    % endfor
	  ##  </select>
	  ##</div>
	  
	  <div class="form-group">
	    <input type="text" name="hostValue" class="form-control" id="hostValue" placeholder="${loc.translate(_("Enter IP"))}">
	    <input type="hidden" name="user" id="user" value="${accessuser.nick}">
	    <input type="hidden" name="type" id="type" value="domain">
	    <input type="hidden" name="csrf" value="${req.get_csrf()}" />
	  </div>
	  
      </div>
      <div class="modal-footer">
	<input type="submit" value="${loc.translate(_("Create"))}" class="btn btn-primary"/>
	</form>
	
	<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
	
      </div>
    </div>
  </div>
</div>

## Hidden modal mailserver creation form
<div class="modal fade" id="formModalMailServer" tabindex="-1" role="dialog" aria-labelledby="formModalMailServerLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
	
	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
	<h4 class="modal-title" id="formModalMailServerLabel">${loc.translate(_("New mail server"))}</h4>
	
      </div>
      <div class="modal-body">
	<form method="POST" action="${req.route_url("pdns.cl.create")}" class="form-inline" role="form" id="hostForm">
	  
	  <div class="form-group">
	    <input type="text" name="hostName" class="form-control" id="hostName" placeholder="${loc.translate(_("Enter host name"))}"/>
	  </div>
	  
	  ##<div class="form-group">
	  ##  <select name="hostType" class="form-control" id="hosttype" placeholder=${loc.translate(_("Host type"))}>
	  ##    % for i in ["NATIVE", "MASTER", "SLAVE", "SUPERSLAVE"]:
	  ##	<option>${i}</option>
	  ##    % endfor
	  ##  </select>
	  ##</div>
	  
	  <div class="form-group">
	    <input type="text" name="hostValue" class="form-control" id="hostValue" placeholder="${loc.translate(_("Enter IP"))}">
	    <input type="hidden" name="user" id="user" value="${accessuser.nick}">
	    <input type="hidden" name="type" id="type" value="mailserver">
	    <input type="hidden" name="csrf" value="${req.get_csrf()}" />
	  </div>
	  
      </div>
      <div class="modal-footer">
	<input type="submit" value="${loc.translate(_("Create"))}" class="btn btn-primary"/>
	</form>
	
	<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
	
      </div>
    </div>
  </div>
</div>

## Hidden modal domain creation form
<div class="modal fade" id="formModalJabber" tabindex="-1" role="dialog" aria-labelledby="formModalJabberLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
	
	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
	<h4 class="modal-title" id="formModalJabberLabel">${loc.translate(_("New jabber server"))}</h4>
	
      </div>
      <div class="modal-body">
	<form method="POST" action="${req.route_url("pdns.cl.create")}" class="form-inline" role="form" id="hostForm">
	  
	  <div class="form-group">
	    <input type="text" name="hostName" class="form-control" id="hostName" placeholder="${loc.translate(_("Enter host name"))}"/>
	  </div>
	  
	  ##<div class="form-group">
	  ##  <select name="hostType" class="form-control" id="hosttype" placeholder=${loc.translate(_("Host type"))}>
	  ##    % for i in ["NATIVE", "MASTER", "SLAVE", "SUPERSLAVE"]:
	  ##	<option>${i}</option>
	  ##    % endfor
	  ##  </select>
	  ##</div>
	  
	  <div class="form-group">
	    <input type="text" name="hostValue" class="form-control" id="hostValue" placeholder="${loc.translate(_("Enter IP"))}">
	    <input type="hidden" name="user" id="user" value="${accessuser.nick}">
	    <input type="hidden" name="type" id="type" value="jabber">
	    <input type="hidden" name="csrf" value="${req.get_csrf()}" />
	  </div>
	  
      </div>
      <div class="modal-footer">
	<input type="submit" value="${loc.translate(_("Create"))}" class="btn btn-primary"/>
	</form>
	
	<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
	
      </div>
    </div>
  </div>
</div>

