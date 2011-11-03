# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-lilypond
# catalog-date 2010-03-12 17:25:27 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-lilypond
Version:	20100312
Release:	1
Summary:	Lilypond code in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-lilypond
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-lilypond.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-lilypond.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-context.bin

%description
Includes lilypond music definitions direct in a ConTeXt
document.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/lilypond/t-lilypond.tex
%doc %{_texmfdistdir}/doc/context/third/lilypond/demo.pdf
%doc %{_texmfdistdir}/doc/context/third/lilypond/t-lilypond.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
