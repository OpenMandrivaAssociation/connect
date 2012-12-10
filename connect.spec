%define	name	connect
%define	version	1.97
%define	release	%mkrel 2

Name:		%{name} 
Version:	%{version}
Release:	%{release} 
Summary:	Relaying command to make network connection via proxy
Source:		%{name}.tar.bz2
URL:		http://bent.latency.net/bent/git/goto-san-connect-1.85/src/connect.html
Group:		Networking/Other 
BuildRoot:	%{_tmppath}/%{name}-%{version}
License:	GPLv2

%description
Connect is the simple relaying command to make network connection 
via SOCKS and https proxy. It is mainly intended to be used as 
proxy command of OpenSSH. You can make SSH session beyond 
the firewall with this command,

Features of connect.c are:

 * Supports SOCKS (version 4/4a/5) and https CONNECT method.
 * Supports NO-AUTH and USERPASS authentication of SOCKS
 * Partially supports telnet proxy (experimental).
 * You can input password from tty, ssh-askpass or environment variable.
 * Run on UNIX or Windows platform.
 * You can compile with various C compiler (cc, gcc, Visual C, 
Borland C. etc.)
 * Simple and general program independent from OpenSSH.
 * You can also relay local socket stream instead of standard I/O.


%prep 
rm -rf %{buildroot}
%setup -q -n connect
# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build 
gcc connect.c -o %{name}

%install
install -m755 connect -D $RPM_BUILD_ROOT/%{_bindir}/%{name}

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%{_bindir}/connect
%doc connect.html emacs-wiki.css



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.97-2mdv2011.0
+ Revision: 610156
- rebuild

* Sat Feb 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.97-1mdv2010.1
+ Revision: 512284
- Fix license
- Fix mix of spaces and tabs
- Fix URL
- Update to 1.97

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.96-4mdv2010.0
+ Revision: 424943
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.96-3mdv2009.0
+ Revision: 243626
- rebuild

* Sun Mar 02 2008 Michael Scherer <misc@mandriva.org> 1.96-1mdv2008.1
+ Revision: 177658
- update to new version 1.96

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.93-3mdv2008.1
+ Revision: 170788
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.93-2mdv2008.1
+ Revision: 136335
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import connect


* Fri Jun 23 2006 Eskild Hustvedt <eskild@mandriva.org> 1.93-2mdv
- Yearly rebuild

* Mon May 23 2005 Eskild Hustvedt <eskild@mandriva.org> 1.93-1mdk
- Minor spec cleanup
- From Patrice Ferlet <metal3d@copix.org>
	- First build
