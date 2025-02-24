Name:           obs-service-run
Version:        0.0.1
Release:        0
Summary:        Obs service that will run command
License:        GPL-3.0-or-later
URL:            https://github.com/huakim-tyk/%{name}
Group:          Development/Tools/Building
BuildArch:      noarch
BuildRequires:  rpm_macro(_obs_service_dir)
Requires:       bash
Source0:        run.pl
Source1:        run.service
%description
%{summary}.

%install
%define file %{_obs_service_dir}/run
%define script %{buildroot}%{file}
mkdir -p %{buildroot}%{_obs_service_dir}
cp %{SOURCE0} %{script}
cp %{SOURCE1} %{script}.service

%post
%postun

%files
%attr(755, root, root) %{file}
%attr(644, root, root) %{file}.service

%changelog
