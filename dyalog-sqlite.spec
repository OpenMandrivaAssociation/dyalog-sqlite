%define name	dyalog-sqlite
%define version 1.0.0
%define release %mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DyAlog SQLITE module
License:	GPL
Group:		Sciences/Computer science
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		ftp://ftp.inria.fr/INRIA/Projects/Atoll/Eric.Clergerie/TAG/%{name}-%{version}.tar.bz2
Url:		http://atoll.inria.fr/packages/packages.html#dyalog-xml
BuildRequires:	dyalog
BuildRequires:	sqlite3-devel
ExclusiveArch:  %{ix86}

%description
A DyALog module providing predicates over SQLITE3 API. This module, while very
preliminary, may be used to create and access sqlite3 databases, for instance
lexicons or lexical preference databases.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	sqlite3-devel
Requires:	%{name} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%setup -q

%build
export CPPFLAGS=-I%{_libdir}/DyALog
export LDFLAGS=-L%{_libdir}/DyALog
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -d -m 755 %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_libdir}/DyALog/%{name}/%{name}.pc %{buildroot}%{_libdir}/pkgconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE README
%{_libdir}/DyALog/%{name}

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/%{name}.pc

