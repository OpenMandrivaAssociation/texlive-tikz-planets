%global tl_name tikz-planets
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.4
Release:	%{tl_revision}.1
Summary:	Illustrate celestial mechanics and the solar system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-planets
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-planets.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-planets.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This TikZ-package makes it easy to illustrate celestial mechanics and
the solar system. You can use it to draw sketches of the eclipses, the
phases of the Moon, etc. The package requires the standard packages
TikZ, xcolor, xstring, and pgfkeys.

