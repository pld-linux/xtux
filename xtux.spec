Summary:	XTux Arena Tournament
Summary(pl):	XTux Arena Tournament
Name:		xtux
Version:	20010601
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://ftp1.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
Patch0:		%{name}-opt.patch
URL:		http://xtux.sourceforge.net/
BuildRequires:	XFree86-devel >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XTux Arena Tournament.

%description -l pl
XTux Arena Tournament.

%prep
%setup -q -n xtux
%patch -p1

%build
%{__make} DATADIR=%{_datadir}/xtux OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xtux}

install xtux tux_serv $RPM_BUILD_ROOT%{_bindir}
cp -rf data/* $RPM_BUILD_ROOT%{_datadir}/xtux

gzip -9nf AUTHORS CHANGELOG README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xtux
