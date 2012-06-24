Summary:	Very simple mouse shooting game
Summary(pl):	Bardzo prosta strzelanka
Name:		OilWar
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.2ndpoint.fi/projektit/filut/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch0:		%{name}-am_remove_install-data-local.patch
URL:		http://www.2ndpoint.fi/projektit/oilwar.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OilWar is a simple game where you shoot enemy soldiers and tanks with
your mouse. The evil army is attacking your land and tries to steal
your oil. Your mission: waste the invaders, protect the oil, protect
the mother land...

%description -l pl
OilWar jest prost� gr� w kt�rej strzelasz do �o�nierzy i czo�g�w 
nieprzyjaciela za pomoc� myszki. Armia wroga atakuje twoje terytorium
i stara si� ukra�� zasoby oleju. Twoja misja: zniszczy� naje�d�c�w,
chroni� olej, chroni� ojczyzn�...

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/applications,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/games/oilwar
%{_datadir}/applications/*.desktop
%{_pixmapsdir}/*.png
%attr(664,root,games) %verify(not size mtime md5) %{_localstatedir}/games/*.scores
