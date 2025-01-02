Name:           obs-service-run
Version:        0.0.1
Release:        0
Summary:        Obs service that will run command
License:        GPL-3.0-or-later
URL:            https://github.com/huakim-tyk/%{name}
Group:          Development/Tools/Building
BuildArch:      noarch
BuildRequires:  rpm_macro(_obs_service_dir)

%description
%{summary}.

%install
%define file %{_obs_service_dir}/run
%define script %{buildroot}%{file}
mkdir -p %{buildroot}%{_obs_service_dir}

cat <<'EOF' > %{script}
#!/bin/bash
while [ -n "$1" ];do
  case $1 in
    --*)
       typeset -a "${1:2}"
       eval "${1:2}+=(\"\$2\")"
       shift; shift;
    ;;
    *)
      shift;
    ;;
  esac
done
eval "outdir=\"\$(realpath -s \"\${outdir:-.}\")\" ; ${command:-". \"\$sourcefile\""}"
exit $?

EOF

cat <<'EOF' > %{script}.service
<service name="run">
  <summary>Example how to create a service</summary>
  <description><![CDATA[
  This service will run an command from command parameter.
  All parameters will be cast as environment variables
  ]]>
  </description>
  <parameter name="sourcefile">
    <description>source file that will be executed if no command given</description>
  </parameter>
  <parameter name="command">
    <description>command that will be launched</description>
  </parameter>
</service>
EOF

%post
%postun

%files
%attr(755, root, root) %{file}
%attr(644, root, root) %{file}.service

%changelog
