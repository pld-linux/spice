Name: spice
Version: 3f4
Release: 17cl
Summary: Berkeley SPICE 3 Circuit Simulator
Summary(pt_BR): SPICE simulador de circuitos
Summary(es): SPICE simulador de circuitos
Group: Mathematics
Group(pt_BR): Matemática
Group(es): Matemática
License: BSD
Source0: http://ftp.ibiblio.org/pub/Linux/apps/circuits/spice3f4.tar.bz2
Source1: http://ftp.ibiblio.org/pub/Linux/apps/circuits/spice3f4-patches-1.2.tar.gz
Patch0: spice-ncurses.patch
Patch1: spice3f4-termcap.patch
Requires: readline >= 2.0
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
SPICE 3 is a general-purpose circuit simulation program for nonlinear
dc, nonlinear transient, and linear ac analyses.  Circuits may contain
resistors, capacitors, inductors, mutual inductors, independent
voltage and current sources, four types of dependent sources,
transmission lines, and the four most common semiconductor devices:
diodes, BJT's, JFET's, and MOSFET's.

This is Spice 3f4 patched to 3f5, and includes the new port patches for
Linux, including GNU Lib C support, GNU Readline command-line editing
and history file support, and native Spice support for X11R6 and MFB.

%description -l pt_BR
SPICE é um programa de propósito geral para simulação de circuitos
para dc não linear, transiente não linear e análises de ac
linear. Circuitos podem conter resistores, capacitores, indutores,
indutores mútuos, fontes independentes de voltagem, quatro tipos de
fontes dependentes, linhas de transmissão e quatro dos dispositivos
semicondutores mais comuns: diodos, BJTs, JFETs e MOSFETs.

%description -l es
SPICE es un programa de propósito general para simulación de
circuitos para dc no linear, transiente no linear y análisis de
ac linear. Los circuitos pueden contener resistores, capacitores,
inductores, inductores mutuos, fuentes independientes de voltaje,
cuatro tipos de fuentes dependientes, líneas de transmisión y
cuatro de los dispositivos semiconductores más comunes: diodos,
BJTs, JFETs y MOSFETs.

%package examples
Summary: Berkeley SPICE 3 Example Files
Summary(pt_BR): Arquivos com exemplos para o SPICE 3 de Berkeley
Summary(es): Archivos con ejemplos para  SPICE 3 de Berkeley
Group: Mathematics
Group(pt_BR): Matemática
Group(es): Matemática
Requires: spice >= 3f4

%description examples
These are SPICE 3 example files for use with Berkeley SPICE 3.

%description -l pt_BR examples
Arquivos com exemplos para o SPICE 3 de Berkeley

%description -l es examples
Archivos con ejemplos para SPICE 3 de Berkeley

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
./util/build linux CC_OPT="%{optflags}"

%install
rm -rf %{buildroot}
# No longer using automatic install
#./util/build linux install CC_OPT="%{optflags}"

mkdir -p %{buildroot}{%{_bindir},%{_libdir}/spice/lib/{scripts,helpdir},%{_mandir}/man{1,3,5}}

for i in spice3 help nutmeg sconvert multidec proc2mod
do
	install -m 0755 src/bin/$i %{buildroot}%{_bindir}
done
install -m 0644 lib/{mfbcap,news} %{buildroot}%{_libdir}/spice/lib
install -m 0644 lib/helpdir/* %{buildroot}%{_libdir}/spice/lib/helpdir
install -m 0644 lib/scripts/* %{buildroot}%{_libdir}/spice/lib/scripts

strip %{buildroot}%{_bindir}/{spice3,help,nutmeg,sconvert,multidec,proc2mod}
cp -r examples %{buildroot}%{_libdir}/spice
install -m 644 man/man1/spice.1 %{buildroot}%{_mandir}/man1
install -m 644 man/man1/nutmeg.1 %{buildroot}%{_mandir}/man1
install -m 644 man/man1/sconvert.1 %{buildroot}%{_mandir}/man1
install -m 644 man/man3/mfb.3 %{buildroot}%{_mandir}/man3
install -m 644 man/man5/mfbcap.5 %{buildroot}%{_mandir}/man5
chmod 644 notes/spice2
cd %{buildroot}%{_mandir}/man1
ln -sf spice.1 spice3.1

%files
%defattr(0644,root,root,0755)
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
%defattr(0644,root,root,0755)
%{_libdir}/spice/examples

%changelog
* Sun Nov 18 2001 Claudio Matsuoka <claudio@conectiva.com>
+ spice-3f4-17cl
- fixed file permissions

* Thu May 10 2001 Arnaldo Carvalho de Melo <acme@conectiva.com>
+ spice-3f4-16cl
- recompiled with new libreadline

* Fri Mar 02 2001 Rodrigo Barbosa <rodrigob@conectiva.com>
+ spice-3f4-15cl
- Updating rpm macros

* Fri Oct 06 2000 Rodrigo Barbosa <rodrigob@conectiva.com>
- Rebuild with ncurses
- Fixed source URLS

* Fri Sep 15 2000 Rodrigo Barbosa <rodrigob@conectiva.com>
- Adopted rpm macros
- New patches from metalab
- Changes to build in %%{buildroot}

* Thu Jan 13 2000 Guilherme Wunsch Manika <gwm@conectiva.com>
- termlib -> ncurses

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %%description translations

* Tue Dec 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- traduções para pt_BR incluídas para Summary, %%description e Group
- compactado com bzip2
