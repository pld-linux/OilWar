Summary:	Very simple mouse shooting game
Summary(pl):	Bardzo prosta strzelanka
Name:		OilWar
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.2ndpoint.fi/projektit/filut/%{name}-%{version}.tar.gz
# Source0-md5:	6286e7f5a5f4f8ce6489a996b188caa2
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch0:		%{name}-am_remove_install-data-local.patch
URL:		http://www.2ndpoint.fi/projektit/oilwar.html
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OilWar is a simple game where you shoot enemy soldiers and tanks with
your mouse. The evil army is attacking your land and tries to steal
your oil. Your mission: waste the invaders, protect the oil, protect
the mother land...

%description -l pl
OilWar jest prost± gr± w której strzela siê do ¿o³nierzy i czo³gów
nieprzyjaciela za pomoc± myszki. Armia wroga atakuje terytorium gracza
i stara siê ukra¶æ zasoby oleju. Misja: zniszczyæ naje¼d¼ców, chroniæ
olej, chroniæ ojczyznê...

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/games/oilwar
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%attr(664,root,games) %verify(not size mtime md5) %{_localstatedir}/games/*.scores
