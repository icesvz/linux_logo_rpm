Name:           linux_logo
Version:        6.0.1
Release:        2%{?dist}
Summary:  Shows a Logo With some System Info.        

# https://rpm-packaging-guide.github.io/

License:   GPL-2.0 license       
URL:  http://www.deater.net/weave/vmwprod/linux_logo/          
Source0: %{name}-%{version}.tgz

BuildRequires:  /usr/bin/xgettext /usr/bin/make /usr/bin/gcc
Requires:  bash

%description
An ANSI Color Penguin Logo that can be run at bootup, at login, and many other interesting times. 
Supports: Linux (most architectures) and Solaris, Irix, AIX, etc.

%prep
%autosetup

%build make
%configure configure
%make_build 

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 linux_logo %{buildroot}/usr/bin/linux_logo

%make_install

%files 
/usr/bin/linux_logo

%license COPYING
%doc ANNOUNCE BUGS CHANGES CHANGES_IN_6.0 LINUX_LOGO.FAQ README README.CUSTOM_LOGOS README.history README.SECURITY TODO USAGE

%changelog
* Wed Jul 19 2023 icesvz
0.0.1
- First version being packaged
