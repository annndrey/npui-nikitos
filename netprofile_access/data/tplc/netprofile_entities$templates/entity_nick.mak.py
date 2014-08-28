# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407176818.875489
_enable_loop = True
_template_filename = '/home/annndrey/test/npui/netprofile_entities/netprofile_entities/templates/entity_nick.mak'
_template_uri = 'netprofile_entities$templates/entity_nick.mak'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        req = context.get('req', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('{__str__}\n<tpl if="data.flags && data.flags.length">\n\t<br />\n\t<tpl for="data.flags">\n\t\t<img class="np-inline-img" src="')
        # SOURCE LINE 5
        __M_writer(filters.html_escape(req.static_url('netprofile_entities:static/img/flags/')))
        __M_writer('{0}.png" alt="{1}" />\n\t</tpl>\n</tpl>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


