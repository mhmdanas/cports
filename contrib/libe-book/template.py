pkgname = "libe-book"
pkgver = "0.1.3"
pkgrel = 5
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "gperf"]
makedepends = [
    "boost-devel",
    "liblangtag-devel",
    "librevenge-devel",
    "libxml2-devel",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "Import reflowable e-book formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://sourceforge.net/projects/libebook"
source = f"$(SOURCEFORGE_SITE)/project/libebook/libe-book-{pkgver}/libe-book-{pkgver}.tar.xz"
sha256 = "7e8d8ff34f27831aca3bc6f9cc532c2f90d2057c778963b884ff3d1e34dfe1f9"


@subpackage("libe-book-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libe-book-devel")
def _devel(self):
    return self.default_devel()
