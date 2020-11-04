Name:           brotli
Version:        1.0.7
Release:        4
Summary:        Lossless compression algorithm

License:        MIT
URL:            https://github.com/google/brotli
Source0:        https://github.com/google/brotli/archive/v%{version}.tar.gz

BuildRequires:  python3-devel gcc-c++ gcc cmake

Patch6000: Verbose-CLI-start-pulling-Shared-Brotli.patch
Patch6001: Ensure-decompression-consumes-all-input.patch
Patch6002: fix-MSVC-configuration-and-c++-compilation-fails.patch
Patch6003: fix-executable-mode-of-decode-js.patch
Patch6004: Fix-include-for-EMCC-build.patch
Patch6005: Add-an-option-to-avoid-building-shared-libraries.patch
Patch6006: Disable-PIC-in-EMCC-mode.patch
Patch6007: Add-missing-const-to-a-couple-of-kConstants.patch
Patch6008: Move-TZCNT-and-BSR-intrinsics-and-add-MSVC-versions.patch
Patch6009: CVE-2020-8927.patch

%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%package     -n python3-%{name}
Requires:       python3
Summary:        Lossless compression algorithm (python 3)
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package installs a Python 3 module.

%package devel
Summary: Lossless compression algorithm (development files)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package installs the development files

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%{__chmod} 644 c/enc/*.[ch]
%{__chmod} 644 c/include/brotli/*.h
%{__chmod} 644 c/tools/brotli.c

%build
mkdir -p build
pushd build
%cmake .. -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%make_build
popd

%py3_build

%install
pushd build
%make_install
%__rm "%{buildroot}%{_libdir}/"*.a
popd

%py3_install
%{__install} -dm755 "%{buildroot}%{_mandir}/man3"

pushd docs
for i in *.3;do
%{__install} -m644 "$i" "%{buildroot}%{_mandir}/man3/${i}brotli"
done

%ldconfig_scriptlets

%check
pushd build
ctest -V
popd

%files
%license LICENSE
%{_bindir}/brotli
%{_libdir}/*.so.*

%files -n python3-%{name}
%license LICENSE
%{python3_sitearch}/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files help
%{_mandir}/man3/*

%changelog
* Wed Nov 4 2020 wangjie<wangjie294@huawei.com> -1.0.7-4
- Type:NA
- ID:NA
- SUG:NA
- DESC:remove python2

* Mon Oct 19 2020 wangjie<wangjie294@huawei.com> -1.0.7-3
- Type:CVE
- CVE:CVE-2020-8927
- SUG:NA
- DESC:fix CVE-2020-8927

* Mon Oct 19 2020 wangjie<wangjie294@huawei.com> -1.0.7-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Synchronize patches from community
       Verbose-CLI-start-pulling-Shared-Brotli.patch
       Ensure-decompression-consumes-all-input.patch
       fix-MSVC-configuration-and-c++-compilation-fails.patch
       fix-executable-mode-of-decode-js.patch
       Fix-include-for-EMCC-build.patch
       Add-an-option-to-avoid-building-shared-libraries.patch
       Disable-PIC-in-EMCC-mode.patch
       Add-missing-const-to-a-couple-of-kConstants.patch
       Move-TZCNT-and-BSR-intrinsics-and-add-MSVC-versions.patch

* Thu Apr 16 2020 chengquan<chengquan3@huawei.com> -1.0.7-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:upgrade software to v1.0.7

* Thu Dec 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.5-3
- fix auto detect of bundled mode

* Thu Sep 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.5-2
- Package init
