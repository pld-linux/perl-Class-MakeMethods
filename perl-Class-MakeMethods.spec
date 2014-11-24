#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	MakeMethods
Summary:	Class::MakeMethods - generate common types of methods
Summary(pl.UTF-8):	Class::MakeMethods - generowanie ogólnych typów metod
Name:		perl-Class-MakeMethods
Version:	1.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	838c98dcf1b1fff4c5d8cffaec32ebbb
URL:		http://search.cpan.org/dist/Class-MakeMethods/
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	%{name}-Template = 1.005
Obsoletes:	perl-Class-MakeMethods-Template < 1.005
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

%description -l pl.UTF-8
Szkielet Class::MakeMethods umożliwia deweloperom Perla szybkie
definiowanie ogólnych typów metod. Gdy moduł korzysta z podklasy klasy
Class::MakeMethods, może on dokonywać wyboru spośród wspieranych typów
metod i podaje nazwę każdej z żądanych metod. Metody są generowane
dynamicznie i instalowane w pakiecie, który je wywołuje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^(require 5.003)(07;)(.*)$/$1_$2$3/' MakeMethods.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

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
%{perl_vendorlib}/Class/MakeMethods/Evaled
%{perl_vendorlib}/Class/MakeMethods/Standard
%{perl_vendorlib}/Class/MakeMethods/Template
%{perl_vendorlib}/Class/MakeMethods/Utility
%{_mandir}/man3/*
