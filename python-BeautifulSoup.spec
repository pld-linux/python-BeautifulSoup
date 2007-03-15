
%define         _module         BeautifulSoup

Summary:	A BeautifulSoup library for Python
Summary(pl.UTF-8):	Biblioteka BeautifulSoup dla Pythona
Name:		python-%{_module}
Version:	3.0.3
Release:	1
License:	Python
Group:		Development/Languages/Python
Source0:	http://www.crummy.com/software/%{_module}/download/%{_module}.tar.gz
# Source0-md5:	7b788918e887b6b2c1bfef28ca4eb0d1
URL:		http://www.crummy.com/software/BeautifulSoup/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beautiful Soup parses arbitrarily invalid SGML and provides a variety of
methods and Pythonic idioms for iterating and searching the parse tree.

%description -l pl.UTF-8
Beautiful Soup parsuje, także wadliwy SGML i dostarcza różnorodne metody
i idiomy pythonowe do iterowania oraz przeszukiwania drzewa wyniku
parsowania.

%prep
%setup -q -n %{_module}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install BeautifulSoupTests.py \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_postclean
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/BeautifulSoupTests.py[co]

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}/BeautifulSoupTests.py
%{py_sitescriptdir}/BeautifulSoup.py[co]
