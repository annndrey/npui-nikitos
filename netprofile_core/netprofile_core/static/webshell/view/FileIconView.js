/**
 * @class NetProfile.view.FileIconView
 * @extends Ext.view.View
 */
Ext.define('NetProfile.view.FileIconView', {
	extend: 'Ext.view.View',
	alias: 'widget.fileiconview',
	requires: [
		'Ext.util.KeyNav',
		'Ext.ux.view.DragSelector',
		'Ext.ux.view.LabelEditor',
		'Ext.ux.view.Draggable'
	],
	mixins: {
		draggable: 'Ext.ux.view.Draggable'
	},

	useColumns: false,
	browser: null,
	getMIME: null,
	iconSize: 48,
	cls: 'np-file-iview',
	emptyText: 'Folder is empty',

	itemSelector: 'div.np-file-wrap',
	overItemCls: 'x-file-item-over',
	multiSelect: true,
	trackOver: true,
	autoScroll: true,

	iconTpl: [
		'<tpl for=".">',
			'<div class="np-file-wrap" id="file_{fileid}">',
				'<div class="np-file-icon"><img src="{staticURL}/static/core/img/mime/{iconSz}/{mime_img}.png" title="{fname}" onerror=\'this.onerror = null; this.src="{staticURL}/static/core/img/mime/{iconSz}/default.png"\' /></div>',
				'<span class="x-editable" title="{fname}">{fname}</span>',
			'</div>',
		'</tpl>',
		'<div class="x-clear"></div>'
	],
	columnTpl: [
		'<tpl for=".">',
			'<div class="np-file-wrap" id="file_{fileid}" style="left: {[ Math.floor((xindex - 1) / values.maxItems) * 202 ]}px; top: {[ ((xindex - 1) % values.maxItems) * 21 ]}px;">',
				'<div class="np-file-icon"><img src="{staticURL}/static/core/img/mime/{iconSz}/{mime_img}.png" title="{fname}" onerror=\'this.onerror = null; this.src="{staticURL}/static/core/img/mime/{iconSz}/default.png"\' /></div>',
				'<span class="x-editable" title="{fname}">{fname}</span>',
			'</div>',
		'</tpl>'
	],

	initComponent: function()
	{
		if(this.useColumns)
			this.tpl = this.columnTpl;
		else
			this.tpl = this.iconTpl;
		this.plugins = [
			Ext.create('Ext.ux.view.DragSelector', { pluginId: 'dragsel' }),
			Ext.create('Ext.ux.view.LabelEditor', {
				dataIndex: 'fname',
				pluginId: 'editor'
			})
		];
		this.emptyText = '<div class="x-view-empty">' + this.emptyText + '</div>';
		this.mixins.draggable.init(this, {
			ddConfig: {
				ddGroup: 'ddFile'
			},
			ghostCls: 'np-file-iview',
			ghostTpl: [
				'<tpl for=".">',
					'<div>{fname}</div>',
				'</tpl>'
			]
		});
		this.nav = null;
		this.callParent(arguments);
		if(this.useColumns)
			this.on('resize', this.onResize, this);
		this.on('afterrender', this.onAfterRender);
	},
	onAfterRender: function(me)
	{
		if(me.useColumns)
		{
			var el = me.getEl();

			el.dom.addEventListener(
				'mousewheel',
				me.onScroll,
				false
			);
			el.dom.addEventListener(
				'DOMMouseScroll',
				me.onScroll,
				false
			);
		}
	},
	onScroll: function(ev)
	{
		var delta = Math.max(-1, Math.min(1, (ev.wheelDelta || -ev.detail))),
			tgt = (ev.currentTarget) ? ev.currentTarget : ev.srcElement;

		if(delta == 1)
		{
			if(tgt.doScroll)
				tgt.doScroll('left');
			else
				tgt.scrollLeft -= 30;
		}
		else
		{
			if(tgt.doScroll)
				tgt.doScroll('right');
			else
				tgt.scrollLeft += 30;
		}
		ev.preventDefault();
	},
	onResize: function(view, w, h, oldw, oldh)
	{
		if(!oldw || !oldh)
			return;
		this.refresh();
	},
	prepareData: function(data)
	{
		if(this.useColumns)
		{
			data.maxHeight = this.browser.body.getHeight() - Ext.getScrollbarSize().height - 2;
			data.maxItems = Math.floor(data.maxHeight / 21);
		}
		data.iconSz = this.iconSize;
		data.baseURL = NetProfile.baseURL;
		data.staticURL = NetProfile.staticURL;
		if(data.mime && this.getMIME)
			data.mime_img = this.getMIME(data.mime);

		return data;
	}
});

