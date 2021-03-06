#!/usr/bin/python


from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

WorkDir = "."

def setup():
    shelltools.system("pwd")
    shelltools.cd("chkrootkit-0.53")
    shelltools.system("sed -i '/^unalias dirname*/a  cd /usr/lib/chkrootkit' chkrootkit")
    shelltools.system("make sense")
    shelltools.cd("..")

def install():
    pisitools.dodir("/usr/lib/chkrootkit")
    pisitools.insinto("/usr/lib/chkrootkit/", "chkrootkit-0.53/check_wtmpx")
    pisitools.insinto("/usr/lib/chkrootkit/", "chkrootkit-0.53/chkdirs")
    pisitools.insinto("/usr/lib/chkrootkit/", "chkrootkit-0.53/chklastlog")
    pisitools.insinto("/usr/lib/chkrootkit/", "chkrootkit-0.53/chkproc")
    pisitools.insinto("/usr/lib/chkrootkit/", "chkrootkit-0.53/chkutmp")
    pisitools.insinto("/usr/lib/chkrootkit/", "chkrootkit-0.53/chkwtmp")
    pisitools.insinto("/usr/lib/chkrootkit/", "chkrootkit-0.53/ifpromisc")
    pisitools.insinto("/usr/lib/chkrootkit/", "chkrootkit-0.53/strings-static")
    pisitools.insinto("/usr/sbin/", "chkrootkit-0.53/chkrootkit")
    pisitools.dosym("../lib/chkrootkit/chklastlog", "/usr/sbin/chklastlog")
    pisitools.dosym("../lib/chkrootkit/chkwtmp", "/usr/sbin/chkwtmp")
