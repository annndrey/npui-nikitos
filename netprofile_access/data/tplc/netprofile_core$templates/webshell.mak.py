# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1408534861.037361
_enable_loop = True
_template_filename = '/home/annndrey/test/git/npui/netprofile_core/netprofile_core/templates/webshell.mak'
_template_uri = 'netprofile_core$templates/webshell.mak'
_source_encoding = 'utf-8'
_exports = []


# SOURCE LINE 2


from netprofile.tpl.filters import jsone



def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 7
    ns = runtime.TemplateNamespace('np', context._clean_inheritance_tokens(), templateuri='netprofile_core:templates/np.mak', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'np')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rt_host = context.get('rt_host', UNDEFINED)
        req = context.get('req', UNDEFINED)
        rt_port = context.get('rt_port', UNDEFINED)
        modules = context.get('modules', UNDEFINED)
        cur_loc = context.get('cur_loc', UNDEFINED)
        res_ajs = context.get('res_ajs', UNDEFINED)
        str = context.get('str', UNDEFINED)
        res_ctl = context.get('res_ctl', UNDEFINED)
        np = _mako_get_namespace(context, 'np')
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer("Ext.Loader.setConfig({enabled: true});\n\nExt.Loader.setPath({\n\t'NetProfile'           : 'static/core/webshell',\n")
        # SOURCE LINE 12
        for module in modules:
            # SOURCE LINE 13
            __M_writer("\t'NetProfile.")
            __M_writer(filters.html_escape(module))
            __M_writer("' : 'static/")
            __M_writer(filters.html_escape(module))
            __M_writer("/webshell',\n")
        # SOURCE LINE 15
        __M_writer("\t'Ext.ux'               : 'static/core/webshell/ux'\n});\n\nExt.require([\n\t'Ext.data.*',\n\t'Ext.direct.*',\n\t'Ext.form.field.Field',\n\t'Ext.tip.*',\n\t'Ext.state.*',\n\t'Ext.util.Cookies',\n\t'Ext.Ajax',\n")
        # SOURCE LINE 26
        for i_ajs in res_ajs:
            # SOURCE LINE 27
            __M_writer("\t'")
            __M_writer(filters.html_escape(i_ajs))
            __M_writer("',\n")
        # SOURCE LINE 29
        __M_writer("\t'NetProfile.model.Basic',\n\t'NetProfile.view.CapabilityGrid',\n\t'Ext.ux.form.MultiField',\n\t'NetProfile.view.Calendar'\n], function()\n{\n\tNetProfile.currentLocale = '")
        # SOURCE LINE 35
        __M_writer(filters.html_escape(cur_loc))
        __M_writer("';\n\tNetProfile.currentUser = '")
        # SOURCE LINE 36
        __M_writer(filters.html_escape(req.user.login))
        __M_writer("';\n\tNetProfile.currentUserId = ")
        # SOURCE LINE 37
        __M_writer(filters.html_escape(req.user.id))
        __M_writer(";\n\tNetProfile.currentSession = '")
        # SOURCE LINE 38
        __M_writer(filters.html_escape(str(req.np_session)))
        __M_writer("';\n\tNetProfile.userSettings = ")
        # SOURCE LINE 39
        __M_writer(jsone(req.user.client_settings(req) ))
        __M_writer(';\n\tNetProfile.rootFolder = ')
        # SOURCE LINE 40
        __M_writer(jsone(req.user.get_root_folder() ))
        __M_writer(";\n\tNetProfile.baseURL = '")
        # SOURCE LINE 41
        __M_writer(filters.html_escape(req.host_url))
        __M_writer("';\n\tNetProfile.staticURL = '")
        # SOURCE LINE 42
        __M_writer(filters.html_escape(req.host_url))
        __M_writer("';\n\t//NetProfile.rtURL = '//")
        # SOURCE LINE 43
        __M_writer(filters.html_escape(rt_host))
        __M_writer(':')
        __M_writer(filters.html_escape(rt_port))
        __M_writer("';\n\tNetProfile.rtURL = '//' + window.location.hostname + ':")
        # SOURCE LINE 44
        __M_writer(filters.html_escape(rt_port))
        __M_writer('\';\n\tNetProfile.rtSocket = null;\n\tNetProfile.rtActiveUIDs = null;\n\tNetProfile.rtMessageRenderers = {\n\t\tfile: function(val, meta, rec)\n\t\t{\n\t\t\tvar fname = Ext.String.htmlEncode(val.fname),\n\t\t\t\tsurl = NetProfile.staticURL;\n\n\t\t\treturn \'<a class="np-file-wrap" href="#" onclick="Ext.getCmp(\\\'npws_filedl\\\').loadFileById(\' + Ext.String.htmlEncode(val.id) + \'); return false;"><img class="np-file-icon" src="\' + surl + \'/static/core/img/mime/16/\' + Ext.String.htmlEncode(val.mime) + \'.png" title="\' + fname + \'" onerror=\\\'this.onerror = null; this.src="\' + surl + \'/static/core/img/mime/16/default.png"\\\' /><span title="\' + fname + \'">\' + fname + \'</span></a>\';\n\t\t}\n\t};\n\tExt.direct.Manager.addProvider(NetProfile.api.Descriptor);\n\tExt.Ajax.defaultHeaders = Ext.apply(Ext.Ajax.defaultHeaders || {}, {\n\t\t\'X-CSRFToken\': \'')
        # SOURCE LINE 58
        __M_writer(filters.html_escape(req.get_csrf()))
        __M_writer('\'\n\t});\n\tNetProfile.msg = function()\n\t{\n\t\tvar msgCt;\n\n\t\tfunction createBox(t, s, cls)\n\t\t{\n\t\t\treturn \'<div class="msg \' + cls + \'"><h3>\' + t + \'</h3><p>\' + s + \'</p></div>\';\n\t\t}\n\n\t\tfunction getMsg(cls, title, args)\n\t\t{\n\t\t\tif(!msgCt)\n\t\t\t\tmsgCt = Ext.DomHelper.insertFirst(document.body, { id: \'msg-div\' }, true);\n\t\t\tvar s = Ext.String.format.apply(String, args);\n\t\t\tvar m = Ext.DomHelper.append(msgCt, createBox(title, s, cls), true);\n\t\t\tm.hide();\n\t\t\tm.slideIn(\'t\').ghost(\'t\', { delay: 1250, remove: true });\n\t\t}\n\n\t\treturn {\n\t\t\tnotify: function(title, fmt)\n\t\t\t{\n\t\t\t\treturn getMsg(\'\', title, Array.prototype.slice.call(arguments, 1));\n\t\t\t},\n\t\t\twarn: function(title, fmt)\n\t\t\t{\n\t\t\t\treturn getMsg(\'warning\', title, Array.prototype.slice.call(arguments, 1));\n\t\t\t},\n\t\t\terr: function(title, fmt)\n\t\t\t{\n\t\t\t\treturn getMsg(\'error\', title, Array.prototype.slice.call(arguments, 1));\n\t\t\t},\n\t\t\tinit: function()\n\t\t\t{\n\t\t\t\tif(!msgCt)\n\t\t\t\t\tmsgCt = Ext.DomHelper.insertFirst(document.body, { id: \'msg-div\' }, true);\n\t\t\t}\n\t\t};\n\t}();\n\n\tExt.define(\'Ext.data.ConnectionNPOver\', {\n\t\toverride: \'Ext.data.Connection\',\n\t\tsetOptions: function(opt, scope)\n\t\t{\n\t\t\tres = this.callParent(arguments);\n\t\t\tif(opt.rawData && (typeof(FormData) !== \'undefined\') && (opt.rawData instanceof FormData))\n\t\t\t\tres.data = opt.rawData;\n\t\t\treturn res;\n\t\t},\n\t\tsetupHeaders: function(xhr, opt, data, params)\n\t\t{\n\t\t\tif(opt.rawData && (typeof(FormData) !== \'undefined\') && (opt.rawData instanceof FormData))\n\t\t\t\treturn {};\n\t\t\tres = this.callParent(arguments);\n\t\t\treturn res;\n\t\t}\n\t});\n\tExt.define(\'Ext.form.field.BaseErrors\', {\n\t\toverride: \'Ext.form.field.Base\',\n\t\tgetErrors: function(value)\n\t\t{\n\t\t\tvar errs, i;\n\n\t\t\terrs = this.callParent(arguments);\n\t\t\tif(this.asyncErrors && this.asyncErrors.length)\n\t\t\t\tfor(i in this.asyncErrors)\n\t\t\t\t{\n\t\t\t\t\tExt.Array.push(errs, this.asyncErrors[i]);\n\t\t\t\t}\n\t\t\treturn errs;\n\t\t}\n\t});\n\n\tExt.define(\'NetProfile.data.IPAddress\', {\n\t\tMAX_IPV4: 0xffffffff,\n\t\tvalue: null,\n\t\tgetValue: function()\n\t\t{\n\t\t\treturn this.value;\n\t\t}\n\t});\n\n\tExt.define(\'NetProfile.data.IPv4Address\', {\n\t\textend: \'NetProfile.data.IPAddress\',\n\t\tconstructor: function(val)\n\t\t{\n\t\t\tif((val !== undefined) && (val !== null) && (val !== \'\'))\n\t\t\t\tthis.setValue(val);\n\t\t},\n\t\tsetValue: function(val)\n\t\t{\n\t\t\tif(Ext.isNumeric(val))\n\t\t\t\tval = parseInt(val);\n\t\t\telse\n\t\t\t\tval = this.parseTextual(val);\n\t\t\tthis.value = val;\n\t\t\treturn this;\n\t\t},\n\t\tsetOctets: function(oct)\n\t\t{\n\t\t\toct = this.parseOctets(oct);\n\t\t\tthis.value = oct;\n\t\t\treturn this;\n\t\t},\n\t\tparseOctets: function(oct)\n\t\t{\n\t\t\tvar ip, i, ioct;\n\n\t\t\tif(oct.length !== 4)\n\t\t\t{\n\t\t\t\tthrow \'Invalid IPv4 octets\';\n\t\t\t}\n\t\t\tip = 0;\n\t\t\tfor(i = 0; i < oct.length; i++)\n\t\t\t{\n\t\t\t\tioct = parseInt(oct[i]);\n\t\t\t\tif(isNaN(ioct) || (ioct < 0) || (ioct > 255) ||\n\t\t\t\t\t\t((oct[i].length > 1) && (oct[i].slice(0, 1) == \'0\')))\n\t\t\t\t\tthrow \'Invalid octet \' + (i + 1) + \' in IPv4 address\';\n\t\t\t\tip = (ip | ioct) >>> 0;\n\t\t\t\tif(i < 3)\n\t\t\t\t\tip = (ip << 8) >>> 0;\n\t\t\t}\n\t\t\treturn ip;\n\t\t},\n\t\tparseTextual: function(val)\n\t\t{\n\t\t\tif(!val.match(/^[0-9.]*$/))\n\t\t\t\tthrow \'Invalid IPv4 address: \' + val;\n\t\t\treturn this.parseOctets(val.split(\'.\'));\n\t\t},\n\t\ttoOctets: function()\n\t\t{\n\t\t\tvar oct, v, i;\n\n\t\t\toct = [0, 0, 0, 0];\n\t\t\tv = this.value;\n\n\t\t\tfor(i = 3; i >= 0; i--)\n\t\t\t{\n\t\t\t\toct[i] = String((v & 0xff));\n\t\t\t\tv = v >>> 8;\n\t\t\t}\n\t\t\treturn oct;\n\t\t},\n\t\ttoString: function()\n\t\t{\n\t\t\treturn this.toOctets().join(\'.\');\n\t\t}\n\t});\n\n\tExt.define(\'NetProfile.data.IPv6Address\', {\n\t\textend: \'NetProfile.data.IPAddress\',\n\t});\n\n\tExt.data.Types.IPV4 = {\n\t\ttype: \'ipv4\',\n\t\tconvert: function(value, record)\n\t\t{\n\t\t\tif(value === null)\n\t\t\t\treturn null;\n\t\t\tif(Ext.isObject(value))\n\t\t\t{\n\t\t\t\tif(Ext.getClassName(value) === \'NetProfile.data.IPv4Address\')\n\t\t\t\t\treturn value;\n\t\t\t\tthrow "Supplied with an unknown object type";\n\t\t\t}\n\t\t\treturn new NetProfile.data.IPv4Address(value);\n\t\t},\n\t\tserialize: function(value, record)\n\t\t{\n\t\t\tif(value === null)\n\t\t\t\treturn null;\n\t\t\tif(Ext.isObject(value) && (Ext.getClassName(value) === \'NetProfile.data.IPv4Address\'))\n\t\t\t\treturn value.value;\n\t\t\treturn value;\n\t\t},\n\t\tsortType: function(t)\n\t\t{\n\t\t\treturn t.value;\n\t\t}\n\t};\n\tExt.data.Types.IPV6 = {\n\t\ttype: \'ipv6\',\n\t\tconvert: function(value, record)\n\t\t{\n\t\t\tif(value === null)\n\t\t\t\treturn null;\n\t\t\treturn new NetProfile.data.IPv6Address(value);\n\t\t},\n\t\tsortType: function(t)\n\t\t{\n\t\t}\n\t};\n\n\tExt.apply(Ext.data.validations, {\n\t\trangeMessage: \'is out of range\',\n\t\trange: function(config, value)\n\t\t{\n\t\t\tif(value === undefined || value === null)\n\t\t\t\treturn false;\n\n\t\t\tif(typeof(value) !== \'number\')\n\t\t\t\treturn false;\n\n\t\t\tvar min = config.min,\n\t\t\t\tmax = config.max;\n\n\t\t\tif((typeof(min) === \'number\') && (value < min))\n\t\t\t\treturn false;\n\t\t\tif((typeof(max) === \'number\') && (value > max))\n\t\t\t\treturn false;\n\n\t\t\treturn true;\n\t\t}\n\t});\n\n\tExt.define(\'NetProfile.model.Language\', {\n\t\textend: \'Ext.data.Model\',\n\t\tfields: [\n\t\t\t{ name: \'code\', type: \'string\' },\n\t\t\t{ name: \'name\', type: \'string\' }\n\t\t]\n\t});\n\tExt.define(\'NetProfile.store.Language\', {\n\t\textend: \'Ext.data.ArrayStore\',\n\t\trequires: \'NetProfile.model.Language\',\n\t\tmodel: \'NetProfile.model.Language\',\n\t\tdata: ')
        # SOURCE LINE 288
        __M_writer(jsone([ (str(l), '%s [%s]' % (l.english_name, l.display_name)) for l in req.locales.values() ] ))
        __M_writer(",\n\t\tstoreId: 'npstore_lang'\n\t});\n\n\tExt.define('NetProfile.model.ConsoleMessage', {\n\t\textend: 'NetProfile.model.Basic',\n\t\tfields: [\n\t\t\t{ name: 'id',   type: 'auto' },\n\t\t\t{ name: 'ts',   type: 'date', dateFormat: 'c' },\n\t\t\t{ name: 'from', type: 'string' },\n\t\t\t{ name: 'bodytype', type: 'string', defaultValue: 'text' },\n\t\t\t{ name: 'data', type: 'auto' }\n\t\t],\n\t\tidProperty: 'id'\n\t});\n\n\tExt.define('NetProfile.model.Menu', {\n\t\textend: 'Ext.data.Model',\n\t\tfields: [\n\t\t\t{ name: 'name', type: 'string' },\n\t\t\t{ name: 'title', type: 'string' },\n\t\t\t{ name: 'order', type: 'int' },\n\t\t\t{ name: 'direct', type: 'string' },\n\t\t\t{ name: 'url', type: 'string' },\n\t\t\t{ name: 'options', type: 'auto' }\n\t\t]\n\t});\n\tExt.define('NetProfile.model.MenuItem', {\n\t\textend: 'Ext.data.Model',\n\t\tfields: [\n\t\t\t{ name: 'id', type: 'string' },\n\t\t\t{ name: 'text', type: 'string' },\n\t\t\t{ name: 'order', type: 'int' },\n\t\t\t{ name: 'leaf', type: 'boolean' },\n\t\t\t{ name: 'iconCls', type: 'string' },\n\t\t\t{ name: 'xview', type: 'string' },\n\t\t\t{ name: 'xhandler', type: 'string' }\n\t\t]\n\t});\n\tExt.define('NetProfile.store.Menu', {\n\t\textend: 'Ext.data.Store',\n\t\trequires: 'NetProfile.model.Menu',\n\t\tmodel: 'NetProfile.model.Menu',\n\t\tdata: ")
        # SOURCE LINE 331
        __M_writer(jsone(modules.get_menu_data(req) ))
        __M_writer(",\n\t\tstoreId: 'npstore_menu'\n\t});\n")
        # SOURCE LINE 334
        for menu in modules.get_menu_data(req):
            def ccall(caller):
                def body():
                    len = context.get('len', UNDEFINED)
                    __M_writer = context.writer()
                    # SOURCE LINE 336
                    if len(menu.extra_fields) > 0:
                        # SOURCE LINE 337
                        __M_writer("\tExt.define('NetProfile.model.customMenu.")
                        __M_writer(filters.html_escape(menu.name))
                        __M_writer("', {\n\t\textend: 'Ext.data.Model',\n\t\tfields: [\n\t\t\t{ name: 'id', type: 'string' },\n\t\t\t{ name: 'text', type: 'string' },\n\t\t\t{ name: 'order', type: 'int' },\n\t\t\t{ name: 'leaf', type: 'boolean' },\n\t\t\t{ name: 'iconCls', type: 'string' },\n")
                        # SOURCE LINE 345
                        for xf in menu.extra_fields:
                            # SOURCE LINE 346
                            __M_writer('\t\t\t')
                            __M_writer(jsone(xf ))
                            __M_writer(',\n')
                        # SOURCE LINE 348
                        __M_writer("\t\t\t{ name: 'xview', type: 'string' },\n\t\t\t{ name: 'xhandler', type: 'string' }\n\t\t]\n\t});\n")
                    # SOURCE LINE 353
                    __M_writer("\tExt.define('NetProfile.store.menu.")
                    __M_writer(filters.html_escape(menu.name))
                    __M_writer("', {\n\t\textend: 'Ext.data.TreeStore',\n\t\trequires: 'NetProfile.model.MenuItem',\n")
                    # SOURCE LINE 356
                    if len(menu.extra_fields) > 0:
                        # SOURCE LINE 357
                        __M_writer("\t\tmodel: 'NetProfile.model.customMenu.")
                        __M_writer(filters.html_escape(menu.name))
                        __M_writer("',\n")
                        # SOURCE LINE 358
                    else:
                        # SOURCE LINE 359
                        __M_writer("\t\tmodel: 'NetProfile.model.MenuItem',\n")
                    # SOURCE LINE 361
                    if menu.direct:
                        # SOURCE LINE 362
                        __M_writer("\t\tdefaultRootProperty: 'records',\n\t\tproxy: {\n\t\t\ttype: 'direct',\n\t\t\tapi: {\n\t\t\t\tcreate:  NetProfile.api.MenuTree.")
                        # SOURCE LINE 366
                        __M_writer(filters.html_escape(menu.direct))
                        __M_writer('_create || Ext.emptyFn,\n\t\t\t\tread:    NetProfile.api.MenuTree.')
                        # SOURCE LINE 367
                        __M_writer(filters.html_escape(menu.direct))
                        __M_writer('_read || Ext.emptyFn,\n\t\t\t\tupdate:  NetProfile.api.MenuTree.')
                        # SOURCE LINE 368
                        __M_writer(filters.html_escape(menu.direct))
                        __M_writer('_update || Ext.emptyFn,\n\t\t\t\tdestroy: NetProfile.api.MenuTree.')
                        # SOURCE LINE 369
                        __M_writer(filters.html_escape(menu.direct))
                        __M_writer("_delete || Ext.emptyFn\n\t\t\t},\n\t\t\treader: {\n\t\t\t\ttype: 'json',\n\t\t\t\troot: 'records',\n\t\t\t\tmessageProperty: 'message',\n\t\t\t\tsuccessProperty: 'success',\n\t\t\t\ttotalProperty: 'total'\n\t\t\t},\n\t\t\twriter: {\n\t\t\t\ttype: 'json',\n\t\t\t\troot: 'records',\n\t\t\t\twriteAllFields: true,\n\t\t\t\tallowSingle: false\n\t\t\t}\n\t\t},\n\t\troot: {\n\t\t\texpanded: true\n\t\t},\n\t\tautoLoad: false,\n\t\tautoSync: false,\n")
                        # SOURCE LINE 390
                    else:
                        # SOURCE LINE 391
                        __M_writer("\t\troot: {\n\t\t\texpanded: true,\n\t\t\tid: 'top',\n\t\t\tchildren: ")
                        # SOURCE LINE 394
                        __M_writer(jsone(modules.get_menu_tree(req, menu.name) ))
                        __M_writer('\n\t\t},\n')
                    # SOURCE LINE 397
                    __M_writer("\t\tstoreId: 'npstore_menu_")
                    __M_writer(filters.html_escape(menu.name))
                    __M_writer("'\n\t});")
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 335
                __M_writer(filters.html_escape(np.limit(cap=(menu.perm))))
            finally:
                context.caller_stack.nextcaller = None
        # SOURCE LINE 401
        __M_writer("\n\tExt.require('NetProfile.view.Viewport');\n")
        # SOURCE LINE 403
        for module in modules:
            # SOURCE LINE 404
            for model in modules[module]:
                # SOURCE LINE 405
                mod = modules[module][model] 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mod'] if __M_key in __M_locals_builtin_stored]))
                __M_writer("\n\tExt.define('NetProfile.proxy.")
                # SOURCE LINE 406
                __M_writer(filters.html_escape(module))
                __M_writer('.')
                __M_writer(filters.html_escape(model))
                __M_writer("', {\n\t\textend: 'Ext.data.proxy.Direct',\n\t\talias: 'proxy.")
                # SOURCE LINE 408
                __M_writer(filters.html_escape(module))
                __M_writer('_')
                __M_writer(filters.html_escape(model))
                __M_writer("',\n\t\tapi: {\n\t\t\tcreate:  NetProfile.api.")
                # SOURCE LINE 410
                __M_writer(filters.html_escape(model))
                __M_writer("['create'],\n\t\t\tread:    NetProfile.api.")
                # SOURCE LINE 411
                __M_writer(filters.html_escape(model))
                __M_writer("['read'],\n\t\t\tupdate:  NetProfile.api.")
                # SOURCE LINE 412
                __M_writer(filters.html_escape(model))
                __M_writer("['update'],\n\t\t\tdestroy: NetProfile.api.")
                # SOURCE LINE 413
                __M_writer(filters.html_escape(model))
                __M_writer("['delete']\n\t\t},\n\t\tsimpleSortMode: false,\n\t\tfilterParam: '__filter',\n\t\tsortParam: '__sort',\n\t\tstartParam: '__start',\n\t\tlimitParam: '__limit',\n\t\tpageParam: '__page',\n\t\tgroupParam: '__group',\n\t\treader: {\n\t\t\ttype: 'json',\n\t\t\tidProperty: '")
                # SOURCE LINE 424
                __M_writer(filters.html_escape(mod.pk))
                __M_writer("',\n\t\t\tmessageProperty: 'message',\n\t\t\troot: 'records',\n\t\t\tsuccessProperty: 'success',\n\t\t\ttotalProperty: 'total'\n\t\t},\n\t\twriter: {\n\t\t\ttype: 'json',\n\t\t\troot: 'records',\n\t\t\twriteAllFields: false,\n\t\t\tallowSingle: false\n\t\t}\n\t});\n\tExt.define('NetProfile.model.")
                # SOURCE LINE 437
                __M_writer(filters.html_escape(module))
                __M_writer('.')
                __M_writer(filters.html_escape(model))
                __M_writer("', {\n\t\textend: 'NetProfile.model.Basic',\n\t\tfields: ")
                # SOURCE LINE 439
                __M_writer(jsone(mod.get_reader_cfg() ))
                __M_writer(',\n\t\tassociations: ')
                # SOURCE LINE 440
                __M_writer(jsone(mod.get_related_cfg() ))
                __M_writer(",\n\t\tidProperty: '")
                # SOURCE LINE 441
                __M_writer(filters.html_escape(mod.pk))
                __M_writer("',\n\t\tclientIdProperty: '_clid',\n\t\tproxy: {\n\t\t\ttype: '")
                # SOURCE LINE 444
                __M_writer(filters.html_escape(module))
                __M_writer('_')
                __M_writer(filters.html_escape(model))
                __M_writer("'\n\t\t}\n\t});\n\tExt.define('NetProfile.store.")
                # SOURCE LINE 447
                __M_writer(filters.html_escape(module))
                __M_writer('.')
                __M_writer(filters.html_escape(model))
                __M_writer("', {\n\t\talias: 'store.")
                # SOURCE LINE 448
                __M_writer(filters.html_escape(module))
                __M_writer('_')
                __M_writer(filters.html_escape(model))
                __M_writer("',\n\t\textend: 'Ext.data.Store',\n\t\trequires: 'NetProfile.model.")
                # SOURCE LINE 450
                __M_writer(filters.html_escape(module))
                __M_writer('.')
                __M_writer(filters.html_escape(model))
                __M_writer("',\n\t\tmodel: 'NetProfile.model.")
                # SOURCE LINE 451
                __M_writer(filters.html_escape(module))
                __M_writer('.')
                __M_writer(filters.html_escape(model))
                __M_writer("',\n\t\tsorters: ")
                # SOURCE LINE 452
                __M_writer(jsone(mod.default_sort ))
                __M_writer(",\n\t\tpageSize: NetProfile.userSettings.datagrid_perpage,\n\t\tremoteFilter: true,\n\t\tremoteGroup: true,\n\t\tremoteSort: true,\n\t\tstoreId: 'npstore_")
                # SOURCE LINE 457
                __M_writer(filters.html_escape(module))
                __M_writer('_')
                __M_writer(filters.html_escape(model))
                __M_writer("',\n\t\tautoLoad: true,\n\t\tautoSync: true\n\t});\n\tExt.define('NetProfile.view.grid.")
                # SOURCE LINE 461
                __M_writer(filters.html_escape(module))
                __M_writer('.')
                __M_writer(filters.html_escape(model))
                __M_writer("', {\n\t\textend: 'NetProfile.view.ModelGrid',\n\t\talias: 'widget.grid_")
                # SOURCE LINE 463
                __M_writer(filters.html_escape(module))
                __M_writer('_')
                __M_writer(filters.html_escape(model))
                __M_writer("',\n\t\tcolumns: ")
                # SOURCE LINE 464
                __M_writer(jsone(mod.get_column_cfg(req) ))
                __M_writer(",\n\t\tapiModule: '")
                # SOURCE LINE 465
                __M_writer(filters.html_escape(module))
                __M_writer("',\n\t\tapiClass: '")
                # SOURCE LINE 466
                __M_writer(filters.html_escape(model))
                __M_writer("',\n\t\tstateId: 'npgrid_")
                # SOURCE LINE 467
                __M_writer(filters.html_escape(module))
                __M_writer('_')
                __M_writer(filters.html_escape(model))
                __M_writer("',\n\t\tstateful: true,\n\t\tsimpleSearch: ")
                # SOURCE LINE 469
                __M_writer(filters.html_escape('true' if mod.easy_search else 'false'))
                __M_writer(',\n\t\textraSearch: ')
                # SOURCE LINE 470
                __M_writer(jsone(mod.get_extra_search_cfg(req) ))
                __M_writer(',\n\t\tdetailPane: ')
                # SOURCE LINE 471
                __M_writer(jsone(mod.get_detail_pane(req) ))
                __M_writer(',\n')
                # SOURCE LINE 472
                if mod.create_wizard:
                    # SOURCE LINE 473
                    __M_writer('\t\tcanCreate: ')
                    def ccall(caller):
                        def body():
                            __M_writer = context.writer()
                            return ''
                        return [body]
                    context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                    try:
                        __M_writer(filters.html_escape(np.jscap(code=(mod.cap_create))))
                    finally:
                        context.caller_stack.nextcaller = None
                    __M_writer(',\n')
                    # SOURCE LINE 474
                else:
                    # SOURCE LINE 475
                    __M_writer('\t\tcanCreate: false,\n')
                # SOURCE LINE 477
                __M_writer('\t\tcanEdit: ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    __M_writer(filters.html_escape(np.jscap(code=(mod.cap_edit))))
                finally:
                    context.caller_stack.nextcaller = None
                __M_writer(',\n\t\tcanDelete: ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 478
                    __M_writer(filters.html_escape(np.jscap(code=(mod.cap_delete))))
                finally:
                    context.caller_stack.nextcaller = None
                __M_writer('\n\t});\n')
        # SOURCE LINE 482
        __M_writer("\n\nExt.application({\n\tname: 'NetProfile',\n\tappFolder: 'static/core/webshell',\n\tautoCreateViewport: false,\n\n\tmodels: [],\n\tstores: [],\n\tcontrollers: [\n\t\t'NetProfile.controller.DataStores',\n\t\t'NetProfile.controller.Users',\n\t\t'NetProfile.controller.FileAttachments',\n")
        # SOURCE LINE 495
        for cont in res_ctl:
            # SOURCE LINE 496
            __M_writer("\t\t'")
            __M_writer(filters.html_escape(cont))
            __M_writer("',\n")
        # SOURCE LINE 498
        __M_writer("\t\t'NetProfile.controller.FileFolders'\n\t],\n\n\tlaunch: function()\n\t{\n\t\tvar state_prov = null,\n\t\t\tstate_loaded = false,\n\t\t\trt_sock = null;\n\n\t\tExt.onReady(NetProfile.msg.init, NetProfile.msg);\n\t\tif('localStorage' in window && window['localStorage'] !== null)\n\t\t{\n\t\t\tstate_prov = new Ext.state.LocalStorageProvider({\n\t\t\t\tprefix: 'nps_'\n\t\t\t});\n\t\t}\n\t\telse\n\t\t{\n\t\t\tstate_prov = new Ext.state.CookieProvider({\n\t\t\t\tprefix: 'nps_'\n\t\t\t});\n\t\t}\n\n\t\tExt.state.Manager.setProvider(state_prov);\n\t\tstate_loaded = state_prov.get('loaded');\n\n\t\tvar npp = Ext.direct.Manager.getProvider('netprofile-provider');\n\t\tnpp.on('exception', function(p, e)\n\t\t{\n\t\t\tif(e && e.message)\n\t\t\t{\n")
        # SOURCE LINE 529
        if req.debug_enabled:
            # SOURCE LINE 530
            __M_writer('\t\t\t\tExt.log.error(e.message);\n')
        # SOURCE LINE 532
        __M_writer("\t\t\t\tNetProfile.msg.err('")
        __M_writer(filters.html_escape(_('Error')))
        __M_writer("', '{0}', e.message);\n\t\t\t}\n\t\t});\n\t\tnpp.on('data', function(p, e)\n\t\t{\n\t\t\tif(e.result && !e.result.success)\n\t\t\t{\n\t\t\t\tif(e.result.message)\n\t\t\t\t{\n")
        # SOURCE LINE 541
        if req.debug_enabled:
            # SOURCE LINE 542
            __M_writer('\t\t\t\t\tExt.log.warn(e.result.message);\n\t\t\t\t\tif(e.result.stacktrace)\n\t\t\t\t\t\tExt.log.info(e.result.stacktrace);\n')
        # SOURCE LINE 546
        __M_writer("\t\t\t\t\tNetProfile.msg.warn('")
        __M_writer(filters.html_escape(_('Warning')))
        __M_writer("', '{0}', e.result.message);\n\t\t\t\t}\n\t\t\t}\n\t\t});\n\n\t\tif(NetProfile.rtURL)\n\t\t{\n\t\t\trt_sock = SockJS(NetProfile.rtURL + '/sock');\n\t\t\trt_sock.onopen = function()\n\t\t\t{\n")
        # SOURCE LINE 556
        if req.debug_enabled:
            # SOURCE LINE 557
            __M_writer("\t\t\t\tExt.log.info('SockJS connected');\n")
        # SOURCE LINE 559
        __M_writer("\t\t\t\tvar msg = {\n\t\t\t\t\ttype:    'auth',\n\t\t\t\t\tuser:    NetProfile.currentUser,\n\t\t\t\t\tuid:     NetProfile.currentUserId,\n\t\t\t\t\tsession: NetProfile.currentSession\n\t\t\t\t};\n\t\t\t\trt_sock.send(Ext.JSON.encode(msg));\n\t\t\t};\n\t\t\trt_sock.onmessage = function(ev)\n\t\t\t{\n\t\t\t\tev.data = Ext.JSON.decode(ev.data);\n")
        # SOURCE LINE 570
        if req.debug_enabled:
            # SOURCE LINE 571
            __M_writer("\t\t\t\tExt.log.info({ dump: ev }, 'SockJS event received');\n")
        # SOURCE LINE 573
        __M_writer("\t\t\t\tif(typeof(ev.data.type) !== 'string')\n\t\t\t\t\treturn;\n\t\t\t\tswitch(ev.data.type)\n\t\t\t\t{\n\t\t\t\t\tcase 'user_enters':\n\t\t\t\t\tcase 'user_leaves':\n\t\t\t\t\t\tvar uid = ev.data.uid,\n\t\t\t\t\t\t\tobj = Ext.getCmp('npmenu_tree_users').getStore().getNodeById('user-' + uid);\n\t\t\t\t\t\tif(!obj)\n\t\t\t\t\t\t\treturn;\n\t\t\t\t\t\tif(ev.data.type === 'user_enters')\n\t\t\t\t\t\t\tobj.set('iconCls', 'ico-status-online');\n\t\t\t\t\t\telse\n\t\t\t\t\t\t\tobj.set('iconCls', 'ico-status-offline');\n\t\t\t\t\t\tbreak;\n\t\t\t\t\tcase 'user_list':\n\t\t\t\t\t\tvar u, uid, obj;\n\t\t\t\t\t\tNetProfile.rtActiveUIDs = ev.data.users;\n\t\t\t\t\t\tfor(u in ev.data.users)\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\tuid = ev.data.users[u];\n\t\t\t\t\t\t\tobj = Ext.getCmp('npmenu_tree_users').getStore().getNodeById('user-' + uid);\n\t\t\t\t\t\t\tif(!obj)\n\t\t\t\t\t\t\t\tcontinue;\n\t\t\t\t\t\t\tobj.set('iconCls', 'ico-status-online');\n\t\t\t\t\t\t}\n\t\t\t\t\t\tbreak;\n\t\t\t\t\tcase 'direct':\n\t\t\t\t\t\tvar store = NetProfile.StoreManager.getConsoleStore(ev.data.msgtype, ev.data.fromid),\n\t\t\t\t\t\t\trec;\n\t\t\t\t\t\tif(store)\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\trec = Ext.create('NetProfile.model.ConsoleMessage');\n\t\t\t\t\t\t\trec.set('ts', new Date(ev.data.ts));\n\t\t\t\t\t\t\tif(ev.data.fromstr)\n\t\t\t\t\t\t\t\trec.set('from', ev.data.fromstr);\n\t\t\t\t\t\t\tif(ev.data.bodytype)\n\t\t\t\t\t\t\t\trec.set('bodytype', ev.data.bodytype);\n\t\t\t\t\t\t\tif(ev.data.msg)\n\t\t\t\t\t\t\t\trec.set('data', ev.data.msg);\n\t\t\t\t\t\t\tstore.add(rec);\n\t\t\t\t\t\t}\n\t\t\t\t\t\tbreak;\n\t\t\t\t}\n\t\t\t}\n\t\t\tNetProfile.rtSocket = rt_sock;\n\t\t}\n\n\t\tif(state_loaded !== 'OK')\n\t\t{\n\t\t\tNetProfile.api.DataCache.load_ls(function(data, res)\n\t\t\t{\n\t\t\t\tif(data && data.state && data.success)\n\t\t\t\t{\n\t\t\t\t\tExt.Object.each(data.state, function(k, v)\n\t\t\t\t\t{\n\t\t\t\t\t\tstate_prov.set(k, v);\n\t\t\t\t\t});\n\t\t\t\t}\n\t\t\t\tstate_prov.set('loaded', 'OK');\n\t\t\t\tExt.create('NetProfile.view.Viewport', {});\n\t\t\t});\n\t\t}\n\t\telse\n\t\t\tExt.create('NetProfile.view.Viewport', {});\n\t}\n});\n\n});\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


