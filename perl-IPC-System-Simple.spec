%define upstream_name    IPC-System-Simple
%define upstream_version 1.21

# find-requires extracts too much, cf https://qa.mandriva.com/show_bug.cgi?id=47678
# therefore, forcing explicit require skipping of Win32
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32(.*)\\)'
%else
%define _requires_exceptions perl.Win32.
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Run commands simply, with detailed diagnostics
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Calling Perl's in-built 'system()' function is easy, determining if it was
successful is _hard_. Let's face it, '$?' isn't the nicest variable in the
world to play with, and even if you _do_ check it, producing a
well-formatted error string takes a lot of work.

'IPC::System::Simple' takes the hard work out of calling external commands.
In fact, if you want to be really lazy, you can just write:

    use IPC::System::Simple qw(system);

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.210.0-4mdv2012.0
+ Revision: 765381
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.210.0-3
+ Revision: 763898
- rebuilt for perl-5.14.x

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.210.0-2
+ Revision: 654231
- rebuild for updated spec-helper

* Tue Mar 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 526816
- update to 1.21

* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.1
+ Revision: 487932
- update to 1.20

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.190.0-1mdv2010.1
+ Revision: 473720
- update to 1.19

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2010.0
+ Revision: 401652
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.18-2mdv2010.0
+ Revision: 371648
- adding temp workaround for bug 47678

* Mon Feb 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.18-1mdv2009.1
+ Revision: 338705
- update to new version 1.18

* Sun Feb 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.17-1mdv2009.1
+ Revision: 336072
- import perl-IPC-System-Simple


* Sun Feb 01 2009 cpan2dist 1.17-1mdv
- initial mdv release, generated with cpan2dist

