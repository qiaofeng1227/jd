Name:           Python3
Version:        3.8.7
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        MIT
URL:            https://github.com/qiaofeng1227/%{name}
Source0:        https://github.com/qiaofeng1227/cello/blob/master/cello-1.0.2.tar.xz

BuildRequires:  gcc,make
Requires: build-essential,libssl-dev,zlib1g-dev,libbz2-dev,libreadline-dev,libsqlite3-dev,wget,curl,llvm,libncurses5-dev,libncursesw5-dev,xz-utils,tk-dev,libffi-dev,liblzma-dev

%description
A simple RPM package to print Hello World

%prep
%setup -q

%build
./configure
make

%install
make PREFIX=/usr DESTDIR=%{?buildroot} install

%files
%defattr(-,root,root,-)
%{_bindir}/my

%changelog


%changelog
* Wed Mar 25 2020 naveen
- first cello package
