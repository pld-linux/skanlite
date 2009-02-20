%define         _state          stable
%define		_kde_ver	4.2.0
%define		qtver		4.4.3
Summary:	Image scanning application
Summary(pl.UTF-8):	Aplikacja do skanowania
Name:		skanlite
Version:	0.2
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kde_ver}/src/extragear/%{name}-%{version}-kde%{_kde_ver}.tar.bz2
# Source0-md5:	a3442f520720099af98510dd7714a07e
URL:		http://www.simonzone.com/software/guidance/
BuildRequires:	kde4-kdegraphics-devel
BuildRequires:	kde4-kdegraphics-ksane
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skanlite is an image scanning application to scan and save images.

%description -l pl.UTF-8
Skanlite jest aplikacją do skanowania i zapisu obrazków.

%prep
%setup -q -n %{name}-%{version}-kde%{_kde_ver}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/skanlite
%{_desktopdir}/kde4/skanlite.desktop
