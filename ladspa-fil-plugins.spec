Summary:	FIL (equalizer filter) LADSPA plugin
Summary(pl.UTF-8):	Wtyczka LADSPA FIL (filtr korektora)
Name:		ladspa-fil-plugins
Version:	0.3.0
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/FIL-plugins-%{version}.tar.bz2
# Source0-md5:	39f34be516752a9740a65547e1128124
Patch0:		%{name}-make.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FIL (equalizer filter) LADSPA plugin.

%description -l pl.UTF-8
Wtyczka LADSPA FIL (filtr korektora).

%prep
%setup -q -n FIL-plugins-%{version}
%patch0 -p1

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/filters.so
