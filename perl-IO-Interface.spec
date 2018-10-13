#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Interface
Version  : 1.09
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/L/LD/LDS/IO-Interface-1.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LD/LDS/IO-Interface-1.09.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-interface-perl/libio-interface-perl_1.09-1.debian.tar.xz
Summary  : 'Access and modify network interface card configuration'
Group    : Development/Tools
License  : Artistic-1.0-Perl Artistic-2.0
Requires: perl-IO-Interface-lib = %{version}-%{release}
Requires: perl-IO-Interface-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
LibIO-Interface-Perl
====================
Perl interface to Unix network interface API

%package dev
Summary: dev components for the perl-IO-Interface package.
Group: Development
Requires: perl-IO-Interface-lib = %{version}-%{release}
Provides: perl-IO-Interface-devel = %{version}-%{release}

%description dev
dev components for the perl-IO-Interface package.


%package lib
Summary: lib components for the perl-IO-Interface package.
Group: Libraries
Requires: perl-IO-Interface-license = %{version}-%{release}

%description lib
lib components for the perl-IO-Interface package.


%package license
Summary: license components for the perl-IO-Interface package.
Group: Default

%description license
license components for the perl-IO-Interface package.


%prep
%setup -q -n IO-Interface-1.09
cd ..
%setup -q -T -D -n IO-Interface-1.09 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IO-Interface-1.09/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Interface
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Interface/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Interface/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/IO/Interface.pm
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/IO/Interface/Simple.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Interface.3
/usr/share/man/man3/IO::Interface::Simple.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/IO/Interface/Interface.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Interface/LICENSE
/usr/share/package-licenses/perl-IO-Interface/deblicense_copyright
