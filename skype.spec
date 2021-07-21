Name: skype
Version:	8.51.0.92
Release:	1
Group: Applications/Internet
Summary: Chat with everyone from your Skype account without any plugin
URL: https://web.skype.com/
License: Public Domain
Requires: xdg-utils
Requires: falkon
Source0: https://forum.openmandriva.org/uploads/default/original/2X/e/e8f0505349809ece424d3ef4e8874508c2989561.svg
BuildArch: noarch

%description
Chat with everyone from your Skype account without any plugin

%prep

%build

%install
# We force falkon because web.skype.com doesn't work in Firefox.
# falkon is installed by default and lightweight, so it should
# be preferred over chromium.
mkdir -p %{buildroot}%{_datadir}/applications/ %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cat >%{buildroot}%{_datadir}/applications/skype.desktop <<'EOF'
[Desktop Entry]
Comment=Chat with everyone from your Skype account without any plugin.
Exec=falkon https://web.skype.com/
Icon=skype
StartupNotify=true
Terminal=false
Type=Application
Categories=Network;InstantMessaging;
EOF
cp -a %{S:0} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/skype.svg

%files
%{_datadir}/applications/skype.desktop
%{_datadir}/icons/hicolor/scalable/apps/skype.svg
