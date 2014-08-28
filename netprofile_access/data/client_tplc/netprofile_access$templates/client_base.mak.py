# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1408616429.244039
_enable_loop = True
_template_filename = '/home/annndrey/test/git/npui/netprofile_access/netprofile_access/templates/client_base.mak'
_template_uri = 'netprofile_access$templates/client_base.mak'
_source_encoding = 'utf-8'
_exports = ['head', 'title']


# SOURCE LINE 2


from netprofile.tpl.filters import jsone_compact



def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def head():
            return render_head(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        req = context.get('req', UNDEFINED)
        cur_loc = context.get('cur_loc', UNDEFINED)
        next = context.get('next', UNDEFINED)
        comb_js = context.get('comb_js', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer('<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" lang="')
        # SOURCE LINE 8
        __M_writer(filters.html_escape(cur_loc))
        __M_writer('">\n<head>\n\t<meta charset="UTF-8" />\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge;chrome=1" />\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n\t<meta name="keywords" content="netprofile" />\n\t<meta name="description" content="NetProfile client UI" />\n\t<meta name="csrf-token" content="')
        # SOURCE LINE 15
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('" />\n')
        # SOURCE LINE 16
        if context.get('trans'):
            # SOURCE LINE 17
            __M_writer('\t<!-- ')
            __M_writer(filters.html_escape(trans))
            __M_writer(' -->\n\t<meta name="js-translations" content="')
            # SOURCE LINE 18
            __M_writer(filters.html_escape(jsone_compact(trans )))
            __M_writer('" />\n')
        # SOURCE LINE 20
        __M_writer('\t<title>NetProfile :: ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\n\t<link rel="shortcut icon" href="')
        # SOURCE LINE 21
        __M_writer(filters.html_escape(req.static_url('netprofile_access:static/favicon.ico')))
        __M_writer('" />\n')
        # SOURCE LINE 22
        if req.debug_enabled:
            # SOURCE LINE 23
            __M_writer('\t<link rel="stylesheet" href="')
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/bootstrap.css')))
            __M_writer('" type="text/css" />\n\t<link rel="stylesheet" href="')
            # SOURCE LINE 24
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/bootstrap-theme.css')))
            __M_writer('" type="text/css" />\n\t<link rel="stylesheet" href="')
            # SOURCE LINE 25
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/bootstrap-datetimepicker.css')))
            __M_writer('" type="text/css" />\n\t<link rel="stylesheet" href="')
            # SOURCE LINE 26
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/font-awesome.css')))
            __M_writer('" type="text/css" />\n\t<noscript><link rel="stylesheet" href="')
            # SOURCE LINE 27
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/jquery.fileupload-noscript.css')))
            __M_writer('" type="text/css" /></noscript>\n\t<noscript><link rel="stylesheet" href="')
            # SOURCE LINE 28
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/jquery.fileupload-ui-noscript.css')))
            __M_writer('" type="text/css" /></noscript>\n\t<!--[if lt IE 9]>\n\t\t<script type="text/javascript" src="')
            # SOURCE LINE 30
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/html5shiv.js')))
            __M_writer('"></script>\n\t\t<script type="text/javascript" src="')
            # SOURCE LINE 31
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/respond.src.js')))
            __M_writer('"></script>\n\t<![endif]-->\n')
            # SOURCE LINE 33
            if comb_js:
                # SOURCE LINE 34
                __M_writer('\t<script type="text/javascript" src="')
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/all.js')))
                __M_writer('"></script>\n')
                # SOURCE LINE 35
            else:
                # SOURCE LINE 36
                __M_writer('\t<script type="text/javascript" src="')
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 37
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.actual.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 38
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.ui.widget.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 39
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/chosen.jquery.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 40
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/moment.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 41
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/bootstrap.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 42
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/bootstrap-datetimepicker.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 43
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jqBootstrapValidation.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 44
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.iframe-transport.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 45
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.fileupload.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 46
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.fileupload-process.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 47
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.fileupload-validate.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 48
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.fileupload-ui.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 49
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/bootstrap-tooltip.js')))
                __M_writer('"></script>\n')
            # SOURCE LINE 51
        else:
            # SOURCE LINE 52
            __M_writer('\t<link rel="stylesheet" href="')
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/bootstrap.min.css')))
            __M_writer('" type="text/css" />\n\t<link rel="stylesheet" href="')
            # SOURCE LINE 53
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/bootstrap-theme.min.css')))
            __M_writer('" type="text/css" />\n\t<link rel="stylesheet" href="')
            # SOURCE LINE 54
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/bootstrap-datetimepicker.min.css')))
            __M_writer('" type="text/css" />\n\t<link rel="stylesheet" href="')
            # SOURCE LINE 55
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/font-awesome.min.css')))
            __M_writer('" type="text/css" />\n\t<noscript><link rel="stylesheet" href="')
            # SOURCE LINE 56
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/jquery.fileupload-noscript.css')))
            __M_writer('" type="text/css" /></noscript>\n\t<noscript><link rel="stylesheet" href="')
            # SOURCE LINE 57
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/jquery.fileupload-ui-noscript.css')))
            __M_writer('" type="text/css" /></noscript>\n\t<!--[if lt IE 9]>\n\t\t<script type="text/javascript" src="')
            # SOURCE LINE 59
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/html5shiv.min.js')))
            __M_writer('"></script>\n\t\t<script type="text/javascript" src="')
            # SOURCE LINE 60
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/respond.min.js')))
            __M_writer('"></script>\n\t<![endif]-->\n')
            # SOURCE LINE 62
            if comb_js:
                # SOURCE LINE 63
                __M_writer('\t<script type="text/javascript" src="')
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/all.min.js')))
                __M_writer('"></script>\n')
                # SOURCE LINE 64
            else:
                # SOURCE LINE 65
                __M_writer('\t<script type="text/javascript" src="')
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 66
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.actual.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 67
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.ui.widget.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 68
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/chosen.jquery.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 69
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/moment.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 70
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/bootstrap.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 71
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/bootstrap-datetimepicker.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 72
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jqBootstrapValidation.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 73
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.iframe-transport.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 74
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.fileupload.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 75
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.fileupload-process.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 76
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.fileupload-validate.min.js')))
                __M_writer('"></script>\n\t<script type="text/javascript" src="')
                # SOURCE LINE 77
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/jquery.fileupload-ui.min.js')))
                __M_writer('"></script>\n')
        # SOURCE LINE 80
        __M_writer('\t<link rel="stylesheet" href="')
        __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/client.css')))
        __M_writer('" type="text/css" />\n\t<noscript><link rel="stylesheet" href="')
        # SOURCE LINE 81
        __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/client-noscript.css')))
        __M_writer('" type="text/css" /></noscript>\n')
        # SOURCE LINE 82
        if not comb_js:
            # SOURCE LINE 83
            __M_writer('\t<script type="text/javascript" src="')
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/js/client.js')))
            __M_writer('"></script>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        # SOURCE LINE 85
        __M_writer('\n</head>\n<body>')
        # SOURCE LINE 87
        __M_writer(filters.html_escape(next.body()))
        __M_writer('</body>\n</html>\n')
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
        # SOURCE LINE 20
        __M_writer(filters.html_escape(_('User Portal', domain='netprofile_access')))
        return ''
    finally:
        context.caller_stack._pop_frame()


