# revision 29898
# category Package
# catalog-ctan /graphics/pgf/contrib/spath3
# catalog-date 2013-04-12 17:56:37 +0200
# catalog-license lppl1.3
# catalog-version 1
Name:		texlive-spath3
Version:	1
Release:	7
Summary:	Manipulate "soft paths" in PGF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/spath3
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.source.tar.xz
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
%{_texmfdistdir}/tex/latex/spath3/spath3.sty
%{_texmfdistdir}/tex/latex/spath3/tikzlibrarycalligraphy.code.tex
%{_texmfdistdir}/tex/latex/spath3/tikzlibraryknots.code.tex
%doc %{_texmfdistdir}/doc/latex/spath3/README.txt
%doc %{_texmfdistdir}/doc/latex/spath3/calligraphy_doc.pdf
%doc %{_texmfdistdir}/doc/latex/spath3/calligraphy_doc.tex
%doc %{_texmfdistdir}/doc/latex/spath3/knots_doc.pdf
%doc %{_texmfdistdir}/doc/latex/spath3/knots_doc.tex
#- source
%doc %{_texmfdistdir}/source/latex/spath3/spath3.dtx
%doc %{_texmfdistdir}/source/latex/spath3/spath3.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
