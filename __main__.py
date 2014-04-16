#! /usr/bin/env python

from subprocess import Popen
from sys import argv

try:
    cmd = argv[1]
except:
    cmd = 'python'

try:
    page = Popen((cmd, 'page.py'))
    screenshot = Popen((cmd, 'screenshot.py'))
    control = Popen((cmd, 'control.py'))
    page.wait()
finally:
    page.terminate()
    screenshot.terminate()
    control.terminate()
