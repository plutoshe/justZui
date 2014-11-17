# coding=utf-8 
import urllib
# params = urllib.urlencode({'location' : "理科教学楼", 'comment' : "测试1", 'groupName' : "马原课好无聊"})
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# print f.read()
# import urllib
# params = urllib.urlencode({'location' : "理科教学楼", 'comment' : "测试2", 'groupName' : "快下课"})
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", 'comment' : "测试4", 'groupName' : "饿死了"})
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# print f.read()


# params = urllib.urlencode({'location' : "理科教学楼"})
# f = urllib.urlopen("http://localhost:1234/groupQuery",params)
# print f.read()



# commentCreate

# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试2"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试3"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试4"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试5"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试6"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试7"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试8"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试9"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "测试10"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()

#comment Like
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 1})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 1})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 3})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 4})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()


# commentQueryNew
# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 0, "groupName" : "快下课", "index" : 4})
# f = urllib.urlopen("http://localhost:1234/commentQueryNew",params)
# print f.read()

# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 4})
# f = urllib.urlopen("http://localhost:1234/commentQueryNew",params)
# print f.read()


# commentQueryNext

# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 7})
# f = urllib.urlopen("http://localhost:1234/commentQueryNext",params)
# print f.read()


# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 0, "groupName" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentQueryNext",params)
# print f.read()

# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 7})
# f = urllib.urlopen("http://localhost:1234/groupQuery",params)
# print f.read()


# query by id

params = urllib.urlencode({'id' : '546794844c0cdc2e1443095b', 'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 7})
f = urllib.urlopen("http://localhost:1234/commentQueryNewById",params)
print f.read()

params = urllib.urlencode({'id' : '546794844c0cdc2e1443095b', 'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "index" : 2})
f = urllib.urlopen("http://localhost:1234/commentQueryNextById",params)
print f.read()

# params = urllib.urlencode({'location' : "理科教学楼", "groupType": 1, "groupName" : "快下课", "content" : "新的测试"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()


# f=urllib.urlopen("http://localhost:1234/locationQuery")
# s=f.read()
# print s