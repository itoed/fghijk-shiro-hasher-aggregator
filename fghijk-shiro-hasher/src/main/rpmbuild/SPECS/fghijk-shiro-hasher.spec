Name:           %{_name}
Version:        %{_version}
Release:        %{_release}
Summary:        FGHIJK Shiro Command Line Hasher
License:        None
BuildArch:      %{_arch}
AutoReqProv:    No
Requires:       jdk
Source0:        fghijk-shiro-hasher-core-%{version}-%{release}-jar-with-dependencies.jar
Source1:        fghijk-shiro-hasher

%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

%define homedir /var/lib/fghijk/shiro-hasher

%description
A hashing tool using Apache Shiro

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{homedir}
cp %{SOURCE0} %{buildroot}%{homedir}/fghijk-shiro-hasher.jar
cp %{SOURCE1} %{buildroot}%{homedir}/

install -dm 755 %{buildroot}%{_bindir}
ln -s %{homedir}/fghijk-shiro-hasher %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%{homedir}/
%attr(700,root,root) %{homedir}/fghijk-shiro-hasher
%{_bindir}/fghijk-shiro-hasher

%changelog
* Thu Jul 31 2014 Eduardo ito <ed@fghijk.local> - 0.1-1
- Initial release
