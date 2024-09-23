pkgname = "gengetopt"
pkgver = "2.23"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "slibtool", "texinfo"]
pkgdesc = "Command line option parser generator"
maintainer = "triallax <triallax@tutanota.om>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gengetopt"
source = f"$(GNU_SITE)/gengetopt/gengetopt-{pkgver}.tar.xz"
sha256 = "b941aec9011864978dd7fdeb052b1943535824169d2aa2b0e7eae9ab807584ac"
hardening = ["vis", "cfi"]
