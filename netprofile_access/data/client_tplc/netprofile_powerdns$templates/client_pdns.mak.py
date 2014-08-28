# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407085477.39622
_enable_loop = True
_template_filename = '/home/annndrey/test/npui/netprofile_powerdns/netprofile_powerdns/templates/client_pdns.mak'
_template_uri = 'netprofile_powerdns$templates/client_pdns.mak'
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
        req = context.get('req', UNDEFINED)
        accessuser = context.get('accessuser', UNDEFINED)
        domainrecords = context.get('domainrecords', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        userdomains = context.get('userdomains', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        # SOURCE LINE 6
        __M_writer('  <button class="btn btn-primary pull-right" data-toggle="modal" data-target="#formModalDomain">\n    <span class="glyphicon glyphicon-plus"></span>\n    ')
        # SOURCE LINE 8
        __M_writer(filters.html_escape(loc.translate(_("Create a new domain"))))
        __M_writer('\n  </button>\n')
        # SOURCE LINE 11
        __M_writer('\n  <h1>')
        # SOURCE LINE 12
        __M_writer(filters.html_escape(loc.translate(_("My domains"))))
        __M_writer('</h1>\n\n')
        # SOURCE LINE 14
        if userdomains is None:
            # SOURCE LINE 15
            __M_writer('  <div class="alert alert-warning">\n    ')
            # SOURCE LINE 16
            __M_writer(filters.html_escape(loc.translate(_("You have no domains yet. Add some?"))))
            __M_writer('\n  </div>\n\n')
            # SOURCE LINE 19
        else:
            # SOURCE LINE 20
            __M_writer('\n  <div class="panel-group" id="accordion">\n\n')
            # SOURCE LINE 23
            for d in userdomains:
                # SOURCE LINE 25
                __M_writer('      <div class="panel panel-default">\n\t<div class="panel-heading">\n\t  <div class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapse')
                # SOURCE LINE 28
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n\t    <span class="glyphicon glyphicon-th-list"></span> <strong>')
                # SOURCE LINE 29
                __M_writer(filters.html_escape(d))
                __M_writer('</strong></a> \n\t    <a data-toggle="modal" data-target="#formModalDomainRecord')
                # SOURCE LINE 30
                __M_writer(filters.html_escape(d.id))
                __M_writer('"><span class="glyphicon glyphicon-plus-sign"></span></a>\n\t    <a data-toggle=\'modal\' href=\'#modalEdit')
                # SOURCE LINE 31
                __M_writer(filters.html_escape(d.id))
                __M_writer('\'><span class="glyphicon glyphicon-pencil"</a> \n\t    <a data-toggle=\'modal\' href=\'#modalDeleteDomain')
                # SOURCE LINE 32
                __M_writer(filters.html_escape(d.id))
                __M_writer('\'><span class="glyphicon glyphicon-remove"></a> \n\t    <br>\n    \t    (should use popover or collapse from bootstrap for records block) <br>\n\t  </div>\n\t</div>\n\t<div id="collapse')
                # SOURCE LINE 37
                __M_writer(filters.html_escape(d.id))
                __M_writer('" class="panel-collapse collapse">\n\t  <div class="panel-body">\n\n')
                # SOURCE LINE 41
                if d.id in [r.domain_id for r in domainrecords]:
                    # SOURCE LINE 42
                    for r in domainrecords:
                        # SOURCE LINE 43
                        if r.domain_id == d.id:
                            # SOURCE LINE 44
                            __M_writer("\t\t  Here's the record:  ")
                            __M_writer(filters.html_escape(r))
                            __M_writer(" \n\t\t  <a data-toggle='modal' href='#modalRecordEdit")
                            # SOURCE LINE 45
                            __M_writer(filters.html_escape(r.id))
                            __M_writer('\'><span class="glyphicon glyphicon-pencil"></a> \n\t\t  <a data-toggle=\'modal\' href=\'#modalDeleteRecord')
                            # SOURCE LINE 46
                            __M_writer(filters.html_escape(r.id))
                            __M_writer('\'><span class="glyphicon glyphicon-remove"></a> \n\t\t  <br>\n\n')
                            # SOURCE LINE 50
                            __M_writer('\t\t  <div class="modal fade" id="modalDeleteRecord')
                            __M_writer(filters.html_escape(r.id))
                            __M_writer('" tabindex="-1" role="dialog" aria-labelledby="modalDeleteRecordLabel" aria-hidden="true">\n\t\t    <div class="modal-dialog">\n\t\t      <div class="modal-content">\n\t\t\t<div class="modal-header">\n\t\t\t  <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t\t</div>\n\t\t\t<div class="modal-body" id="domain')
                            # SOURCE LINE 56
                            __M_writer(filters.html_escape(d.id))
                            __M_writer('">\n\t\t\t  <h4 class="modal-title">')
                            # SOURCE LINE 57
                            __M_writer(filters.html_escape(loc.translate(_("Really delete record"))))
                            __M_writer(' <strong>')
                            __M_writer(filters.html_escape(r
												      ))
                            # SOURCE LINE 58
                            __M_writer('</strong>?</h4>\n\t\t\t  <form method="POST" action="')
                            # SOURCE LINE 59
                            __M_writer(filters.html_escape(req.route_url("pdns.cl.delete")))
                            __M_writer('" class="form-inline" role="form" id="deleteForm">\n\t\t\t    <div class="form-group">\n\t\t\t      <input type="hidden" name="user" id="user" value="')
                            # SOURCE LINE 61
                            __M_writer(filters.html_escape(accessuser.nick))
                            __M_writer('"\n\t\t\t      <input type="hidden" name="domainid" id="domainid" value="')
                            # SOURCE LINE 62
                            __M_writer(filters.html_escape(d.id))
                            __M_writer('">\n\t\t\t      <input type="hidden" name="recordid" id="recordid" value="')
                            # SOURCE LINE 63
                            __M_writer(filters.html_escape(r.id))
                            __M_writer('">\n\t\t\t      <input type="hidden" name="csrf" value="')
                            # SOURCE LINE 64
                            __M_writer(filters.html_escape(req.get_csrf()))
                            __M_writer('" />\n\t\t\t    </div>\n\t\t\t</div>\n\t\t\t<div class="modal-footer">\n       \t\t\t  <input type="submit" value="')
                            # SOURCE LINE 68
                            __M_writer(filters.html_escape(loc.translate(_("Delete"))))
                            __M_writer('" class="btn btn-primary"/>\n\t\t\t  </form>\n\t\t\t  <button type="button" class="btn btn-default" data-dismiss="modal">')
                            # SOURCE LINE 70
                            __M_writer(filters.html_escape(loc.translate(_("Cancel"))))
                            __M_writer('</button>\n\t\t\t</div>\n\t\t      </div>\n\t\t    </div>\n\t\t  </div>\n\t\t  \n')
                            # SOURCE LINE 77
                            __M_writer('\n')
                            # SOURCE LINE 79
                            __M_writer('\t\t  <div class="modal fade" id="modalRecordEdit')
                            __M_writer(filters.html_escape(r.id))
                            __M_writer('" tabindex="-1" role="dialog" aria-labelledby="formModalDomainRecordLabel')
                            __M_writer(filters.html_escape(r.id))
                            __M_writer('" aria-hidden="true">\n\t\t    <div class="modal-dialog modal-lg">\n\t\t      <div class="modal-content">\n\t\t\t<div class="modal-header">\n\t\t\t  \n\t\t\t  <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t\t  <h4 class="modal-title" id="formModalDomainRecordLabel')
                            # SOURCE LINE 85
                            __M_writer(filters.html_escape(r.id))
                            __M_writer('">')
                            __M_writer(filters.html_escape(loc.translate(_("Edit DNS record"))))
                            __M_writer('</h4>\n\t\t\t  \n\t\t\t</div>\n\t\t\t<div class="modal-body">\n\t\t\t  \n\t\t\t  <form method="POST" action="')
                            # SOURCE LINE 90
                            __M_writer(filters.html_escape(req.route_url("pdns.cl.edit")))
                            __M_writer('" class="form-inline" role="form" id="dnsForm">\n\t\t\t    <div class="form-group">\n\t\t\t      <input type="text" name="name" size="23" class="form-control" id="name" value="')
                            # SOURCE LINE 92
                            __M_writer(filters.html_escape(r.name))
                            __M_writer('"/>\n\t\t\t    </div>\n\t\t\t    \n\t\t\t    <div class="form-group">\n\t\t\t      <input type="text" name="content" class="form-control" id="content" value="')
                            # SOURCE LINE 96
                            __M_writer(filters.html_escape(r.content))
                            __M_writer('"/>\n\t\t\t    </div>\n\t\t\t    \n\t\t\t    <div class="form-group">\n\t\t\t      <select name="type" class="form-control" id="type">\n')
                            # SOURCE LINE 101
                            for o in ["A", "AAAA", "CNAME", "MX", "SOA", "TXT", "PRT", "HINFO", "SRV", "NAPTR"]:
                                # SOURCE LINE 102
                                if o == r.rtype:
                                    # SOURCE LINE 103
                                    __M_writer('       \t\t\t\t    <option selected>')
                                    __M_writer(filters.html_escape(o))
                                    __M_writer('</option>\n')
                                    # SOURCE LINE 104
                                else:
                                    # SOURCE LINE 105
                                    __M_writer('       \t\t\t\t    <option>')
                                    __M_writer(filters.html_escape(o))
                                    __M_writer('</option>\n')
                            # SOURCE LINE 108
                            __M_writer('\t\t\t      </select>\n\t\t\t    </div>\n\t\t\t    \n\t\t\t    <div class="form-group">\n\t\t\t      <input type="text" name="ttl" size="6" class="form-control" id="ttl" value="')
                            # SOURCE LINE 112
                            __M_writer(filters.html_escape(r.ttl))
                            __M_writer('"/>\n\t\t\t    </div>\n\n\n\t\t\t    <div class="form-group">\n\t\t\t      <input type="text" name="prio" size="4" class="form-control" id="prio" value="')
                            # SOURCE LINE 117
                            __M_writer(filters.html_escape(r.prio))
                            __M_writer('">\n\t\t\t      <input type="hidden" name="recordid" id="recordid" value="')
                            # SOURCE LINE 118
                            __M_writer(filters.html_escape(r.id))
                            __M_writer('">\n\t\t\t      <input type="hidden" name="type" id="type" value="record">\n\t\t\t      <input type="hidden" name="csrf" value="')
                            # SOURCE LINE 120
                            __M_writer(filters.html_escape(req.get_csrf()))
                            __M_writer('" />\n\t\t\t    </div>\n\t\t\t    \n\t\t\t</div>\n\t\t\t<div class="modal-footer">\n\t\t\t  <input type="submit" value="')
                            # SOURCE LINE 125
                            __M_writer(filters.html_escape(loc.translate(_("Save"))))
                            __M_writer('" class="btn btn-primary"/>\n\t\t\t  </form>\n\t\t\t  \n\t\t\t  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t\t\t  \n\t\t\t</div>\n\t\t      </div>\n\t\t    </div>\n\t\t  </div>\n')
                            # SOURCE LINE 135
                            __M_writer('\t\t  \n')
                    # SOURCE LINE 138
                else:
                    # SOURCE LINE 139
                    __M_writer('      \t      There\'s no records for this domain yet. <a data-toggle="modal" data-target="#formModalDomainRecord')
                    __M_writer(filters.html_escape(d.id))
                    __M_writer('"><span class="glyphicon glyphicon-plus-sign">Add one?</a>\n')
                # SOURCE LINE 141
                __M_writer('\n      </div>\n\t</div>\n      </div>\n      \n')
                # SOURCE LINE 147
                __M_writer('      <div class="modal fade" id="modalEdit')
                __M_writer(filters.html_escape(d.id))
                __M_writer('" tabindex="-1" role="dialog" aria-labelledby="modalEditLabel" aria-hidden="true">\n\t<div class="modal-dialog">\n\t  <div class="modal-content">\n            <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n              <h4 class="modal-title">')
                # SOURCE LINE 152
                __M_writer(filters.html_escape(loc.translate(_("Edit domain"))))
                __M_writer(' ')
                __M_writer(filters.html_escape(d))
                __M_writer('</h4>\n            </div>\n            <div class="modal-body" id="domain')
                # SOURCE LINE 154
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n\t      <form method="POST" action="')
                # SOURCE LINE 155
                __M_writer(filters.html_escape(req.route_url("pdns.cl.edit")))
                __M_writer('" class="form-inline" role="form" id="hostForm">\n\t\t\n     \t\t<div class="form-group">\n\t\t  <input type="text" name="hostName" class="form-control" id="hostName" value="')
                # SOURCE LINE 158
                __M_writer(filters.html_escape(d))
                __M_writer('"/>\n\t\t</div>\n\t\t\n\t\t<div class="form-group">\n\t\t  <select name="hostType" class="form-control" id="hosttype" placeholder=')
                # SOURCE LINE 162
                __M_writer(filters.html_escape(loc.translate(_("Host type"))))
                __M_writer('>\n')
                # SOURCE LINE 163
                for i in ["NATIVE", "MASTER", "SLAVE", "SUPERSLAVE"]:
                    # SOURCE LINE 164
                    if i == d.dtype:
                        # SOURCE LINE 165
                        __M_writer('\t\t\t<option selected>')
                        __M_writer(filters.html_escape(i))
                        __M_writer('</option>\n')
                        # SOURCE LINE 166
                    else:
                        # SOURCE LINE 167
                        __M_writer('\t\t\t<option>')
                        __M_writer(filters.html_escape(i))
                        __M_writer('</option>\n')
                # SOURCE LINE 170
                __M_writer('\t\t  </select>\t\n\t\t  \n\t\t  <input type="text" name="hostValue" class="form-control" id="hostValue" value="')
                # SOURCE LINE 172
                __M_writer(filters.html_escape(d.master))
                __M_writer('">\n\t\t  <input type="hidden" name="user" id="user" value="')
                # SOURCE LINE 173
                __M_writer(filters.html_escape(accessuser.nick))
                __M_writer('">\n\t\t  <input type="hidden" name="domainid" id="domainid" value="')
                # SOURCE LINE 174
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n\t\t  <input type="hidden" name="type" id="type" value="domain">\n\t\t  <input type="hidden" name="csrf" value="')
                # SOURCE LINE 176
                __M_writer(filters.html_escape(req.get_csrf()))
                __M_writer('" />\n\t\t</div>\n\t\t\n\t    </div>\n            <div class="modal-footer">\n       \t      <input type="submit" value="')
                # SOURCE LINE 181
                __M_writer(filters.html_escape(loc.translate(_("Save"))))
                __M_writer('" class="btn btn-primary"/>\n\t      </form>\n\t      \n              <button type="button" class="btn btn-default" data-dismiss="modal">')
                # SOURCE LINE 184
                __M_writer(filters.html_escape(loc.translate(_("Close"))))
                __M_writer('</button>\n            </div>\n\t  </div>\n\t</div>\n      </div>\n')
                # SOURCE LINE 190
                __M_writer('      \n')
                # SOURCE LINE 192
                __M_writer('      <div class="modal fade" id="modalDeleteDomain')
                __M_writer(filters.html_escape(d.id))
                __M_writer('" tabindex="-1" role="dialog" aria-labelledby="modalDeleteDomainLabel" aria-hidden="true">\n\t<div class="modal-dialog">\n\t  <div class="modal-content">\n            <div class="modal-header">\n              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n            </div>\n            <div class="modal-body" id="domain')
                # SOURCE LINE 198
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n              <h4 class="modal-title">')
                # SOURCE LINE 199
                __M_writer(filters.html_escape(loc.translate(_("Really delete domain"))))
                __M_writer(' <strong>')
                __M_writer(filters.html_escape(d))
                __M_writer('</strong>?</h4>\n\t      <form method="POST" action="')
                # SOURCE LINE 200
                __M_writer(filters.html_escape(req.route_url("pdns.cl.delete")))
                __M_writer('" class="form-inline" role="form" id="deleteForm">\n\t\t<div class="form-group">\n\t\t  <input type="hidden" name="user" id="user" value="')
                # SOURCE LINE 202
                __M_writer(filters.html_escape(accessuser.nick))
                __M_writer('">\n\t\t  <input type="hidden" name="domainid" id="domainid" value="')
                # SOURCE LINE 203
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n\t\t  <input type="hidden" name="csrf" value="')
                # SOURCE LINE 204
                __M_writer(filters.html_escape(req.get_csrf()))
                __M_writer('" />\n\t\t</div>\n\t    </div>\n            <div class="modal-footer">\n       \t      <input type="submit" value="')
                # SOURCE LINE 208
                __M_writer(filters.html_escape(loc.translate(_("Delete"))))
                __M_writer('" class="btn btn-primary"/>\n\t      </form>\n              <button type="button" class="btn btn-default" data-dismiss="modal">')
                # SOURCE LINE 210
                __M_writer(filters.html_escape(loc.translate(_("Cancel"))))
                __M_writer('</button>\n            </div>\n\t  </div>\n\t</div>\n      </div>\n      \n')
                # SOURCE LINE 217
                __M_writer('  \n')
                # SOURCE LINE 219
                __M_writer('  \n      <div class="modal fade" id="formModalDomainRecord')
                # SOURCE LINE 220
                __M_writer(filters.html_escape(d.id))
                __M_writer('" tabindex="-1" role="dialog" aria-labelledby="formModalDomainRecordLabel" aria-hidden="true">\n\t<div class="modal-dialog modal-lg">\n\t  <div class="modal-content">\n\t    <div class="modal-header">\n\t      \n\t      <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t      <h4 class="modal-title" id="formModalDomainRecordLabel">')
                # SOURCE LINE 226
                __M_writer(filters.html_escape(loc.translate(_("New DNS record"))))
                __M_writer('</h4>\n\t      \n\t    </div>\n\t    <div class="modal-body">\n\t      \n\t      <form method="POST" action="')
                # SOURCE LINE 231
                __M_writer(filters.html_escape(req.route_url("pdns.cl.create")))
                __M_writer('" class="form-inline" role="form" id="dnsForm">\n\t\t<div class="form-group">\n\t\t  <input type="text" name="name" size="23" class="form-control" id="name" placeholder="')
                # SOURCE LINE 233
                __M_writer(filters.html_escape(loc.translate(_("Name"))))
                __M_writer('">\n\t\t</div>\n\t\t\n\t\t<div class="form-group">\n\t\t  <input type="text" name="content" class="form-control" id="content" placeholder="')
                # SOURCE LINE 237
                __M_writer(filters.html_escape(loc.translate(_("Content"))))
                __M_writer('">\n\t\t</div>\n\t\t\n\t\t<div class="form-group">\n\t\t  <select name="type" class="form-control" id="type" placeholder="')
                # SOURCE LINE 241
                __M_writer(filters.html_escape(loc.translate(_("Record Type"))))
                __M_writer('">\n')
                # SOURCE LINE 242
                for o in ["A", "AAAA", "CNAME", "MX", "SOA", "TXT", "PRT", "HINFO", "SRV", "NAPTR"]:
                    # SOURCE LINE 243
                    __M_writer('       \t\t      <option>')
                    __M_writer(filters.html_escape(o))
                    __M_writer('</option>\n')
                # SOURCE LINE 245
                __M_writer('\t\t  </select>\n\t\t</div>\n\t\t<div class="form-group">\n\t\t  <input type="text" size="6" name="ttl" class="form-control" id="ttl" placeholder="')
                # SOURCE LINE 248
                __M_writer(filters.html_escape(loc.translate(_("TTL"))))
                __M_writer('">\n\t\t</div>\n\t\t\n\t\t<div class="form-group">\n\t\t  <input type="text" name="prio" size="15" class="form-control" id="prio" placeholder="')
                # SOURCE LINE 252
                __M_writer(filters.html_escape(loc.translate(_("MX-field priority"))))
                __M_writer('">\n\t\t  <input type="hidden" name="domainid" id="domainid" value="')
                # SOURCE LINE 253
                __M_writer(filters.html_escape(d.id))
                __M_writer('">\n\t\t  <input type="hidden" name="type" id="type" value="record">\n\t\t  <input type="hidden" name="csrf" value="')
                # SOURCE LINE 255
                __M_writer(filters.html_escape(req.get_csrf()))
                __M_writer('" />\n\t\t</div>\n\t\t\n\t    </div>\n\t    <div class="modal-footer">\n\t      <input type="submit" value="')
                # SOURCE LINE 260
                __M_writer(filters.html_escape(loc.translate(_("Create"))))
                __M_writer('" class="btn btn-primary"/>\n\t      </form>\n\t      \n\t      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t      \n\t    </div>\n\t  </div>\n\t</div>\n      </div>\n')
                # SOURCE LINE 270
                __M_writer('      \n')
            # SOURCE LINE 272
            __M_writer('    \n')
        # SOURCE LINE 274
        __M_writer('  \n  \n')
        # SOURCE LINE 277
        __M_writer('    <div class="modal fade" id="formModalDomain" tabindex="-1" role="dialog" aria-labelledby="formModalDomainLabel" aria-hidden="true">\n      <div class="modal-dialog">\n\t<div class="modal-content">\n\t  <div class="modal-header">\n\t    \n\t    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t    <h4 class="modal-title" id="formModalDomainLabel">')
        # SOURCE LINE 283
        __M_writer(filters.html_escape(loc.translate(_("New domain"))))
        __M_writer('</h4>\n\t    \n\t  </div>\n\t  <div class="modal-body">\n\t    <form method="POST" action="')
        # SOURCE LINE 287
        __M_writer(filters.html_escape(req.route_url("pdns.cl.create")))
        __M_writer('" class="form-inline" role="form" id="hostForm">\n\t      \n\t      <div class="form-group">\n\t\t<input type="text" name="hostName" class="form-control" id="hostName" placeholder="')
        # SOURCE LINE 290
        __M_writer(filters.html_escape(loc.translate(_("Enter host"))))
        __M_writer('"/>\n\t      </div>\n\t      \n\t      <div class="form-group">\n\t\t<select name="hostType" class="form-control" id="hosttype" placeholder=')
        # SOURCE LINE 294
        __M_writer(filters.html_escape(loc.translate(_("Host type"))))
        __M_writer('>\n')
        # SOURCE LINE 295
        for i in ["NATIVE", "MASTER", "SLAVE", "SUPERSLAVE"]:
            # SOURCE LINE 296
            __M_writer('\t\t    <option>')
            __M_writer(filters.html_escape(i))
            __M_writer('</option>\n')
        # SOURCE LINE 298
        __M_writer('\t\t</select>\n\t      </div>\n\t      \n\t      <div class="form-group">\n\t\t<input type="text" name="hostValue" class="form-control" id="hostValue" placeholder="')
        # SOURCE LINE 302
        __M_writer(filters.html_escape(loc.translate(_("Master nameserver IP"))))
        __M_writer('">\n\t\t<input type="hidden" name="user" id="user" value="')
        # SOURCE LINE 303
        __M_writer(filters.html_escape(accessuser.nick))
        __M_writer('">\n\t\t<input type="hidden" name="type" id="type" value="domain">\n\t\t<input type="hidden" name="csrf" value="')
        # SOURCE LINE 305
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('" />\n\t      </div>\n\t      \n\t  </div>\n\t  <div class="modal-footer">\n\t    <input type="submit" value="')
        # SOURCE LINE 310
        __M_writer(filters.html_escape(loc.translate(_("Create"))))
        __M_writer('" class="btn btn-primary"/>\n\t    </form>\n\t    \n\t    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t    \n\t  </div>\n\t</div>\n      </div>\n    </div>\n  </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


