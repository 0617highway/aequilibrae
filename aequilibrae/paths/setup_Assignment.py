"""
 -----------------------------------------------------------------------------------------------------------
 Package:    AequilibraE

 Name:       Auxiliary code
 Purpose:    Compiles AequilibraE's Cython code

 Original Author:  Pedro Camargo (c@margo.co)
 Contributors:
 Last edited by: Pedro Camrgo

 Website:    www.AequilibraE.com
 Repository:  https://github.com/AequilibraE/AequilibraE

 Created:    01/01/2013
 Updated:    30/09/2016
 Copyright:   (c) AequilibraE authors
 Licence:     See LICENSE.TXT
 -----------------------------------------------------------------------------------------------------------
 """

from __future__ import division, print_function, absolute_import
import sys
import os

sys.dont_write_bytecode = True

import numpy as np

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

from Cython.Distutils import build_ext

import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

here = os.path.dirname(os.path.realpath(__file__))
whole_path = os.path.join(here, 'AoN.pyx')

ext_module = Extension('AoN',
                       [whole_path],
                       # extra_compile_args=['/fopenmp'],
                       # extra_link_args=['/fopenmp'],
                       include_dirs=[np.get_include()])

setup(cmdclass={'build_ext': build_ext},
      ext_modules=[ext_module])
