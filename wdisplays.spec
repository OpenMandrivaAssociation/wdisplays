Name:     wdisplays
Version:  1.1.3
Release:  1
Summary:  GUI display configurator for wlroots compositors
License:  GPLv3+
URL:      https://github.com/artizirk/wdisplays
Source:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(epoxy)
BuildRequires: meson
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)

Requires:  hicolor-icon-theme
 
%description
wdisplays is a graphical application for configuring displays in
Wayland compositors. It borrows some code from kanshi. It should work
in any compositor that implements the
wlr-output-management-unstable-v1 protocol, including sway. The goal
of this project is to allow precise adjustment of display settings in
kiosks, digital signage, and other elaborate multi-monitor setups.
 
%prep
%autosetup -p1
 
%build
%meson
%meson_build

%install
%meson_install

find %{buildroot}
 
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    --set-icon %{name} \
    --set-key=Terminal --set-value=false \
    --remove-key=Version \
    --add-category=Settings --add-category=HardwareSettings \
    %{buildroot}/%{_datadir}/applications/network.cycles.%{name}.desktop
 
%files
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*
%doc README.md
%license LICENSES/*
