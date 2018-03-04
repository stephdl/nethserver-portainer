Summary: nethserver-portainer  install portainer
%define name nethserver-portainer
Name: %{name}
%define version 0.1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Requires: python-kitchen
Requires: libxml2-python
Requires: yum-utils
Requires: pigz
Requires: container-selinux
Requires: docker-ce
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
Portainer is a lightweight management UI which allows you to easily manage your different Docker environments (Docker hosts or Swarm clusters).
Portainer is meant to be as simple to deploy as it is to use. It consists of a single container that can run on any Docker engine (can be deployed as Linux container or a Windows native container).
Portainer allows you to manage your Docker containers, images, volumes, networks and more ! It is compatible with the standalone Docker engine and with Docker Swarm mode.

%changelog
* Tue May 09 2017 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial

%prep
%setup

%build
%{makedocs}
perl createlinks
mkdir -p root/var/lib/portainer

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
 --dir /var/lib/portainer 'attr(0660,root,docker)' \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%config(noreplace) /etc/yum.repos.d/docker-ce.repo
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
