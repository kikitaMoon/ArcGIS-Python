# -*- coding: utf-8 -*-
__author__ = 'kikita'

from distutils.core import setup
import py2exe

# Exclude "arcpy" from the Py2exe setup.py script.
options = {"py2exe": {"excludes": ["arcpy"]}}
setup(console=['HelloPy2exe.py'], options=options)
