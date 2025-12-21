%define module rsa

Name:           python-%{module}
Version:        4.9.1
Release:        1
Summary:        Pure-Python RSA implementation
License:        Apache-2.0
Group:          Development/Python
URL:            https://pypi.org/project/rsa/
Source0:        https://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(poetry-core)
BuildRequires:  python%{pyver}dist(wheel)

%description
Pure-Python RSA implementation.

%files
%doc README.md
%license LICENSE
%{_bindir}/py%{module}-{verify,sign,priv2pub,keygen,encrypt,decrypt}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
