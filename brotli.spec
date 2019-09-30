Name:           brotli
Version:        1.0.5
Release:        2
Summary:        Lossless compression algorithm

License:        MIT
URL:            https://github.com/google/brotli
Source0:        https://github.com/google/brotli/archive/v%{version}.tar.gz

BuildRequires:  python2-devel python3-devel gcc-c++ gcc cmake

%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%package     -n python2-%{name}
Summary:        Lossless compression algorithm (python 2)
Requires:       python2
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
This package installs a Python 2 module.

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
%autosetup -n %{name}-%{version}

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

%py2_build
%py3_build

%install
pushd build
%make_install
%__rm "%{buildroot}%{_libdir}/"*.a
popd

%py2_install
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

%{__python2} setup.py test
%{__python3} setup.py test

%files
%license LICENSE
%{_bindir}/brotli
%{_libdir}/*.so.*

%files -n python2-%{name}
%license LICENSE
%{python2_sitearch}/*

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
* Thu Sep 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.5-2
- Package init
