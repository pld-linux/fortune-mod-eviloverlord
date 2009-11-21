Summary:	Things I'd Do If I Ever Became An Evil Overlord
Summary(pl.UTF-8):	Rzeczy, które bym zrobił, gdybym zdobył władzę nad światem
Name:		fortune-mod-eviloverlord
Version:	20091121
Release:	1
License:	Distributable + WTFPL
Group:		Applications/Games
# git clone git://github.com/pawelz/fortune-mod-eviloverlord
Source0:	http://xatka.net/~z/PLD/%{name}-%{version}.tar.bz2
# Source0-md5:	d019f96f1364b7c69c32e2c101f1de86
Source1:	http://www.eviloverlord.com/lists/overlord.html
# Source1-md5:	b7852206caff4f2eaaecd8006fb068d4
Source2:	http://www.eviloverlord.com/lists/dungeon_a.html
# Source2-md5:	d75189fb65d1c84981d49628b75aa11a
Source3:	http://www.eviloverlord.com/lists/dungeon_b.html
# Source3-md5:	7c5a3feea32ec429a8e9ee5bb531e2b4
URL:		http://www.eviloverlord.com/lists/overlord.html
BuildRequires:	fortune-mod
Requires:	fortune-mod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Things I'd Do If I Ever Became An Evil Overlord.

%description -l pl.UTF-8
Rzeczy, które bym zrobił, gdybym zdobył władzę nad światem.

%prep
%setup -q

cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .

%build
./eviloverlord.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes
install eviloverlord* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%{_datadir}/games/fortunes/*
