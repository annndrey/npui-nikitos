# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1408539248.268405
_enable_loop = True
_template_filename = '/home/annndrey/test/git/npui/netprofile_access/netprofile_access/templates/client_guest.mak'
_template_uri = 'netprofile_access$templates/client_guest.mak'
_source_encoding = 'utf-8'
_exports = ['menubar', 'title']


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
        next = context.get('next', UNDEFINED)
        def menubar():
            return render_menubar(context._locals(__M_locals))
        req = context.get('req', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menubar'):
            context['self'].menubar(**pageargs)
        

        # SOURCE LINE 6
        __M_writer('\n')
        # SOURCE LINE 7
        __M_writer(filters.html_escape(next.body()))
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menubar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        req = context.get('req', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        def menubar():
            return render_menubar(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n\t\t\t\t\t<li><a href="')
        # SOURCE LINE 5
        __M_writer(filters.html_escape(req.route_url('access.cl.login')))
        __M_writer('" title="')
        __M_writer(filters.html_escape(_('Go back to login page')))
        __M_writer('">')
        __M_writer(filters.html_escape(_('Already Registered')))
        __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(filters.html_escape(_('Register')))
        return ''
    finally:
        context.caller_stack._pop_frame()


