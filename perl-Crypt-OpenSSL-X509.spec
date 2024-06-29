#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Crypt
%define		pnam	OpenSSL-X509
Summary:	Crypt::OpenSSL::X509 - Perl extension to OpenSSL's X509 API
Name:		perl-%{pdir}-%{pnam}
Version:	1.811
Release:	7
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8c9212dc0ce4d3924ec9739acf445cd
URL:		http://search.cpan.org/dist/Crypt-OpenSSL-X509/
BuildRequires:	perl(Module::Install)
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This implement a large majority of OpenSSL's useful X509 API.

The email() method supports both certificates where the subject is of
the form: "... CN=Firstname lastname/emailAddress=user@domain", and
also certificates where there is a X509v3 Extension of the form
"X509v3 Subject Alternative Name: email=user@domain".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Crypt/OpenSSL/*.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/X509
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/X509/*.so
%{_mandir}/man3/*
