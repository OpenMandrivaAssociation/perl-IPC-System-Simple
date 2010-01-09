%define upstream_name    IPC-System-Simple
%define upstream_version 1.20

# find-requires extracts too much, cf https://qa.mandriva.com/show_bug.cgi?id=47678
# therefore, forcing explicit require skipping of Win32
%define _requires_exceptions perl.Win32.

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Run commands simply, with detailed diagnostics
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(List::Util)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

