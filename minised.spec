Summary:	A smaller, cheaper, faster SED implementation
Name:		minised
Version:	1.13
Release:	%mkrel 2
License:	GPL
Group:		File tools
URL:		http://www.exactcode.de/site/open_source/minised/
Source0:	http://dl.exactcode.de/oss/minised/%{name}-%{version}.tar.gz
BuildRequires:	dietlibc-devel >= 0.32
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a smaller, cheaper, faster SED implementation. Minix uses it. GNU used
to use it, until they built their own sed around an extended (some would say
over-extended) regexp package. For embedded use we searched for a tiny sed
implementation especially for use with the dietlibc and found Eric S. Raymond's
sed implementation quite handy. Though it suffered several bugs and was not
under active maintenance anymore. After sending a bunch of fixes we agreed to
continue maintaining this lovely, historic sed implementation.

%prep

%setup -q

%build

make CC="diet gcc -D_BSD_SOURCE -D_GNU_SOURCE -s -static" CFLAGS="-Os -Wall -static"

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/minised
%{_mandir}/man1/minised.1*

