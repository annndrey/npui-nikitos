# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407176814.518601
_enable_loop = True
_template_filename = '/home/annndrey/test/lib/python3.2/site-packages/netprofile_core-0.3-py3.2.egg/netprofile_core/templates/base.mak'
_template_uri = 'netprofile_core$templates/base.mak'
_source_encoding = 'utf-8'
_exports = ['head', 'title']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        res_ljs = context.get('res_ljs', UNDEFINED)
        def head():
            return render_head(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        req = context.get('req', UNDEFINED)
        res_css = context.get('res_css', UNDEFINED)
        res_js = context.get('res_js', UNDEFINED)
        cur_loc = context.get('cur_loc', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" lang="')
        # SOURCE LINE 3
        __M_writer(filters.html_escape(cur_loc))
        __M_writer('">\n<head>\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge;chrome=1" />\n\t<meta name="keywords" content="netprofile" />\n\t<meta name="description" content="NetProfile administrative UI" />\n\t<title>NetProfile :: ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 9
        __M_writer('</title>\n\t<link rel="shortcut icon" href="')
        # SOURCE LINE 10
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/favicon.ico')))
        __M_writer('" />\n')
        # SOURCE LINE 11
        for i_css in res_css:
            # SOURCE LINE 12
            __M_writer('\t<link rel="stylesheet" href="')
            __M_writer(filters.html_escape(req.static_url(i_css)))
            __M_writer('" type="text/css" media="screen, projection" />\n')
        # SOURCE LINE 14
        for i_js in res_js:
            # SOURCE LINE 15
            __M_writer('\t<script type="text/javascript" src="')
            __M_writer(filters.html_escape(req.static_url(i_js)))
            __M_writer('" charset="UTF-8"></script>\n')
        # SOURCE LINE 17
        if (cur_loc is not None) and (cur_loc != 'en'):
            # SOURCE LINE 18
            for i_js in res_ljs:
                # SOURCE LINE 19
                __M_writer('    <script type="text/javascript" src="')
                __M_writer(filters.html_escape(req.static_url(i_js)))
                __M_writer('" charset="UTF-8"></script>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        # SOURCE LINE 22
        __M_writer('\n</head>\n<body>')
        # SOURCE LINE 24
        __M_writer(filters.html_escape(self.body()))
        __M_writer('</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head():
            return render_head(context)
        __M_writer = context.writer()
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
        # SOURCE LINE 9
        __M_writer(filters.html_escape(_('Home')))
        return ''
    finally:
        context.caller_stack._pop_frame()


