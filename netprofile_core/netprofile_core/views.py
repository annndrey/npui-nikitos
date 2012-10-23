from pyramid.response import Response
from pyramid.view import (
	forbidden_view_config,
	view_config
)
from pyramid.security import (
	authenticated_userid,
	forget,
	remember
)
from pyramid.httpexceptions import (
	HTTPForbidden,
	HTTPFound,
	HTTPNotFound
)

from sqlalchemy.exc import DBAPIError

from netprofile.common.modules import IModuleManager
from netprofile.db.connection import DBSession

from .models import (
	User,
	UserState
)

@view_config(route_name='core.home', renderer='netprofile_core:templates/home.mak', permission='USAGE')
def home_screen(request):
	mmgr = request.registry.getUtility(IModuleManager)
	tpldef = {
		'res_css' : mmgr.get_css(request),
		'res_js'  : mmgr.get_js(request)
	}
	return tpldef

@forbidden_view_config()
def do_forbidden(request):
	if authenticated_userid(request):
		return HTTPForbidden()
	loc = request.route_url('core.login', _query=(('next', request.path),))
	return HTTPFound(location=loc)

@view_config(route_name='core.login', renderer='netprofile_core:templates/login.mak')
def do_login(request):
	next = request.params.get('next')
	if (not next) or (not next.startswith('/')):
		next = request.route_url('core.home')
	login = ''
	did_fail = False
	if 'submit' in request.POST:
		login = request.POST.get('user', '')
		passwd = request.POST.get('pass', '')
		csrf = request.POST.get('csrf', '').encode()

		if csrf == request.session.get_csrf_token():
			sess = DBSession()
			reg = request.registry
			hash_con = reg.settings['netprofile.auth.hash'] or 'sha1'
			salt_len = int(reg.settings['netprofile.auth.salt_length']) or 4
			q = sess.query(User).filter(User.state == UserState.active).filter(User.enabled == True).filter(User.login == login)
			for user in q:
				if user.check_password(passwd, hash_con, salt_len):
					headers = remember(request, login)
					if 'auth.acls' in request.session:
						del request.session['auth.acls']
					return HTTPFound(location=next, headers=headers)
		did_fail = True

	mmgr = request.registry.getUtility(IModuleManager)

	return {
		'login'   : login,
		'next'    : next,
		'failed'  : did_fail,
		'res_css' : mmgr.get_css(request),
		'res_js'  : mmgr.get_js(request)
	}

@view_config(route_name='core.logout')
def do_logout(request):
	if 'auth.acls' in request.session:
		del request.session['auth.acls']
	headers = forget(request)
	loc = request.route_url('core.login')
	return HTTPFound(location=loc, headers=headers)

@view_config(route_name='core.js.webshell', renderer='netprofile_core:templates/webshell.mak', permission='USAGE')
def js_webshell(request):
	tpldef = {}
	mmgr = request.registry.getUtility(IModuleManager)
	tpldef['modules'] = mmgr.get_module_browser()
	return tpldef

def dpane_simple(model):
	cont = {
		'border' : 0,
		'layout' : {
			'type'    : 'hbox',
			'align'   : 'stretch',
			'padding' : 4
		},
		'items' : [{
			'xtype' : 'npform',
			'flex'  : 2
		}, {
			'xtype' : 'splitter'
		}, {
			'xtype'  : 'tabpanel',
			'flex'   : 3
		}]
	}
	return cont

def dpane_user(model):
	cont = {
		'border' : 0,
		'layout' : {
			'type'    : 'hbox',
			'align'   : 'stretch',
			'padding' : 4
		},
		'items' : [{
			'xtype' : 'npform',
			'flex'  : 2
		}, {
			'xtype' : 'splitter'
		}, {
			'xtype' : 'tabpanel',
			'activeTab' : 0,
			'flex' : 3,
			'defaults' : {
				'bodyPadding' : 4,
				'layout' : 'anchor'
			},
			'items' : [{
				'title' : 'Tab 1',
				'border' : 0,
				'html' : 'tab 1 cont'
			}, {
				'title' : 'Tab 2',
				'border' : 0,
				'html' : 'tab 2 cont'
			}]
		}]
	}
	return cont

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_netprofile_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

