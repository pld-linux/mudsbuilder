Summary:	mudsbuilder - tool for area drawing and code generation
Summary(pl):	mudsbuilder - narzêdzie to rysowania i generowania kodu lokacji
Name:		mudsbuilder
Version:	0.5.3
Release:	0.1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/mudsbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	c20ae4fadd87a66dda2741db36ed79fe
BuildRequires:	libgnomeui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gereacreator - tool for area drawing and code generation. Code is
generated based on a Mudlib template, which makes it easy to adjust
output for virtually any mudlib.

%description -l pl
Gerecreator jest narzêdziem do rysowania oraz tworzenia kodu lokacji.
Dziêki zastosowaniu szablonów kod wynikowy mo¿na w ³atwy sposób
przystosowaæ do u¿ywanego przez nas Mudliba.

%prep
%setup -q -n %{name}-%{version}/gereacreator

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install src/gereacreator $RPM_BUILD_ROOT%{_bindir}
install etc/gereacreator.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README.html ChangeLog AUTHORS etc/merentha.mlt
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %{_sysconfdir}/*
