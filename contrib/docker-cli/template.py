pkgname = "docker-cli"
pkgver = "27.0.1"
pkgrel = 0
build_style = "makefile"
_commit = "7fafd33de04cf7d3e8e06900cb022ad65cd12a52"
make_cmd = "gmake"
make_build_target = "dynbinary"
hostmakedepends = [
    "bash",
    "gmake",
    "go",
    "go-md2man",
    "pkgconf",
]
depends = ["git"]
pkgdesc = "Container and image management tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://docker.com"
source = f"https://github.com/docker/cli/archive/v{pkgver}.tar.gz"
sha256 = "f73d47bd7dc176097c0e20797df1ec54bfaab3422aafd8810fd6830b626fe306"
env = {
    "AUTO_GOPATH": "1",
    "GITCOMMIT": _commit,
    "VERSION": pkgver,
    "DISABLE_WARN_OUTSIDE_CONTAINER": "1",
}
# objcopy fails to split on ppc
options = ["!debug", "!check"]


def init_prepare(self):
    from cbuild.util import golang

    self.env["GOPATH"] = str(self.chroot_cwd)
    self.env["GOBIN"] = str(self.chroot_cwd / "bin")
    self.env["CGO_ENABLED"] = "1"
    self.env.update(golang.get_go_env(self))


def do_prepare(self):
    self.do("gmake", "manpages", allow_network=True)


def pre_build(self):
    self.mkdir(self.cwd / "src/github.com/docker", parents=True)
    self.ln_s(self.chroot_cwd, self.cwd / "src/github.com/docker/cli")


def do_install(self):
    dbin = (self.cwd / "build/docker").resolve().name
    self.install_bin(f"build/{dbin}", name="docker")

    self.install_completion("contrib/completion/bash/docker", "bash")
    self.install_completion("contrib/completion/fish/docker.fish", "fish")
    self.install_completion("contrib/completion/zsh/_docker", "zsh")

    self.install_man("man/man1/docker.1")
    self.install_man("man/man1/docker-build.1")
    self.install_man("man/man1/docker-run.1")
    self.install_man("man/man5/Dockerfile.5")
    self.install_man("man/man5/docker-config-json.5")
    self.install_man("man/man8/dockerd.8")
