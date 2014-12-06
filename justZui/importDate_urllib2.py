import urllib
import urllib2
import os
import json
import datetime

starttime = datetime.datetime.now()
endtime = datetime.datetime.now()
print (endtime - starttime).seconds

username = 'rxs'
password = 'rxs'
prefix = "ftp://rxs:rxs@115.28.91.77/weibo/data/"
url = prefix + "log.txt"

print("calling %s with %s:%s\n" % (url, username, password))

#passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
#passman.add_password(None, url, username, password)
#urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))
f = os.popen('wc -l serverLog.txt')
oldLine = f.read().split()[0]

#req = urllib2.Request(url)
f = urllib2.urlopen(url)
#f1 = urllib2.urlopen("ftp://rxs:rxs@115.28.91.77/weibo/data/20141205/1788911247_130501.txt")
#data = f1.read()
#print(data)
for i, line in enumerate(f):
	if i == 710:#> int(oldLine): 
		now = line.split()
		inputFileDate = now[0].replace('-','');
		inputFile = now[2] + '_' + now[1].replace(':', '')[0:4]
		if now[1][0:2] != '18':
			inputFile += '01.txt'
		else:
			inputFile += '02.txt'
		filepath = prefix + inputFileDate + '/' + inputFile
		print filepath
		f = urllib2.urlopen(filepath)
		output_file = f.read()
		# output_json = json.loads(output_file)

		# print output_json
		#sftp.get(filepath, localpath)
		print 1

print("finish")
endtime = datetime.datetime.now()
print (endtime - starttime).seconds
starttime = datetime.datetime.now()

