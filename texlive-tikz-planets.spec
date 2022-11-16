Name:		texlive-tikz-planets
Version:	55002
Release:	1
Summary:	Illustrate celestial mechanics and the solar system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-planets
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-planets.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-planets.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This TikZ-package makes it easy to illustrate celestial
mechanics and the solar system. You can use it to draw sketches
of the eclipses, the phases of the Moon, etc. The package
requires the standard packages TikZ, xcolor, xstring, and
pgfkeys.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-planets
%doc %{_texmfdistdir}/doc/latex/tikz-planets

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
