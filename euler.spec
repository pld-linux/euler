%define		ver1	1.59
%define		ver2	1

Summary:	EULER, a program for doing mathematics on the computer
Summary(pl):	EULER, program do obliczeñ matematycznych na komputerze
Name:		euler
Version:	%{ver1}.%{ver2}
Release:	2
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
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

%build
cd source
%{__make} \
	CC="%{__cc} %{rpmcflags} -DINSTALL_DIR=\\\"%{_prefix}\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_bindir}}
cd source
%{__make} install \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix}
cd ..

#rm -rf $RPM_BUILD_ROOT%{_datadir}/euler/docs 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/euler
#%doc docs/*
%doc README ChangeLog TODO
