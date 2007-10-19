%define name	libopensync-plugin-opie
%define version	0.33
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	OPIE plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	LGPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= 0.20
BuildRequires:	libneon-devel
BuildRequires:  libcurl-devel
BuildRequires:	scons

%description
This plugin allows applications using OpenSync to synchronise via OPIE

%prep
%setup -q

%build
scons prefix=%{_prefix} libsuffix=%{_lib}

%install
rm -rf $RPM_BUILD_ROOT
scons install DESTDIR=%{buildroot}

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
%{_libdir}/opensync/formats/*
