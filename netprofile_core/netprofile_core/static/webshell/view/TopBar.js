Ext.define('NetProfile.view.TopBar', {
	extend: 'Ext.toolbar.Toolbar',
	alias: 'widget.topbar',
	requires: [
		'Ext.menu.Menu',
		'Ext.container.ButtonGroup',
		'Ext.form.*',
		'NetProfile.view.Form',
		'NetProfile.view.Wizard'
	],
	id: 'npws_topbar',
	stateId: 'npws_topbar',
	stateful: true,
	collapsible: false,
	height: 32,

	toolsText: 'Tools',
	toolsTipText: 'Various tools and windows',
	logoutText: 'Log out',
	logoutTipText: 'Log out of the application and return to login screen.',
	chLangText: 'Change language',
	aboutText: 'About…',

	initComponent: function()
	{
		this.items = [{
			text: this.toolsText,
			iconCls: 'ico-tool',
			tooltip: { text: this.toolsTipText, title: this.toolsText },
			menu: {
				xtype: 'menu',
				items: [{
					xtype: 'menuitem',
					showSeparator: false,
					iconCls: 'ico-locale',
					text: this.chLangText,
					menu: {
						xtype: 'menu',
						plain: true,
						showSeparator: false,
						items: [{
							xtype: 'buttongroup',
							plain: true,
							title: this.chLangText,
							titleAlign: 'left',
							columns: 1,
							defaults: {
								margin: 3,
							},
							items: [{
								xtype: 'combo',
								editable: false,
								itemId: 'ch_lang',
								store: Ext.create('NetProfile.store.Language'),
								displayField: 'name',
								valueField: 'code',
								value: NetProfile.currentLocale,
								listeners: {
									change: function(fld, newval)
									{
										window.location = '/core/noop?__locale=' + newval;
									}
								}
							}]
						}]
					}
				}, '-', {
					text: this.aboutText,
					iconCls: 'ico-info',
					listeners: {
						click: function(el, ev)
						{
						}
					}
				}]
			}
		}, '->', {
			text: this.logoutText,
			iconCls: 'ico-logout',
			tooltip: { text: this.logoutTipText, title: this.logoutText },
			handler: function()
			{
				var sp = Ext.state.Manager.getProvider();
				if(sp && sp.state)
				{
					NetProfile.api.DataCache.save_ls(sp.state, function(data, res)
					{
						Ext.Object.getKeys(sp.state).forEach(function(k)
						{
							sp.clear(k);
						});
						sp.clear('loaded');
						window.location.href = '/logout';
					}.bind(this));
				}
				else
					window.location.href = '/logout';
			},
			scope: this
		}];
		this.callParent(arguments);
	}
});

