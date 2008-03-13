Name: 	 	libopensync-plugin-opie
Summary: 	OPIE plugin for OpenSync synchronization framework
Epoch:		1
Version: 	0.22
Release: 	%{mkrel 1}
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	GPLv2
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	libneon-devel
BuildRequires:  libcurl-devel
Requires:	libopensync >= %{epoch}:%{version}

%description
This plugin allows OPIE-based devices to synchronize using the OpenSync
framework.

%prep
%setup -q
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
%{_libdir}/opensync/formats/opie.*
