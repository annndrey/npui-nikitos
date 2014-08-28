# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407176818.205914
_enable_loop = True
_template_filename = '/home/annndrey/test/lib/python3.2/site-packages/netprofile_core-0.3-py3.2.egg/netprofile_core/templates/home.mak'
_template_uri = 'netprofile_core$templates/home.mak'
_source_encoding = 'utf-8'
_exports = ['head']


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
    return runtime._inherit_from(context, 'netprofile_core:templates/base.mak', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def head():
            return render_head(context._locals(__M_locals))
        req = context.get('req', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        # SOURCE LINE 9
        __M_writer('\n\n\t<!-- Fields required for b/c history management -->\n\t<form id="history-form" class="x-hide-display">\n\t\t<input type="hidden" id="x-history-field" />\n\t\t<iframe id="x-history-frame"></iframe>\n\t</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head():
            return render_head(context)
        req = context.get('req', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n\t<script type="text/javascript">//<![CDATA[\n\t\tExt.BLANK_IMAGE_URL = \'')
        # SOURCE LINE 5
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/extjs/resources/themes/images/default/tree/s.gif')))
        __M_writer('\';\n\t//]]></script>\n\t<script type="text/javascript" src="')
        # SOURCE LINE 7
        __M_writer(filters.html_escape(req.route_url('extapi')))
        __M_writer('" charset="UTF-8"></script>\n\t<script type="text/javascript" src="')
        # SOURCE LINE 8
        __M_writer(filters.html_escape(req.route_url('core.js.webshell')))
        __M_writer('" charset="UTF-8"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


