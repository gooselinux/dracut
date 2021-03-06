# Variables must be defined
%define with_switch_root	1
%define with_nbd		1

# switchroot provided by util-linux-ng in F-12+
%if 0%{?fedora} > 11 || 0%{?rhel} >= 6
%define with_switch_root 0
%endif
# nbd in Fedora only
%if 0%{?rhel} >= 6
%define with_nbd 0
%endif

%if %{defined gittag}
%define rdist .git%{gittag}%{?dist}
%define dashgittag -%{gittag}
%else
%define rdist %{?dist}
%endif

Name: dracut
Version: 004
Release: 33.2%{?rdist}
Summary: Initramfs generator using udev
Group: System Environment/Base		
License: GPLv2+	
URL: http://apps.sourceforge.net/trac/dracut/wiki
# Source can be generated by 
# http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=snapshot;h=%{?dashgittag};sf=tgz
Source0: dracut-%{version}%{?dashgittag}.tar.bz2

Patch1: 0001-init-fixed-emergency_shell-argument-parsing.patch
Patch2: 0002-mdraid-prefer-etc-mdadm.conf-over-etc-mdadm-mdadm.co.patch
Patch3: 0003-base-fix-selinux-handling-if-.autorelabel-is-present.patch
Patch4: 0004-Add-a-check-file-for-multipath.patch
Patch6: 0006-beautified-man-pages.patch
Patch7: 0007-init-dashified.patch
Patch8: 0008-dasd_mod-changed-prio-of-cmdline-hook-to-be-executed.patch
Patch9: 0009-test-iSCSI-fixed-test-script.patch
Patch10: 0010-rootfs-block-strip-ro-rw-options-from-fstab-options.patch
Patch11: 0011-zfcp-install-s390utils-script-rather-than-local-one.patch
Patch12: 0012-add-preliminary-IPv6-support.patch
Patch13: 0013-Move-multipath-scan-earlier.-It-must-go-before-any-o.patch
Patch14: 0014-make-nfs4-work.patch
Patch15: 0015-nfs-suppress-error-message-about-missing-passwd.patch
Patch16: 0016-Fixed-Move-multipath-scan-earlier.-It-must-go-before.patch
Patch17: 0017-add-etc-dracut.conf.d.patch
Patch18: 0018-dracut.conf-added-add_dracutmodules.patch
Patch19: 0019-removed-cdrom-hack-for-live-CDs.patch
Patch20: 0020-nfs4-rpc.idmapd-does-not-accept-parameters-anymore.patch
Patch21: 0021-fix-selinux-disabled-state.patch
Patch22: 0022-s390-_cio_free-needs-seq.patch
Patch23: 0023-fix-lib64-check.patch
Patch24: 0024-mount-root-do-not-pollute-init-arguments.patch
Patch25: 0025-selinux-fix-selinux-0-handling.patch
Patch26: 0026-fix-IFS-restoring.patch
Patch27: 0027-dracut-removed-local-not-inside-of-function.patch
Patch28: 0028-mount-root-skip-comments.patch
Patch29: 0029-mount-root-also-filter-defaults-from-mount-options.patch
Patch30: 0030-dracut-add-check-if-we-can-write-to-the-output-image.patch
Patch31: 0031-Use-multipath-if-it-s-installed-and-being-used-for-t.patch
Patch35: 0035-parse-kernel.sh-must-have-a-shebang.patch
Patch37: 0037-kernel-modules-add-keyboard-kernel-modules.patch
Patch38: 0038-udev-rules-choose-between-several-firmware-upload-to.patch
Patch39: 0039-add-readonly-overlay-support-for-dmsquash.patch
Patch40: 0040-dmsquash-live-use-getsize64-instead-of-getsize.patch
Patch41: 0041-Fix-boot-with-user-suspend-and-no-resume-kernel-argu.patch
Patch42: 0042-Pass-init-argument-s-to-real-init.patch
Patch44: 0044-dmsquash-live-root-use-blockdev-with-getsz.patch
Patch45: 0045-rpmversion-install-add-shebang.patch
Patch47: 0047-dracut-do-a-full-ldconfig-in-the-initramfs.patch
Patch48: 0048-dracut-move-ldconfig-after-include.patch
Patch49: 0049-test-use-ldconfig-processing-for-roots-as-well.patch
Patch50: 0050-xen-try-harder-to-locate-xen-detect.patch
Patch55: 0055-silence-xen-detect-detection.patch
Patch56: 0056-kernel-modules-installkernel-force-install-some-modu.patch
Patch57: 0057-lvm_scan-use-ignoremonitoring-rather-than-monitor-n.patch
Patch58: 0058-Add-dcb-support-to-dracut-s-FCoE-support-rh563794.patch
Patch59: 0059-fcoe-soft-install-fcoe-bins.patch
Patch60: 0060-lvm-lvm_scan.sh-silence-lvm-version-check.patch
Patch62: 0062-dracut.spec-remove-libselinux-libsepol-requirement.patch
Patch66: 0066-updated-NEWS-moved-tag-005.patch
Patch67: 0067-dracut.8-fixed-LUKS-paragraph.patch
Patch68: 0068-dracut.8-add-information-which-parameter-can-be-spec.patch
Patch69: 0069-dmraid-parse-different-error-messages.patch
Patch70: 0070-init-add-hacky-cdrom-polling-mechanism.patch
Patch71: 0071-add-module-btrfs.patch
Patch72: 0072-teach-dmsquash-live-root-to-use-rootflags.patch
Patch73: 0073-init-trigger-with-action-add.patch
Patch74: 0074-add-missing-paragraph-for-add-drivers.patch
Patch75: 0075-manpage-addition-for-kernel-drivers.patch
Patch76: 0076-dracut-add_drivers-from-the-command-line-should-add-.patch
Patch77: 0077-AUTHORS-updated.patch
Patch78: 0078-kernel-modules-hardcode-sr_mod.patch
Patch79: 0079-kernel-modules-only-remove-ocfs2-if-all-filesystems-.patch
Patch80: 0080-dracut.spec-add-btrfs-module.patch
Patch81: 0081-Use-pigz-for-gzipping-if-available.patch
Patch82: 0082-nfs-fixed-nsswitch.conf-parsing.patch
Patch83: 0083-network-removed-bogus-udev-rules.patch
Patch84: 0084-network-correct-rules-for-multiple-nics.patch
Patch85: 0085-nfs-add-missing-nfsidmap-libs.patch
Patch86: 0086-udev-rules-be-more-careful-about-md-devices-and-blki.patch
Patch87: 0087-dracut-lib-turn-of-shell-debug-mode-in-strstr-and-ge.patch
Patch88: 0088-mdraid-try-to-start-container-childs-manually-with-m.patch
Patch89: 0089-init-fix-cdrom-polling-loop.patch
Patch90: 0090-init-do-not-redirect-to.patch
Patch91: 0091-loginit-turn-off-debugging.patch
Patch93: 0093-run-qemu-add-usr-libexec-qemu-kvm-to-search.patch
Patch95: 0095-add-rd_retry-kernel-command-line-parameter.patch
Patch101: 0101-dracut.spec-removed-e2fsprogs-requirement.patch
Patch103: 0103-NEWS-update.patch
Patch105: 0105-Needs-btrfsctl-not-btrfs-module.patch
Patch106: 0106-btfrs-load-btrfs-module-and-updated-NEWS.patch
Patch107: 0107-kernel-modules-add-more-hardcoded-modules.patch
Patch109: 0109-dracut.conf-use-as-default-for-config-variables.patch
Patch110: 0110-znet-use-ccw-init-and-ccw-rules-from-s390utils-in-dr.patch
Patch111: 0111-znet-renamed-rd_CCW-to-rd_ZNET.patch
Patch112: 0112-fcoe-add-sbin-vconfig-and-the-8021q-kernel-module.patch
Patch113: 0113-dracut.8-fix-rd_LVM_LV-description.patch
Patch114: 0114-plymouth-only-display-luksname-and-device-for-multip.patch
Patch115: 0115-dracut.spec-remove-elfutils-libelf-requirement.patch
Patch116: 0116-use-grep-directly-without-nm-to-drop-binutils-requir.patch
Patch117: 0117-plymouth-plymouth-populate-initrd-get-rid-of-awk.patch
Patch118: 0118-dracut-get-rid-of-the-file-command.patch
Patch120: 0120-90mdraid-dracut-functions-fix-md-raid-hostonly-detec.patch
Patch121: 0121-40network-parse-ip-opts.sh-add-ip-auto6-to-valid-opt.patch
Patch122: 0122-40network-dhclient-script-be-more-verbose.patch
Patch123: 0123-40network-ifup-be-more-verbose.patch
Patch125: 0125-95fcoe-fcoe-up-wait_for_if_up.patch
Patch126: 0126-get-rid-of-rdnetdebug.patch
Patch130: 0130-selinux-loadpolicy.sh-exit-for-selinux-0.patch
Patch131: 0131-dracut-functions-check-if-specific-dracut-module-is-.patch
Patch132: 0132-dracut-functions-beautified-warnings.patch
Patch133: 0133-multipath-simplify-and-install-wwids-rhbz-595719.patch
Patch134: 0134-multipath-remove-multipath-udev-rules-if-no-multipat.patch
Patch136: 0136-Just-look-for-cryptroot-instead-of-sbin-cryptroot.patch
Patch137: 0137-Have-cryptroot-ask-load-dm_crypt-if-needed.patch
Patch140: 0140-90crypt-crypto_LUKS-identifier-corrected.patch
Patch142: 0142-plymouth-cryptroot-ask.sh-beautify-password-prompt.patch
Patch143: 0143-iscsi-add-support-for-multiple-netroot-iscsi.patch
Patch145: 0145-lvm-install-lvm-mirror-and-snaphot-libs.patch
Patch146: 0146-network-depend-on-ifcfg-if-etc-sysconfig-network-scr.patch
Patch147: 0147-crypt-install-more-aes-modules.patch
Patch148: 0148-network-strip-pxelinux-hardware-type-field-from-BOOT.patch
Patch152: 0152-fixed-ip-dhcp6.patch
Patch153: 0153-dracut.8-add-note-about-putting-IPv6-addresses-in-br.patch
Patch154: 0154-dracut.8-changed-IPv6-addresses-to-the-documentation.patch
Patch155: 0155-fips-fixes-copy-paste-error-for-check.patch
Patch156: 0156-crypt-add-fpu-kernel-module.patch
Patch157: 0157-Write-rules-for-symlinks-to-dev-.udev-rules.d-for-la.patch
Patch158: 0158-dracut-functions-set-LANG-C-for-ldd-output-parsing.patch
Patch159: 0159-dracut-functions-use-LC_ALL-C-rather-than-LANG-C.patch
Patch160: 0160-dmsquash-resume-do-not-name-the-dev-.udev-rules-like.patch
Patch166: 0166-dmsquash-live-mount-live-image-at-dev-.initramfs-liv.patch
Patch167: 0167-fcoe-moved-fcoeup-to-initqueue-udev-timeouts.patch
Patch169: 0169-dmsquash-live-depend-on-dm-module.patch
Patch170: 0170-dm-load-dm_mod-if-device-mapper-not-in-proc-misc.patch
Patch171: 0171-dmsquash-live-do-not-umount-dev-.initramfs-live-for-.patch
Patch172: 0172-plymouth-depend-on-crypt-if-cryptsetup-exists.patch
Patch174: 0174-crypt-assemble-70-luks.rules-dynamically.patch
Patch175: 0175-crypt-removed-default-70-luks.rules.patch
Patch176: 0176-crypt-parse-crypt.sh-fix-end-label-for-luks-udev-rul.patch
Patch178: 0178-crypt-wait-for-all-rd_LUKS_UUID-disks-to-appear.patch
Patch196: 0196-mknod-with-mode-and-set-umask-for-the-rest.patch
Patch197: 0197-lvm-wait-for-all-rd_LVM_LV-and-rd_LVM_VG-specified-t.patch
Patch198: 0198-fcoe-add-sleeps-to-fcoe-up.patch

Patch200: dracut-004-mkinitrd.patch

Patch1137: 1137-init-do-not-umask.patch
Patch1138: 1138-selinux-fixed-error-handling-for-load-policy.patch
Patch1139: 1139-crypt-strip-luks-from-rd_LUKS_UUID.patch
Patch1140: 1140-dracut-functions-filter_kernel_modules-search-in-ext.patch

Patch1144: 1144-add-96insmodpost-dracut-module.patch

Patch1200: dracut-honor-DM_UDEV_DISABLE_OTHER_RULES_FLAG.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} > 12 || 0%{?rhel} >= 6
# no "provides", because dracut does not offer
# all functionality of the obsoleted packages
Obsoletes: mkinitrd <= 6.0.93
Obsoletes: mkinitrd-devel <= 6.0.93
Obsoletes: nash <= 6.0.93
Obsoletes: libbdevid-python <= 6.0.93
%endif

Requires: bash
Requires: bzip2
Requires: coreutils
Requires: cpio
Requires: dash
Requires: filesystem >= 2.1.0
Requires: findutils
Requires: grep
Requires: gzip
Requires: initscripts >= 8.63-1
Requires: kbd
Requires: mktemp >= 1.5-5
Requires: module-init-tools >= 3.7-9
Requires: mount
Requires: plymouth >= 0.8.0-0.2009.29.09.19.1
Requires: plymouth-scripts
Requires: sed
Requires: tar
Requires: udev
Requires: util-linux-ng >= 2.16
Requires: which

%if ! 0%{?with_switch_root}
Requires: util-linux-ng >= 2.16
BuildArch: noarch
%endif

%description
dracut is a new, event-driven initramfs infrastructure based around udev.

%package network
Summary: Dracut modules to build a dracut initramfs with network support
Requires: %{name} = %{version}-%{release}
Requires: dhclient rpcbind nfs-utils 
Requires: iscsi-initiator-utils
%if %{with_nbd}
Requires: nbd
%endif
Requires: net-tools iproute
Requires: bridge-utils
Requires: vconfig

%description network
This package requires everything which is needed to build a generic
all purpose initramfs with network support with dracut.

%package fips
Summary: Dracut modules to build a dracut initramfs with an integrity check
Requires: %{name} = %{version}-%{release}
Requires: hmaccalc
%if 0%{?rhel} > 5
# For Alpha 3, we want nss instead of nss-softokn
Requires: nss
%else
Requires: nss-softokn
%endif
Requires: nss-softokn-freebl

%description fips
This package requires everything which is needed to build an
all purpose initramfs with dracut, which does an integrity check.

%package generic
Summary: Metapackage to build a generic initramfs with dracut
Requires: %{name} = %{version}-%{release}
Requires: %{name}-network = %{version}-%{release}

%description generic
This package requires everything which is needed to build a generic
all purpose initramfs with dracut.


%package kernel
Summary: Metapackage to build generic initramfs with dracut with only kernel modules
Requires: %{name} = %{version}-%{release}

%description kernel
This package requires everything which is needed to build a initramfs with all
kernel modules and firmware files needed by dracut modules.

%package tools
Summary: Dracut tools to build the local initramfs
Requires: %{name} = %{version}-%{release}
Requires: coreutils cryptsetup-luks device-mapper
Requires: diffutils dmraid findutils gawk grep lvm2
Requires: module-init-tools sed
Requires: cpio gzip

%description tools
This package contains tools to assemble the local initrd and host configuration.

%prep
%setup -q -n %{name}-%{version}%{?dashgittag}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch35 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch44 -p1
%patch45 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch62 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch93 -p1
%patch95 -p1
%patch101 -p1
%patch103 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch125 -p1
%patch126 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch136 -p1
%patch137 -p1
%patch140 -p1
%patch142 -p1
%patch143 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch166 -p1
%patch167 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch178 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1

%patch200 -p1

%patch1137 -p1
%patch1138 -p1
%patch1139 -p1
%patch1140 -p1
%patch1144 -p1
%patch1200 -p1

chmod 0755 modules.d/*/check
# make rpmlint happy
chmod 0755 modules.d/*/install
chmod 0755 modules.d/*/installkernel
chmod 0755 modules.d/45ifcfg/write-ifcfg.sh
chmod 0755 modules.d/96insmodpost/insmodpost.sh

%build
make WITH_SWITCH_ROOT=0%{?with_switch_root}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT sbindir=/sbin \
     sysconfdir=/etc mandir=%{_mandir} WITH_SWITCH_ROOT=0%{?with_switch_root}

echo %{name}-%{version}-%{release} > $RPM_BUILD_ROOT/%{_datadir}/dracut/modules.d/10rpmversion/dracut-version
rm $RPM_BUILD_ROOT/%{_datadir}/dracut/modules.d/01fips/check

mkdir -p $RPM_BUILD_ROOT/boot/dracut
mkdir -p $RPM_BUILD_ROOT/var/lib/dracut/overlay
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log
touch $RPM_BUILD_ROOT%{_localstatedir}/log/dracut.log

%if 0%{?fedora} <= 12 && 0%{?rhel} < 6
rm $RPM_BUILD_ROOT/sbin/mkinitrd
rm $RPM_BUILD_ROOT/sbin/lsinitrd
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README HACKING TODO COPYING AUTHORS NEWS
/sbin/dracut
%if 0%{?with_switch_root}
/sbin/switch_root
%endif
%if 0%{?fedora} > 12 || 0%{?rhel} >= 6
/sbin/mkinitrd
/sbin/lsinitrd
%endif
%dir %{_datadir}/dracut
%{_datadir}/dracut/dracut-functions
%config(noreplace) /etc/dracut.conf
%dir /etc/dracut.conf.d
%{_mandir}/man8/dracut.8*
%{_mandir}/man5/dracut.conf.5*
%{_datadir}/dracut/modules.d/00dash
%{_datadir}/dracut/modules.d/10redhat-i18n
%{_datadir}/dracut/modules.d/10rpmversion
%{_datadir}/dracut/modules.d/50plymouth
%{_datadir}/dracut/modules.d/60xen
%{_datadir}/dracut/modules.d/90btrfs
%{_datadir}/dracut/modules.d/90crypt
%{_datadir}/dracut/modules.d/90dm
%{_datadir}/dracut/modules.d/90dmraid
%{_datadir}/dracut/modules.d/90dmsquash-live
%{_datadir}/dracut/modules.d/90kernel-modules
%{_datadir}/dracut/modules.d/90lvm
%{_datadir}/dracut/modules.d/90mdraid
%{_datadir}/dracut/modules.d/90multipath
%{_datadir}/dracut/modules.d/95debug
%{_datadir}/dracut/modules.d/95resume
%{_datadir}/dracut/modules.d/95rootfs-block
%{_datadir}/dracut/modules.d/95dasd
%{_datadir}/dracut/modules.d/95dasd_mod
%{_datadir}/dracut/modules.d/95zfcp
%{_datadir}/dracut/modules.d/95znet
%{_datadir}/dracut/modules.d/95terminfo
%{_datadir}/dracut/modules.d/95udev-rules
%{_datadir}/dracut/modules.d/95uswsusp
%{_datadir}/dracut/modules.d/96insmodpost
%{_datadir}/dracut/modules.d/98syslog
%{_datadir}/dracut/modules.d/99base
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/dracut.log

%files network
%defattr(-,root,root,0755)
%doc README HACKING TODO COPYING AUTHORS NEWS
%{_datadir}/dracut/modules.d/40network
%{_datadir}/dracut/modules.d/95fcoe
%{_datadir}/dracut/modules.d/95iscsi
%{_datadir}/dracut/modules.d/95nbd
%{_datadir}/dracut/modules.d/95nfs
%{_datadir}/dracut/modules.d/45ifcfg

%files fips
%defattr(-,root,root,0755)
%doc COPYING
%{_datadir}/dracut/modules.d/01fips

%files kernel 
%defattr(-,root,root,0755)
%doc README.kernel

%files generic
%defattr(-,root,root,0755)
%doc README.generic

%files tools 
%defattr(-,root,root,0755)
%doc COPYING NEWS
%{_mandir}/man8/dracut-gencmdline.8*
%{_mandir}/man8/dracut-catimages.8*
/sbin/dracut-gencmdline
/sbin/dracut-catimages
%dir /boot/dracut
%dir /var/lib/dracut
%dir /var/lib/dracut/overlay
 
%changelog
* Fri Jan 07 2011 Harald Hoyer <harald@redhat.com> 004-33.2
- chmod 0755 modules.d/96insmodpost/insmodpost.sh
Resolves: rhbz#661298

* Wed Dec 08 2010 Harald Hoyer <harald@redhat.com> 004-33.1
- add 96insmodpost dracut module
Resolves: rhbz#661298

* Tue Nov 09 2010 Harald Hoyer <harald@redhat.com> 004-33
- honor DM_UDEV_DISABLE_OTHER_RULES_FLAG
Resolves: rhbz#651402

* Thu Aug 19 2010 Harald Hoyer <harald@redhat.com> 004-32
- do not call dracut with hostonly from within mkinitrd
Resolves: rhbz#624826

* Wed Aug 11 2010 Harald Hoyer <harald@redhat.com> 004-31
- also search in "updates"
Resolves: rhbz#622641

* Tue Aug 10 2010 Harald Hoyer <harald@redhat.com> 004-30
- search for kernel modules also in "extra" and "weak-updates"
Resolves: rhbz#622641

* Thu Jul 29 2010 Harald Hoyer <harald@redhat.com> 004-29
- strip "luks-" from rd_LUKS_UUID while processing
Resolves: rhbz#607699

* Thu Jul 29 2010 Harald Hoyer <harald@redhat.com> 004-28
- do not set strict umask
Resolves: rhbz#617526

* Tue Jul 27 2010 Harald Hoyer <harald@redhat.com> 004-27
- fixed device permission
Resolves: rhbz#617526 

* Fri Jul 23 2010 Harald Hoyer <harald@redhat.com> 004-26
- wait for LVM and crypt devices to appear
Resolves: rhbz#607699
- add sleeps to fcoe-up and move it out of udev
Resolves: rhbz#611976
- fixed selinux return code handling
Resolves: rhbz#615950

* Fri Jul 09 2010 Harald Hoyer <harald@redhat.com> 004-25
- mount live images to /dev/.initramfs/live and do not
  umount it, so that cdrom_id works in the real root
  and /dev/live is pointing to the correct device
Resolves: rhbz#605356

* Mon Jul 05 2010 Harald Hoyer <harald@redhat.com> 004-24
- removed dependency of tools, which should be installed 
  by anaconda
Resolves: rhbz#598509

* Tue Jun 29 2010 Harald Hoyer <harald@redhat.com> 004-23
- add vconfig requirement to dracut-network
Resolves: rhbz#608015
- fixed dhcp6 option for ip argument
Resolves: rhbz#605283

* Mon Jun 21 2010 Harald Hoyer <harald@redhat.com> 004-22
- add fpu kernel module to crypt
Resolves: rhbz#600170

* Fri Jun 11 2010 Harald Hoyer <harald@redhat.com> 004-21
- Remove requirements, which are not really needed
Resolves: rhbz#598509
- fixed copy of network config to /dev/.initramfs/ (patch 146)
Resolves: rhbz#594649
- more password beauty (patch 142)
Resolves: rhbz#561092
- support multiple iSCSI disks (patch 143)
Resolves: rbhz#580190
- fixed selinux=0 (patch 130)
Resolves: rhbz#593080
- add support for booting LVM snapshot root volume (patch 145)
Resolves: rbhz#602723
- remove hardware field from BOOTIF= (patch 148)
Resolves: rhbz#599593
- add aes kernel modules and fix crypt handling (patch 137, patch 140 and patch 147)
Resolves: rhbz#600170

* Wed Jun 02 2010 Phil Knirsch <pknirsch@redhat.com> 004-20.1
- Reverted and fixed up most of the requirement changes
Resolves: #598509

* Thu May 27 2010 Harald Hoyer <harald@redhat.com> 004-20
- fixed Requirements
- fixed autoip6 
Resolves: rhbz#538388
- fixed multipath
Resolves: rhbz#595719

* Thu May 06 2010 Harald Hoyer <harald@redhat.com> 004-19
- only display short password messages
Resolves: rhbz#561092

* Thu May 06 2010 Harald Hoyer <harald@redhat.com> 004-18
- fixed dracut manpages 
Resolves: rhbz#589109
- use ccw-init and ccw rules from s390utils
Resolves: rhbz#533494
- fixed fcoe
Resolves: rhbz#486244
- various other bugfixes seen in Fedora

* Thu Mar 25 2010 Harald Hoyer <harald@redhat.com> 004-17
- removed firmware requirements (rhbz#572634)
- add /etc/dracut.conf.d
- Resolves: rhbz#572634

* Fri Mar 19 2010 Harald Hoyer <harald@redhat.com> 004-16
- fixed rpmlint errors (rhbz#570547)
- removed firmware package from dracut-kernel (rhbz#572634)
- add dcb support to dracut's FCoE support (rhbz#563794)
- force install some modules in hostonly mode (rhbz#573094)
- various other bugfixes
- Resolves: rhbz#570547, rhbz#572634, rhbz#563794, rhbz#573094

* Thu Feb 18 2010 Harald Hoyer <harald@redhat.com> 004-15
- fixed "selinux=0" booting (rhbz#566376)
- fixed internal IFS handling
- Resolves: rhbz#566376

* Wed Feb 17 2010 Harald Hoyer <harald@redhat.com> 004-14
- fixed remount root (rhbz#566246)
- Resolves: rhbz#566246

* Wed Feb 17 2010 Harald Hoyer <harald@redhat.com> 004-13
- fixed multipath scanning
- fixed NFS4 (rhbz#564293)
- add /etc/dracut.conf.d config dir
- fixed selinux disabled state
- fixed s390 cio scripts
- fixed lib64 check (rhbz#562113)
- Resolves: rhbz#564293, rhbz#562113 

* Mon Feb 08 2010 Harald Hoyer <harald@redhat.com> 004-12
- add IPv6 support
- fixed multipath check
- fixed selinux autorelabel case
- Resolves: rhbz#546615 rhbz#553195

* Tue Jan 26 2010 Harald Hoyer <harald@redhat.com> 004-3
- fix selinux handling if .autorelabel is present
- Resolves: rhbz#557744

* Wed Jan 20 2010 Harald Hoyer <harald@redhat.com> 004-2
- fix emergency_shell argument parsing
- Related: rhbz#543948

* Fri Jan 15 2010 Harald Hoyer <harald@redhat.com> 004-1
- version 004
- Resolves: rhbz#529339 rhbz#533494 rhbz#548550 
- Resolves: rhbz#548555 rhbz#553195

* Wed Jan 13 2010 Harald Hoyer <harald@redhat.com> 003-3
- add Obsoletes of mkinitrd/nash/libbdevid-python
- Related: rhbz#543948

* Wed Jan 13 2010 Warren Togami <wtogami@redhat.com> 003-2
- nbd is Fedora only

* Fri Nov 27 2009 Harald Hoyer <harald@redhat.com> 003-1
- version 003

* Mon Nov 23 2009 Harald Hoyer <harald@redhat.com> 002-26
- add WITH_SWITCH_ROOT make flag
- add fips requirement conditional
- add more device mapper modules (bug #539656)

* Fri Nov 20 2009 Dennis Gregorovic <dgregor@redhat.com> - 002-25.1
- nss changes for Alpha 3

* Thu Nov 19 2009 Harald Hoyer <harald@redhat.com> 002-25
- add more requirements for dracut-fips (bug #539257)

* Tue Nov 17 2009 Harald Hoyer <harald@redhat.com> 002-24
- put fips module in a subpackage (bug #537619)

* Tue Nov 17 2009 Harald Hoyer <harald@redhat.com> 002-23
- install xdr utils for multipath (bug #463458)

* Thu Nov 12 2009 Harald Hoyer <harald@redhat.com> 002-22
- add module 90multipath
- add module 01fips
- renamed module 95ccw to 95znet (bug #533833)
- crypt: ignore devices in /etc/crypttab (root is not in there)
- dasd: only install /etc/dasd.conf in hostonly mode (bug #533833)
- zfcp: only install /etc/zfcp.conf in hostonly mode (bug #533833)
- kernel-modules: add scsi_dh scsi_dh_rdac scsi_dh_emc (bug #527750)
- dasd: use dasdconf.sh from s390utils (bug #533833)

* Fri Nov 06 2009 Harald Hoyer <harald@redhat.com> 002-21
- fix rd_DASD argument handling (bug #531720)
- Resolves: rhbz#531720

* Wed Nov 04 2009 Harald Hoyer <harald@redhat.com> 002-20
- fix rd_DASD argument handling (bug #531720)
- Resolves: rhbz#531720

* Tue Nov 03 2009 Harald Hoyer <harald@redhat.com> 002-19
- changed rd_DASD to rd_DASD_MOD (bug #531720)
- Resolves: rhbz#531720

* Tue Oct 27 2009 Harald Hoyer <harald@redhat.com> 002-18
- renamed lvm/device-mapper udev rules according to upstream changes
- fixed dracut search path issue

* Mon Oct 26 2009 Harald Hoyer <harald@redhat.com> 002-17
- load dm_mod module (bug #530540)

* Fri Oct 09 2009 Jesse Keating <jkeating@redhat.com> - 002-16
- Upgrade plymouth to Requires(pre) to make it show up before kernel

* Thu Oct 08 2009 Harald Hoyer <harald@redhat.com> 002-15
- s390 ccw: s/layer1/layer2/g

* Thu Oct 08 2009 Harald Hoyer <harald@redhat.com> 002-14
- add multinic support
- add s390 zfcp support
- add s390 network support

* Wed Oct 07 2009 Harald Hoyer <harald@redhat.com> 002-13
- fixed init=<command> handling
- kill loginit if "rdinitdebug" specified
- run dmsquash-live-root after udev has settled (bug #527514)

* Tue Oct 06 2009 Harald Hoyer <harald@redhat.com> 002-12
- add missing loginit helper
- corrected dracut manpage

* Thu Oct 01 2009 Harald Hoyer <harald@redhat.com> 002-11
- fixed dracut-gencmdline for root=UUID or LABEL

* Thu Oct 01 2009 Harald Hoyer <harald@redhat.com> 002-10
- do not destroy assembled raid arrays if mdadm.conf present
- mount /dev/shm 
- let udevd not resolve group and user names
- preserve timestamps of tools on initramfs generation
- generate symlinks for binaries correctly
- moved network from udev to initqueue
- mount nfs3 with nfsvers=3 option and retry with nfsvers=2
- fixed nbd initqueue-finished
- improved debug output: specifying "rdinitdebug" now logs
  to dmesg, console and /init.log
- stop udev before killing it
- add ghost /var/log/dracut.log
- dmsquash: use info() and die() rather than echo
- strip kernel modules which have no x bit set
- redirect stdin, stdout, stderr all RW to /dev/console
  so the user can use "less" to view /init.log and dmesg

* Tue Sep 29 2009 Harald Hoyer <harald@redhat.com> 002-9
- make install of new dm/lvm udev rules optionally
- correct dasd module typo

* Fri Sep 25 2009 Warren Togami <wtogami@redhat.com> 002-8
- revert back to dracut-002-5 tarball 845dd502
  lvm2 was reverted to pre-udev

* Wed Sep 23 2009 Harald Hoyer <harald@redhat.com> 002-7
- build with the correct tarball

* Wed Sep 23 2009 Harald Hoyer <harald@redhat.com> 002-6
- add new device mapper udev rules and dmeventd 
  bug 525319, 525015

* Wed Sep 23 2009 Warren Togami <wtogami@redaht.com> 002-5
- Revert back to -3, Add umount back to initrd
  This makes no functional difference to LiveCD.  See Bug #525319

* Mon Sep 21 2009 Warren Togami <wtogami@redhat.com> 002-4
- Fix LiveCD boot regression

* Mon Sep 21 2009 Harald Hoyer <harald@redhat.com> 002-3
- bail out if selinux policy could not be loaded and 
  selinux=0 not specified on kernel command line 
  (bug #524113)
- set finished criteria for dmsquash live images

* Fri Sep 18 2009 Harald Hoyer <harald@redhat.com> 002-2
- do not cleanup dmraids
- copy over lvm.conf

* Thu Sep 17 2009 Harald Hoyer <harald@redhat.com> 002-1
- version 002
- set correct PATH
- workaround for broken mdmon implementation

* Wed Sep 16 2009 Harald Hoyer <harald@redhat.com> 001-12
- removed lvm/mdraid/dmraid lock files
- add missing ifname= files

* Wed Sep 16 2009 Harald Hoyer <harald@redhat.com> 001-11
- generate dracut-version during rpm build time

* Tue Sep 15 2009 Harald Hoyer <harald@redhat.com> 001-10
- add ifname= argument for persistent netdev names
- new /initqueue-finished to check if the main loop can be left
- copy mdadm.conf if --mdadmconf set or mdadmconf in dracut.conf

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-9
- added Requires: plymouth-scripts

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-8
- plymouth: use plymouth-populate-initrd
- add add_drivers for dracut and dracut.conf
- do not mount /proc and /selinux manually in selinux-load-policy

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-7
- add scsi_wait_scan to be sure everything was scanned

* Tue Sep 08 2009 Harald Hoyer <harald@redhat.com> 001-6
- fixed several problems with md raid containers
- fixed selinux policy loading

* Tue Sep 08 2009 Harald Hoyer <harald@redhat.com> 001-5
- patch does not honor file modes, fixed them manually

* Mon Sep 07 2009 Harald Hoyer <harald@redhat.com> 001-4
- fixed mdraid for IMSM

* Mon Sep 07 2009 Harald Hoyer <harald@redhat.com> 001-3
- fixed bug, which prevents installing 61-persistent-storage.rules (bug #520109)

* Thu Sep 03 2009 Harald Hoyer <harald@redhat.com> 001-2
- fixed missing grep for md
- reorder cleanup

* Wed Sep 02 2009 Harald Hoyer <harald@redhat.com> 001-1
- version 001
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Aug 14 2009 Harald Hoyer <harald@redhat.com> 0.9-1
- version 0.9

* Thu Aug 06 2009 Harald Hoyer <harald@redhat.com> 0.8-1
- version 0.8 
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Jul 24 2009 Harald Hoyer <harald@redhat.com> 0.7-1
- version 0.7
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Wed Jul 22 2009 Harald Hoyer <harald@redhat.com> 0.6-1
- version 0.6
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Jul 17 2009 Harald Hoyer <harald@redhat.com> 0.5-1
- version 0.5
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Sat Jul 04 2009 Harald Hoyer <harald@redhat.com> 0.4-1
- version 0.4
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Thu Jul 02 2009 Harald Hoyer <harald@redhat.com> 0.3-1
- version 0.3
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Wed Jul 01 2009 Harald Hoyer <harald@redhat.com> 0.2-1
- version 0.2

* Fri Jun 19 2009 Harald Hoyer <harald@redhat.com> 0.1-1
- first release

* Thu Dec 18 2008 Jeremy Katz <katzj@redhat.com> - 0.0-1
- Initial build

