Name:           xob
Version:        0.3
Release:        1
Summary:        Lightweight overlay volume (or anything) bar for X11
License:        GPL-3.0-only
Group:          Graphical desktop/Other
URL:            https://github.com/florentc/xob
Source0:        https://github.com/florentc/xob/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libconfig)

%description
xob (X Overlay Bar) is a lightweight, configurable overlay volume, backlight
or progress bar for the X Window System (and Wayland compositors with
XWayland). Values read on standard input are displayed as a bar over other
windows, which vanishes after a configurable timeout.

%prep
%autosetup -p1

%build
%make_build CC="%{__cc}" CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" \
    prefix=%{_prefix} sysconfdir=%{_sysconfdir}

%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/xob
%{_mandir}/man1/xob.1*
%dir %{_sysconfdir}/xob
%config(noreplace) %{_sysconfdir}/xob/styles.cfg
