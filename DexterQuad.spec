
#TODO: make install should copy all game files not only docs and binaries
#TODO2: dexterquad should search its files from %{_bindir} in %{_datadir}/%{name}
#TODO3:	dexterquad have some font problems :(

Summary:	Dexter Quad - 2D top-down scrolling game
Summary(pl):	Dexter Quad - gra z pionowo przewijanym ekranem 2D
Name:		DexterQuad
Version:	0.1.6
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://gazer.daemonbsd.com.ar/juegos/dexterquad/files/%{name}-%{version}.tar.gz
# Source0-md5:	5f4538fedf809548438cab8da93b5c4a
Source1:	http://gazer.daemonbsd.com.ar/juegos/dexterquad/files/intro.mpg
# Source1-md5:	d3663578b758a98e820cd01fe1ac16f0
Source2:	http://gazer.daemonbsd.com.ar/juegos/dexterquad/files/level01.mp3
# Source2-md5:	620ed4acc64b1ca29ece264a6749b9f5
Patch0:		%{name}-make.patch
URL:		http://gazer.daemonbsd.com.ar/juegos/dexterquad/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libogg >= 1.0
BuildRequires:	smpeg-devel
Requires:	OpenGL
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
Requires:	SDL_mixer >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1


%description
DexterQuad is a 2D top-down scrolling game written in C++, using the
SDL library for cross-platform programming.

%description -l pl
DexterQuad to dwuwymiarowa gra z pionowym przewijaniem ekranu,
napisana w C++ przy u¿yciu biblioteki SDL w celu zapewnienia
wieloplatformowo¶ci.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cp src/dexterquad 	$RPM_BUILD_ROOT%{_datadir}/%{name}

cp -r src/Comunes	$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/Enemigos	$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/Estructuras	$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/Forms		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/Idioma	$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/Mapas		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/Menu		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/Naves		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/fonts		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/pilotos	$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/sound		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r src/video		$RPM_BUILD_ROOT%{_datadir}/%{name}

cp %{SOURCE1}		$RPM_BUILD_ROOT%{_datadir}/%{name}/video
cp %{SOURCE2}		$RPM_BUILD_ROOT%{_datadir}/%{name}/sound/music

cat > $RPM_BUILD_ROOT/%{_bindir}/dexterquad <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
./dexterquad \$@
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO

%attr(755,root,root) %{_bindir}/dexterquad
%dir %{_datadir}/%{name}
# isn't it arch-dependent library??? if so - it cannot be in %{_datadir}!!!
%attr(755,root,root) %{_datadir}/%{name}/dexterquad
# can't the following be simplified?
%dir %{_datadir}/%{name}/Comunes
%{_datadir}/%{name}/Comunes/*
%dir %{_datadir}/%{name}/Enemigos
%{_datadir}/%{name}/Enemigos/*
%dir %{_datadir}/%{name}/Forms
%{_datadir}/%{name}/Forms/*
%dir %{_datadir}/%{name}/Idioma
%{_datadir}/%{name}/Idioma/*
%dir %{_datadir}/%{name}/Menu
%{_datadir}/%{name}/Menu/*
%dir %{_datadir}/%{name}/fonts
%{_datadir}/%{name}/fonts/*
%dir %{_datadir}/%{name}/pilotos
%{_datadir}/%{name}/pilotos/*
%dir %{_datadir}/%{name}/video
%{_datadir}/%{name}/video/*
%dir %{_datadir}/%{name}/Estructuras
%dir %{_datadir}/%{name}/Estructuras/STorreta
%{_datadir}/%{name}/Estructuras/STorreta/*
%dir %{_datadir}/%{name}/Estructuras/Torreta
%{_datadir}/%{name}/Estructuras/Torreta/*
%dir %{_datadir}/%{name}/Mapas
%dir %{_datadir}/%{name}/Mapas/Nivel01
%{_datadir}/%{name}/Mapas/Nivel01/*
%dir %{_datadir}/%{name}/Naves
%dir %{_datadir}/%{name}/Naves/Caza
%{_datadir}/%{name}/Naves/Caza/*
%dir %{_datadir}/%{name}/Naves/Ferny
%{_datadir}/%{name}/Naves/Ferny/*
%dir %{_datadir}/%{name}/Naves/Jorge
%{_datadir}/%{name}/Naves/Jorge/*
%dir %{_datadir}/%{name}/Naves/Sagar
%{_datadir}/%{name}/Naves/Sagar/*
%dir %{_datadir}/%{name}/sound
%dir %{_datadir}/%{name}/sound/efectos
%{_datadir}/%{name}/sound/efectos/*
%dir %{_datadir}/%{name}/sound/music
%{_datadir}/%{name}/sound/music/*
