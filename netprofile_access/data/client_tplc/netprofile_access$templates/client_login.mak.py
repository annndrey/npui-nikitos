# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1409231706.719626
_enable_loop = True
_template_filename = '/home/annndrey/test/git/npui/netprofile_access/netprofile_access/templates/client_login.mak'
_template_uri = 'netprofile_access$templates/client_login.mak'
_source_encoding = 'utf-8'
_exports = ['head', 'title']


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
        def head():
            return render_head(context._locals(__M_locals))
        can_recover = context.get('can_recover', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        can_usesocial = context.get('can_usesocial', UNDEFINED)
        req = context.get('req', UNDEFINED)
        cur_loc = context.get('cur_loc', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        can_reg = context.get('can_reg', UNDEFINED)
        login_providers = context.get('login_providers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        # SOURCE LINE 16
        __M_writer('\n\n<div class="container">\n<form class="form-signin" role="form" method="post" action="')
        # SOURCE LINE 19
        __M_writer(filters.html_escape(req.route_url('access.cl.login')))
        __M_writer('">\n\t<h2 class="form-signin-heading">')
        # SOURCE LINE 20
        __M_writer(filters.html_escape(_('Log In')))
        __M_writer('</h2>\n')
        # SOURCE LINE 21
        for msg in req.session.pop_flash():
            # SOURCE LINE 22
            __M_writer('\t<div class="alert alert-')
            __M_writer(filters.html_escape(msg['class'] if 'class' in msg else 'success'))
            __M_writer(' alert-dismissable" role="alert">\n\t\t<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\n\t\t')
            # SOURCE LINE 24
            __M_writer(filters.html_escape(msg['text']))
            __M_writer('\n\t</div>\n')
        # SOURCE LINE 27
        __M_writer('\t<input type="hidden" id="csrf" name="csrf" value="')
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('" />\n\t<input type="text" class="form-control" placeholder="')
        # SOURCE LINE 28
        __M_writer(filters.html_escape(_('User Name')))
        __M_writer('" required="required" autofocus="autofocus" id="user" name="user" title="')
        __M_writer(filters.html_escape(_('Enter your user name here')))
        __M_writer('" value="" maxlength="254" tabindex="1" autocomplete="off" />\n\t<input type="password" class="form-control" placeholder="')
        # SOURCE LINE 29
        __M_writer(filters.html_escape(_('Password')))
        __M_writer('" required="required" id="pass" name="pass" title="')
        __M_writer(filters.html_escape(_('Enter your password here')))
        __M_writer('" value="" maxlength="254" tabindex="2" autocomplete="off" />\n\t<button type="submit" class="btn btn-lg btn-primary btn-block" id="submit" name="submit" title="')
        # SOURCE LINE 30
        __M_writer(filters.html_escape(_('Log in to your account')))
        __M_writer('" tabindex="3">')
        __M_writer(filters.html_escape(_('Log In')))
        __M_writer('</button>\n</form>\n<form class="form-signin" role="form" method="get" action="')
        # SOURCE LINE 32
        __M_writer(filters.html_escape(req.route_url('access.cl.login')))
        __M_writer('">\n\t<div class="input-group">\n\t\t<label class="input-group-addon" for="__locale">')
        # SOURCE LINE 34
        __M_writer(filters.html_escape(_('Language')))
        __M_writer('</label>\n\t\t<select class="form-control chosen-select" id="__locale" name="__locale" tabindex="4">\n')
        # SOURCE LINE 36
        for lang in req.locales:
            # SOURCE LINE 37
            __M_writer('\t\t\t<option label="')
            __M_writer(filters.html_escape('%s [%s]' % (req.locales[lang].english_name, req.locales[lang].display_name)))
            __M_writer('" value="')
            __M_writer(filters.html_escape(lang))
            __M_writer('"')
            # SOURCE LINE 38
            if lang == cur_loc:
                # SOURCE LINE 39
                __M_writer(' selected="selected"')
            # SOURCE LINE 41
            __M_writer('>')
            __M_writer(filters.html_escape('%s [%s]' % (req.locales[lang].english_name, req.locales[lang].display_name)))
            __M_writer('</option>\n')
        # SOURCE LINE 43
        __M_writer('\t\t</select>\n\t\t<span class="input-group-btn">\n\t\t\t<button type="submit" class="btn btn-default" id="lang_submit" title="')
        # SOURCE LINE 45
        __M_writer(filters.html_escape(_('Change your current language')))
        __M_writer('">')
        __M_writer(filters.html_escape(_('Change')))
        __M_writer('</button>\n\t\t</span>\n\t</div>\n\t<div>\n')
        # SOURCE LINE 49
        if can_reg:
            # SOURCE LINE 50
            __M_writer('\t\t<a href="')
            __M_writer(filters.html_escape(req.route_url('access.cl.register')))
            __M_writer('" id="register" class="btn btn-default" title="')
            __M_writer(filters.html_escape(_('Register new account')))
            __M_writer('" tabindex="5">')
            __M_writer(filters.html_escape(_('Register')))
            __M_writer('</a>\n')
        # SOURCE LINE 52
        if can_recover:
            # SOURCE LINE 53
            __M_writer('\t\t<a href="')
            __M_writer(filters.html_escape(req.route_url('access.cl.restorepass')))
            __M_writer('" id="restorepass" class="btn btn-info pull-right" title="')
            __M_writer(filters.html_escape(_('Recover lost password via e-mail')))
            __M_writer('" tabindex="6">')
            __M_writer(filters.html_escape(_('Lost Password?')))
            __M_writer('</a>\n')
        # SOURCE LINE 55
        if can_usesocial:
            # SOURCE LINE 56
            __M_writer('                <a href="#" id=\'registersocial\' class="btn btn-default" data-toggle="popover" title="')
            __M_writer(filters.html_escape(_('Login with...')))
            __M_writer('" data-content=\'\n')
            # SOURCE LINE 57
            for lp in login_providers.keys():
                # SOURCE LINE 58
                __M_writer('\t\t   <span><a href="')
                __M_writer(filters.html_escape(req.route_url('access.cl.oauthwrapper')))
                __M_writer('?prov=')
                __M_writer(filters.html_escape(lp.lower()))
                __M_writer('"><img src="')
                __M_writer(filters.html_escape(req.static_url('netprofile_access:static/img/loginproviders/%s.png' % lp)))
                __M_writer('" title="')
                __M_writer(filters.html_escape(lp.capitalize()))
                __M_writer('"></a><span>\n')
            # SOURCE LINE 60
            __M_writer("\t\t  '>")
            __M_writer(filters.html_escape(_('Login with...')))
            __M_writer('</a>\n')
        # SOURCE LINE 62
        __M_writer('\t</div>\n</form>\n\n</div>\n\n')
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
        # SOURCE LINE 5
        __M_writer('\t<link rel="stylesheet" href="')
        __M_writer(filters.html_escape(req.static_url('netprofile_access:static/css/login.css')))
        __M_writer('" type="text/css" />\n\n<script type="text/javascript">\n$(document).ready(function(){\n   $("#registersocial").popover({\n     placement : \'bottom\',\n     html : \'true\'\n    });\n});\n</script>\n\n')
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
        __M_writer(filters.html_escape(_('Log In')))
        return ''
    finally:
        context.caller_stack._pop_frame()


