# coding=utf-8 
#-utf-8-
import sys
import json
import re
import urllib
import urllib2
import paramiko
import os
from subprocess import call
reload(sys)
sys.setdefaultencoding( "utf-8" )
nonspace = re.compile(r'\S')



#now1 = call(['wc', '-l', 'log.txt']).split()[2]


def iterparse(j):
    decoder = json.JSONDecoder()
    pos = 0
    while True:
        matched = nonspace.search(j, pos)
        if not matched:
            break
        pos = matched.start()
        try:
        	decoded, pos = decoder.raw_decode(j, pos)
        except:
        	print("decode error")
        yield decoded

def commentCreate(content):
    params = urllib.urlencode({'location' : 0, "groupType": 0, "title" : "", "content" : content})
    try:
    	f = urllib.urlopen("http://localhost:1234/commentCreate",params)
    except:
    	print("Link server error!")
    

def updateNowComments():
	rawdata = open("temp.txt").read()
	for decoded in iterparse(rawdata):
		commentCreate(decoded['text'])
		now_data = decoded['comments']
		rep = 0
		for comment in now_data:
			rep+=1
			if (rep > 10):
				break
			else:
				commentCreate(comment['text'])

def lineProcess(sftp, line, suffix):
	now = line.split()
	inputFileDate = now[0].replace('-','');
	inputFile = now[2] + '_' + now[1].replace(':', '')[0:4] + suffix
	
	filepath = '/home/rxs/weibo/data/' + inputFileDate + '/' + inputFile
	localpath =  './temp.txt'
	print filepath, localpath
	try:
		sftp.get(filepath, localpath)
		updateNowComments()
	except: 
		print("sftp error when get " + inputFileDate + '/' + inputFile)
	
def updateNovelty():
	host = "115.28.91.77"
	port = 22
	transport = paramiko.Transport((host, port))

	# Auth

	password = "rxs"
	username = "rxs"
	transport.connect(username = username, password = password)
	sftp = paramiko.SFTPClient.from_transport(transport)

	# Download

	filepath = '/home/rxs/weibo/data/log.txt'
	localpath =  './log.txt'	
	sftp.get(filepath, localpath)
	updateNowComments()
	
	f = os.popen('date')
	now = f.read()
	f1 = os.popen('wc -l log.txt')
	newLine = f1.read().split()[0]
	f2 = os.popen('wc -l serverLog.txt')
	oldLine = f2.read().split()[0]
	print oldLine, newLine
	fp = open("log.txt")
	for i, line in enumerate(fp):
		if i >= oldLine: 
			print i
			lineProcess(sftp, line, "01.txt")
			lineProcess(sftp, line, "02.txt")
			

	fp.close()
	call(['mv', 'log.txt', 'serverLog.txt'])

	sftp.close()
	transport.close()


