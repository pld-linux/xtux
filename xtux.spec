Summary:	X11 client server network game featuring opensource mascots
Summary(pl):	Klient pod X11 gry klient-serwer z postaciami ¶wiata opensource
Summary(pt_BR):	Jogo cliente-servidor para X11 com mascotes do código aberto
Name:		xtux
Version:	20010601
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp1.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
# Source0-md5:	609ebca3902761bba636323d310eb091
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-opt.patch
URL:		http://xtux.sourceforge.net/
BuildRequires:	XFree86-devel >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XTux Arena is a client server network game for X11 featuring
opensource mascots, like Linus, RMS, Gnome, KDE, and of course tux.
Players can compete in a multiplayer deathmatch mode (called holywar)
or play against the computer (cooperative multiplayer supported) in a
mission against Microsoft.

%description -l pl
XTux Arena to klient pod X11 gry klient-serwer z postaciami ¶wiata
opensource, takimi jak Linus, RMS, Gnome, KDE i oczywi¶cie tux. Gracze
mog± wspó³zawodniczyæ w trybie deathmatch ("¶wiêta wojna") lub graæ
przeciwko komputerowi (tryb wspó³pracy) w misji przeciwko Microsoft.

%description -l pt_BR
O Xtux Arena é um jogo em rede cliente-servidor para X11 onde estrelam
mascotes do código aberto, como Linus, RMS, Gnome, KDE e é claro, o
pingüim tux. Os jogadores podem competir em modo mate-ou-morra
(deathmatch), chamado holywar, ou jogar contra o computador (modo
cooperativo suportado) numa missão contra a Microsoft(R).

%prep
%setup -q -n xtux
%patch -p1

%build
%{__make} DATADIR=%{_datadir}/xtux OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xtux,%{_applnkdir}/Games,%{_pixmapsdir}}

install xtux tux_serv $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

cp -rf data/* $RPM_BUILD_ROOT%{_datadir}/xtux


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xtux
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
