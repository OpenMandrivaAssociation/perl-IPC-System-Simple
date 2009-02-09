
%define realname   IPC-System-Simple
%define version    1.18
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Run commands simply, with detailed diagnostics
Source:     http://www.cpan.org/modules/by-module/IPC/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(List::Util)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
Calling Perl's in-built 'system()' function is easy, determining if it was
successful is _hard_. Let's face it, '$?' isn't the nicest variable in the
world to play with, and even if you _do_ check it, producing a
well-formatted error string takes a lot of work.

'IPC::System::Simple' takes the hard work out of calling external commands.
In fact, if you want to be really lazy, you can just write:

    use IPC::System::Simple qw(system);

%prep
%setup -q -n %{realname}-%{version} 

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


