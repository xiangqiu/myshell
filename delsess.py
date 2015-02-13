#!/usr/bin/env python
import os,re
filenames = os.listdir('/tmp/')
patton = 'sess'
for i in filenames:
    res=re.search(patton,filenames[i])
    if res != none:
        newfilename.append(filenames[i])
    endif
endfor
print newfilename
