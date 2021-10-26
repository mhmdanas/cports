pkgname = "bubblewrap"
pkgver = "0.5.0"
pkgrel = 0
build_style = "gnu_configure"
# FIXME: enable when we have xsltproc
configure_args = ["--disable-man"]
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
makedepends = ["libcap-devel"]
checkdepends = ["bash", "libcap-progs"]
pkgdesc = "Unprivileged sandboxing tool"
maintainer = "q66 <daniel@octaforge.org>"
license = "LGPL-2.0-or-later"
url = "https://github.com/containers/bubblewrap"
source = f"https://github.com/containers/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "16fdaf33799d63104e347e0133f909196fe90d0c50515d010bcb422eb5a00818"
tool_flags = {"CFLAGS": ["-Wno-error,-Wformat-nonliteral"]}
