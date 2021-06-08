%bcond_with check
%global _unpackaged_files_terminate_build 0 
%global debug_package   %{nil}
%global common_description %{expand: Something like everything, but nothing is really like anything...}
%global dname dkms
%global lname libs
%global sname server

Name:          deepin-anything
Version:       5.0.1
Release:       2
Summary:       Something like everything, but nothing is really like anything...
License:       GPLv3
URL:           https://uos-packages.deepin.com/uos/pool/main/d/deepin-anything/
Source0:       %{name}-%{version}.orig.tar.xz

BuildRequires: qt5-qtbase-devel
BuildRequires: dtkcore-devel
BuildRequires: udisks2-qt5
BuildRequires: udisks2-qt5-devel
BuildRequires: libmount
BuildRequires: libmount-devel


%description
%{common_description}

%package -n %{name}-%{dname}
Summary:    %{summary}
%description -n %{name}-%{dname}


%package -n %{name}-%{lname}
Summary:    %{summary}
%description -n %{name}-%{lname}

%package -n %{name}-%{sname}
Summary:    %{summary}
%description -n %{name}-%{sname}

%prep
%setup
sed -i 's|lib/|lib64/|g' Makefile

%build
export PATH=$PATH:%{_libdir}/qt5/bin
%{__make}

%install
%make_install
mkdir -p %{?buildroot}/usr/lib/modules-load.d/
mkdir -p %{buildroot}/usr/lib/systemd/system/
install -Dm644 server/tool/deepin-anything-tool.service %{buildroot}/usr/lib/systemd/system/
install -Dm644 server/monitor/deepin-anything-monitor.service %{buildroot}/usr/lib/systemd/system/

%files -n  %{name}-%{dname}
%exclude /usr/lib/modules-load.d/anything.conf
%{_usrsrc}/deepin-anything-0.0/*

%files -n  %{name}-%{lname}
%{_libdir}/libanything.so
%{_libdir}/libanything.so.1
%{_libdir}/libanything.so.1.0
%{_libdir}/libanything.so.1.0.0

%files -n  %{name}-%{sname}
%{_bindir}/deepin-anything-monitor
%{_bindir}/deepin-anything-tool
%{_bindir}/deepin-anything-tool-ionice
%{_libdir}/libdeepin-anything-server-lib.so
%{_libdir}/libdeepin-anything-server-lib.so.0
%{_libdir}/libdeepin-anything-server-lib.so.0.0
%{_libdir}/libdeepin-anything-server-lib.so.0.0.1
%{_libdir}/deepin-anything-server-lib/plugins/handlers/README.txt
%{_libdir}/deepin-anything-server-lib/plugins/handlers/libupdate-lft.so
%{_datadir}/dbus-1/interfaces/com.deepin.anything.xml
%{_datadir}/dbus-1/system-services/com.deepin.anything.service
%{_sysconfdir}/dbus-1/system.d/com.deepin.anything.conf
%exclude /usr/lib/systemd/system/deepin-anything-monitor.service
/usr/lib/systemd/system/deepin-anything-tool.service


%changelog
* Tue Jun 08 2021 weidong <weidong@uniontech.com> - 5.0.1-2
- openEuler kernel don't support vfs,so delete deepin-anything-monitor.service

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.1-1
- Package init
