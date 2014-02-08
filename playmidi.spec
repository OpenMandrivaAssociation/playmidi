Summary:	A MIDI sound file player
Name:		playmidi
Version:	2.5
Release:	16
Source0:	%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/playmidi/
License:	GPLv2+
Group:		Sound
Patch0:		%{name}-2.3-hertz.patch
Patch1:		%{name}-2.3-awe2.patch
Patch2:		playmidi-2.4-lib64.patch
Patch3:		%{name}-2.4-midimap.patch
Patch4:		playmidi-2.4-CAN-2005-0020.patch
Patch5:		%{name}-2.5-fix-str-fmt.patch
Patch6:		%{name}-2.5-fix-overlinking.patch
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xt)

%package X11
Summary:	An X Window System based MIDI sound file player
Requires:	%{name} = %{version}
Group:		Sound

%description
Playmidi plays MIDI (Musicial Instrument Digital Interface) sound
files through a sound card synthesizer.  This package includes basic
drum samples for use with simple FM synthesizers.

Install playmidi if you want to play MIDI files using your computer's
sound card.

%description X11
Playmidi-X11 provides an X Window System interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound
card synthesizer.  This package includes basic drum samples for use
with simple FM synthesizers.

Install playmidi-X11 if you want to use an X interface to play MIDI
sound files using your computer's sound card.

%prep
%setup -q -n %{name}-2.4
%patch0 -p1 -b .consthertz
%patch1 -p1 -b .awe2
%patch2 -p1 -b .lib64
%patch3 -p1 -b .midimap
%patch4 -p1 -b .can-2005-0020
%patch5 -p1 -b .strfmt
%patch6 -p1 -b .overlinking

%build
./Configure << EOF
2
EOF

PATH=.:$PATH

%{__make} CFLAGS="%optflags" LDFLAGS="%ldflags" LIB="%{_lib}" %{name}
%{__make} CFLAGS="%optflags" LDFLAGS="%ldflags" LIB="%{_lib}" x%{name}

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/app-defaults/XPlaymidi
install -d %{buildroot}%{_mandir}/man1

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m0755 x%{name} %{buildroot}%{_bindir}/x%{name}
install -m0644 XPlaymidi.ad %{buildroot}%{_datadir}/app-defaults/XPlaymidi
install -m0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

install -d %{buildroot}%{_sysconfdir}/midi
for n in std.o3 drums.o3 std.sb drums.sb; do
    install -m 644 $n -D %{buildroot}%{_sysconfdir}/midi/$n
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc QuickStart COPYING BUGS
%{_bindir}/%{name}
%dir %{_sysconfdir}/midi
%config(noreplace) %{_sysconfdir}/midi/std.o3
%config(noreplace) %{_sysconfdir}/midi/std.sb
%config(noreplace) %{_sysconfdir}/midi/drums.o3
%config(noreplace) %{_sysconfdir}/midi/drums.sb
%{_mandir}/man1/%{name}.1*

%files X11
%defattr(-,root,root)
%doc QuickStart COPYING BUGS
%{_bindir}/x%{name}
%{_datadir}/app-defaults/XPlaymidi


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5-13mdv2011.0
+ Revision: 667783
- mass rebuild

* Sat Jan 01 2011 Funda Wang <fwang@mandriva.org> 2.5-12mdv2011.0
+ Revision: 626941
- tighten BR

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5-11mdv2011.0
+ Revision: 607179
- rebuild

* Fri Feb 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.5-10mdv2010.1
+ Revision: 501089
- Fix Rpmlint warnings
- fix licence

* Thu May 21 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 2.5-9mdv2010.0
+ Revision: 378385
- fix str fmt (1 patch added)
- fix overlinking (1 patch added)
- fix license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5-8mdv2008.1
+ Revision: 180869
- bunzip the patches
- fix #24754

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5-7mdv2008.1
+ Revision: 179238
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 2.5-6mdv2008.0
+ Revision: 74312
- Import playmidi



* Wed Sep 20 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 2.5-6mdv2007.0
- Rebuild against ncurse

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.5-5mdk
- Rebuild

* Fri Feb 25 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.5-4mdk
- security update for CAN-2005-0020 (Vincent Danen <vdanen@mandrakesoft.com>)

* Thu Oct  2 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.5-3mdk
- lib64 fixes

* Sun Jun 15 2003 Stefan van der Eijk <stefan@eijk.nu> 2.5-2mdk
- BuildRequires

* Sun Jun 15 2003 Per ÿyvind Karlsen <peroyvind@sintrax.net> 2.5-1mdk
- 2.5
- updated URL
- macroize
- drop S0 (merged upstream)
- drop P2, much better to override the variable than patching it
- configure in %%build stage
- fix unowned dir
- cleanups

* Thu Nov 22 2001 Yves Duret <yduret@mandrakesoft.com> 2.4-21mdk
- fix url tag missing

* Wed Jul 11 2001 Yves Duret <ydret@mandrakesoft.com> 2.4-20mdk
- sanitized spec file : macros, s/Copy/lic/ ..

* Sun Dec 24 2000 Yves Duret <yduret@mandrakesoft.com> 2.4-19mdk
- %%doc missing
- removed bz2 lines for man pages

* Thu Dec 21 2000 Yves Duret <yduret@mandrakesoft.com> 2.4-18mdk
- added %%config(noreplace)

* Sun Dec 17 2000 Yves Duret <yduret@mandrakesoft.com> 2.4-17mdk
- macroization

* Mon Sep 25 2000 Maurizio De Cecco <maurizio@mandrakesoft.com> 2.4-16mdk
- Resource file not a config file anymore.

* Mon Aug 09 2000 Maurizio De Cecco <maurizio@mandrakesoft.com> 2.4-15mdk
- Added macros for mandir and bindir.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4-14mdk
- automatically added BuildRequires

* Tue Apr 11 2000 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Fixed Distribution name

* Thu Apr 10 2000 Maurizio De Cecco  <maurizio@mandrakesoft.com>
- Fixed error in the new Group structure

* Thu Mar 16 2000 Maurizio De Cecco  <maurizio@mandrakesoft.com>
- Adapted to the new Group structure

* Wed Nov 17 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Don't ship splaymidi(r).

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Tue Feb 23 1999 Bill Nottingham <notting@redhat.com>
- wmconfig goes away

* Mon Dec 28 1998 Bill Nottingham <notting@redhat.com>
- build against glibc-2.1

* Mon Nov 23 1998 Bill Nottingham <notting@redhat.com>
- oops. We broke FM synth. Fixed.

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- updated to version 2.4

* Wed Sep  9 1998 Bill Nottingham <notting@redhat.com>
- added AWE32 support

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root
- sound font data in /etc/midi

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
