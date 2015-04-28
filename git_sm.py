#!/usr/bin/env python
import os,time,datetime
os.chdir('/home/wwwroot/kj/SharpMake')
os.system("git pull")
print time.strftime('%Y-%m-%d %H:%M:%S')+"\n";
