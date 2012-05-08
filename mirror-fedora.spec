Name: mirror-fedora
Summary: Create a mirror of Fedora
Version: 0.9
Release: 2.%(date +%%Y%%m%%d.%%H).dlb.%(echo $DIST)
License: GPL+
Group: Applications/System
URL: http://github.com/dlbewley/%{name}
Source0: %{name}-%{version}.tgz
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: rsync
Requires: mirrormanager-client
Requires: initscripts

%description 
Automates the update of a Fedora mirror, and reports status to MirrorManager.

%prep 
%setup -q -n %{name}

%install 
%{__rm}     -fr %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_datadir}/%{name}
%{__install} -d %{buildroot}%{_sysconfdir}/cron.d
%{__install} -d %{buildroot}%{_sysconfdir}/tmpfiles.d
%{__install} -d %{buildroot}%{_sysconfdir}/%{name}
%{__install} -d %{buildroot}%{_localstatedir}/run/%{name}
%{__install} -d -m 0710 %{buildroot}%{_localstatedir}/lock/%{name}
%{__install} -m 0755 -p %{name} %{buildroot}%{_bindir}/
%{__install} -m 0644 -p excludes %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -m 0600 -p password %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -m 0644 -p %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -m 0444 -p %{name}.cron %{buildroot}%{_sysconfdir}/cron.d/%{name}
%{__install} -m 0644 %{name}-tmpfiles.conf %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf

%clean 
rm -fr %{buildroot}

%pre 

%preun 

%post

%postun 

%files 
%defattr(-,root,root) 
%doc README
%dir %{_datadir}/%{name}/
%dir %{_localstatedir}/run/%{name}/
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/password
%config(noreplace) %{_sysconfdir}/%{name}/excludes
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%config(noreplace) %{_sysconfdir}/tmpfiles.d/%{name}.conf

%changelog 
* Tue May 08 2012 Dale Bewley <dale@bewley.net> 0.9-2
- Add conf file to override MIRROR_ROOT or anything else.

* Thu May 05 2011 Dale Bewley <dale@bewley.net> 0.9
- Do not include report_mirror, require mirrormanager-client
- Use tmpfiles.d

* Tue Mar 30 2010 Dale Bewley <dlbewley@lib.ucdavis.edu> 0.2
- Update spec with macros
- Make crontab a config file

* Wed Feb 03 2008 Dale Bewley <dlbewley@lib.ucdavis.edu> 0.1-20080213.12.ucd
- Add locking

* Thu Nov 29 2007 Dale Bewley <dlbewley@lib.ucdavis.edu> 0.1-20071129.16.ucd
- Make get_fedora.password a config file

* Tue Oct 23 2007 Mike Harris <mwharris@lib.ucdavis.edu> 0.1-20071023.15.ucd
— Initial release
