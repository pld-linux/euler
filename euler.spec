%define		ver1	1.60
%define		ver2	6

Summary:	EULER, a program for doing mathematics on the computer
Summary(pl):	EULER, program do obliczeñ matematycznych na komputerze
Name:		euler
Version:	%{ver1}.%{ver2}
Release:	2
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/euler/%{name}-%{version}.tar.gz
# Source0-md5:	e56a0f41c184fc2f416457f0c5ece78f
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-doc_path.patch
Patch1:		%{name}-gcc33.patch
URL:		http://euler.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EULER is a program for quickly and interactively computing with real
and complex numbers and matrices, or with intervals, in the style of
MatLab, Octave,... It can draw and animate your functions in two and
three dimensions.

%description -l pl
EULER jest programem do szybkich i interaktywnych obliczeñ na liczbach
rzeczywistych i zespolonych, z przedzia³ami, w stylu MatLaba,
Octave... Mo¿e narysowaæ i animowaæ funkcje w dwóch lub trzech
wymiarach.

%prep
%setup -q -n %{name}-%{ver1}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} -DINSTALL_DIR=\\\"%{_prefix}\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/euler

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/euler
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
