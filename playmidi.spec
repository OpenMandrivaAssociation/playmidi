Summary:	A MIDI sound file player
Name: 		playmidi
Version:	2.5
Release: 	%mkrel 9
Source0: 	%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/playmidi/
License: 	GPL
Group: 		Sound
Patch0: 	%{name}-2.3-hertz.patch
Patch1: 	%{name}-2.3-awe2.patch
Patch2:		playmidi-2.4-lib64.patch
Patch3: 	%{name}-2.4-midimap.patch
Patch4:		playmidi-2.4-CAN-2005-0020.patch
BuildRequires:	ncurses-devel X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%package X11
Summary:	An X Window System based MIDI sound file player
Requires: 	%{name} = %{version}
Group: 		Sound

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

%build
./Configure << EOF
2
EOF

PATH=.:$PATH

%{__make} CFLAGS="$RPM_OPT_FLAGS" LIB="%{_lib}" %{name}
%{__make} CFLAGS="$RPM_OPT_FLAGS" LIB="%{_lib}" x%{name}

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
