#
# Copyright 2008-2012 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#

SUBDIRS = netconf sos storage gluster

include $(top_srcdir)/build-aux/Makefile.subs

dist_vdsm_PYTHON = \
	alignmentScan.py \
	API.py \
	BindingXMLRPC.py \
	blkid.py \
	caps.py \
	clientIF.py \
	configNetwork.py \
	debugPluginClient.py \
	dmidecodeUtil.py \
	guestIF.py \
	hooking.py \
	hooks.py \
	kaxmlrpclib.py \
	ksm.py \
	logUtils.py \
	lsblk.py \
	md_utils.py \
	mkimage.py \
	momIF.py \
	neterrors.py \
	netmodels.py \
	parted_utils.py \
	sampling.py \
	sourceRoute.py \
	sourceRouteThread.py \
	supervdsm.py \
	tc.py \
	vdsmDebugPlugin.py \
	vmChannels.py \
	vm.py \
	zombieReaper.py \
	$(NULL)

dist_vdsmexec_SCRIPTS = \
	ovirt_functions.sh

nodist_vdsmexec_SCRIPTS = \
	vdsm-gencerts.sh \
	vdsmd_init_common.sh \
	$(NULL)

nodist_vdsm_PYTHON = \
	dsaversion.py \
	dumpStorageTable.py

nodist_vdsm_SCRIPTS = \
	mk_sysprep_floppy \
	vdsm-store-net-config

nodist_noinst_DATA = \
	logger.conf \
	mom.conf \
	sudoers.vdsm \
	supervdsmd.init \
	supervdsmd.service \
	supervdsmd.upstart \
	svdsm.logger.conf \
	vdsm-logrotate.conf \
	vdsm-restore-net-config.init \
	vdsm-restore-net-config.upstart \
	vdsm-tmpfiles.d.conf \
	vdsm-tmpfiles.upstart \
	vdsm.rwtab \
	vdsmd.init \
	vdsmd.service \
	vdsmd.upstart \
	$(NULL)

dist_vdsm_SCRIPTS = \
	addNetwork \
	daemonAdapter \
	delNetwork \
	get-conf-item \
	respawn \
	set-conf-item \
	supervdsmServer \
	vdsm \
	vdsm-restore-net-config \
	$(NULL)

nodist_man8_MANS = \
	vdsmd.8

CLEANFILES = \
	config.log \
	$(nodist_vdsm_SCRIPTS) \
	$(nodist_vdsmlib_PYTHON) \
	$(nodist_noinst_DATA) \
	$(nodist_vdsmexec_SCRIPTS) \
	$(nodist_vdsm_PYTHON) \
	$(nodist_man8_MANS)

EXTRA_DIST = \
	dsaversion.py.in \
	dumpStorageTable.py.in \
	libvirt_password \
	limits.conf \
	logger.conf.in \
	mk_sysprep_floppy.in \
	mom.conf.in \
	mom.d/00-python.policy \
	mom.d/01-parameters.policy \
	mom.d/02-balloon.policy \
	mom.d/03-ksm.policy \
	sourceRoute.sh \
	sudoers.vdsm.in \
	supervdsmd.init.in \
	supervdsmd.service.in \
	supervdsmd.upstart.in \
	svdsm.logger.conf.in \
	vdsm-gencerts.sh.in \
	vdsm-libvirt-access.pkla \
	vdsm-libvirt-access.rules \
	vdsm-libvirt-logrotate \
	vdsm-logrotate \
	vdsm-logrotate.conf.in \
	vdsm-modules-load.d.conf \
	vdsm-restore-net-config.init.in \
	vdsm-restore-net-config.service \
	vdsm-restore-net-config.upstart.in \
	vdsm-store-net-config.in \
	vdsm-sysctl.conf \
	vdsm-tmpfiles.d.conf.in \
	vdsm-tmpfiles.upstart.in \
	vdsm.rwtab.in \
	vdsmd.8.in \
	vdsmd.init.in \
	vdsmd.service.in \
	vdsmd.upstart.in \
	vdsmd_init_common.sh.in \
	$(NULL)

all-local: \
	$(nodist_vdsm_PYTHON) \
	$(nodist_vdsm_SCRIPTS) \
	$(nodist_noinst_DATA) \
	$(nodist_man8_MANS)

install-data-hook:
	chmod 440 $(DESTDIR)$(sysconfdir)/sudoers.d/50_vdsm
	chmod 775 $(DESTDIR)$(localstatedir)/lib/libvirt/qemu/channels

install-data-local: \
		install-data-dhclient-hooks \
		install-data-libvirtpass \
		install-data-logger \
		install-data-logrotate \
		install-data-mom \
		install-data-rwtab \
		install-data-sudoers \
		install-data-sysctl
	$(MKDIR_P) $(DESTDIR)$(vdsmrepo)
	$(MKDIR_P) $(DESTDIR)$(vdsmrepo)/hsm-tasks
	$(MKDIR_P) $(DESTDIR)$(vdsmrepo)/mnt
	$(MKDIR_P) $(DESTDIR)$(vdsmtsdir)/keys
	$(MKDIR_P) $(DESTDIR)$(vdsmtsdir)/certs
	$(MKDIR_P) $(DESTDIR)$(vdsmlogdir)
	$(MKDIR_P) $(DESTDIR)$(vdsmrundir)
	$(MKDIR_P) $(DESTDIR)$(vdsmrundir)/sourceRoutes
	$(MKDIR_P) $(DESTDIR)$(vdsmrundir)/trackedInterfaces
	$(MKDIR_P) $(DESTDIR)$(vdsmrundir)/payload
	$(MKDIR_P) $(DESTDIR)$(vdsmlibdir)/netconfback
	$(MKDIR_P) $(DESTDIR)$(vdsmpoolsdir)
	$(MKDIR_P) $(DESTDIR)$(vdsmbackupdir)
	$(MKDIR_P) $(DESTDIR)$(localstatedir)/lib/libvirt/qemu/channels

uninstall-local: \
		uninstall-data-dhclient-hooks \
		uninstall-data-libvirtpass \
		uninstall-data-logger \
		uninstall-data-logrotate \
		uninstall-data-mom \
		uninstall-data-rwtab \
		uninstall-data-sudoers \
		uninstall-data-sysctl

install-data-logger:
	$(MKDIR_P) $(DESTDIR)$(vdsmconfdir)
	$(INSTALL_DATA) logger.conf $(DESTDIR)$(vdsmconfdir)/logger.conf
	$(INSTALL_DATA) svdsm.logger.conf \
	    $(DESTDIR)$(vdsmconfdir)/svdsm.logger.conf

uninstall-data-logger:
	$(RM) $(DESTDIR)$(vdsmconfdir)/logger.conf
	$(RM) $(DESTDIR)$(vdsmconfdir)/svdsm.logger.conf

install-data-libvirtpass:
	$(MKDIR_P) $(DESTDIR)$(vdsmtsdir)/keys
	$(INSTALL_DATA) -m 600 $(srcdir)/libvirt_password \
		$(DESTDIR)$(vdsmtsdir)/keys/libvirt_password

uninstall-data-libvirtpass:
	$(RM) $(DESTDIR)$(vdsmtsdir)/keys/libvirt_password

install-data-rwtab:
	$(MKDIR_P) $(DESTDIR)$(sysconfdir)/rwtab.d
	$(INSTALL_DATA) vdsm.rwtab \
		$(DESTDIR)$(sysconfdir)/rwtab.d/vdsm

uninstall-data-rwtab:
	$(RM) $(DESTDIR)$(sysconfdir)/rwtab.d/vdsm

install-data-logrotate:
	$(MKDIR_P) $(DESTDIR)$(sysconfdir)/logrotate.d
	$(INSTALL_DATA) $(builddir)/vdsm-logrotate.conf \
		$(DESTDIR)$(sysconfdir)/logrotate.d/vdsm
	$(MKDIR_P) $(DESTDIR)$(sysconfdir)/cron.hourly
	$(INSTALL_SCRIPT) $(srcdir)/vdsm-logrotate \
		$(DESTDIR)$(sysconfdir)/cron.hourly/vdsm-logrotate
	$(MKDIR_P) $(DESTDIR)$(sysconfdir)/cron.d
	$(INSTALL_DATA) $(srcdir)/vdsm-libvirt-logrotate \
		$(DESTDIR)$(sysconfdir)/cron.d/vdsm-libvirt-logrotate

uninstall-data-logrotate:
	$(RM) $(DESTDIR)$(sysconfdir)/logrotate.d/vdsm
	$(RM) $(DESTDIR)$(sysconfdir)/cron.hourly/vdsm-logrotate
	$(RM) $(DESTDIR)$(sysconfdir)/cron.d/vdsm-libvirt-logrotate

install-data-mom:
	$(MKDIR_P) $(DESTDIR)$(vdsmconfdir)/mom.d
	$(INSTALL_DATA) mom.d/*.policy \
		$(DESTDIR)$(vdsmconfdir)/mom.d
	$(INSTALL_DATA) mom.conf \
		$(DESTDIR)$(vdsmconfdir)/mom.conf

uninstall-data-mom:
		$(RM) $(DESTDIR)$(vdsmconfdir)/mom.d/*.policy
		$(RM) $(DESTDIR)$(vdsmconfdir)/mom.conf

install-data-sudoers:
	$(MKDIR_P) $(DESTDIR)$(sysconfdir)/sudoers.d
	$(INSTALL_DATA) sudoers.vdsm \
		$(DESTDIR)$(sysconfdir)/sudoers.d/50_vdsm

uninstall-data-sudoers:
	$(RM) $(DESTDIR)$(sysconfdir)/sudoers.d/50_vdsm

install-data-sysctl:
	$(MKDIR_P) $(DESTDIR)$(sysconfdir)/sysctl.d
	$(INSTALL_DATA) $(srcdir)/vdsm-sysctl.conf \
		$(DESTDIR)$(sysconfdir)/sysctl.d/vdsm

uninstall-data-sysctl:
	$(RM) $(DESTDIR)$(sysconfdir)/sysctl.d/vdsm

install-data-dhclient-hooks:
	$(MKDIR_P) $(DESTDIR)$(sysconfdir)/dhcp/dhclient.d
	$(INSTALL_DATA) sourceRoute.sh \
		$(DESTDIR)$(sysconfdir)/dhcp/dhclient.d/sourceRoute.sh
	chmod 755 $(DESTDIR)$(sysconfdir)/dhcp/dhclient.d/sourceRoute.sh

uninstall-data-dhclient-hooks:
	$(RM) $(DESTDIR)$(sysconfdir)/dhcp/dhclient.d/sourceRoute.sh
