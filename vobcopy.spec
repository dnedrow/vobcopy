Name: vobcopy
Summary: vobcopy copies DVD .vob files to harddisk
Version: 0.5.14
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://vobcopy.org/projects/c/c.shtml
Source0: %{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libdvdread
BuildPrereq: libdvdread-devel

%description
vobcopy called without arguments will find the mounted dvd and copy the
title with the most chapters to the current working directory (thats the
directory you're invoking vobcopy from). It will merge together the
sub-vobs of each title-vob (vts_xx_yy.vob => the xx is the title-vob,
the yy and friends are the sub-vobs, mostly of 1 GB size) and copy them
to harddisk in 2 GB chunks. It will get the title of the movie from the
dvd and copy the data to name-of-moviexx-1.vob, name-of-moviexx-2.vob
(the xx being the title number). Also possible is to mirror the whole video
dvd content and single files can also be copied.

%prep 
%setup -q

%build 
export CFLAGS="$RPM_OPT_FLAGS"
make

%install 
rm -fr %{buildroot}
install -d -m 0755 %{buildroot}/%{_bindir}
install -d -m 0755 %{buildroot}/%{_mandir}/man1
install -d -m 0755 %{buildroot}/%{_mandir}/de
install -d -m 0755 %{buildroot}/%{_mandir}/de/man1
install -m 0755 vobcopy %{buildroot}/%{_bindir}/
install -m 0644 vobcopy.1 %{buildroot}/%{_mandir}/man1/
install -m 0644 vobcopy.1.de %{buildroot}/%{_mandir}/de/man1/vobcopy.1

%clean 
rm -fr %{buildroot}

%files 
%defattr(-,root,root) 
%{_bindir}/* 
%{_mandir}/* 
%doc Changelog COPYING README Release-Notes TODO alternative_programs.txt

%changelog 

* Sun Oct 24 2004 Robos  <robos@muon.de>
- 0.5.14-rc1: - misc *bsd fixes and first straight OSX support

* Mon Mar 7 2004 Robos  <robos@muon.de>
- 0.5.12-1: -m off-by-one error fixed

* Mon Jan 19 2004 Robos <robos@muon.de>
- 0.5.10-1: -O now works 
  	    cleanup



* Wed Nov 13 2003 Robos <robos@muon.de>
- 0.5.9-1: -F now accepts factor number
  	   cleanups and small bugfix
  	   new vobcopy.spec

* Sun Nov 09 2003 Florin Andrei <florin@andrei.myip.org>
- 0.5.8-2: libdvdread is now a pre-requisite

* Sun Nov 09 2003 Florin Andrei <florin@andrei.myip.org>
- first package, 0.5.8-1
