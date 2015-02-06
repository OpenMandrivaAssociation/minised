Summary:	A smaller, cheaper, faster SED implementation
Name:		minised
Version:	1.14
Release:	2
License:	BSD
Group:		File tools
Url:		http://www.exactcode.de/site/open_source/minised/
Source0:	http://dl.exactcode.de/oss/minised/%{name}-%{version}.tar.gz
Patch0:		minised-1.14-sfmt.patch
BuildRequires:	dietlibc-devel

%description
This is a smaller, cheaper, faster SED implementation. Minix uses it. GNU used
to use it, until they built their own sed around an extended (some would say
over-extended) regexp package. For embedded use we searched for a tiny sed
implementation especially for use with the dietlibc and found Eric S. Raymond's
sed implementation quite handy. Though it suffered several bugs and was not
under active maintenance anymore. After sending a bunch of fixes we agreed to
continue maintaining this lovely, historic sed implementation.

%files
%doc README
%{_bindir}/minised
%{_mandir}/man1/minised.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
make CC="diet gcc -D_BSD_SOURCE -D_GNU_SOURCE -static" CFLAGS="%{optflags} -static"

%install
%makeinstall_std


