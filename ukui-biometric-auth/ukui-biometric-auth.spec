# enable download source
%undefine _disable_source_fetch

Name:           ukui-biometric-auth
Version:        master
Release:        1%{?dist}
Summary:        ukui-biometric-auth

License:        GPLv2+
URL:            https://github.com/ukui/%{name}
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

Patch0:        ukui-biometric-auth-libdir.patch

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  pam-devel
BuildRequires:  polkit-qt5-1-devel

Requires: pam-biometric
Requires: ukui-polkit

%description
ukui-biometric-auth



%package -n pam-biometric
Summary: Insertable authentication module for PAM




%description -n pam-biometric
 The indispensable part for biometric authentication in
 ukui desktop environment.
 This package contains a modules for PAM.




%package -n ukui-polkit

Summary: UKUI authentication agent for PolicyKit-1


%description -n ukui-polkit
 The ukui-polkit package supports general authentication and
 biometric authentication that the service is provided by the
 biometric-auth package.


%prep

%setup -q
%patch0 -p0

%build
mkdir cmake-build
pushd cmake-build
%cmake3 ..
%{make_build}
popd

%install
pushd cmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
popd
mkdir  -p  %{buildroot}/usr/share/man/man1/
gzip -c man/bioctl.1 > %{buildroot}/usr/share/man/man1/bioctl.1.gz
gzip -c man/bioauth.1 > %{buildroot}/usr/share/man/man1/bioauth.1.gz
gzip -c man/biodrvctl.1 > %{buildroot}/usr/share/man/man1/biodrvctl.1.gz

%files
%doc debian/changelog debian/copyright
%{_datadir}/ukui-biometric/images
%{_datadir}/ukui-biometric/i18n_qm/es.qm
%{_datadir}/ukui-biometric/i18n_qm/fr.qm
%{_datadir}/ukui-biometric/i18n_qm/pt.qm
%{_datadir}/ukui-biometric/i18n_qm/ru.qm
%{_datadir}/ukui-biometric/i18n_qm/zh_CN.qm
%{_datadir}/ukui-biometric/i18n_qm/bo.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/bo.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/tr.qm
%{_datadir}/ukui-biometric/i18n_qm/tr.qm


%files -n pam-biometric
%{_bindir}/bioauth
%{_bindir}/bioctl
%{_bindir}/biodrvctl
%{_sysconfdir}/biometric-auth/ukui-biometric.conf
%{_libdir}/security/pam_biometric.so
%{_datadir}/pam-configs/pam-biometric
%{_datadir}/polkit-1/actions/org.freedesktop.plicykit.pkexec.bioctl.policy
%{_datadir}/polkit-1/actions/org.freedesktop.plicykit.pkexec.biodrvctl.policy
%{_datadir}/ukui-biometric/i18n_qm/bioauth-bin
%{_mandir}/man1/bioctl.1.gz
%{_mandir}/man1/bioauth.1.gz
%{_mandir}/man1/biodrvctl.1.gz


%files -n  ukui-polkit
%{_sysconfdir}/xdg/autostart/polkit-ukui-authentication-agent-1.desktop
%{_libdir}/ukui-polkit/polkit-ukui-authentication-agent-1
%{_datadir}/ukui-biometric/i18n_qm/polkit/es.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/fr.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/pt.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/ru.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/zh_CN.qm
        