#!/usr/bin/env python
import os,re,sys
filenames=os.listdir('.')
oldext = raw_input('type in old extension:')
if oldext:
    print 'success!'
else:
    sys.exit()
newext = raw_input('type in new extension:')
if newext:
    print 'success!'
else:
    sys.exit()
oldext = '.'+oldext
newext = '.'+newext
for file in filenames:
    a,b = os.path.splitext(file)
    if b == oldext:
        newname = a+newext
        os.rename(file,newname)
    else:
        pass
raw_input('Implementation success!Press any key to continue!')

