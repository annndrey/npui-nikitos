# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407176818.682889
_enable_loop = True
_template_filename = '/home/annndrey/test/lib/python3.2/site-packages/netprofile_core-0.3-py3.2.egg/netprofile_core/templates/np.mak'
_template_uri = 'netprofile_core$templates/np.mak'
_source_encoding = 'utf-8'
_exports = ['jscap', 'limit']


# SOURCE LINE 2


from pyramid.security import has_permission



def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer('\n\n')
        # SOURCE LINE 16
        __M_writer('\n\n')
        # SOURCE LINE 22
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_jscap(context,code):
    __M_caller = context.caller_stack._push_frame()
    try:
        req = context.get('req', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 9
        if code is None:
            # SOURCE LINE 10
            __M_writer('true')
            # SOURCE LINE 11
        elif has_permission(code, req.context, req):
            # SOURCE LINE 12
            __M_writer('true')
            # SOURCE LINE 13
        else:
            # SOURCE LINE 14
            __M_writer('false')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_limit(context,cap=None,xcap=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        req = context.get('req', UNDEFINED)
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 19
        if ((cap is None) or ((cap is not None) and has_permission(cap, req.context, req))) and ((xcap is None) or ((xcap is not None) and (not has_permission(xcap, req.context, req)))):
            # SOURCE LINE 20
            __M_writer(filters.html_escape(caller.body()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


