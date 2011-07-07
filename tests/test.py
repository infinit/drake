#!/usr/bin/env python3

import os
import os.path
import sys

myself = os.getcwd()
dir = os.path.dirname(__file__)
if dir:
  myself += '/%s' % dir
sys.path = [myself + '/../src'] + sys.path

import doctest
import drake
import drake.git
import drake.python
import drake.utils

doctest.testmod(drake)
doctest.testmod(drake.git)
doctest.testmod(drake.python)
doctest.testmod(drake.utils)
