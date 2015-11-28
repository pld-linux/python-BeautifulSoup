
%define         _module         BeautifulSoup

Summary:	A BeautifulSoup library for Python
Summary(pl.UTF-8):	Biblioteka BeautifulSoup dla Pythona
Name:		python-%{_module}
Version:	3.2.1
Release:	2
License:	Python
Group:		Development/Languages/Python
Source0:	http://www.crummy.com/software/%{_module}/download/3.x/%{_module}-%{version}.tar.gz
# Source0-md5:	5ad1a8550a19bfc945baac23eb8293ed
URL:		http://www.crummy.com/software/BeautifulSoup/
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beautiful Soup parses arbitrarily invalid SGML and provides a variety
of methods and Pythonic idioms for iterating and searching the parse
tree.

%description -l pl.UTF-8
Beautiful Soup parsuje, także wadliwy SGML i dostarcza różnorodne
metody i idiomy pythonowe do iterowania oraz przeszukiwania drzewa
wyniku parsowania.

%prep
%setup -q -n %{_module}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

install BeautifulSoupTests.py \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_postclean
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/BeautifulSoupTests.py[co]

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/BeautifulSoupTests.py
%{py_sitescriptdir}/BeautifulSoup.py[co]
%{py_sitescriptdir}/BeautifulSoup-%{version}-*.egg-info
