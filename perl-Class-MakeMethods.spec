#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	MakeMethods
Summary:	Class::MakeMethods - generate common types of methods
Summary(pl):	Class::MakeMethods - generowanie ogólnych typów metod
Name:		perl-Class-MakeMethods
Version:	1.005
Release:	2
License:	GPL / Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.readme
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Class::MakeMethods framework allows Perl class developers to
quickly define common types of methods. When a module uses a subclass
of Class::MakeMethods, it can select from the supported method types,
and specify a name for each method desired. The methods are
dynamically generated and installed in the calling package.

%description -l pl
Szkielet Class::MakeMethods umo¿liwia deweloperom Perla szybkie
definiowanie ogólnych typów metod. Gdy modu³ korzysta z podklasy
klasy Class::MakeMethods, mo¿e on dokonywaæ wyboru spo¶ród wspieranych
typów metod i podaje nazwê ka¿dej z ¿±danych metod. Metody s±
generowane dynamicznie i instalowane w pakiecie, który je wywo³uje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
perl -pi -e 's/^(require 5.003)(07;)(.*)$/$1_$2$3/' MakeMethods.pm

%build
perl Makefile.PL
%{__make}
# %{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_sitelib}/Class/MakeMethods.pm
%dir %{perl_sitelib}/Class/MakeMethods
%{perl_sitelib}/Class/MakeMethods/*.pm
%{perl_sitelib}/Class/MakeMethods/Basic
%{perl_sitelib}/Class/MakeMethods/Composite
%{perl_sitelib}/Class/MakeMethods/Standard
%{perl_sitelib}/Class/MakeMethods/Utility
%{_mandir}/man3/*
