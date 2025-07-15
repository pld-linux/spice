Summary:	Berkeley SPICE 3 Circuit Simulator
Summary(es.UTF-8):	SPICE simulador de circuitos
Summary(pl.UTF-8):	Symulator układów elektronicznych Berkeley SPICE 3
Summary(pt_BR.UTF-8):	SPICE simulador de circuitos
Name:		spice
Version:	3f5sfix
Release:	7
License:	BSD
Group:		Applications/Math
Source0:	http://www.ibiblio.org/pub/Linux/apps/circuits/%{name}%{version}.tar.gz
# Source0-md5:	b4a86690d2d56db3045a27ff75245356
Patch0:		%{name}-gcc-4.1.patch
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# /usr/lib/rpm/bin/debugedit: canonicalization unexpectedly shrank by one character
%define		_enable_debug_packages	0

%description
SPICE 3 is a general-purpose circuit simulation program for nonlinear
dc, nonlinear transient, and linear ac analyses. Circuits may contain
resistors, capacitors, inductors, mutual inductors, independent
voltage and current sources, four types of dependent sources,
transmission lines, and the four most common semiconductor devices:
diodes, BJT's, JFET's, and MOSFET's.

This is Spice 3f4 patched to 3f5, and includes the new port patches
for Linux, including GNU Lib C support, GNU Readline command-line
editing and history file support, and native Spice support for X11R6
and MFB.

%description -l es.UTF-8
SPICE es un programa de propósito general para simulación de circuitos
para dc no linear, transiente no linear y análisis de ac linear. Los
circuitos pueden contener resistores, capacitores, inductores,
inductores mutuos, fuentes independientes de voltaje, cuatro tipos de
fuentes dependientes, líneas de transmisión y cuatro de los
dispositivos semiconductores más comunes: diodos, BJTs, JFETs y
MOSFETs.

%description -l pl.UTF-8
SPICE 3 to ogólnego przeznaczenia symulator układów elektronicznych do
analizy nieliniowej prądu stałego i liniowej prądu zmiennego. Obwody
mogą zawierać rezystory, kondensatory, cewki, niezależne źródła
napięciowe i prądowe, cztery rodzaje zależnych źródeł, linie
transmisyjne, cztery najbardziej popularne rodzaje półprzewodników:
diody, BJT, JFET i MOSFET.

%description -l pt_BR.UTF-8
SPICE é um programa de propósito geral para simulação de circuitos
para dc não linear, transiente não linear e análises de ac linear.
Circuitos podem conter resistores, capacitores, indutores, indutores
mútuos, fontes independentes de voltagem, quatro tipos de fontes
dependentes, linhas de transmissão e quatro dos dispositivos
semicondutores mais comuns: diodos, BJTs, JFETs e MOSFETs.

%package examples
Summary:	Berkeley SPICE 3 Example Files
Summary(es.UTF-8):	Archivos con ejemplos para  SPICE 3 de Berkeley
Summary(pl.UTF-8):	Przykładowe pliki do Berkeley SPICE 3
Summary(pt_BR.UTF-8):	Arquivos com exemplos para o SPICE 3 de Berkeley
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}

%description examples
These are SPICE 3 example files for use with Berkeley SPICE 3.

%description examples -l es.UTF-8
Archivos con ejemplos para SPICE 3 de Berkeley.

%description examples -l pl.UTF-8
Pakiet zawiera przykładowe pliki do Berkeley SPICE 3.

%description examples -l pt_BR.UTF-8
Arquivos com exemplos para o SPICE 3 de Berkeley.

%prep
%setup -q -n %{name}%{version}
%patch -P0 -p1

%build
./util/build linux \
	CC_OPT="-I/usr/include/X11/ -I/usr/include/X11/Xaw/ %{rpmcflags}" \
	LDFLAGS="-ltinfo -lm %{rpmldflags}" \
	S_SPICE_EXEC_DIR="%{_libdir}/spice/" \
	S_SPICE_LIB_DIR="%{_datadir}/spice/" \
	LIBX="-lXaw -lX11 -lXt"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/spice,%{_datadir}/spice/{scripts,helpdir},%{_mandir}/man1}

install obj/bin/{nutmeg,sconvert,spice3} $RPM_BUILD_ROOT%{_bindir}
install obj/bin/{help,makeidx,multidec,proc2mod} $RPM_BUILD_ROOT%{_libdir}/spice
ln -s spice3 $RPM_BUILD_ROOT%{_bindir}/spice

install lib/{mfbcap,news} $RPM_BUILD_ROOT%{_datadir}/spice/
install lib/helpdir/* $RPM_BUILD_ROOT%{_datadir}/spice/helpdir
install lib/scripts/* $RPM_BUILD_ROOT%{_datadir}/spice/scripts

install man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

echo ".so spice.1" > $RPM_BUILD_ROOT%{_mandir}/man1/spice3.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme readme.Linux Linux.changes notes/{spice2,internal}
%doc 3f5patches/README*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/spice
%attr(755,root,root) %{_libdir}/spice/*
%{_datadir}/spice
%{_mandir}/man1/*
