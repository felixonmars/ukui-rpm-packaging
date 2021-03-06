# enable download source
%undefine _disable_source_fetch
#%define debug_package %{nil}

Name:           kylin-display-switch
Version:        master
Release:        1%{?dist}
Summary:        Gui tool for display switching


License:        GPLv2+
URL:            https://github.com/ukui/kylin-display-switch
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

BuildArch:      x86_64

BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-distutils-extra
BuildRequires: python3-rpm-macros


Requires:  python3-qt5
Requires:  python3-xlib

%description
 Kylin Display Switch is a Gui tool managing display output.
 Super_L + P/F3/F7 are utilized to activate display switching.
 .
 It also monitors CapsLock and NumLock key, when these
 buttons are clicked, corresponding reminder will popper up.

%prep

%setup -q
 
%build

%{py3_build} 

%install
%{py3_install}

mkdir -p %{buildroot}/usr/share/doc/kylin-display-switch/ 
cp debian/copyright  %{buildroot}/usr/share/doc/kylin-display-switch/
gzip -c  debian/changelog >  %{buildroot}/usr/share/doc/kylin-display-switch/changelog.gz


%files
%{_datadir}/doc/kylin-display-switch/changelog.gz
%{_datadir}/doc/kylin-display-switch/copyright
%{_sysconfdir}/xdg/autostart/kylin-display-switch.desktop
%{_bindir}/kds
%{_datadir}/kylin-display-switch/
%{_datadir}/locale/bo/LC_MESSAGES/kylin-display-switch.mo
%{_datadir}/locale/es/LC_MESSAGES/kylin-display-switch.mo
%{_datadir}/locale/fr/LC_MESSAGES/kylin-display-switch.mo
%{_datadir}/locale/pt/LC_MESSAGES/kylin-display-switch.mo
%{_datadir}/locale/ru/LC_MESSAGES/kylin-display-switch.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kylin-display-switch.mo
%{_mandir}/man1/kds.1.gz
%{python3_sitelib}/kylin_display_switch-*.egg-info
