Name:           icp
Version:        1.1
Release:        1%{?dist}
Summary:        icp (internet copy).

License:        GPL2
URL:            https://github.com/syrian2012/icp
Source0:        %{name}-%{version}.tar.gz
Requires:       pv
Requires:       tar
Requires:       pigz
Requires:       openssh-clients

BuildArch:      noarch

%description
icp (internet copy) - Fastest way to copy files/directories over the internet based on SSH.

%prep
%setup -q

%build
# No compilation needed for a script

%install
install -Dm755 icp.sh %{buildroot}/usr/local/bin/icp

%files
/usr/local/bin/icp
%doc

%changelog
* Fri Aug 23 2024 Mohammad Haidar mhd4.hz@gmail.com - 1.1-1
- Initial package

