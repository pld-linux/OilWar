Summary:	Very simple mouse shooting game.
Name:		OilWar
Version:	1.1.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.2ndpoint.fi/projektit/filut/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://www.2ndpoint.fi/projektit/oilwar.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OilWar is a simple game where you shoot enemy soldiers and tanks with
your mouse. The evil army is attacking your land and tries to steal
your oil. Your mission: waste the invaders, protect the oil, protect
the mother land...

%prep
%setup -q -n %{name}-%{version}

%build
rm -f missing
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/oilwar/*
%attr(666,root,root) %{_localstatedir}/lib/games/*.scores
%{_applnkdir}/Games/Arcade/*.desktop
%{_pixmapsdir}/*.png
