#!/usr/bin/python


from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

WorkDir = "."

def setup():
    shelltools.system("ls -la")

def install():
    print("Test install")
