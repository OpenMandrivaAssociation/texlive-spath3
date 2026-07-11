%global tl_name spath3
%global tl_revision 79231

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9
Release:	%{tl_revision}.1
Summary:	Manipulate soft paths in PGF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/spath3
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spath3.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The spath3 library provides methods for manipulating the "soft paths" of
TikZ/PGF. Packaged with it are two TikZ libraries that make use of the
methods provided. These are libraries for drawing calligraphic paths and
for drawing knot diagrams.

