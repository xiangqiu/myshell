#!/usr/bin/env python
import os,re
filenames = os.listdir('/tmp/')
patton = 'sess'
newfilename = []
for i in filenames:
    res=re.search(patton,i)
    if res:
        newfilename.append(i)
for i in newfilename:
    os.system('rm -rf /tmp/'+i)
