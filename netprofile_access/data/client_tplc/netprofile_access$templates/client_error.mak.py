# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407507778.391518
_enable_loop = True
_template_filename = '/home/annndrey/test/npui/netprofile_access/netprofile_access/templates/client_error.mak'
_template_uri = 'netprofile_access$templates/client_error.mak'
_source_encoding = 'utf-8'
_exports = []


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
        req = context.get('req', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        error = context.get('error', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\t<div class="jumbotron"><div class="container">\n\t\t<h1>')
        # SOURCE LINE 5
        __M_writer(filters.html_escape(error))
        __M_writer(' <small>')
        __M_writer(filters.html_escape(_('Error %d', domain='netprofile_access') % req.response.status_code))
        __M_writer('</small></h1>\n')
        # SOURCE LINE 6
        if req.response.status_code == 404:
            # SOURCE LINE 7
            __M_writer('\t\t<p>\n\t\t\t')
            # SOURCE LINE 8
            __M_writer(filters.html_escape(_('There is no page with the address you provided.', domain='netprofile_access')))
            __M_writer('\n\t\t\t')
            # SOURCE LINE 9
            __M_writer(filters.html_escape(_('We\'re really sorry about that.', domain='netprofile_access')))
            __M_writer('\n\t\t</p>\n')
            # SOURCE LINE 11
        elif req.response.status_code == 403:
            # SOURCE LINE 12
            __M_writer('\t\t<p>\n\t\t\t')
            # SOURCE LINE 13
            __M_writer(filters.html_escape(_('You don\'t have the credentials that are required to access this page.', domain='netprofile_access')))
            __M_writer('\n')
            # SOURCE LINE 14
            if not req.user:
                # SOURCE LINE 15
                __M_writer('\t\t\t')
                __M_writer(filters.html_escape(_('Maybe you forgot to log in?', domain='netprofile_access')))
                __M_writer('\n')
                # SOURCE LINE 16
            else:
                # SOURCE LINE 17
                __M_writer('\t\t\t')
                __M_writer(filters.html_escape(_('We\'re really sorry about that.', domain='netprofile_access')))
                __M_writer('\n')
            # SOURCE LINE 19
            __M_writer('\t\t</p>\n')
        # SOURCE LINE 21
        __M_writer('\t\t<p>')
        __M_writer(filters.html_escape(_('You can contact support or try again.', domain='netprofile_access')))
        __M_writer('</p>\n\t\t<p class="pull-right">\n')
        # SOURCE LINE 23
        if req.referer:
            # SOURCE LINE 24
            __M_writer('\t\t\t<a class="btn btn-info btn-lg" role="button" href="')
            __M_writer(filters.html_escape(req.referer))
            __M_writer('" title="')
            __M_writer(filters.html_escape(_('Go back from where you came', domain='netprofile_access')))
            __M_writer('">\n\t\t\t\t<span class="glyphicon glyphicon-backward"></span>\n\t\t\t\t')
            # SOURCE LINE 26
            __M_writer(filters.html_escape(_('Go Back', domain='netprofile_access')))
            __M_writer('\n\t\t\t</a>\n')
        # SOURCE LINE 29
        if req.user:
            # SOURCE LINE 30
            __M_writer('\t\t\t<a class="btn btn-primary btn-lg" role="button" href="')
            __M_writer(filters.html_escape(req.route_url('access.cl.home')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(_('Return to home page', domain='netprofile_access')))
            __M_writer('">\n\t\t\t\t<span class="glyphicon glyphicon-home"></span>\n\t\t\t\t')
            # SOURCE LINE 32
            __M_writer(filters.html_escape(_('Go Home', domain='netprofile_access')))
            __M_writer('\n\t\t\t</a>\n')
            # SOURCE LINE 34
        else:
            # SOURCE LINE 35
            __M_writer('\t\t\t<a class="btn btn-primary btn-lg" role="button" href="')
            __M_writer(filters.html_escape(req.route_url('access.cl.login')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(_('Return to sign in page', domain='netprofile_access')))
            __M_writer('">\n\t\t\t\t<span class="glyphicon glyphicon-log-in"></span>\n\t\t\t\t')
            # SOURCE LINE 37
            __M_writer(filters.html_escape(_('Log In', domain='netprofile_access')))
            __M_writer('\n\t\t\t</a>\n')
        # SOURCE LINE 40
        __M_writer('\t\t</p>\n\t</div></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


