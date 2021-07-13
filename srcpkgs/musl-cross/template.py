pkgname = "musl-cross"
version = "1.2.2"
revision = 0
wrksrc = f"musl-{version}"
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
hostmakedepends = ["gmake"]
makedepends = ["clang-rt-cross-base"]
depends = []
make_cmd = "gmake"
short_desc = "Musl C library - cross toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
homepage = "http://www.musl-libc.org/"
distfiles = [f"http://www.musl-libc.org/releases/musl-{version}.tar.gz"]
checksum = ["9b969322012d796dc23dda27a35866034fa67d8fb67e0e2c45c913c3d43219dd"]

# segfaults otherwise
hardening = ["!scp"]

from cbuild.util import compiler, make
from cbuild import cpu

_targets = ["aarch64", "ppc64le", "x86_64"]

def do_configure(self):
    for an in _targets:
        if cpu.target() == an:
            continue

        with self.profile(an):
            at = self.build_profile.short_triplet
            # musl build dir
            mbpath = self.abs_wrksrc / f"build-{an}"
            mbpath.mkdir(exist_ok = True)
            # configure musl
            with self.stamp(f"{an}_configure") as s:
                s.check()
                self.do(
                    self.chroot_wrksrc / "configure",
                    configure_args + ["--host=" + at], build = True,
                    wrksrc = self.chroot_wrksrc / f"build-{an}",
                    env = {
                        "CC": "clang -target " + at
                    }
                )

def do_build(self):
    for an in _targets:
        if cpu.target() == an:
            continue

        with self.profile(an):
            mbpath = self.abs_wrksrc / f"build-{an}"
            mbpath.mkdir(exist_ok = True)
            with self.stamp(f"{an}_build") as s:
                s.check()
                make.Make(
                    self, wrksrc = self.chroot_wrksrc / f"build-{an}"
                ).build()

def do_install(self):
    for an in _targets:
        if cpu.target() == an:
            continue

        with self.profile(an):
            at = self.build_profile.short_triplet
            self.install_dir(f"usr/{at}/usr/lib")
            self.install_link("usr/lib", f"usr/{at}/lib")
            make.Make(
                self, wrksrc = self.chroot_wrksrc / f"build-{an}"
            ).install([
                "DESTDIR=" + str(self.chroot_destdir / "usr" / at)
            ], default_args = False)
            self.unlink(f"usr/{at}/lib")

def _gen_crossp(an, at):
    @subpackage(f"musl-cross-{an}", cpu.target() != an)
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        self.depends = [f"clang-rt-cross-base-{an}"]
        return [f"usr/{at}"]
    if cpu.target() != an:
        depends.append(f"musl-cross-{an}")

for an in _targets:
    with current.profile(an):
        _gen_crossp(an, current.build_profile.short_triplet)
