# -*- coding: utf-8 -*-
# *****************************************************************************
# __init__.py
# specify above directory as python module
#
# Author              :        Erik Hammer (ehammer@tesla.com)
#
#
# *****************************************************************************

import os

def path():
	return __file__.rsplit(os.sep, 1)[0] + os.sep
