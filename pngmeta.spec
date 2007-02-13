Summary:	Display metadata information from PNG images
Summary(pl.UTF-8):	Pokazywanie metadanych z plików graficznych PNG
Name:		pngmeta
Version:	1.11
Release:	1
License:	distributable
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/pmt/%{name}-%{version}.tar.gz
# Source0-md5:	5d495f7668f7ccc64a1576c8cfd15506
URL:		http://pmt.sourceforge.net/pngmeta/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small filter program extracts metadata from PNG images and
displays them as either HTML, SOIF, RDF/XML or simple fields and
values.

%description -l pl.UTF-8
Ten mały program filtrujący wyciąga metadane z plików graficznych
PNG i wyświetla je w jednym z formatów: HTML, SOIF, RDF/XML lub jako
pola i wartości.

%prep
%setup -q

%build
%{__autoconf}
%{__aclocal}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README test*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
