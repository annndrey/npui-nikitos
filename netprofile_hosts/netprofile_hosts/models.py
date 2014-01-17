#!/usr/bin/env python
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-
#
# NetProfile: Hosts module - Models
# © Copyright 2013 Alex 'Unik' Unigovsky
#
# This file is part of NetProfile.
# NetProfile is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later
# version.
#
# NetProfile is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General
# Public License along with NetProfile. If not, see
# <http://www.gnu.org/licenses/>.

from __future__ import (
	unicode_literals,
	print_function,
	absolute_import,
	division
)

__all__ = [
	'Host',
	'HostGroup',
	'Service',
	'ServiceType'
]

from sqlalchemy import (
	Column,
	FetchedValue,
	ForeignKey,
	Index,
	Sequence,
	TIMESTAMP,
	Unicode,
	UnicodeText,
	func,
	text
)

from sqlalchemy.orm import (
	backref,
	relationship
)

from sqlalchemy.ext.associationproxy import association_proxy

from netprofile.db.connection import Base
from netprofile.db.fields import (
	ASCIIString,
	ASCIIText,
	DeclEnum,
	NPBoolean,
	UInt8,
	UInt16,
	UInt32,
	UInt64,
	npbool
)
from netprofile.db.ddl import Comment
from netprofile.tpl import TemplateObject
from netprofile.ext.columns import MarkupColumn
from netprofile.ext.wizards import (
	SimpleWizard,
	Step,
	Wizard
)

from pyramid.i18n import (
	TranslationStringFactory,
	get_localizer
)

from netprofile_domains.models import ObjectVisibility

_ = TranslationStringFactory('netprofile_hosts')

class Host(Base):
	"""
	Host object.
	"""
	__tablename__ = 'hosts_def'
	__table_args__ = (
		Comment('Hosts'),
		Index('hosts_def_u_hostname', 'domainid', 'name', unique=True),
		Index('hosts_def_i_hgid', 'hgid'),
		Index('hosts_def_i_entityid', 'entityid'),
		Index('hosts_def_i_aliasid', 'aliasid'),
		Index('hosts_def_i_cby', 'cby'),
		Index('hosts_def_i_mby', 'mby'),
		{
			'mysql_engine'  : 'InnoDB',
			'mysql_charset' : 'utf8',
			'info'          : {
				'cap_menu'      : 'BASE_HOSTS',
				'cap_read'      : 'HOSTS_LIST',
				'cap_create'    : 'HOSTS_CREATE',
				'cap_edit'      : 'HOSTS_EDIT',
				'cap_delete'    : 'HOSTS_DELETE',
				'menu_name'     : _('Hosts'),
				'show_in_menu'  : 'modules',
				'menu_order'    : 10,
				'menu_main'     : True,
				'default_sort'  : ({ 'property': 'name', 'direction': 'ASC' },),
				'grid_view'     : (
					MarkupColumn(
						name='name',
						header_string=_('Name'),
						template='{__str__}',
						column_flex=3,
						sortable=True
					),
					'group', 'entity'
				),
				'form_view'     : (
					'name', 'domain',
					'group', 'entity',
					'original', 'descr',
					'ctime', 'cby',
					'mtime', 'mby'
				),
				'easy_search'   : ('name',),
				'detail_pane'   : ('netprofile_core.views', 'dpane_simple'),
				'create_wizard' : 
					Wizard(
						Step('name', 'domain', 'entity', title=_('New host data')),
						Step('group', 'original', 'descr', title=_('New host details')),
						title=_('Add new host')
					)
			}
		}
	)
	id = Column(
		'hostid',
		UInt32(),
		Sequence('hosts_def_hostid_seq'),
		Comment('Host ID'),
		primary_key=True,
		nullable=False,
		info={
			'header_string' : _('ID')
		}
	)
	group_id = Column(
		'hgid',
		UInt32(),
		ForeignKey('hosts_groups.hgid', name='hosts_def_fk_hgid', onupdate='CASCADE'),
		Comment('Host group ID'),
		nullable=False,
		info={
			'header_string' : _('Group'),
			'filter_type'   : 'list',
			'column_flex'   : 1
		}
	)
	entity_id = Column(
		'entityid',
		UInt32(),
		ForeignKey('entities_def.entityid', name='hosts_def_fk_entityid', onupdate='CASCADE', ondelete='CASCADE'),
		Comment('Entity ID'),
		nullable=False,
		info={
			'header_string' : _('Entity'),
			'filter_type'   : 'none',
			'column_flex'   : 1
		}
	)
	domain_id = Column(
		'domainid',
		UInt32(),
		ForeignKey('domains_def.domainid', name='hosts_def_fk_domainid', onupdate='CASCADE'),
		Comment('Domain ID'),
		nullable=False,
		info={
			'header_string' : _('Domain'),
			'filter_type'   : 'list'
		}
	)
	name = Column(
		Unicode(255),
		Comment('Host Name'),
		nullable=False,
		info={
			'header_string' : _('Name')
		}
	)
	original_id = Column(
		'aliasid',
		UInt32(),
		ForeignKey('hosts_def.hostid', name='hosts_def_fk_aliasid', ondelete='CASCADE', onupdate='CASCADE'),
		Comment('Aliased host ID'),
		nullable=True,
		default=None,
		server_default=text('NULL'),
		info={
			'header_string' : _('Aliased'),
			'filter_type'   : 'list'
		}
	)
	creation_time = Column(
		'ctime',
		TIMESTAMP(),
		Comment('Time of creation'),
		nullable=True,
		default=None,
		server_default=FetchedValue(),
		info={
			'header_string' : _('Created'),
			'read_only'     : True
		}
	)
	modification_time = Column(
		'mtime',
		TIMESTAMP(),
		Comment('Time of last modification'),
		nullable=False,
		server_default=func.current_timestamp(),
		server_onupdate=func.current_timestamp(),
		info={
			'header_string' : _('Modified'),
			'read_only'     : True
		}
	)
	created_by_id = Column(
		'cby',
		UInt32(),
		ForeignKey('users.uid', name='hosts_def_fk_cby', ondelete='SET NULL', onupdate='CASCADE'),
		Comment('Created by'),
		nullable=True,
		default=None,
		server_default=text('NULL'),
		info={
			'header_string' : _('Created'),
			'read_only'     : True
		}
	)
	modified_by_id = Column(
		'mby',
		UInt32(),
		ForeignKey('users.uid', name='hosts_def_fk_mby', ondelete='SET NULL', onupdate='CASCADE'),
		Comment('Last modified by'),
		nullable=True,
		default=None,
		server_default=text('NULL'),
		info={
			'header_string' : _('Modified'),
			'read_only'     : True
		}
	)
	description = Column(
		'descr',
		UnicodeText(),
		Comment('Host description'),
		nullable=True,
		default=None,
		server_default=text('NULL'),
		info={
			'header_string' : _('Description')
		}
	)

	group = relationship(
		'HostGroup',
		innerjoin=True,
		backref='hosts'
	)
	entity = relationship(
		'Entity',
		innerjoin=True,
		backref=backref(
			'hosts',
			cascade='all, delete-orphan',
			passive_deletes=True
		)
	)
	domain = relationship(
		'Domain',
		innerjoin=True,
		backref='hosts'
	)
	original = relationship(
		'Host',
		backref=backref(
			'aliases',
			cascade='all, delete-orphan',
			passive_deletes=True
		),
		remote_side=[id]
	)
	created_by = relationship(
		'User',
		foreign_keys=created_by_id,
		backref='created_hosts'
	)
	modified_by = relationship(
		'User',
		foreign_keys=modified_by_id,
		backref='modified_hosts'
	)
	services = relationship(
		'Service',
		backref=backref(
			'host',
			innerjoin=True
		),
		cascade='all, delete-orphan',
		passive_deletes=True
	)

	def __str__(self):
		if self.domain:
			return '%s.%s' % (
				str(self.name),
				str(self.domain)
			)
		return '%s' % str(self.name)

class HostGroup(Base):
	"""
	Host group object.
	"""
	__tablename__ = 'hosts_groups'
	__table_args__ = (
		Comment('Host groups'),
		Index('hosts_groups_u_hgname', 'name', unique=True),
		{
			'mysql_engine'  : 'InnoDB',
			'mysql_charset' : 'utf8',
			'info'          : {
				'cap_menu'      : 'BASE_HOSTS',
				'cap_read'      : 'HOSTS_LIST',
				'cap_create'    : 'HOSTS_GROUPS_CREATE',
				'cap_edit'      : 'HOSTS_GROUPS_EDIT',
				'cap_delete'    : 'HOSTS_GROUPS_DELETE',
				'menu_name'     : _('Host Groups'),
				'show_in_menu'  : 'admin',
				'menu_order'    : 10,
				'default_sort'  : ({ 'property': 'name', 'direction': 'ASC' },),
				'grid_view'     : ('name', 'public'),
				'form_view'     : (
					'name', 'public',
					'startoffset', 'endoffset',
					'startoffset6', 'endoffset6',
					'use_hwaddr', 'use_dhcp', 'use_banning'
				),
				'easy_search'   : ('name',),
				'detail_pane'   : ('netprofile_core.views', 'dpane_simple'),
				'create_wizard' : SimpleWizard(title=_('Add new host group'))
			}
		}
	)
	id = Column(
		'hgid',
		UInt32(),
		Sequence('hosts_groups_hgid_seq'),
		Comment('Host group ID'),
		primary_key=True,
		nullable=False,
		info={
			'header_string' : _('ID')
		}
	)
	name = Column(
		Unicode(255),
		Comment('Host group name'),
		nullable=False,
		info={
			'header_string' : _('Name'),
			'column_flex'   : 1
		}
	)
	public = Column(
		NPBoolean(),
		Comment('Is host group globally visible?'),
		nullable=False,
		default=True,
		server_default=npbool(True),
		info={
			'header_string' : _('Public')
		}
	)
	ipv4_start_offset = Column(
		'startoffset',
		UInt16(),
		Comment('IP allocator start offset'),
		nullable=False,
		default=0,
		server_default=text('0'),
		info={
			'header_string' : _('IPv4 Start Offset')
		}
	)
	ipv4_end_offset = Column(
		'endoffset',
		UInt16(),
		Comment('IP allocator end offset'),
		nullable=False,
		default=0,
		server_default=text('0'),
		info={
			'header_string' : _('IPv4 End Offset')
		}
	)
	ipv6_start_offset = Column(
		'startoffset6',
		UInt64(),
		Comment('IPv6 allocator start offset'),
		nullable=False,
		default=0,
		server_default=text('0'),
		info={
			'header_string' : _('IPv6 Start Offset')
		}
	)
	ipv6_end_offset = Column(
		'endoffset6',
		UInt64(),
		Comment('IPv6 allocator end offset'),
		nullable=False,
		default=0,
		server_default=text('0'),
		info={
			'header_string' : _('IPv6 End Offset')
		}
	)
	use_hwaddr = Column(
		NPBoolean(),
		Comment('Use unique hardware address check'),
		nullable=False,
		default=True,
		server_default=npbool(True),
		info={
			'header_string' : _('Unique Hardware Address')
		}
	)
	use_dhcp = Column(
		NPBoolean(),
		Comment('Use DHCP'),
		nullable=False,
		default=True,
		server_default=npbool(True),
		info={
			'header_string' : _('DHCP')
		}
	)
	use_banning = Column(
		NPBoolean(),
		Comment('Use banning system'),
		nullable=False,
		default=True,
		server_default=npbool(True),
		info={
			'header_string' : _('Banning System')
		}
	)

	def __str__(self):
		return '%s' % self.name

class ServiceProtocol(DeclEnum):
	"""
	Service type protocol enumeration.
	"""
	all = 'all', _('All'), 10
	tcp = 'tcp', _('TCP'), 20
	udp = 'udp', _('UDP'), 30

class ServiceType(Base):
	"""
	Service type object.
	"""
	__tablename__ = 'services_types'
	__table_args__ = (
		Comment('Service types'),
		Index('services_types_u_abbrev', 'abbrev', unique=True),
		Index('services_types_u_name', 'name', unique=True),
		{
			'mysql_engine'  : 'InnoDB',
			'mysql_charset' : 'utf8',
			'info'          : {
				'cap_menu'      : 'BASE_SERVICES',
				'cap_read'      : 'SERVICES_LIST',
				'cap_create'    : 'SERVICES_CREATE',
				'cap_edit'      : 'SERVICES_EDIT',
				'cap_delete'    : 'SERVICES_DELETE',
				'menu_name'     : _('Service Types'),
				'show_in_menu'  : 'admin',
				'menu_order'    : 20,
				'default_sort'  : ({ 'property': 'name', 'direction': 'ASC' },),
				'grid_view'     : ('abbrev', 'name', 'proto', 'port_start', 'port_end'),
				'form_view'     : ('abbrev', 'name', 'proto', 'port_start', 'port_end', 'alias'),
				'easy_search'   : ('abbrev', 'name'),
				'detail_pane'   : ('netprofile_core.views', 'dpane_simple'),
				'create_wizard' : SimpleWizard(title=_('Add new service type'))
			}
		}
	)
	id = Column(
		'stid',
		UInt32(),
		Sequence('services_types_stid_seq'),
		Comment('Service type ID'),
		primary_key=True,
		nullable=False,
		info={
			'header_string' : _('ID')
		}
	)
	abbreviation = Column(
		'abbrev',
		ASCIIString(32),
		Comment('Service type abbreviation'),
		nullable=False,
		info={
			'header_string' : _('Abbrev.')
		}
	)
	name = Column(
		Unicode(255),
		Comment('Service type name'),
		nullable=False,
		info={
			'header_string' : _('Name')
		}
	)
	protocol = Column(
		'proto',
		ServiceProtocol.db_type(),
		Comment('Used protocol(s)'),
		nullable=False,
		default=ServiceProtocol.all,
		server_default=ServiceProtocol.all,
		info={
			'header_string' : _('Protocol')
		}
	)
	start_port = Column(
		'port_start',
		UInt16(),
		Comment('Port range start'),
		nullable=False,
		info={
			'header_string' : _('Start Port')
		}
	)
	end_port = Column(
		'port_end',
		UInt16(),
		Comment('Port range end'),
		nullable=False,
		info={
			'header_string' : _('End Port')
		}
	)
	alias = Column(
		ASCIIText(),
		Comment('List of alternate names'),
		nullable=True,
		default=None,
		server_default=text('NULL'),
		info={
			'header_string' : _('Aliases')
		}
	)

	services = relationship(
		'Service',
		backref=backref(
			'type',
			innerjoin=True
		)
	)

	def __str__(self):
		if self.abbreviation:
			if self.name:
				return '[%s] %s' % (
					str(self.abbreviation),
					str(self.name)
				)
			else:
				return str(self.abbreviation)
		return self.name

class Service(Base):
	"""
	Service object.
	"""
	__tablename__ = 'services_def'
	__table_args__ = (
		Comment('Services'),
		Index('services_def_u_service', 'hostid', 'stid', unique=True),
		Index('services_def_i_stid', 'stid'),
		{
			'mysql_engine'  : 'InnoDB',
			'mysql_charset' : 'utf8',
			'info'          : {
				'cap_menu'      : 'BASE_SERVICES',
				'cap_read'      : 'SERVICES_LIST',
				'cap_create'    : 'SERVICES_CREATE',
				'cap_edit'      : 'SERVICES_EDIT',
				'cap_delete'    : 'SERVICES_DELETE',
				'menu_name'     : _('Service Types'),
				'grid_view'     : ('host', 'type', 'priority', 'weight', 'vis'),
				'form_view'     : ('host', 'type', 'priority', 'weight', 'vis'),
				'create_wizard' : SimpleWizard(title=_('Add new service'))
			}
		}
	)
	id = Column(
		'sid',
		UInt32(),
		Sequence('services_def_sid_seq'),
		Comment('Service ID'),
		primary_key=True,
		nullable=False,
		info={
			'header_string' : _('ID')
		}
	)
	host_id = Column(
		'hostid',
		UInt32(),
		ForeignKey('hosts_def.hostid', name='services_def_fk_hostid', ondelete='CASCADE', onupdate='CASCADE'),
		Comment('Host ID'),
		nullable=False,
		info={
			'header_string' : _('Host'),
			'filter_type'   : 'none'
		}
	)
	type_id = Column(
		'stid',
		UInt32(),
		ForeignKey('services_types.stid', name='services_def_fk_stid', onupdate='CASCADE'),
		Comment('Service type ID'),
		nullable=False,
		info={
			'header_string' : _('Type'),
			'filter_type'   : 'list',
			'column_flex'   : 1
		}
	)
	priority = Column(
		UInt32(),
		Comment('Service priority'),
		nullable=False,
		default=0,
		server_default=text('NULL'),
		info={
			'header_string' : _('Priority')
		}
	)
	weight = Column(
		UInt32(),
		Comment('Service weight'),
		nullable=False,
		default=0,
		server_default=text('NULL'),
		info={
			'header_string' : _('Weight')
		}
	)
	visibility = Column(
		'vis',
		ObjectVisibility.db_type(),
		Comment('Service visibility'),
		nullable=False,
		default=ObjectVisibility.internal,
		server_default=ObjectVisibility.internal,
		info={
			'header_string' : _('Visibility')
		}
	)
