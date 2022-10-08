%global _empty_manifest_terminate_build 0
Name:		python-hole
Version:	0.7.0
Release:	1
Summary:	Python API for interacting with *hole.
License:	MIT
URL:		https://github.com/fabaff/python-hole
Source0:	https://files.pythonhosted.org/packages/48/30/b9c8207e4fab8f6b26ff903066ec2a150fdb373335fc71d779b06ef522ca/hole-0.7.0.tar.gz
BuildArch:	noarch


%description
Python API for interacting with a *hole instance.

%package -n python3-hole
Summary:	Python API for interacting with *hole.
Provides:	python-hole
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-hole
Python API for interacting with a *hole instance.

%package help
Summary:	Development documents and examples for hole
Provides:	python3-hole-doc
%description help
Python API for interacting with a *hole instance.

%prep
%autosetup -n hole-0.7.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-hole -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed Sep 21 2022 hkgy <kaguyahatu@outlook.com> - 0.7.0-1
- Update to 0.7.0

* Wed Sep 01 2021 Python_Bot <Python_Bot@openeuler.org> - 0.5.1-1
- Package Init
