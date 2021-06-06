# -*- coding: utf-8 -*-
# *****************************************************************************
# setup.py
# adds gitpath to sys.path
#
# Author              :        Erik Hammer (ehammer@tesla.com)
#
#
# *****************************************************************************

import os
import sys
import glob

gitPath = os.getcwd()


def UbuntuFindPath():
    searchPath = ''
    for d in gitPath.split(os.sep):
        if d:
            searchPath = searchPath + os.sep + d
            os.chdir(searchPath)
            for f in glob.glob(".bashrc"):
                return searchPath
    return None


def WindowsFindPath():
    sysPathList = sys.path
    for sysPath in sysPathList:
        if 'site-packages' in sysPath.split(os.sep)[-1]:
            return sysPath
    return None


def UpdateBashrc(path):
    lineExists = False
    exportStr = 'export PYTHONPATH=\"${PYTHONPATH}:' + gitPath + os.sep + '\"'
    with open(path + os.sep + '.bashrc', 'rb') as fp:
        lines = fp.readlines()
        for line in lines:
            if exportStr in line:
                lineExists = True
                break
    if not lineExists:
        with open(path + os.sep + '.bashrc', 'a') as fp:
            fp.write(exportStr)
            print('added gitpath to PYTHONPATH')
    else:
        print('gitPath already in PYTHONPATH')


def AddGitPath(path):
    lineExists = False
    try:
        with open(path + os.sep + 'gitpath.pth', 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                if gitPath in line:
                    lineExists = True
                    break
    except IOError:
        print('gitPath.pth does not exist')

    if not lineExists:
        with open(path + os.sep + 'gitpath.pth', 'w') as fp:
            fp.write(gitPath + os.sep)
            print('added gitpath to PYTHONPATH')
    else:
        print('gitPath already in PYTHONPATH')


if os.name == 'posix':
    bashrcPath = UbuntuFindPath()
    if bashrcPath is not None:
        UpdateBashrc(bashrcPath)
    else:
        print('could not find .bashrc !')
elif os.name == 'nt':
    anacondaPath = WindowsFindPath()
    if anacondaPath is not None:
        AddGitPath(anacondaPath)
    else:
        print('could not find Anaconda2\lib\site-packagages')
else:
    print('operating system not recognized, add gitpath manually to PYTHONPATH')
