#!/usr/bin/env python
import os,time,datetime
os.chdir('/home/wwwroot/SharpMake')
os.system("git pull")
print time.strftime('%Y-%m-%d %H:%M:%S')+"\n";
