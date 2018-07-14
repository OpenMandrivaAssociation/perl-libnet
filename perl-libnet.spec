%global __requires_exclude perl\\(Mac::
%define modname	libnet
%define modver	3.04

Summary:	Perl module implementing various network protocols
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		http://metacpan.org/pod/Net::FTP
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHAY/libnet-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
libnet is a collection of perl5 modules which all related to network
programming.

The majority of the modules available provided the client side of
popular server-client protocols that are used in the internet
community.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor <<EOF
n
n
EOF
%make

%check
%make test

%install
%make_install

%files
%doc README
%{perl_vendorlib}/Net
%{_mandir}/man3/*
