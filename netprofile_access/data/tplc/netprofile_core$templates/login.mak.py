# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407176814.505559
_enable_loop = True
_template_filename = '/home/annndrey/test/lib/python3.2/site-packages/netprofile_core-0.3-py3.2.egg/netprofile_core/templates/login.mak'
_template_uri = 'netprofile_core$templates/login.mak'
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
    return runtime._inherit_from(context, 'netprofile_core:templates/base.mak', _template_uri)
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
        failed = context.get('failed', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        # SOURCE LINE 6
        __M_writer('\n\n<form method="post" action="')
        # SOURCE LINE 8
        __M_writer(filters.html_escape(req.route_url('core.login')))
        __M_writer('">\n<div id="login_outer">\n\t<img alt="NetProfile" src="')
        # SOURCE LINE 10
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/img/nplogo.png')))
        __M_writer('" />\n\t<input type="hidden" id="csrf" name="csrf" value="')
        # SOURCE LINE 11
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('" />\n\t<input type="hidden" name="next" value="')
        # SOURCE LINE 12
        __M_writer(filters.html_escape(next))
        __M_writer('" />\n')
        # SOURCE LINE 13
        if failed:
            # SOURCE LINE 14
            __M_writer('\t<div class="elem errmsg">\n\t\t')
            # SOURCE LINE 15
            __M_writer(filters.html_escape(_('Authentication failed.')))
            __M_writer('\n\t</div>\n')
        # SOURCE LINE 18
        __M_writer('\t<div class="elem">\n\t\t<label for="user">')
        # SOURCE LINE 19
        __M_writer(filters.html_escape(_('User Name')))
        __M_writer('</label><br />\n\t\t<input type="text" class="text x-form-field x-form-required-field x-form-text" id="user" name="user" value="" size="28" maxlength="254" tabindex="1" style="width: 100%;" autocomplete="off" />\n\t</div>\n\t<div class="elem">\n\t\t<label for="pass">')
        # SOURCE LINE 23
        __M_writer(filters.html_escape(_('Password')))
        __M_writer('</label><br />\n\t\t<input type="password" class="text x-form-field x-form-required-field x-form-text" id="pass" name="pass" value="" size="28" maxlength="254" tabindex="2" style="width: 100%;" autocomplete="off" />\n\t</div>\n\t<div class="elem">\n\t\t<label for="__locale">')
        # SOURCE LINE 27
        __M_writer(filters.html_escape(_('Language')))
        __M_writer('</label><br />\n\t\t<select class="text" id="__locale" name="__locale" tabindex="3" style="width: 100%;" autocomplete="off">\n')
        # SOURCE LINE 29
        for lang in req.locales:
            # SOURCE LINE 30
            __M_writer('\t\t\t<option label="')
            __M_writer(filters.html_escape('%s [%s]' % (req.locales[lang].english_name, req.locales[lang].display_name)))
            __M_writer('" value="')
            __M_writer(filters.html_escape(lang))
            __M_writer('"')
            # SOURCE LINE 31
            if lang == cur_loc:
                # SOURCE LINE 32
                __M_writer(' selected="selected"')
            # SOURCE LINE 34
            __M_writer('>')
            __M_writer(filters.html_escape('%s [%s]' % (req.locales[lang].english_name, req.locales[lang].display_name)))
            __M_writer('</option>\n')
        # SOURCE LINE 36
        __M_writer('\t\t</select>\n\t</div>\n\t<div class="footer">\n\t\t<button type="submit" id="submit" name="submit" title="Log In" tabindex="4">')
        # SOURCE LINE 39
        __M_writer(filters.html_escape(_('Log In')))
        __M_writer('</button>\n\t</div>\n</div>\n</form>\n\n<script type="text/javascript">\n\tvar fld;\n\n\tfld = document.getElementById(\'user\');\n\tif(fld)\n\t{\n\t\tfld.value = \'\';\n\t\tfld.focus();\n\t}\n\n\tfld = document.getElementById(\'pass\');\n\tif(fld)\n\t\tfld.value = \'\';\n\n\tfunction on_change_lang()\n\t{\n\t\tvar f, q, re;\n\n\t\tf = document.getElementById(\'user\');\n\t\tif(f.value === \'\')\n\t\t{\n\t\t\tf = document.getElementById(\'__locale\');\n\t\t\tif(f)\n\t\t\t{\n\t\t\t\tq = window.location.search;\n\t\t\t\tif(q)\n\t\t\t\t{\n\t\t\t\t\tre = /__locale=[\\w_-]+/;\n\t\t\t\t\tif(q.match(re))\n\t\t\t\t\t\tq = q.replace(re, \'__locale=\' + f.value);\n\t\t\t\t\telse\n\t\t\t\t\t\tq += \'&__locale=\' + f.value;\n\t\t\t\t}\n\t\t\t\telse\n\t\t\t\t\tq = \'?__locale=\' + f.value;\n\t\t\t\twindow.location.search = q;\n\t\t\t}\n\t\t}\n\t\treturn false;\n\t}\n\n\tfld = document.getElementById(\'__locale\');\n\tif(fld)\n\t\tfld.onchange = on_change_lang;\n</script>\n\n')
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
        # SOURCE LINE 4
        __M_writer('\n\t<link rel="stylesheet" href="')
        # SOURCE LINE 5
        __M_writer(filters.html_escape(req.static_url('netprofile_core:static/css/login.css')))
        __M_writer('" type="text/css" media="screen, projection" />\n')
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


