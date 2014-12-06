# coding=utf-8 
import sys
import json
import re
import urllib
import urllib2

reload(sys)
sys.setdefaultencoding( "utf-8" )

nonspace = re.compile(r'\S')
def iterparse(j):
    decoder = json.JSONDecoder()
    pos = 0
    while True:
        matched = nonspace.search(j, pos)
        if not matched:
            break
        pos = matched.start()
        decoded, pos = decoder.raw_decode(j, pos)
        yield decoded

def commentCreate(content):
    print content
    params = urllib.urlencode({"location" : 0, "groupType": 0, "title" : "", "content" : content})
    f = urllib.urlopen("http://182.92.243.187:1234/commentCreate",params)
    

rawdata = open("temp.txt").read()
for decoded in iterparse(rawdata):
    commentCreate(decoded['text'])
    now_data = decoded['comments']
    for comment in now_data:
        commentCreate(comment['text'])