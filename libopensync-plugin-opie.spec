%define name	libopensync-plugin-opie
%define version	0.20
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	OPIE plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		svn://svn.opensync.org/plugins/opie/%{name}-%{version}.tar.bz2
Patch0:         libopensync-plugin-opie-gcc-warnings.diff
URL:		http://www.opensync.org
License:	LGPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= 0.20
BuildRequires:	libneon-devel
BuildRequires:  libcurl-devel

%description
This plugin allows applications using OpenSync to synchronise via OPIE

%prep
%setup -q
%patch0
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
%{_libdir}/opensync/formats/opie.*


