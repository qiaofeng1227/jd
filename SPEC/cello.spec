Name:           cello
Version:        1.0.2
Release:        1%{?dist}
Summary:        Hello World example implemented in C22444

License:        MIT

BuildRequires:  gcc
BuildRequires:  make
      

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
