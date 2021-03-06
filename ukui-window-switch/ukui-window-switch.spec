# enable download source
%undefine _disable_source_fetch

Name:           ukui-window-switch
Version:        master
Release:        1%{?dist}
Summary:        Front of the window switch



License:        GPLv2+
URL:            https://github.com/ukui/qt5-ukui-platformtheme
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

BuildArch:      x86_64



BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: gtk3-devel
BuildRequires: libwnck3-devel

Requires: ukwm



%description
 Front of the window switcher in UKUI desktop environment.
 Provides the display function(Display window thumbnails and application
 icons) when the window is switching (press Alt+Tab key).

%prep

%setup -q
 
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

%files
%doc debian/copyright debian/changelog
%{_sysconfdir}/ukui/ukui-window-switch/ukui-window-switch.conf
%{_bindir}/ukui-window-switch
%{_datadir}/dbus-1/services/org.ukui.WindowSwitch.service
%{_datadir}/ukui-window-switch/
