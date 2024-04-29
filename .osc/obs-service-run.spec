Name:           obs-service-run
Version:        0.0.1
Release:        0
Summary:        Obs service that will run command
License:        GPL-3.0-or-later
URL:            https://github.com/huakim-tyk/%{name}
Group:          Development/Tools/Building
BuildArch:      noarch
%description
%{summary}.

%prep

%install
%define dir %{_usr}/lib/obs/service/
%define file %{dir}/run 
%define script %{buildroot}%{file}
mkdir -p %{buildroot}%{dir}

cat <<'EOF' > %{script}
#!/bin/bash
while [ -n "$1" ];do
  case $1 in
    --*) 
      export "${1:2}=$2"; shift; shift;
    ;;
    *)
      shift;
    ;;
  esac
done
 
eval "$command"
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
  <parameter name="command">
    <description>command that will executed</description>
  </parameter>
</service>
EOF

%post
%postun

%files
%attr(755, root, root) %{file}
%attr(644, root, root) %{file}.service

%changelog
