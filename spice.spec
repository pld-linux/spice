Summary:	Berkeley SPICE 3 Circuit Simulator
Summary(es):	SPICE simulador de circuitos
Summary(pl):	Symulator uk³adów elektronicznych Berkeley SPICE 3
Summary(pt_BR):	SPICE simulador de circuitos
Name:		spice
Version:	3f5sfix
Release:	1
License:	BSD
Group:		Applications/Math
Source0:	ftp://sunsite.unc.edu/apps/circuits/%{name}%{version}.tar.gz
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es
SPICE es un programa de propósito general para simulación de circuitos
para dc no linear, transiente no linear y análisis de ac linear. Los
circuitos pueden contener resistores, capacitores, inductores,
inductores mutuos, fuentes independientes de voltaje, cuatro tipos de
fuentes dependientes, líneas de transmisión y cuatro de los
dispositivos semiconductores más comunes: diodos, BJTs, JFETs y
MOSFETs.

%description -l pl
SPICE 3 to ogólnego przeznaczenia symulator uk³adów elektronicznych do
analizy nieliniowej pr±du sta³ego i liniowej pr±du zmiennego. Obwody
mog± zawieraæ rezystory, kondensatory, cewki, niezale¿ne ¼ród³a
napiêciowe i pr±dowe, cztery rodzaje zale¿nych ¼róde³, linie
transmisyjne, cztery najbardziej popularne rodzaje pó³przewodników:
diody, BJT, JFET i MOSFET.

%description -l pt_BR
SPICE é um programa de propósito geral para simulação de circuitos
para dc não linear, transiente não linear e análises de ac linear.
Circuitos podem conter resistores, capacitores, indutores, indutores
mútuos, fontes independentes de voltagem, quatro tipos de fontes
dependentes, linhas de transmissão e quatro dos dispositivos
semicondutores mais comuns: diodos, BJTs, JFETs e MOSFETs.

%package examples
Summary:	Berkeley SPICE 3 Example Files
Summary(es):	Archivos con ejemplos para  SPICE 3 de Berkeley
Summary(pl):	Przyk³adowe pliki do Berkeley SPICE 3
Summary(pt_BR):	Arquivos com exemplos para o SPICE 3 de Berkeley
Group:		Applications/Math
Requires:	%{name} >= 3f4

%description examples
These are SPICE 3 example files for use with Berkeley SPICE 3.

%description examples -l es
Archivos con ejemplos para SPICE 3 de Berkeley.

%description examples -l pl
Pakiet zawiera przyk³adowe pliki do Berkeley SPICE 3.

%description examples -l pt_BR
Arquivos com exemplos para o SPICE 3 de Berkeley.

%prep 
%setup -q -n %{name}%{version}

%build
./util/build linux \
	CC_OPT="%{rpmcflags}" \
	LDFLAGS="-ltinfo -lm %{rpmldflags}" \
	S_SPICE_EXEC_DIR="%{_libdir}/spice/" \
	S_SPICE_LIB_DIR="%{_datadir}/spice/" 

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

gzip -9nf readme readme.Linux Linux.changes notes/{spice2,internal} 3f5patches/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz notes/*.gz 3f5patches/README*
%attr(0755,root,root) %{_bindir}/*
%dir %{_libdir}/spice
%attr(0755,root,root) %{_libdir}/spice/*
%{_datadir}/spice
%{_mandir}/man1/*
