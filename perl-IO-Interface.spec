#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Interface
Version  : 1.09
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/L/LD/LDS/IO-Interface-1.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LD/LDS/IO-Interface-1.09.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-interface-perl/libio-interface-perl_1.09-1.debian.tar.xz
Summary  : 'Access and modify network interface card configuration'
Group    : Development/Tools
License  : Artistic-1.0-Perl Artistic-2.0
Requires: perl-IO-Interface-license = %{version}-%{release}
Requires: perl-IO-Interface-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
LibIO-Interface-Perl
====================
Perl interface to Unix network interface API

%package dev
Summary: dev components for the perl-IO-Interface package.
Group: Development
Provides: perl-IO-Interface-devel = %{version}-%{release}
Requires: perl-IO-Interface = %{version}-%{release}

%description dev
dev components for the perl-IO-Interface package.


%package license
Summary: license components for the perl-IO-Interface package.
Group: Default

%description license
license components for the perl-IO-Interface package.


%package perl
Summary: perl components for the perl-IO-Interface package.
Group: Default
Requires: perl-IO-Interface = %{version}-%{release}

%description perl
perl components for the perl-IO-Interface package.


%prep
%setup -q -n IO-Interface-1.09
cd %{_builddir}
tar xf %{_sourcedir}/libio-interface-perl_1.09-1.debian.tar.xz
cd %{_builddir}/IO-Interface-1.09
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-Interface-1.09/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
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
cp %{_builddir}/IO-Interface-1.09/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Interface/a2f577cb02ca740b64c1398d64a4b9cc4b45a19d
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Interface/233bdc16b94c4f3c7411c49c4cedea3779e9de1d
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Interface.3
/usr/share/man/man3/IO::Interface::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Interface/233bdc16b94c4f3c7411c49c4cedea3779e9de1d
/usr/share/package-licenses/perl-IO-Interface/a2f577cb02ca740b64c1398d64a4b9cc4b45a19d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
