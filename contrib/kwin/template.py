pkgname = "kwin"
pkgver = "6.1.2"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    "(kwin-testClientMachine"  # initTestCase() segfaults in libc.so after 5s
    + "|kwin-testPointerInput"  # 11/130 subtests fail, cursor image (specifically fallback) changes problematic?
    + "|^kwin-testXdgShellWindow$"  # testDesktopFileName() Compared values are not the same ("" vs "wayland"), xdgshellwindow_test.cpp(675)
    + "|kwin-testScreenEdges"  # 8/20 subtests fail, testPushBack() & testTouchCallback() invalid touch moves
    + "|kwin-testPlasmaWindow"  # testLockScreenNoPlasmaWindow() '!waylandServer()->isScreenLocked()' returned FALSE, plasmawindow_test.cpp(267)
    + "|kwin-testScriptingScreenEdge"  # 4/18 subtests fail, testTouchEdge() & testDeclarativeTouchEdge() invalid touch moves
    + "|kwin-testDrm"  # testAmsDetection() segfaults
    + "|kwin-testButtonRebind"  # ppc64le fail weirdness?
    + "|kwin-testColorspaces"  # out of range on ppc64le float accuracy
    + ")",
    # parallel tests cause a bunch of flakes
    "-j1",
]
# D-Bus session needed by kwin-testLibinputDevice, X11 required by half the tests
make_check_wrapper = ["dbus-run-session", "xwfb-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libcap-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "breeze-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "kdecoration-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kglobalacceld-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kidletime-devel",
    "kirigami-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kpackage-devel",
    "kpipewire-devel",
    "krunner-devel",
    "kscreenlocker-devel",
    "kservice-devel",
    "ksvg-devel",
    "kwayland-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "lcms2-devel",
    "libcap-devel",
    "libdisplay-info-devel",
    "libei-devel",
    "libplasma-devel",
    "libqaccessibilityclient-devel",
    "libxcvt-devel",
    "pipewire-devel",
    "plasma-activities-devel",
    "plasma-wayland-protocols",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsensors-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
    "xcb-util-devel",
    "xwayland-devel",
]
depends = [
    "hwdata",
    "qt6-qtmultimedia",
    "xwayland",
]
checkdepends = [
    "breeze",
    "dbus",
    "mesa-utils",
    "xwayland-run",
] + depends
pkgdesc = "KDE Window Manager and Wayland Compositor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only"
)
url = "https://invent.kde.org/plasma/kwin"
source = f"$(KDE_SITE)/plasma/{'.'.join(pkgver.split('.')[0:3])}/kwin-{pkgver}.tar.xz"
sha256 = "82c582c83b01d42ac8dd6ca5fbc4b8daeea192b54dd1c859703e6f033455c00f"
file_modes = {
    "usr/bin/kwin_wayland": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/kwin_wayland": {
        "security.capability": "cap_sys_nice+ep",
    },
}
# CFI: breaks lots of tests
hardening = ["vis", "!cfi"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kwin-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
