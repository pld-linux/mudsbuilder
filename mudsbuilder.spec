Summary:	mudsbuilder - tool for area drawing and code generation
Summary(pl.UTF-8):	mudsbuilder - narzędzie to rysowania i generowania kodu lokacji
Name:		mudsbuilder
Version:	0.5.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/mudsbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	07f2d63892fe6d7351fbeb4d5aaf55ee
BuildRequires:	libgnomeui-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gereacreator - tool for area drawing and code generation. Code is
generated based on a Mudlib template, which makes it easy to adjust
output for virtually any mudlib.

%description -l pl.UTF-8
Gerecreator jest narzędziem do rysowania oraz tworzenia kodu lokacji.
Dzięki zastosowaniu szablonów kod wynikowy można w łatwy sposób
przystosować do używanego przez nas Mudliba.

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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
