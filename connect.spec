%define name    connect
%define version 1.96
%define release %mkrel 1

Name:           %{name} 
Version:        %{version}
Release:        %{release} 
Summary:        Relaying command to make network connection via proxy
Source:         %{name}.tar.bz2
URL:            http://www.taiyo.co.jp/~gotoh/ssh/connect.html
Group:          Networking/Other 
BuildRoot:	%{_tmppath}/%{name}-%{version}
License:	GPL

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

