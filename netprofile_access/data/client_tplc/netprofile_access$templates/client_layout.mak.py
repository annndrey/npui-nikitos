# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407085477.46558
_enable_loop = True
_template_filename = '/home/annndrey/test/npui/netprofile_access/netprofile_access/templates/client_layout.mak'
_template_uri = 'netprofile_access$templates/client_layout.mak'
_source_encoding = 'utf-8'
_exports = ['menubar']


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
    return runtime._inherit_from(context, 'netprofile_access:templates/client_base.mak', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        loc = context.get('loc', UNDEFINED)
        menu = context.get('menu', UNDEFINED)
        self = context.get('self', UNDEFINED)
        req = context.get('req', UNDEFINED)
        next = context.get('next', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        def menubar():
            return render_menubar(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n<div id="wrap">\n\t<nav class="navbar navbar-default navbar-fixed-top" role="navigation">\n\t\t<div class="container">\n\t\t\t<div class="navbar-header">\n\t\t\t\t<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#main-navbar">\n\t\t\t\t\t<span class="sr-only">')
        # SOURCE LINE 9
        __M_writer(filters.html_escape(_('Toggle navigation', domain='netprofile_access')))
        __M_writer('</span>\n\t\t\t\t\t<span class="icon-bar"></span>\n\t\t\t\t\t<span class="icon-bar"></span>\n\t\t\t\t\t<span class="icon-bar"></span>\n\t\t\t\t</button>\n\t\t\t\t<span class="navbar-brand" href="#">\n\t\t\t\t\t<span class="large">NetProfile</span>\n\t\t\t\t\t<span class="small">')
        # SOURCE LINE 16
        __M_writer(filters.html_escape(self.title()))
        __M_writer('</span>\n\t\t\t\t</span>\n\t\t\t</div>\n\t\t\t<div class="collapse navbar-collapse" id="main-navbar">\n\t\t\t\t<ul class="no-js nav navbar-nav navbar-right">\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menubar'):
            context['self'].menubar(**pageargs)
        

        # SOURCE LINE 39
        __M_writer('\n\t\t\t\t\t<li class="dropdown">\n\t\t\t\t\t\t<a href="#" class="dropdown-toggle flag-toggle" data-toggle="dropdown" id="flag-toggle" title="')
        # SOURCE LINE 41
        __M_writer(filters.html_escape(_('Change Language', domain='netprofile_access')))
        __M_writer('">\n\t\t\t\t\t\t\t<img src="')
        # SOURCE LINE 42
        __M_writer(filters.html_escape(req.static_url('netprofile_access:static/img/flags/%s.png' % req.locale_name)))
        __M_writer('" alt="')
        __M_writer(filters.html_escape(_('Currently Selected Language', domain='netprofile_access')))
        __M_writer('" />\n\t\t\t\t\t\t\t<b class="caret"></b>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="flag-toggle">\n')
        # SOURCE LINE 46
        for lang in req.locales:
            # SOURCE LINE 47
            __M_writer('\t\t\t\t\t\t\t<li')
            # SOURCE LINE 48
            if lang == req.locale_name:
                # SOURCE LINE 49
                __M_writer(' class="disabled"')
            # SOURCE LINE 51
            __M_writer('><a class="lang-select" href="')
            __M_writer(filters.html_escape(req.current_route_url(_query={'__locale' : lang})))
            __M_writer('" role="menuitem" tabindex="-1">\n\t\t\t\t\t\t\t\t<img src="')
            # SOURCE LINE 52
            __M_writer(filters.html_escape(req.static_url('netprofile_access:static/img/flags/%s.png' % lang)))
            __M_writer('" />\n\t\t\t\t\t\t\t\t')
            # SOURCE LINE 53
            __M_writer(filters.html_escape(req.locales[lang].english_name))
            __M_writer(' [')
            __M_writer(filters.html_escape(req.locales[lang].display_name))
            __M_writer(']\n\t\t\t\t\t\t\t</a></li>\n')
        # SOURCE LINE 56
        __M_writer('\t\t\t\t\t\t</ul>\n\t\t\t\t\t</li>\n')
        # SOURCE LINE 58
        if req.user:
            # SOURCE LINE 59
            __M_writer('\t\t\t\t\t<li class="dropdown">\n\t\t\t\t\t\t<a href="#" class="dropdown-toggle" data-toggle="dropdown" id="user-toggle" title="')
            # SOURCE LINE 60
            __M_writer(filters.html_escape(_('User Menu', domain='netprofile_access')))
            __M_writer('">\n\t\t\t\t\t\t\t<span class="glyphicon glyphicon-user"></span>\n\t\t\t\t\t\t\t')
            # SOURCE LINE 62
            __M_writer(filters.html_escape(req.user.nick))
            __M_writer('\n\t\t\t\t\t\t\t<b class="caret"></b>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="user-toggle">\n\t\t\t\t\t\t\t<li><a href="')
            # SOURCE LINE 66
            __M_writer(filters.html_escape(req.route_url('access.cl.chpass')))
            __M_writer('" role="menuitem" tabindex="-1">')
            __M_writer(filters.html_escape(_('Change Password', domain='netprofile_access')))
            __M_writer('</a></li>\n\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t<li><a href="')
            # SOURCE LINE 68
            __M_writer(filters.html_escape(req.route_url('access.cl.logout')))
            __M_writer('" role="menuitem" tabindex="-1"><span class="glyphicon glyphicon-log-out"></span> ')
            __M_writer(filters.html_escape(_('Log Out', domain='netprofile_access')))
            __M_writer('</a></li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</li>\n')
        # SOURCE LINE 72
        __M_writer('\t\t\t\t</ul>\n\t\t\t</div>\n\t\t</div>\n\t</nav>\n\n\t<div class="container" role="main">\n')
        # SOURCE LINE 78
        if context.get('crumbs'):
            # SOURCE LINE 79
            __M_writer('\t<ol class="breadcrumb">\n')
            # SOURCE LINE 80
            for cr in crumbs:
                # SOURCE LINE 81
                __M_writer('\t\t<li')
                __M_writer(filters.html_escape(' class="active"' if ('url' not in cr) else ''))
                __M_writer('>\n')
                # SOURCE LINE 82
                if 'url' in cr:
                    # SOURCE LINE 83
                    __M_writer('\t\t\t<a href="')
                    __M_writer(filters.html_escape(cr['url']))
                    __M_writer('">')
                    __M_writer(filters.html_escape(cr['text']))
                    __M_writer('</a>\n')
                    # SOURCE LINE 84
                else:
                    # SOURCE LINE 85
                    __M_writer('\t\t\t')
                    __M_writer(filters.html_escape(cr['text']))
                    __M_writer('\n')
                # SOURCE LINE 87
                __M_writer('\t\t</li>\n')
            # SOURCE LINE 89
            __M_writer('\t</ol>\n')
        # SOURCE LINE 91
        for msg in req.session.pop_flash():
            # SOURCE LINE 92
            __M_writer('\n\t<div class="alert alert-')
            # SOURCE LINE 93
            __M_writer(filters.html_escape(msg['class'] if 'class' in msg else 'success'))
            __M_writer(' alert-dismissable" role="alert">\n\t\t<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\n\t\t')
            # SOURCE LINE 95
            __M_writer(filters.html_escape(msg['text']))
            __M_writer('\n\t</div>\n\n')
        # SOURCE LINE 99
        __M_writer(filters.html_escape(next.body()))
        __M_writer('\n\t</div>\n</div>\n\n<div id="footer" role="banner">\n\t<span class="single-line">Copyright © 2013-2014 <a href="http://netprofile.ru">')
        # SOURCE LINE 104
        __M_writer(filters.html_escape(_('NetProfile.ru Team', domain='netprofile_access')))
        __M_writer('</a>.</span>\n\t<span class="single-line">')
        # SOURCE LINE 105
        __M_writer(filters.html_escape(_('License:', domain='netprofile_access')))
        __M_writer(' <a href="http://www.gnu.org/licenses/agpl-3.0.html">AGPLv3</a>+</span>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menubar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        menu = context.get('menu', UNDEFINED)
        req = context.get('req', UNDEFINED)
        loc = context.get('loc', UNDEFINED)
        def menubar():
            return render_menubar(context)
        __M_writer = context.writer()
        # SOURCE LINE 22
        for item in menu:
            # SOURCE LINE 23
            if item.get('route') and req.matched_route and (item.get('route') == req.matched_route.name):
                # SOURCE LINE 24
                __M_writer('\t\t\t\t\t<li class="active">\n\t\t\t\t\t\t<a href="#">')
                # SOURCE LINE 25
                __M_writer(filters.html_escape(loc.translate(item['text'])))
                __M_writer('</a>\n')
                # SOURCE LINE 26
            elif item.get('route'):
                # SOURCE LINE 27
                __M_writer('\t\t\t\t\t<li')
                # SOURCE LINE 28
                if item.get('cls'):
                    # SOURCE LINE 29
                    __M_writer(' class="')
                    __M_writer(filters.html_escape(item['cls']))
                    __M_writer('"')
                # SOURCE LINE 31
                if item.get('title'):
                    # SOURCE LINE 32
                    __M_writer(' title="')
                    __M_writer(filters.html_escape(loc.translate(item['title'])))
                    __M_writer('"')
                # SOURCE LINE 34
                __M_writer('>\n\t\t\t\t\t\t<a href="')
                # SOURCE LINE 35
                __M_writer(filters.html_escape(req.route_url(item['route'], traverse=())))
                __M_writer('">')
                __M_writer(filters.html_escape(loc.translate(item['text'])))
                __M_writer('</a>\n')
            # SOURCE LINE 37
            __M_writer('\t\t\t\t\t</li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


