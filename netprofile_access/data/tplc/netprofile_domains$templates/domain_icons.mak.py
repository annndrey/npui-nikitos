# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407176819.178631
_enable_loop = True
_template_filename = '/home/annndrey/test/npui/netprofile_domains/netprofile_domains/templates/domain_icons.mak'
_template_uri = 'netprofile_domains$templates/domain_icons.mak'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        req = context.get('req', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('<tpl if="enabled">\n\t<img class="np-inline-img" src="')
        # SOURCE LINE 2
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/img/enabled.png')))
        __M_writer('" />\n<tpl else>\n\t<img class="np-inline-img" src="')
        # SOURCE LINE 4
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/img/disabled.png')))
        __M_writer('" />\n</tpl>\n<tpl if="public">\n\t<img class="np-inline-img" src="')
        # SOURCE LINE 7
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/img/public.png')))
        __M_writer('" />\n<tpl else>\n\t<img class="np-inline-img" src="')
        # SOURCE LINE 9
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/img/private.png')))
        __M_writer('" />\n</tpl>\n<tpl if="signed">\n\t<img class="np-inline-img" src="')
        # SOURCE LINE 12
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/img/lock.png')))
        __M_writer('" />\n<tpl else>\n\t<img class="np-inline-img" src="')
        # SOURCE LINE 14
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/img/unlock.png')))
        __M_writer('" />\n</tpl>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


