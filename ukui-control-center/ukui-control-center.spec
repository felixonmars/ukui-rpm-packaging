# enable download source
%undefine _disable_source_fetch

Name:           ukui-control-center
Version:        master
Release:        1%{?dist}
Summary:        utilities to configure the UKUI desktop


License:        GPLv2+
URL:            https://github.com/ukui/%{name}
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

Patch0:        ukui-control-center-libdir.patch

BuildArch:      x86_64

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  glib2-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libxklavier-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  dconf-devel
BuildRequires:  redshift
BuildRequires:  edid-decode
BuildRequires:  libmatemixer-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  libxml2-devel
BuildRequires:  libkscreen-qt5-devel
BuildRequires:  kf5-ki18n-devel
Recommends: edid-decode
Recommends: redshift
Recommends: qt5-qtquickcontrols


Suggests: gsettings-desktop-schemas
Suggests: mate-common
Suggests: ukui-power-manager
Suggests: ukui-session-manager
Suggests: ukui-screensaver
Suggests: ukui-settings-daemon
Suggests: qt5-qtgraphicaleffects

%description
utilities to configure the UKUI desktop
 The UKUI control center contains configuration applets for the UKUI desktop,
 allowing to set accessibility configuration, desktop fonts, keyboard
 and mouse properties, sound setup, desktop theme and background, user
 interface properties, screen resolution, and other UKUI parameters.

%prep
%setup -q
%patch0 -p0

%build
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
popd
mkdir -p %{buildroot}/usr/share/dbus-1/system-services/ %{buildroot}/etc/dbus-1/system.d/ 
cp registeredQDbus/conf/com.control.center.qt.systemdbus.service %{buildroot}/usr/share/dbus-1/system-services/
cp registeredQDbus/conf/com.control.center.qt.systemdbus.conf %{buildroot}/etc/dbus-1/system.d/
 

%files
%doc debian/copyright debian/changelog
%{_sysconfdir}/dbus-1/system.d/com.control.center.qt.systemdbus.conf
%{_bindir}/launchSysDbus
%{_bindir}/ukui-control-center
%{_libdir}/control-center/
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/ukui-control-center.desktop
%{_datadir}/dbus-1/system-services/com.control.center.qt.systemdbus.service
%{_datadir}/ukui/faces/*
%{_datadir}/locale/zh_CN/LC_MESSAGES/installer-timezones.mo