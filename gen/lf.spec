%define debug_package %{nil}

Name: lf
Version: r14
Release: 1%{?dist}
Summary: lf is a terminal file manager written in Go

License: MIT
URL: https://github.com/gokcehan/lf
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: golang

%description
lf (as in "list files") is a terminal file manager written in Go. It is heavily inspired by ranger with some missing and extra features. Some of the missing features are deliberately omitted since they are better handled by external tools.

%prep
%autosetup

%build
./gen/build.sh -o %{_builddir}/lf

%install
mkdir -p %{buildroot}%{_bindir}
cp %{_builddir}/lf %{buildroot}%{_bindir}
# Todo:
# Add lfrc.example, lfcd.sh, lf.1, lf.vim, lf.fish, lfcd.fish

%files
%{_bindir}/lf

%doc README.md
%license LICENSE
