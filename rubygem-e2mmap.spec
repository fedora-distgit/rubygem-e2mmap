# Generated from e2mmap-0.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name e2mmap

Name: rubygem-%{gem_name}
Version: 0.1.0
Release: 1%{?dist}
Summary: Module for defining custom exceptions with specific messages
License: BSD-2-Clause
URL: https://github.com/ruby/e2mmap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
Module for defining custom exceptions with specific messages.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/e2mmap.gemspec

%changelog
* Thu Oct 20 2022 Pavel Valena <pvalena@redhat.com> - 0.1.0-1
- Initial package
