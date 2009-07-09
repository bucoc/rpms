# $Id$
# Authority: dag
# Upstream: Miko O'Sullivan <miko$idocs,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Taxi

Summary: Taint-aware, XML-ish data serialization
Name: perl-Data-Taxi
Version: 0.95
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Taxi/

Source: http://www.cpan.org/modules/by-module/Data/Data-Taxi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Taint-aware, XML-ish data serialization.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/Data::Taxi.3pm*
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/Taxi/
%{perl_vendorlib}/Data/Taxi.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.95-1
- Updated to version 0.95.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.94-1
- Initial package. (using DAR)
