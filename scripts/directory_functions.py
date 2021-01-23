#!/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*- 

import os


def getMainDirectory():
    path = os.getcwd()
    return path

def goToMainDirectory(path):
    if (path != os.getcwd()):
        os.chdir(path)

def goToWorkingDirectory():
    path = os.getcwd()
    if not(path.split('/')[-1] == 'blog'):
        path = path + '/data/raw_data/blog'
        os.chdir(path)

