# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1409229635.327899
_enable_loop = True
_template_filename = '/home/annndrey/test/git/npui/netprofile_access/netprofile_access/templates/client_chpass.mak'
_template_uri = 'netprofile_access$templates/client_chpass.mak'
_source_encoding = 'utf-8'
_exports = ['title']


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
        errors = context.get('errors', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        req = context.get('req', UNDEFINED)
        min_pwd_len = context.get('min_pwd_len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n\n<h1>')
        # SOURCE LINE 5
        __M_writer(filters.html_escape(_('Password Change Form')))
        __M_writer('</h1>\n')
        # SOURCE LINE 6
        if 'csrf' in errors:
            # SOURCE LINE 7
            __M_writer('<div class="alert alert-warning alert-dismissable">\n\t<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\n\t')
            # SOURCE LINE 9
            __M_writer(filters.html_escape(errors['csrf']))
            __M_writer('\n</div>\n')
        # SOURCE LINE 12
        __M_writer('\n<form method="post" novalidate="novalidate" action="')
        # SOURCE LINE 13
        __M_writer(filters.html_escape(req.route_url('access.cl.chpass')))
        __M_writer('" id="chpass-form" class="form-horizontal" role="form">\n<fieldset>\n\t<legend>')
        # SOURCE LINE 15
        __M_writer(filters.html_escape(_('Account Settings')))
        __M_writer('</legend>\n\t<div class="row form-group')
        # SOURCE LINE 16
        __M_writer(filters.html_escape(' has-warning' if 'oldpass' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="oldpass">')
        # SOURCE LINE 17
        __M_writer(filters.html_escape(_('Old Password')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="password"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="oldpass"\n\t\t\t\tname="oldpass"\n\t\t\t\ttitle="')
        # SOURCE LINE 25
        __M_writer(filters.html_escape(_('Enter your old password')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 26
        __M_writer(filters.html_escape(_('Enter your old password')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="2"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 31
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 32
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 36
        if 'oldpass' in errors:
            # SOURCE LINE 37
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['oldpass']))
            __M_writer('</li>\n')
        # SOURCE LINE 39
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n</fieldset>\n<fieldset>\n\t<legend>')
        # SOURCE LINE 44
        __M_writer(filters.html_escape(_('New Password')))
        __M_writer('</legend>\n\t<div class="row form-group')
        # SOURCE LINE 45
        __M_writer(filters.html_escape(' has-warning' if 'pass' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="pass">')
        # SOURCE LINE 46
        __M_writer(filters.html_escape(_('New Password')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="password"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="pass"\n\t\t\t\tname="pass"\n\t\t\t\ttitle="')
        # SOURCE LINE 54
        __M_writer(filters.html_escape(_('Enter your new desired password')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 55
        __M_writer(filters.html_escape(_('Enter your new desired password')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tminlength="')
        # SOURCE LINE 58
        __M_writer(filters.html_escape(str(min_pwd_len)))
        __M_writer('"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="2"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 61
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-minlength-message="')
        # SOURCE LINE 62
        __M_writer(filters.html_escape(_('This field is too short')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 63
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 67
        if 'pass' in errors:
            # SOURCE LINE 68
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['pass']))
            __M_writer('</li>\n')
        # SOURCE LINE 70
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n\t<div class="row form-group')
        # SOURCE LINE 73
        __M_writer(filters.html_escape(' has-warning' if 'pass2' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="pass2">')
        # SOURCE LINE 74
        __M_writer(filters.html_escape(_('Repeat Password')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="password"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="pass2"\n\t\t\t\tname="pass2"\n\t\t\t\ttitle="')
        # SOURCE LINE 82
        __M_writer(filters.html_escape(_('Repeat previously entered password')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 83
        __M_writer(filters.html_escape(_('Repeat previously entered password')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tminlength="')
        # SOURCE LINE 86
        __M_writer(filters.html_escape(str(min_pwd_len)))
        __M_writer('"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="3"\n\t\t\t\tdata-validation-match-match="pass"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 90
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-minlength-message="')
        # SOURCE LINE 91
        __M_writer(filters.html_escape(_('This field is too short')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 92
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t\tdata-validation-match-message="')
        # SOURCE LINE 93
        __M_writer(filters.html_escape(_('Passwords must match')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 97
        if 'pass2' in errors:
            # SOURCE LINE 98
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['pass2']))
            __M_writer('</li>\n')
        # SOURCE LINE 100
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n</fieldset>\n<div class="form-actions row">\n\t<p class="col-sm-4 legend"><span class="req">*</span> ')
        # SOURCE LINE 105
        __M_writer(filters.html_escape(_('Fields marked with this symbol are required.')))
        __M_writer('</p>\n\t<div class="controls col-sm-8">\n\t\t<input type="hidden" id="csrf" name="csrf" value="')
        # SOURCE LINE 107
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('" />\n\t\t<button type="submit" class="btn btn-primary btn-large" id="submit" name="submit" title="')
        # SOURCE LINE 108
        __M_writer(filters.html_escape(_('Change your password')))
        __M_writer('" tabindex="10">')
        __M_writer(filters.html_escape(_('Change Password')))
        __M_writer('</button>\n\t</div>\n</div>\n</form>\n\n')
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
        __M_writer(filters.html_escape(_('Change Password')))
        return ''
    finally:
        context.caller_stack._pop_frame()


