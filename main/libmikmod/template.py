pkgname = "libmikmod"
pkgver = "3.3.11.1"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Mikmod module player and library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://mikmod.shlomifish.org"
source = f"$(SOURCEFORGE_SITE)/mikmod/libmikmod-{pkgver}.tar.gz"
sha256 = "ad9d64dfc8f83684876419ea7cd4ff4a41d8bcd8c23ef37ecb3a200a16b46d19"
# CFI: crashes in sc2 ucm
hardening = ["vis", "!cfi"]


@subpackage("libmikmod-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/info"])
