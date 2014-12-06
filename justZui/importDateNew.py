# coding=utf-8 
#-utf-8-
# import urllib2
# url = "115.28.91.77"
# f = urllib2.urlopen(url) 
# with open("demo2.zip", "wb") as code:
#    code.write(f.read()) 
# import codecs

# f=open('./cralwer/data/20141204/1494848464_010501.txt')
# f1=codecs.open('./a.tst', "w", "utf-8")
# while true:


#    else:
#     f1.write(unichr(int(tmp,16)))
# f.close()
# f1.close()
# import os
# import paramiko

# ssh = paramiko.SSHClient()
# ssh.load_host_keys(os.path.expanduser(os.path.join("~",".ssh","known_hosts")))
# ssh.connect(server,username=username,password=password)
# sftp = ssh.open_sftp()
# remote_file = sftp.file(remotepath,"wb")
# remote_file.set_pipelined(True)
# remote_file.write(data)
# sftp.close()
# ssh.close()

# import urllib2
# import os
# import paramiko

# ssh = paramiko.SSHClient()
# ssh.load_host_keys(os.path.expanduser(os.path.join("~",".ssh","known_hosts")))
# ssh.connect("115.28.91.77",username='rsx',password='rsx')




# # Execute shell remotely
# stdin, stdout, stderr = client.exec_command("ls -alh")
# stdout.read()


# # Open sftp session
# sftp = client.open_sftp()
# remote_file = sftp.file('/home/rsx/weibo/data/',"wb")
# remote_file.set_pipelined(True)
# remote_file.write(data)
# Make a dir
#sftp.mkdir('abc')

# sftp.get(firewall.sh', '/tmp/firewall.sh')

#sftp.put('/tmp/firewall.sh', 'firewall_new.sh')

# coding=utf-8 
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
    print(content)
    params = urllib.urlencode({'location' : 0, "groupType": 0, "title" : "", "content" : content})
    try:
    	f = urllib.urlopen("http://182.92.243.187:1234/commentCreate",params)
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
			print rep, comment['text']
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

	f = os.popen('date')
	now = f.read()
	f1 = os.popen('wc -l log.txt')
	newLine = f1.read().split()[0]
	f2 = os.popen('wc -l serverLog.txt')
	oldLine = f2.read().split()[0]
	print oldLine, newLine
	fp = open("log.txt")
	for i, line in enumerate(fp):
		if i >= int(oldLine): 
			print i
			lineProcess(sftp, line, "01.txt")
			lineProcess(sftp, line, "02.txt")
			

	fp.close()
	call(['mv', 'log.txt', 'serverLog.txt'])

	sftp.close()
	transport.close()
