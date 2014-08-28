# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1408539248.221302
_enable_loop = True
_template_filename = '/home/annndrey/test/git/npui/netprofile_access/netprofile_access/templates/client_register.mak'
_template_uri = 'netprofile_access$templates/client_register.mak'
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
    return runtime._inherit_from(context, 'netprofile_access:templates/client_guest.mak', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        errors = context.get('errors', UNDEFINED)
        must_recaptcha = context.get('must_recaptcha', UNDEFINED)
        req = context.get('req', UNDEFINED)
        min_pwd_len = context.get('min_pwd_len', UNDEFINED)
        rc_public = context.get('rc_public', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        must_verify = context.get('must_verify', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n\n<h1>')
        # SOURCE LINE 5
        __M_writer(filters.html_escape(_('Registration Form')))
        __M_writer('</h1>\n<p>')
        # SOURCE LINE 6
        __M_writer(filters.html_escape(_('Please fill in this form so we can properly set up your account.')))
        __M_writer('</p>\n')
        # SOURCE LINE 7
        if must_verify:
            # SOURCE LINE 8
            __M_writer('<p><strong>')
            __M_writer(filters.html_escape(_('Note:')))
            __M_writer('</strong> ')
            __M_writer(filters.html_escape(_('You will receive a confirmation e-mail with an activation link. Your account will be inactive until you click this link.')))
            __M_writer('</p>\n')
        # SOURCE LINE 10
        if 'csrf' in errors:
            # SOURCE LINE 11
            __M_writer('<div class="alert alert-warning alert-dismissable">\n\t<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\n\t')
            # SOURCE LINE 13
            __M_writer(filters.html_escape(errors['csrf']))
            __M_writer('\n</div>\n')
        # SOURCE LINE 16
        __M_writer('\n<form method="post" novalidate="novalidate" action="')
        # SOURCE LINE 17
        __M_writer(filters.html_escape(req.route_url('access.cl.register')))
        __M_writer('" id="register-form" class="form-horizontal" role="form">\n<fieldset>\n\t<legend>')
        # SOURCE LINE 19
        __M_writer(filters.html_escape(_('Account Settings')))
        __M_writer('</legend>\n\t<div class="row form-group')
        # SOURCE LINE 20
        __M_writer(filters.html_escape(' has-warning' if 'user' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="user">')
        # SOURCE LINE 21
        __M_writer(filters.html_escape(_('User Name')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="text"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="user"\n\t\t\t\tname="user"\n\t\t\t\ttitle="')
        # SOURCE LINE 29
        __M_writer(filters.html_escape(_('Enter your user name here')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 30
        __M_writer(filters.html_escape(_('Enter your user name here')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tmaxlength="254"\n\t\t\t\tpattern="[\\w\\d._-]+"\n\t\t\t\ttabindex="1"\n\t\t\t\tdata-validation-ajax-ajax="')
        # SOURCE LINE 36
        __M_writer(filters.html_escape(req.route_url('access.cl.check.nick')))
        __M_writer('"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 37
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 38
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t\tdata-validation-pattern-message="')
        # SOURCE LINE 39
        __M_writer(filters.html_escape(_('Invalid character was used')))
        __M_writer('"\n\t\t\t\tdata-validation-ajax-message="')
        # SOURCE LINE 40
        __M_writer(filters.html_escape(_('This username is already taken')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 44
        if 'user' in errors:
            # SOURCE LINE 45
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['user']))
            __M_writer('</li>\n')
        # SOURCE LINE 47
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n\t<div class="row form-group')
        # SOURCE LINE 50
        __M_writer(filters.html_escape(' has-warning' if 'email' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="email">')
        # SOURCE LINE 51
        __M_writer(filters.html_escape(_('E-mail')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="email"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="email"\n\t\t\t\tname="email"\n\t\t\t\ttitle="')
        # SOURCE LINE 59
        __M_writer(filters.html_escape(_('Enter your e-mail address')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 60
        __M_writer(filters.html_escape(_('Enter your e-mail address')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="2"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 65
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 66
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t\tdata-validation-email-message="')
        # SOURCE LINE 67
        __M_writer(filters.html_escape(_('Invalid e-mail format')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 71
        if 'email' in errors:
            # SOURCE LINE 72
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['email']))
            __M_writer('</li>\n')
        # SOURCE LINE 74
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n\t<div class="row form-group')
        # SOURCE LINE 77
        __M_writer(filters.html_escape(' has-warning' if 'pass' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="pass">')
        # SOURCE LINE 78
        __M_writer(filters.html_escape(_('Password')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="password"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="pass"\n\t\t\t\tname="pass"\n\t\t\t\ttitle="')
        # SOURCE LINE 86
        __M_writer(filters.html_escape(_('Enter your desired password')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 87
        __M_writer(filters.html_escape(_('Enter your desired password')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tminlength="')
        # SOURCE LINE 90
        __M_writer(filters.html_escape(str(min_pwd_len)))
        __M_writer('"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="3"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 93
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-minlength-message="')
        # SOURCE LINE 94
        __M_writer(filters.html_escape(_('This field is too short')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 95
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 99
        if 'pass' in errors:
            # SOURCE LINE 100
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['pass']))
            __M_writer('</li>\n')
        # SOURCE LINE 102
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n\t<div class="row form-group')
        # SOURCE LINE 105
        __M_writer(filters.html_escape(' has-warning' if 'pass2' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="pass2">')
        # SOURCE LINE 106
        __M_writer(filters.html_escape(_('Repeat Password')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="password"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="pass2"\n\t\t\t\tname="pass2"\n\t\t\t\ttitle="')
        # SOURCE LINE 114
        __M_writer(filters.html_escape(_('Repeat previously entered password')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 115
        __M_writer(filters.html_escape(_('Repeat previously entered password')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tminlength="')
        # SOURCE LINE 118
        __M_writer(filters.html_escape(str(min_pwd_len)))
        __M_writer('"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="4"\n\t\t\t\tdata-validation-match-match="pass"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 122
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-minlength-message="')
        # SOURCE LINE 123
        __M_writer(filters.html_escape(_('This field is too short')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 124
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t\tdata-validation-match-message="')
        # SOURCE LINE 125
        __M_writer(filters.html_escape(_('Passwords must match')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 129
        if 'pass2' in errors:
            # SOURCE LINE 130
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['pass2']))
            __M_writer('</li>\n')
        # SOURCE LINE 132
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n</fieldset>\n<fieldset>\n\t<legend>')
        # SOURCE LINE 137
        __M_writer(filters.html_escape(_('Personal Information')))
        __M_writer('</legend>\n\t<div class="row form-group')
        # SOURCE LINE 138
        __M_writer(filters.html_escape(' has-warning' if 'name_family' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="name_family">')
        # SOURCE LINE 139
        __M_writer(filters.html_escape(_('Family Name')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="text"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="name_family"\n\t\t\t\tname="name_family"\n\t\t\t\ttitle="')
        # SOURCE LINE 147
        __M_writer(filters.html_escape(_('Enter your family name')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 148
        __M_writer(filters.html_escape(_('Enter your family name')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="5"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 153
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 154
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 158
        if 'name_family' in errors:
            # SOURCE LINE 159
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['name_family']))
            __M_writer('</li>\n')
        # SOURCE LINE 161
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n\t<div class="row form-group')
        # SOURCE LINE 164
        __M_writer(filters.html_escape(' has-warning' if 'name_given' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="name_given">')
        # SOURCE LINE 165
        __M_writer(filters.html_escape(_('Given Name')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="text"\n\t\t\t\tclass="form-control"\n\t\t\t\trequired="required"\n\t\t\t\tid="name_given"\n\t\t\t\tname="name_given"\n\t\t\t\ttitle="')
        # SOURCE LINE 173
        __M_writer(filters.html_escape(_('Enter your given name')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 174
        __M_writer(filters.html_escape(_('Enter your given name')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="6"\n\t\t\t\tdata-validation-required-message="')
        # SOURCE LINE 179
        __M_writer(filters.html_escape(_('This field is required')))
        __M_writer('"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 180
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<span class="req">*</span>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 184
        if 'name_given' in errors:
            # SOURCE LINE 185
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['name_given']))
            __M_writer('</li>\n')
        # SOURCE LINE 187
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n\t<div class="row form-group')
        # SOURCE LINE 190
        __M_writer(filters.html_escape(' has-warning' if 'name_middle' in errors else ''))
        __M_writer('">\n\t\t<label class="col-sm-4 control-label" for="name_middle">')
        # SOURCE LINE 191
        __M_writer(filters.html_escape(_('Middle Name')))
        __M_writer('</label>\n\t\t<div class="controls col-sm-8">\n\t\t\t<input\n\t\t\t\ttype="text"\n\t\t\t\tclass="form-control"\n\t\t\t\tid="name_middle"\n\t\t\t\tname="name_middle"\n\t\t\t\ttitle="')
        # SOURCE LINE 198
        __M_writer(filters.html_escape(_('Enter your middle name')))
        __M_writer('"\n\t\t\t\tplaceholder="')
        # SOURCE LINE 199
        __M_writer(filters.html_escape(_('Enter your middle name')))
        __M_writer('"\n\t\t\t\tvalue=""\n\t\t\t\tsize="30"\n\t\t\t\tmaxlength="254"\n\t\t\t\ttabindex="7"\n\t\t\t\tdata-validation-maxlength-message="')
        # SOURCE LINE 204
        __M_writer(filters.html_escape(_('This field is too long')))
        __M_writer('"\n\t\t\t/>\n\t\t\t<div class="help-block"><ul role="alert">\n')
        # SOURCE LINE 207
        if 'name_middle' in errors:
            # SOURCE LINE 208
            __M_writer('\t\t\t\t<li>')
            __M_writer(filters.html_escape(errors['name_middle']))
            __M_writer('</li>\n')
        # SOURCE LINE 210
        __M_writer('\t\t\t</ul></div>\n\t\t</div>\n\t</div>\n</fieldset>\n')
        # SOURCE LINE 214
        if must_recaptcha:
            # SOURCE LINE 215
            __M_writer('<fieldset>\n\t<legend>')
            # SOURCE LINE 216
            __M_writer(filters.html_escape(_('User Validation')))
            __M_writer('</legend>\n\t<div class="row recaptcha-row form-group"><div class="col-sm-offset-4 col-sm-8">\n')
            # SOURCE LINE 218
            if 'recaptcha' in errors:
                # SOURCE LINE 219
                __M_writer('\t\t<div class="alert alert-warning alert-dismissable">\n\t\t\t<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\n\t\t\t')
                # SOURCE LINE 221
                __M_writer(filters.html_escape(errors['recaptcha']))
                __M_writer('\n\t\t</div>\n')
            # SOURCE LINE 224
            __M_writer('\t\t<script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=')
            __M_writer(filters.html_escape(rc_public))
            __M_writer('"></script>\n\t\t<noscript>\n\t\t\t<iframe src="http://www.google.com/recaptcha/api/noscript?k=')
            # SOURCE LINE 226
            __M_writer(filters.html_escape(rc_public))
            __M_writer('" height="300" width="500" frameborder="0"></iframe><br />\n\t\t\t<textarea name="recaptcha_challenge_field" rows="3" cols="40"></textarea>\n\t\t\t<input type="hidden" name="recaptcha_response_field" value="manual_challenge" />\n\t\t</noscript>\n\t</div></div>\n</fieldset>\n')
        # SOURCE LINE 233
        __M_writer('<div class="form-actions row">\n\t<p class="col-sm-4 legend"><span class="req">*</span> ')
        # SOURCE LINE 234
        __M_writer(filters.html_escape(_('Fields marked with this symbol are required.')))
        __M_writer('</p>\n\t<div class="controls col-sm-8">\n\t\t<input type="hidden" id="csrf" name="csrf" value="')
        # SOURCE LINE 236
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('" />\n\t\t<button type="submit" class="btn btn-primary btn-large" id="submit" name="submit" title="')
        # SOURCE LINE 237
        __M_writer(filters.html_escape(_('Register new account')))
        __M_writer('" tabindex="10">')
        __M_writer(filters.html_escape(_('Register')))
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
        __M_writer(filters.html_escape(_('Register')))
        return ''
    finally:
        context.caller_stack._pop_frame()


