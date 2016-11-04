#!/usr/bin/env python
import commands,os,re,sys

gitdir = '/Users/maohuitao/Downloads/d1/'
git = '/Downloads/d1/'
publish = '/Downloads/d3/'
ignore = ['.DS_Store','log','conf','.git']

os.system('cd '+gitdir+" && git pull")

def fileCopy(tmp_x,tmp_old_x):
    if os.path.exists(tmp_x):
        x_time = os.path.getmtime(tmp_x)
        old_x_time = os.path.getmtime(tmp_old_x)
        if old_x_time > x_time:
            os.system('cp -f '+tmp_old_x+' '+tmp_x)
    else:
        os.system('cp -f '+tmp_old_x+' '+tmp_x)
    pass

def sync(gitdir):
    publishdir = gitdir.replace(git,publish)

    if os.path.exists(publishdir) == False:
        os.mkdir(publishdir)
    for x in os.listdir(gitdir):
        if x in ignore:
            continue
        if os.path.isdir(os.path.join(gitdir,x)):
            sync(os.path.join(gitdir,x))
        else:
            tmp_x = os.path.join(publishdir,x)
            tmp_old_x = os.path.join(gitdir,x)
            fileCopy(tmp_x,tmp_old_x)
        pass

sync(gitdir)

