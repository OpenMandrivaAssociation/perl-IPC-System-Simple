%define modname	IPC-System-Simple
%define modver 1.25

# find-requires extracts too much, cf https://qa.mandriva.com/show_bug.cgi?id=47678
# therefore, forcing explicit require skipping of Win32
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32(.*)\\)'
%else
%define _requires_exceptions perl.Win32.
%endif

Summary:	Run commands simply, with detailed diagnostics
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IPC/IPC-System-Simple-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Calling Perl's in-built 'system()' function is easy, determining if it was
successful is _hard_. Let's face it, '$?' isn't the nicest variable in the
world to play with, and even if you _do_ check it, producing a
well-formatted error string takes a lot of work.

'IPC::System::Simple' takes the hard work out of calling external commands.
In fact, if you want to be really lazy, you can just write:

    use IPC::System::Simple qw(system);

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*


