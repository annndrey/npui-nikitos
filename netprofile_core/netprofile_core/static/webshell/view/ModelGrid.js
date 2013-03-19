Ext.define('NetProfile.view.ModelGrid', {
	extend: 'Ext.grid.Panel',
	alias: 'widget.modelgrid',
	requires: [
		'Ext.grid.*',
		'Ext.data.*',
		'Ext.util.*',
		'Ext.state.*',
		'Ext.form.*',
		'Ext.menu.*',
		'Ext.toolbar.Paging',
		'Ext.toolbar.TextItem',
		'Ext.window.MessageBox',
		'Ext.ux.grid.FiltersFeature',
		'Ext.ux.grid.SimpleSearchFeature',
		'Ext.ux.grid.ExtraSearchFeature',
		'Ext.ux.CheckColumn',
		'Ext.ux.EnumColumn',
		'Ext.ux.IPAddressColumn',
		'Ext.ux.form.field.DateTime',
		'Ext.ux.form.field.IPv4',
		'Ext.ux.form.field.Password',
		'Ext.ux.form.DynamicCheckboxGroup',
		'NetProfile.view.ModelSelect'
	],
	rowEditing: true,
	simpleSearch: false,
	extraSearch: null,
	actionCol: true,
	propBar: true,
	selectRow: false,
	selectField: null,
	selectIdField: null,
	extraParams: null,
	extraParamProp: null,
	extraParamRelProp: null,
	apiModule: null,
	apiClass: null,
	detailPane: null,
	hideColumns: null,
	canCreate: false,
	canEdit: false,
	canDelete: false,
	border: 0,

	emptyText: 'Sorry, but no items were found.',
	clearText: 'Clear',
	clearTipText: 'Clear filtering and sorting.',
	addText: 'Add',
	addTipText: 'Add new object.',
	addWindowText: 'Add new object',
	propTipText: 'Display object properties',
	deleteTipText: 'Delete object',
	deleteMsgText: 'Are you sure you want to delete this object?',
	actionTipText: 'Object actions',

	dockedItems: [],
	plugins: [],
	viewConfig: {
		stripeRows: true,
		plugins: []
	},
	initComponent: function()
	{
		if(this.selectRow)
		{
			this.canCreate = false;
			this.canEdit = false;
			this.canDelete = false;
		}
		if(!this.canEdit)
			this.rowEditing = false;
		this.features = [{
			ftype: 'filters',
			multi: true,
			encode: false,
			local: false
		}];
		if(this.extraSearch)
			this.features.push({
				ftype: 'extrasearch',
				local: false
			});
		if(this.simpleSearch)
			this.features.push({
				ftype: 'simplesearch',
				local: false
			});
		var tbitems = [{
			text: this.clearText,
			tooltip: { text: this.clearTipText, title: this.clearText },
			iconCls: 'ico-clear',
			handler: function()
			{
				store = this.getStore();
				if(this.filters)
					this.filters.clearFilters(true);
				if(this.ssearch)
					this.ssearch.clearValue(true);
				if(this.xsearch)
					this.xsearch.clearValue(true);
				store.sorters.clear();
				this.saveState();
				store.loadPage(1);
				return true;
			},
			scope: this
		}];
		if(this.canCreate)
			tbitems.push({
				text: this.addText,
				tooltip: { text: this.addTipText, title: this.addText },
				iconCls: 'ico-add',
				handler: function()
				{
					var wiz_win = Ext.create('Ext.window.Window', {
						layout: 'fit',
						minWidth: 500,
						maxHeight: 650,
						title: this.addWindowText,
						modal: true
					});
					var wiz = Ext.create('NetProfile.view.Wizard', {
						stateful: false,
						wizardCls: this.apiClass,
						createInto: this.store
					});
					wiz_win.add(wiz);
					wiz_win.show();

					return true;
				},
				scope: this
			});
		this.dockedItems = [{
			xtype: 'toolbar',
			dock: 'top',
			itemId: 'toolTop',
			items: tbitems
		}];
		if(this.actionCol)
		{
			var has_action = false;
			this.columns.forEach(function(col)
			{
				if(col.xtype == 'actioncolumn')
					has_action = true;
			}, this);
			if(!has_action)
			{
				var i = [{
					iconCls: 'ico-props',
					tooltip: this.propTipText,
					handler: function(grid, rowidx, colidx, item, e, record)
					{
						return this.selectRecord(record);
					},
					scope: this
				}];
				if(this.canDelete)
					i.push({
						iconCls: 'ico-delete',
						tooltip: this.deleteTipText,
						handler: function(grid, rowidx, colidx, item, e, record)
						{
							if(this.store)
								Ext.MessageBox.confirm(
									this.deleteTipText,
									this.deleteMsgText + '<div class="np-object-frame">' + record.get('__str__') + '</div>',
									function(btn)
									{
										if(btn === 'yes')
											this.store.remove(record);
										return true;
									}.bind(this)
								);
							return true;
						},
						scope: this
					});
				if(i.length > 0)
					this.columns.push({
						xtype: 'actioncolumn',
						width: i.length * 20,
						items: i,
						sortable: false,
						resizable: false,
						menuDisabled: true,
						tooltip: this.actionTipText
					});
			}
		}
		this.plugins = [];
		if(this.rowEditing)
			this.plugins.push({
				ptype: 'rowediting',
				autoCancel: true,
				clicksToEdit: 2,
				clicksToMoveEditor: 1
			});

		if(!this.store && this.apiModule && this.apiClass)
			this.store = NetProfile.StoreManager.getStore(this.apiModule, this.apiClass, this, !this.stateful);

		this.callParent();

		this.addDocked({
			xtype: 'pagingtoolbar',
			dock: 'bottom',
			store: this.store,
			displayInfo: NetProfile.userSettings.datagrid_showrange
		});

		this.on({
			beforerender: function(grid)
			{
				this.columns.forEach(function(col)
				{
					if(grid.hideColumns && Ext.Array.contains(grid.hideColumns, col.dataIndex))
						col.hidden = true;
				});
			},
			selectionchange: function(sel, recs, opts)
			{
				if(!sel.hasSelection() || (sel.getSelectionMode() != 'SINGLE'))
					return true;
				if(!recs || !recs.length)
					return true;
				return this.selectRecord(recs[0]);
			},
			itemdblclick: function(view, record, item, idx, ev, opts)
			{
				if(this.selectRow)
				{
					if(this.selectIdField)
					{
						if(Ext.isString(this.selectIdField))
						{
							var form = this.selectField.up('form'),
								rec = form.getRecord();
							if(rec)
								rec.set(this.selectIdField, record.getId());
							else if(this.selectField.hiddenField)
								form.getForm().findField(this.selectField.hiddenField).setValue(record.getId());
							else
								form.getForm().findField(this.selectIdField).setValue(record.getId());
						}
						else
							this.selectIdField.setValue(record.getId());
					}
					if(this.selectField)
						this.selectField.setValue(record.get('__str__'));
					this.up('window').close();
				}
				return true;
			},
			scope: this
		});
	},
	selectRecord: function(record)
	{
		if(this.propBar && this.detailPane && !this.selectRow)
		{
			var pb = Ext.getCmp('npws_propbar');
			if(!pb)
				return true;
			if(this.detailPane)
			{
				pb.addRecordTab(this.apiModule, this.apiClass, this.detailPane, record);
				pb.show();

				var view = this.getView(),
					node = view.getNode(record);
				if(node)
					node.scrollIntoView(view);
			}
		}
		return true;
	},
	applyState: function(state)
	{
		var me = this,
			columns = me.columns;
		me.fstate = state;
		me.callParent(arguments);
		me.columns = columns;
	}
});

