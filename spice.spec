Summary:	Berkeley SPICE 3 Circuit Simulator
Summary(es):	SPICE simulador de circuitos
Summary(pl):	Symulator uk³adów elektronicznych Berkeley SPICE 3
Summary(pt_BR):	SPICE simulador de circuitos
Name:		spice
Version:	3f4
Release:	17cl
License:	BSD
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	http://ftp.ibiblio.org/pub/Linux/apps/circuits/%{name}%{version}.tar.bz2
Source1:	http://ftp.ibiblio.org/pub/Linux/apps/circuits/%{name}%{version}-patches-1.2.tar.gz
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}3f4-termcap.patch
Requires:	readline >= 2.0
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
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
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
%setup -q -n spice3f4 -a 1
%patch0 -p1
patch -s -p1 -E < spice3f4-patches-1.2/spice3f4.defaults.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.3f5.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.fixes.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.newlnx.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.xlibs.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.glibc.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.dirs.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.rdln.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.fixes2.patch
patch -s -p1 < spice3f4-patches-1.2/spice3f4.smith.patch
find . -name "*.orig" -exec rm {} \;
%patch1 -p1

%build
./util/build linux CC_OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
# No longer using automatic install
#./util/build linux install CC_OPT="%{optflags}"

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/spice/lib/{scripts,helpdir},%{_mandir}/man{1,3,5}}

for i in spice3 help nutmeg sconvert multidec proc2mod
do
	install -m 0755 src/bin/$i $RPM_BUILD_ROOT%{_bindir}
done
install -m 0644 lib/{mfbcap,news} $RPM_BUILD_ROOT%{_libdir}/spice/lib
install -m 0644 lib/helpdir/* $RPM_BUILD_ROOT%{_libdir}/spice/lib/helpdir
install -m 0644 lib/scripts/* $RPM_BUILD_ROOT%{_libdir}/spice/lib/scripts

cp -rf examples $RPM_BUILD_ROOT%{_libdir}/spice
install man/man1/spice.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/man1/nutmeg.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/man1/sconvert.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/man3/mfb.3 $RPM_BUILD_ROOT%{_mandir}/man3
install man/man5/mfbcap.5 $RPM_BUILD_ROOT%{_mandir}/man5
cd $RPM_BUILD_ROOT%{_mandir}/man1
ln -sf spice.1 spice3.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme readme.Linux notes/spice2
%doc spice3f4-patches-1.2/README.patches
%dir %{_libdir}/spice
%{_libdir}/spice/lib
%attr(0755,root,root)%{_bindir}/spice3
%attr(0755,root,root)%{_bindir}/help
%attr(0755,root,root)%{_bindir}/nutmeg
%attr(0755,root,root)%{_bindir}/sconvert
%attr(0755,root,root)%{_bindir}/multidec
%attr(0755,root,root)%{_bindir}/proc2mod
%{_mandir}/man1/spice.1*
%{_mandir}/man1/spice3.1*
%{_mandir}/man1/nutmeg.1*
%{_mandir}/man1/sconvert.1*
%{_mandir}/man3/mfb.3*
%{_mandir}/man5/mfbcap.5*

%files examples
%defattr(644,root,root,755)
%{_libdir}/spice/examples
