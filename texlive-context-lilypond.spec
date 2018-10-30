# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-lilypond
# catalog-date 2010-03-12 17:25:27 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-lilypond
Version:	20100312
Release:	11
Summary:	Lilypond code in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-lilypond
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-lilypond.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-lilypond.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
Includes lilypond music definitions direct in a ConTeXt
document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/lilypond/t-lilypond.tex
%doc %{_texmfdistdir}/doc/context/third/lilypond/demo.pdf
%doc %{_texmfdistdir}/doc/context/third/lilypond/t-lilypond.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100312-2
+ Revision: 750502
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100312-1
+ Revision: 718137
- texlive-context-lilypond
- texlive-context-lilypond
- texlive-context-lilypond
- texlive-context-lilypond

