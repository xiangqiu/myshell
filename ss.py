#!/usr/bin/env python
import os,time,datetime
os.system("/usr/bin/python2.6 /usr/bin/ssserver -c /etc/ss.json -d restart")
print time.strftime('%Y-%m-%d %H:%M:%S')+"\n";
