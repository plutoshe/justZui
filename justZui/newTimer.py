import schedule
import time
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
import importDateNew


# schedule.every(5).seconds.do(importDateNew.hello)
# schedule.every().hour.do(importDateNew.hello)
schedule.every().day.at("1:15").do(importDateNew.updateNovelty)
schedule.every().day.at("7:15").do(importDateNew.updateNovelty)
schedule.every().day.at("10:15").do(importDateNew.updateNovelty)
schedule.every().day.at("13:15").do(importDateNew.updateNovelty)
schedule.every().day.at("16:15").do(importDateNew.updateNovelty)
schedule.every().day.at("18:15").do(importDateNew.updateNovelty)
schedule.every().day.at("21:15").do(importDateNew.updateNovelty)
schedule.every().day.at("23:15").do(importDateNew.updateNovelty)


while 1:
    schedule.run_pending()
		    time.sleep(1)
		    
