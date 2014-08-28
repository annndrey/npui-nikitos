# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1408540423.997425
_enable_loop = True
_template_filename = '/home/annndrey/test/git/npui/netprofile_postfix/netprofile_postfix/templates/client_mail.mak'
_template_uri = 'netprofile_postfix$templates/client_mail.mak'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'netprofile_access:templates/client_layout.mak', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        loc = context.get('loc', UNDEFINED)
        maildomains = context.get('maildomains', UNDEFINED)
        req = context.get('req', UNDEFINED)
        accessuser = context.get('accessuser', UNDEFINED)
        mailboxes = context.get('mailboxes', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        userdomains = context.get('userdomains', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        # SOURCE LINE 5
        __M_writer('<button class="btn btn-primary pull-right" data-toggle="modal" data-target="#formModalDomain">\n  <span class="glyphicon glyphicon-plus"></span>\n  ')
        # SOURCE LINE 7
        __M_writer(filters.html_escape(loc.translate(_("Attach a new domain"))))
        __M_writer('\n</button>\n')
        # SOURCE LINE 10
        __M_writer('\n')
        # SOURCE LINE 12
        __M_writer('<button class="btn btn-primary pull-right" data-toggle="modal" data-target="#formModalMailbox">\n  <span class="glyphicon glyphicon-plus"></span>\n  ')
        # SOURCE LINE 14
        __M_writer(filters.html_escape(loc.translate(_("Create a new mailbox"))))
        __M_writer('\n</button>\n')
        # SOURCE LINE 17
        __M_writer('\n<h1>')
        # SOURCE LINE 18
        __M_writer(filters.html_escape(loc.translate(_("My mailboxes"))))
        __M_writer('</h1>\n\n')
        # SOURCE LINE 21
        if maildomains is None:
            # SOURCE LINE 22
            __M_writer('      <div class="alert alert-warning">\n\t')
            # SOURCE LINE 23
            __M_writer(filters.html_escape(loc.translate(_("You have no domains to attach a mailbox."))))
            __M_writer('\n\n')
            # SOURCE LINE 26
            __M_writer('\t<button class="btn btn-primary btn-sm pull-right" data-toggle="modal" data-target="#formModalDomain">\n\t  <span class="glyphicon glyphicon-plus"></span>\n\n\t  ')
            # SOURCE LINE 29
            __M_writer(filters.html_escape(loc.translate(_("Create a new domain"))))
            __M_writer('\n\t</button>\n      </div>\n      \n')
            # SOURCE LINE 35
        elif maildomains is not None and mailboxes is None:
            # SOURCE LINE 36
            __M_writer('     <div class="alert alert-warning">\n       ')
            # SOURCE LINE 37
            __M_writer(filters.html_escape(loc.translate(_("You have no mailbox."))))
            __M_writer('\n       <button class="btn btn-primary btn-sm pull-right" data-toggle="modal" data-target="#formModalMailbox">\n\t <span class="glyphicon glyphicon-plus"></span>\n\t ')
            # SOURCE LINE 40
            __M_writer(filters.html_escape(loc.translate(_("Create a new one?"))))
            __M_writer('\n       </button>\n     </div>\n\n')
            # SOURCE LINE 46
        else:
            # SOURCE LINE 47
            __M_writer('  <div class="panel-group" id="accordion">\n')
            # SOURCE LINE 48
            for d in maildomains:
                # SOURCE LINE 49
                __M_writer('      <div class="panel panel-default">\n\t<div class="panel-heading">\n\t  <div class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapse')
                # SOURCE LINE 52
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n\t      <span class="glyphicon glyphicon-th-list"></span> <strong>')
                # SOURCE LINE 53
                __M_writer(filters.html_escape(d))
                __M_writer('</strong></a> \n\t    <a data-toggle="modal" data-target="#formModalMailbox')
                # SOURCE LINE 54
                __M_writer(filters.html_escape(d.id))
                __M_writer('"><span class="glyphicon glyphicon-plus-sign"></span></a>\n\t    <a data-toggle=\'modal\' href=\'#modalDomainEdit')
                # SOURCE LINE 55
                __M_writer(filters.html_escape(d.id))
                __M_writer('\'><span class="glyphicon glyphicon-pencil"</a> \n\t      <a data-toggle=\'modal\' href=\'#modalDomainDelete')
                # SOURCE LINE 56
                __M_writer(filters.html_escape(d.id))
                __M_writer('\'><span class="glyphicon glyphicon-remove"></a> \n\t  </div>\n\t</div>\n\t\n\t<div id="collapse')
                # SOURCE LINE 60
                __M_writer(filters.html_escape(d.id))
                __M_writer('" class="panel-collapse collapse">\n\t  <div class="panel-body">\n\t    \n')
                # SOURCE LINE 63
                if d.domain in [m.domain for m in mailboxes]:
                    # SOURCE LINE 64
                    for mb in mailboxes:
                        # SOURCE LINE 65
                        if mb.domain == d.domain:
                            # SOURCE LINE 66
                            __M_writer('\t\t  ')
                            __M_writer(filters.html_escape(mb))
                            __M_writer('@')
                            __M_writer(filters.html_escape(d))
                            __M_writer("\n\t\t  <a data-toggle='modal' href='#modalMboxEdit")
                            # SOURCE LINE 67
                            __M_writer(filters.html_escape(mb.id))
                            __M_writer('\'><span class="glyphicon glyphicon-pencil"></a> \n\t\t    <a data-toggle=\'modal\' href=\'#modalMboxDelete')
                            # SOURCE LINE 68
                            __M_writer(filters.html_escape(mb.id))
                            __M_writer('\'><span class="glyphicon glyphicon-remove"></a> \n\t\t      <br>\n\n')
                            # SOURCE LINE 72
                            __M_writer('\t\t      <div class="modal fade" id="modalMboxDelete')
                            __M_writer(filters.html_escape(mb.id))
                            __M_writer('" tabindex="-1" role="dialog" aria-labelledby="modalMboxDeleteLabel" aria-hidden="true">\n\t\t\t\n\t\t\t<div class="modal-dialog">\n\t\t\t  <div class="modal-content">\n\t\n\t\t\t    <div class="modal-header">\n\t\t\t      <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t\t    </div>\n\t\t\t    \n\t\t\t    <div class="modal-body" id="domain')
                            # SOURCE LINE 81
                            __M_writer(filters.html_escape(d.id))
                            __M_writer('">\n\t\t\t      <h4 class="modal-title">')
                            # SOURCE LINE 82
                            __M_writer(filters.html_escape(loc.translate(_("Really delete mailbox"))))
                            __M_writer(' <strong>')
                            __M_writer(filters.html_escape(mb))
                            __M_writer('@')
                            __M_writer(filters.html_escape(d))
                            __M_writer('</strong>?</h4>\n\t\t\t      \n\t\t\t      <form method="POST" action="')
                            # SOURCE LINE 84
                            __M_writer(filters.html_escape(req.route_url("postfix.cl.delete")))
                            __M_writer('" class="form-inline" role="form" id="deleteForm">\n\t\t\t\t<div class="form-group">\n\t\t\t\t  <input type="hidden" name="user" id="user" value="')
                            # SOURCE LINE 86
                            __M_writer(filters.html_escape(accessuser.nick))
                            __M_writer('"\n\t\t\t\t  <input type="hidden" name="domainid" id="domainid" value="')
                            # SOURCE LINE 87
                            __M_writer(filters.html_escape(d.id))
                            __M_writer('">\n\t\t\t\t  <input type="hidden" name="mboxid" id="mboxid" value="')
                            # SOURCE LINE 88
                            __M_writer(filters.html_escape(mb.id))
                            __M_writer('">\n\t\t\t\t  <input type="hidden" name="type" id="type" value="mbox">\n\t\t\t\t  <input type="hidden" name="csrf" value="')
                            # SOURCE LINE 90
                            __M_writer(filters.html_escape(req.get_csrf()))
                            __M_writer('" />\n\t\t\t\t</div>\n\t\t\t    </div>\n\t\t\t    <div class="modal-footer">\n       \t\t\t      <input type="submit" value="')
                            # SOURCE LINE 94
                            __M_writer(filters.html_escape(loc.translate(_("Delete"))))
                            __M_writer('" class="btn btn-primary"/>\n\t\t\t      </form>\n\t\t\t      <button type="button" class="btn btn-default" data-dismiss="modal">')
                            # SOURCE LINE 96
                            __M_writer(filters.html_escape(loc.translate(_("Cancel"))))
                            __M_writer('</button>\n\t\t\t    </div>\n\t\t\t  </div>\n\t\t\t</div>\n\t\t      </div>\n\t\t      \n')
                            # SOURCE LINE 103
                            __M_writer('\t\t      \n')
                            # SOURCE LINE 105
                            __M_writer('\t\t      <div class="modal fade" id="modalMboxEdit')
                            __M_writer(filters.html_escape(mb.id))
                            __M_writer('" tabindex="-1" role="dialog" aria-labelledby="formModalMboxLabel')
                            __M_writer(filters.html_escape(mb.id))
                            __M_writer('" aria-hidden="true">\n\t\t\t<div class="modal-dialog">\n\t\t\t  <div class="modal-content">\n\t\t\t    <div class="modal-header">\n     \n\t\t\t      <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t\t      <h4 class="modal-title" id="formModalMboxLabel')
                            # SOURCE LINE 111
                            __M_writer(filters.html_escape(mb.id))
                            __M_writer('">')
                            __M_writer(filters.html_escape(loc.translate(_("Edit mailbox "))))
                            __M_writer(filters.html_escape(mb))
                            __M_writer('@')
                            __M_writer(filters.html_escape(d))
                            __M_writer('</h4>\n\t\t\t    </div>\n\t\t\t    <div class="modal-body">\n\t\t\t      \n\t\t\t      <form method="POST" action="')
                            # SOURCE LINE 115
                            __M_writer(filters.html_escape(req.route_url("postfix.cl.edit")))
                            __M_writer('" class="form-inline" role="form" id="editForm">\n\t\t\t\t<div class="form-group">\n\t\t\t\t  <input type="text" name="mbName" class="form-control" id="mbName" value="')
                            # SOURCE LINE 117
                            __M_writer(filters.html_escape(mb))
                            __M_writer('"/>\n\t\t\t\t</div>\n\t\t\t\t@\n\t\t\t\t<div class="form-group">\n\t\t\t\t  <select name="mbDomain" class="form-control" id="mbDomain">\n')
                            # SOURCE LINE 122
                            for mbd in maildomains:
                                # SOURCE LINE 123
                                if mbd.domain == mb.domain:	
                                    # SOURCE LINE 124
                                    __M_writer('       \t\t\t\t\t<option selected>')
                                    __M_writer(filters.html_escape(mbd))
                                    __M_writer('</option>\n')
                                    # SOURCE LINE 125
                                else:
                                    # SOURCE LINE 126
                                    __M_writer('\t\t\t\t\t<option>')
                                    __M_writer(filters.html_escape(mbd))
                                    __M_writer('</option>\n')
                            # SOURCE LINE 129
                            __M_writer('\t\t\t\t  </select>\n\t\t\t\t</div>\n\t\t\n\t\t\t\t<div class="form-group">\n\t\t\t\t  <input type="password" name="mbPassword" class="form-control" id="mbPassword" value="')
                            # SOURCE LINE 133
                            __M_writer(filters.html_escape(mb.password))
                            __M_writer('">\n\t\t\t\t  <input type="hidden" name="mbUsername" id="mbUsername" value="')
                            # SOURCE LINE 134
                            __M_writer(filters.html_escape(mb.username))
                            __M_writer('">\n\t\t\t\t  <input type="hidden" name="id" id="id" value="')
                            # SOURCE LINE 135
                            __M_writer(filters.html_escape(mb.id))
                            __M_writer('">\n\t\t\t\t  <input type="hidden" name="csrf" value="')
                            # SOURCE LINE 136
                            __M_writer(filters.html_escape(req.get_csrf()))
                            __M_writer('" />\n\t\t\t\t</div>\n\t\t\t    </div>\n\t\t\t    <div class="modal-footer">\n\t\t\t      <input type="submit" value="')
                            # SOURCE LINE 140
                            __M_writer(filters.html_escape(loc.translate(_("Save"))))
                            __M_writer('" class="btn btn-primary"/>\n\t\t\t      </form>\n\t\t\t      \n\t\t\t      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t\t\t      \n\t\t\t    </div>\n\t\t\t  </div>\n\t\t\t</div>\n\t\t      </div>\n')
                            # SOURCE LINE 150
                            __M_writer('\t\t      \n')
                    # SOURCE LINE 153
                else:
                    # SOURCE LINE 155
                    __M_writer('      \t      There\'s no mailboxes for this domain yet. <button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#formModalMailbox')
                    __M_writer(filters.html_escape(d.id))
                    __M_writer('"><span class="glyphicon glyphicon-plus-sign">')
                    __M_writer(filters.html_escape(loc.translate(_("Add one?"))))
                    __M_writer(' </button>\n')
                # SOURCE LINE 157
                __M_writer('\t    \n\t  </div>\n\t</div>\n      </div>\n      \n')
                # SOURCE LINE 163
                __M_writer('      <div class="modal fade" id="modalDomainEdit')
                __M_writer(filters.html_escape(d.id))
                __M_writer('" tabindex="-1" role="dialog" aria-labelledby="modalDomainEditLabel')
                __M_writer(filters.html_escape(d.id))
                __M_writer('" aria-hidden="true">\n\t<div class="modal-dialog">\n\t  <div class="modal-content">\n\t    <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n              <h4 class="modal-title" id="modalDomainEditLabel')
                # SOURCE LINE 168
                __M_writer(filters.html_escape(d.id))
                __M_writer('">')
                __M_writer(filters.html_escape(loc.translate(_("Edit domain"))))
                __M_writer(' ')
                __M_writer(filters.html_escape(d))
                __M_writer('</h4>\n            </div>\n            <div class="modal-body">\n\t      <form method="POST" action="')
                # SOURCE LINE 171
                __M_writer(filters.html_escape(req.route_url("postfix.cl.edit")))
                __M_writer('" class="form-inline" role="form" id="createDomainForm">\n\t\t<div class="form-group">\n\t\t  <input type="text" name="mbDomainDescription" class="form-control" id="mbDomainDescription" placeholder="')
                # SOURCE LINE 173
                __M_writer(filters.html_escape(loc.translate(_("Domain description"))))
                __M_writer('" value="')
                __M_writer(filters.html_escape(d.description))
                __M_writer('"/>\n\t\t</div>\n\n\t\t<div class="form-group">\n\t\t  <input type="hidden" name="mbUsername" id="mbUsername" value="')
                # SOURCE LINE 177
                __M_writer(filters.html_escape(accessuser.nick))
                __M_writer('">\n\t\t  <input type="hidden" name="did" id="did" value="')
                # SOURCE LINE 178
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n\t\t  <input type="hidden" name="csrf" value="')
                # SOURCE LINE 179
                __M_writer(filters.html_escape(req.get_csrf()))
                __M_writer('" />\n\t\t</div>\n\t    </div>\n\n            <div class="modal-footer">\n       \t      <input type="submit" value="')
                # SOURCE LINE 184
                __M_writer(filters.html_escape(loc.translate(_("Save"))))
                __M_writer('" class="btn btn-primary"/>\n\t\t\t      </form>\n')
                # SOURCE LINE 187
                __M_writer('              <button type="button" class="btn btn-default" data-dismiss="modal">')
                __M_writer(filters.html_escape(loc.translate(_("Close"))))
                __M_writer('</button>\n            </div>\n\t  </div>\n\t</div>\n      </div>\n')
                # SOURCE LINE 193
                __M_writer('      \n')
                # SOURCE LINE 195
                __M_writer('      <div class="modal fade" id="modalDomainDelete')
                __M_writer(filters.html_escape(d.id))
                __M_writer('" tabindex="-1" role="dialog" aria-labelledby="modalDeleteDomainLabel" aria-hidden="true">\n\t<div class="modal-dialog">\n\t  <div class="modal-content">\n            <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n            </div>\n            <div class="modal-body" id="domain')
                # SOURCE LINE 201
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n              <h4 class="modal-title">')
                # SOURCE LINE 202
                __M_writer(filters.html_escape(loc.translate(_("Really delete domain"))))
                __M_writer(' <strong>')
                __M_writer(filters.html_escape(d))
                __M_writer('</strong>?</h4>\n\t      <form method="POST" action="')
                # SOURCE LINE 203
                __M_writer(filters.html_escape(req.route_url("postfix.cl.delete")))
                __M_writer('" class="form-inline" role="form" id="domainDeleteform">\n\t\t<div class="form-group">\n\t\t  <input type="hidden" name="user" id="user" value="')
                # SOURCE LINE 205
                __M_writer(filters.html_escape(accessuser.nick))
                __M_writer('">\n\t\t  <input type="hidden" name="domainid" id="domainid" value="')
                # SOURCE LINE 206
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n\t\t  <input type="hidden" name="type" id="type" value="domain">\n\t\t  <input type="hidden" name="csrf" value="')
                # SOURCE LINE 208
                __M_writer(filters.html_escape(req.get_csrf()))
                __M_writer('" />\n\t\t</div>\n\t    </div>\n            <div class="modal-footer">\n       \t      <input type="submit" value="')
                # SOURCE LINE 212
                __M_writer(filters.html_escape(loc.translate(_("Delete"))))
                __M_writer('" class="btn btn-primary"/>\n\t      </form>\n              <button type="button" class="btn btn-default" data-dismiss="modal">')
                # SOURCE LINE 214
                __M_writer(filters.html_escape(loc.translate(_("Cancel"))))
                __M_writer('</button>\n            </div>\n\t  </div>\n\t</div>\n      </div>\n      \n')
                # SOURCE LINE 221
                __M_writer('      \n')
                # SOURCE LINE 224
                __M_writer('      <div class="modal fade" id="formModalMailbox')
                __M_writer(filters.html_escape(d.id))
                __M_writer('" tabindex="-1" role="dialog" aria-labelledby="formModalMailboxLabel" aria-hidden="true">\n\t<div class="modal-dialog modal-lg">\n\t  <div class="modal-content">\n\t    <div class="modal-header">\n\t      \n\t      <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t      <h4 class="modal-title" id="formModalMailboxLabel">')
                # SOURCE LINE 230
                __M_writer(filters.html_escape(loc.translate(_("New mailbox for "))))
                __M_writer(filters.html_escape(d.domain))
                __M_writer('</h4>\n\t      \n\t    </div>\n\t    <div class="modal-body">\n\t      \n\t      <form method="POST" action="')
                # SOURCE LINE 235
                __M_writer(filters.html_escape(req.route_url("postfix.cl.create")))
                __M_writer('" class="form-inline" role="form" id="createMailboxForm">\n')
                # SOURCE LINE 237
                __M_writer('\t\t<div class="form-group">\n\t\t  <input type="text" name="mbName" class="form-control" id="mbName" placeholder="')
                # SOURCE LINE 238
                __M_writer(filters.html_escape(loc.translate(_("mailbox"))))
                __M_writer('">\n\t\t</div>\n\t\t@\n\t\t<div class="form-group">\n\t\t  <select name="mbDomain" class="form-control" id="mbDomain" placeholder="')
                # SOURCE LINE 242
                __M_writer(filters.html_escape(loc.translate(_("domain"))))
                __M_writer('">\n')
                # SOURCE LINE 243
                for mbd in maildomains:
                    # SOURCE LINE 244
                    if mbd.id == d.id:	
                        # SOURCE LINE 245
                        __M_writer('       \t\t\t<option selected>')
                        __M_writer(filters.html_escape(mbd))
                        __M_writer('</option>\n')
                        # SOURCE LINE 246
                    else:
                        # SOURCE LINE 247
                        __M_writer('\t\t\t<option>')
                        __M_writer(filters.html_escape(mbd))
                        __M_writer('</option>\n')
                # SOURCE LINE 250
                __M_writer('\t\t  </select>\n\t\t</div>\n\t\t<div class="form-group">\n\t\t  <input type="password" name="mbPassword" class="form-control" id="mbPassword" placeholder="')
                # SOURCE LINE 253
                __M_writer(filters.html_escape(loc.translate(_("password"))))
                __M_writer('">\n\t\t  <input type="hidden" name="mbUsername" id="mbUsername" value="')
                # SOURCE LINE 254
                __M_writer(filters.html_escape(accessuser.nick))
                __M_writer('">\n\t\t  <input type="hidden" name="type" id="type" value="mbox">\n\t\t  <input type="hidden" name="csrf" value="')
                # SOURCE LINE 256
                __M_writer(filters.html_escape(req.get_csrf()))
                __M_writer('" />\n\t\t</div>\n\t\t\n\t    </div>\n\t    <div class="modal-footer">\n\t      <input type="submit" value="')
                # SOURCE LINE 261
                __M_writer(filters.html_escape(loc.translate(_("Create"))))
                __M_writer('" class="btn btn-primary"/>\n\t      </form>\n\t      \n\t      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t      \n\t    </div>\n\t  </div>\n\t</div>\n      </div>\n')
                # SOURCE LINE 271
                __M_writer('      \n')
            # SOURCE LINE 273
            __M_writer('    \n')
        # SOURCE LINE 275
        __M_writer('\n')
        # SOURCE LINE 277
        __M_writer('<div class="modal fade" id="formModalMailbox" tabindex="-1" role="dialog" aria-labelledby="formModalMailboxLabel" aria-hidden="true">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <div class="modal-header">\n\t\n\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t<h4 class="modal-title" id="formModalMailboxLabel">')
        # SOURCE LINE 283
        __M_writer(filters.html_escape(loc.translate(_("New mailbox"))))
        __M_writer('</h4>\n\t\n      </div>\n      <div class="modal-body">\n\t<form method="POST" action="')
        # SOURCE LINE 287
        __M_writer(filters.html_escape(req.route_url("postfix.cl.create")))
        __M_writer('" class="form-inline" role="form" id="createMailboxForm">\n\t  <div class="form-group">\n\t    <input type="text" name="mbName" class="form-control" id="mbName" placeholder="')
        # SOURCE LINE 289
        __M_writer(filters.html_escape(loc.translate(_("mailbox"))))
        __M_writer('"/>\n\t  </div>\n\t  @\n\t  <div class="form-group">\n\t    <select name="mbDomain" class="form-control" id="mbDomain" placeholder=')
        # SOURCE LINE 293
        __M_writer(filters.html_escape(loc.translate(_("domain"))))
        __M_writer('>\n')
        # SOURCE LINE 294
        for d in maildomains:
            # SOURCE LINE 295
            __M_writer('\t\t<option>')
            __M_writer(filters.html_escape(d))
            __M_writer('</option>\n')
        # SOURCE LINE 297
        __M_writer('\t    </select>\n\t  </div>\n\t  <div class="form-group">\n\t    <input type="password" name="mbPassword" class="form-control" id="mbPassword" placeholder="')
        # SOURCE LINE 300
        __M_writer(filters.html_escape(loc.translate(_("password"))))
        __M_writer('">\n\t    <input type="hidden" name="mbUsername" id="mbUsername" value="')
        # SOURCE LINE 301
        __M_writer(filters.html_escape(accessuser.nick))
        __M_writer('">\n\t    <input type="hidden" name="type" id="type" value="mbox">\n\t    <input type="hidden" name="csrf" value="')
        # SOURCE LINE 303
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('" />\n\t  </div>\n      </div>\n      <div class="modal-footer">\n\t<input type="submit" value="')
        # SOURCE LINE 307
        __M_writer(filters.html_escape(loc.translate(_("Create"))))
        __M_writer('" class="btn btn-primary"/>\n\t</form>\n\t<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n      </div>\n    </div>\n  </div>\n</div>\n')
        # SOURCE LINE 315
        __M_writer('\n')
        # SOURCE LINE 317
        __M_writer('<div class="modal fade" id="formModalDomain" tabindex="-1" role="dialog" aria-labelledby="formModalDomainLabel" aria-hidden="true">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <div class="modal-header">\n\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t<h4 class="modal-title" id="formModalDomainLabel">')
        # SOURCE LINE 322
        __M_writer(filters.html_escape(loc.translate(_("New domain attachment"))))
        __M_writer('</h4>\n      </div>\n      <div class="modal-body">\n\t<form method="POST" action="')
        # SOURCE LINE 325
        __M_writer(filters.html_escape(req.route_url("postfix.cl.create")))
        __M_writer('" class="form-inline" role="form" id="createDomainForm">\n\t  <div class="form-group">\n')
        # SOURCE LINE 328
        __M_writer('\t    <select name="mbDomain" class="form-control" id="mbDomain" placeholder=')
        __M_writer(filters.html_escape(loc.translate(_("Domain"))))
        __M_writer('>\n')
        # SOURCE LINE 329
        for ud in userdomains:
            # SOURCE LINE 330
            __M_writer('\t\t<option>')
            __M_writer(filters.html_escape(ud))
            __M_writer('</option>\n')
        # SOURCE LINE 332
        __M_writer('\t    </select>\n\t  </div>\n\t  <div class="form-group">\n\t    <input type="text" name="mbDomainDescription" class="form-control" id="mbDomainDescription" placeholder="')
        # SOURCE LINE 335
        __M_writer(filters.html_escape(loc.translate(_("Domain description"))))
        __M_writer('"/>\n\t  </div>\n\n\t  <div class="form-group">\n\t    <input type="hidden" name="mbUsername" id="mbUsername" value="')
        # SOURCE LINE 339
        __M_writer(filters.html_escape(accessuser.nick))
        __M_writer('">\n\t    <input type="hidden" name="type" id="type" value="domain">\n\t    <input type="hidden" name="csrf" value="')
        # SOURCE LINE 341
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('" />\n\t  </div>\n      </div>\n      <div class="modal-footer">\n\t<input type="submit" value="')
        # SOURCE LINE 345
        __M_writer(filters.html_escape(loc.translate(_("Create"))))
        __M_writer('" class="btn btn-primary"/>\n\t</form>\n\t<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n      </div>\n    </div>\n  </div>\n</div>\n')
        # SOURCE LINE 353
        __M_writer('</div>\n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


