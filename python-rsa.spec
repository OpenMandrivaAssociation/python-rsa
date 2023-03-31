%define module rsa

Name:           python-%{module}
Version:        4.9
Release:        2
Summary:        Pure-Python RSA implementation
License:        ASLv2
Group:          Development/Python
URL:            https://pypi.org/project/rsa/
Source0:        https://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description
Pure-Python RSA implementation.

%files
%doc README.md
%{_bindir}/pyrsa*
%{python_sitelib}/%{module}*

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%autopatch -p1

# drop bundled egg-info
rm -rf *.egg-info/

%build
%py_build

%install
%py_install
