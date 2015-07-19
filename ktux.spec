Summary:	Tux-in-a-Spaceship screensaver
Name:		ktux
Version:	15.04.3
Release:	2
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel

%description
Tux-in-a-Spaceship screensaver.

%files
%{_bindir}/ktux
%{_datadir}/apps/ktux
%{_iconsdir}/hicolor/*/apps/ktux.*
%{_datadir}/kde4/services/ScreenSavers/ktux.desktop

#-------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

