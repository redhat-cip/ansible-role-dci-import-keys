Name:       ansible-role-dci-import-keys
Version:    0.0.VERS
Release:    3%{?dist}
Summary:    ansible-role-dci-import-keys
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-import-keys
Source0:    ansible-role-dci-import-keys-%{version}.tar.gz

BuildArch:  noarch
Requires:   dci-ansible

%description
An Ansible role to automate the key import process

%prep
%setup -qc


%build

%install
mkdir -p %{buildroot}%{_datadir}/dci/roles/dci-import-keys
chmod 755 %{buildroot}%{_datadir}/dci/roles/dci-import-keys

cp -r defaults %{buildroot}%{_datadir}/dci/roles/dci-import-keys
cp -r tasks %{buildroot}%{_datadir}/dci/roles/dci-import-keys


%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-import-keys


%changelog
* Thu Jun 04 2020 Bill Peck <bpeck@redhat.com> - 0.0.1-2
- Rebuild for RHEL-8

* Wed Apr 19 2018 Cedric Lecomte <clecomte@redhat.com> - 0.0.1-1
- Initial release
