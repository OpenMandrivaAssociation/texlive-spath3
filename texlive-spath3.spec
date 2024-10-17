Name:		texlive-spath3
Version:	71396
Release:	1
Summary:	Manipulate "soft paths" in PGF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/spath3
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The spath3 library provides methods for manipulating the "soft
paths" of TikZ/PGF. Packaged with it are two TikZ libraries
that make use of the methods provided. These are libraries for
drawing calligraphic paths and for drawing knot diagrams.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spath3
%doc %{_texmfdistdir}/doc/latex/spath3
#- source
%doc %{_texmfdistdir}/source/latex/spath3

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
