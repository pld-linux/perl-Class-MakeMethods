#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	MakeMethods
Summary:	Class::MakeMethods - generate common types of methods
Summary(pl):	Class::MakeMethods - generowanie og�lnych typ�w metod
Name:		perl-Class-MakeMethods
Version:	1.008
Release:	1
License:	GPL or Artistic
Vendor:		M. Simon Cavalletto <simonm@cavalletto.org>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a4dc500af63d8612eb4065cf0d14c66d
URL:		http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.readme
%if 0%{!?_without_tests:1}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	%{name}-Template = 1.005
Obsoletes:	%{name}-Template < 1.005
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# this belongs to unfinished code - we have no choice...
%define		_noautoreq	'perl(Class::MakeMethods::Template::Array)'

%description
The Class::MakeMethods framework allows Perl class developers to
quickly define common types of methods. When a module uses a subclass
of Class::MakeMethods, it can select from the supported method types,
and specify a name for each method desired. The methods are
dynamically generated and installed in the calling package.

%description -l pl
Szkielet Class::MakeMethods umo�liwia deweloperom Perla szybkie
definiowanie og�lnych typ�w metod. Gdy modu� korzysta z podklasy
klasy Class::MakeMethods, mo�e on dokonywa� wyboru spo�r�d wspieranych
typ�w metod i podaje nazw� ka�dej z ��danych metod. Metody s�
generowane dynamicznie i instalowane w pakiecie, kt�ry je wywo�uje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^(require 5.003)(07;)(.*)$/$1_$2$3/' MakeMethods.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Class/MakeMethods.pm
%dir %{perl_vendorlib}/Class/MakeMethods
%{perl_vendorlib}/Class/MakeMethods/*.pm
%{perl_vendorlib}/Class/MakeMethods/Basic
%{perl_vendorlib}/Class/MakeMethods/Composite
%{perl_vendorlib}/Class/MakeMethods/Emulator
%{perl_vendorlib}/Class/MakeMethods/Standard
%{perl_vendorlib}/Class/MakeMethods/Template
%{perl_vendorlib}/Class/MakeMethods/Utility
%{_mandir}/man3/*
