# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407176818.913636
_enable_loop = True
_template_filename = '/home/annndrey/test/npui/netprofile_entities/netprofile_entities/templates/entity_data.mak'
_template_uri = 'netprofile_entities$templates/entity_data.mak'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        req = context.get('req', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('<tpl if="data.addrs && data.addrs.length">\n<tpl for="data.addrs">\n\t<div>\n\t\t<img class="np-inline-img" src="')
        # SOURCE LINE 4
        __M_writer(filters.html_escape(req.static_url('netprofile_entities:static/img/house_small.png')))
        __M_writer('" />\n\t\t{.}\n\t</div>\n</tpl>\n</tpl>\n<tpl if="data.address">\n\t<div>\n\t\t<img class="np-inline-img" src="')
        # SOURCE LINE 11
        __M_writer(filters.html_escape(req.static_url('netprofile_entities:static/img/house_small.png')))
        __M_writer('" />\n\t\t{data.address}\n\t</div>\n</tpl>\n<tpl if="data.phones && data.phones.length">\n\t<div>\n<tpl for="data.phones">\n\t<span>\n\t\t<img class="np-inline-img" src="')
        # SOURCE LINE 19
        __M_writer(filters.html_escape(req.static_url('netprofile_entities:static/img')))
        __M_writer('/{img}.png" />\n\t\t{str}\n\t</span>\n</tpl>\n\t</div>\n</tpl>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


