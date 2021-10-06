%define module rsa

Name:           python-%{module}
Version:        4.7.2
Release:        %mkrel 1
Summary:        Pure-Python RSA implementation
License:        ASLv2
Group:          Development/Python
URL:            https://pypi.org/project/rsa/
Source0:        https://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
BuildArch:      noarch

%description
Pure-Python RSA implementation.

%package -n python3-%module
Summary:        Pure-Python 3 RSA implementation
Group:          Development/Python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}
Obsoletes:      python2-rsa < 4.0-2

%description -n python3-%module
Pure-Python 3 RSA implementation.

%files -n python3-%{module}
%doc README.md
%{_bindir}/pyrsa*
%{python3_sitelib}/%{module}*

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%autopatch -p1

# drop bundled egg-info
rm -rf *.egg-info/

%build
%py3_build

%install
%py3_install
