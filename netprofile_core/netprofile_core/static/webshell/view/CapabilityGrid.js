/**
 * @class NetProfile.view.CapabilityGrid
 * @extends Ext.grid.Panel
 */
Ext.define('NetProfile.view.CapabilityGrid', {
	extend: 'Ext.grid.Panel',
	alias: 'widget.capgrid',
	requires: [
		'Ext.grid.*',
		'Ext.data.*',
		'Ext.util.*',
		'Ext.state.*',
		'Ext.form.*',
		'Ext.menu.*',
		'Ext.toolbar.Paging',
		'Ext.toolbar.TextItem',
		'NetProfile.store.PrivCap',
		'Ext.ux.window.CenterWindow'
	],

	ownerId: null,
	code: null,
	apiGet: null,
	apiSet: null,
	canSet: false,
	showACL: true,
	border: 0,
	invalidateScrollerOnRefresh: false,

	textName: 'Name',
	textValue: 'Value',
	textAllowed: 'Allowed',
	textDenied: 'Denied',
	textNotDefined: 'Not Defined',
	textTipACL: 'Edit ACLs',

	dockedItems: [],
	plugins: [],
	viewConfig: {
		stripeRows: true,
		plugins: []
	},

	initComponent: function()
	{
		this.columns = [{
			header: this.textName,
			dataIndex: 'name',
			name: 'name',
			flex: 2
		}, {
			header: this.textValue,
			dataIndex: 'value',
			name: 'value',
			sortable: false,
			width: 120,
		    renderer: function(value, meta, record, rowidx, colidx, store)
			{
				var col = this.columns[colidx];

				if(value === true)
					return Ext.String.format(
						'<img class="np-cap-icon" src="{0}/static/core/img/priv_allowed.png" alt="{1}" title="{1}" />{1}',
						NetProfile.staticURL, this.textAllowed
					);
				if(value === false)
					return Ext.String.format(
						'<img class="np-cap-icon" src="{0}/static/core/img/priv_denied.png" alt="{1}" title="{1}" />{1}',
						NetProfile.staticURL, this.textDenied
					);
				if(value === null)
					return Ext.String.format(
						'<img class="np-cap-icon" src="{0}/static/core/img/priv_undef.png" alt="{1}" title="{1}" />{1}',
						NetProfile.staticURL, this.textNotDefined
					);
		        return value;
		    },
			editor: {
				xtype: 'combobox',
				format: 'string',
				editable: false,
				valueField: 'id',
				displayField: 'value',
				forceSelection: false,
				allowBlank: true,
				queryMode: 'local',
				emptyText: this.textNotDefined,
				store: {
					xtype: 'simplestore',
					fields: ['id', 'value'],
					data: [{
						id: null,
						value: this.textNotDefined
					}, {
						id: true,
						value: this.textAllowed
					}, {
						id: false,
						value: this.textDenied
					}]
				}
			}
		}];
		if(this.showACL)
			this.columns.push({
				xtype: 'actioncolumn',
				width: 20,
				items: [{
					iconCls: 'ico-mod-acl',
					tooltip: this.textTipACL,
					handler: function(grid, rowi, coli, item, e, rec)
					{
						var acl_win, grid_cfg;

						acl_win = Ext.create('Ext.ux.window.CenterWindow', {
							title: this.textTipACL + ': ' + rec.get('name'),
							modal: true
						});
						grid_cfg = {
							xtype: 'capgrid',
							stateId: null,
							stateful: false,
							showACL: false,
							ownerId: this.ownerId,
							code: rec.get('code')
						};
						if(this.apiGet)
							grid_cfg.apiGet = this.apiGet.replace('Privilege', 'ACL');
						if(this.apiSet)
							grid_cfg.apiSet = this.apiSet.replace('Privilege', 'ACL');
						acl_win.add(Ext.create('NetProfile.view.CapabilityGrid', grid_cfg));
						acl_win.show();
					},
					scope: this
				}],
				sortable: false,
				resizable: false,
				menuDisabled: true,
				renderer: function(val, meta, rec, row, col, store, view)
				{
					if(!rec.get('hasacls'))
						meta.style = 'display: none;';
				}
			});

		this.plugins.push({
			ptype: 'cellediting',
			clicksToEdit: 1
		});

		if(!this.store)
		{
			this.store = Ext.create('NetProfile.store.PrivCap', {
				proxy: {
					type: 'direct',
					api: {
						create: Ext.emptyFn,
						read: this.apiGet,
						update: this.apiSet,
						destroy: Ext.emptyFn
					},
					reader: {
						type: 'json',
						idProperty: 'privid',
						messageProperty: 'message',
						root: 'records',
						successProperty: 'success',
						totalProperty: 'total'
					},
					writer: {
						type: 'json',
						root: 'records',
						writeAllFields: true,
						allowSingle: false
					},
					extraParams: { owner: this.ownerId, code: this.code }
				},
				listeners: {
					beforeload: {
						fn: function(st, op)
						{
							if(!this.ownerId)
							{
								var rec = this.up('panel[cls~=record-tab]');

								if(rec && rec.record)
								{
									this.ownerId = rec.record.getId();
									st.proxy.extraParams = { owner: this.ownerId };
								}
							}
						},
						scope: this,
						single: true
					}
				}
			});
		}

		this.callParent();
	}
});

