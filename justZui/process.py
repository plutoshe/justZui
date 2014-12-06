import sys
import json
import re
import urllib
import urllib2
import paramiko
import os
from subprocess import call
import datetime
from threading import Timer


x=datetime.datetime.today()
t_str = '2014-12-31 16:26:23'
d = datetime.datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')
delta_day = datetime.timedelta(days=1)
delta_test = datetime.timedelta(seconds=30)
delta_minute = datetime.timedelta(minutes=1)
runtime = [1,7,10,13,16,18,21,23]
test_runtime = [0,5,10,15,20,25,30,35,40,45,50,55]

def hello_world():
	
	x=datetime.datetime.today()
	print x
	t = Timer(delta_minute, hello_world)
	t.start()



for i in test_runtime:
	y=x.replace(day=x.day, hour=x.hour, minute=x.minute, second=i, microsecond=0)
	if (y > x):
		print 1
	else:
		y = y + delta_minute
		print 0
	delta_t=y-x
	secs=delta_t.seconds+1
	print secs
	#t = Timer(secs, hello_world)
	#t.start()		
	#processArr.append(delta+1)



    #...
