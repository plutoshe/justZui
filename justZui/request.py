# coding=utf-8 
# commentCreate
# commentQueryNew
# commentQueryNext
# f = urllib.urlopen("http://182.92.243.187:1234/commentQueryUpdated/",params)
# f = urllib.urlopen("http://182.92.243.187:1234/locationQuery/")
# f = urllib.urlopen("http://182.92.243.187:1234/locationUpdate",params)
# f = urllib.urlopen("http://182.92.243.187:1234/locationUpdate/",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# f = urllib.urlopen("http://localhost:1234/commentQueryNew",params)
# f = urllib.urlopen("http://localhost:1234/commentQueryNew",params)
# f = urllib.urlopen("http://localhost:1234/commentQueryNewById",params)
# f = urllib.urlopen("http://localhost:1234/commentQueryNext",params)
# f = urllib.urlopen("http://localhost:1234/commentQueryNext",params)
# f = urllib.urlopen("http://localhost:1234/commentQueryNextById",params)
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# f = urllib.urlopen("http://localhost:1234/groupDegrade/",params)
# f = urllib.urlopen("http://localhost:1234/groupExist/",params)
# f = urllib.urlopen("http://localhost:1234/groupQuery",params)
# f=urllib.urlopen("http://localhost:1234/locationQuery")
import urllib
import json

# params = urllib.urlencode({'version' : 1.14, "update_content" : "无"})
# f = urllib.urlopen("http://localhost:1234/specificVersion", params)
# print f.read()
# params = urllib.urlencode({'version' : 1.15, "update_content" : "无"})
# f = urllib.urlopen("http://localhost:1234/versionUpdate", params)
# print f.read()

# params = urllib.urlencode({"locationName" : "新的bbs", "subclass" : 1})
# f = urllib.urlopen("http://localhost:1234/newLocationCreate", params)
# print f.read()
# params = urllib.urlencode({"locationName" : "新的bbs", "subclass" : 4})
# f = urllib.urlopen("http://localhost:1234/specificLocationQuery", params)
# print f.read()


# params = urllib.urlencode({'location' : 0, "title" : "f啊D8@#!  123123@(*&^&  &"})
# f = urllib.urlopen("http://localhost:1234/groupCreate", params)


# params = urllib.urlencode({'location' : 0, "groupType" : 2, "mark" : 0, "title" : "f啊D8@#!  123123@(*&^&  &", 'content' : "111吐&&&&&&槽&dddd   32432!@#%^@#&@*@*"})
# f = urllib.urlopen("http://localhost:1234/commentCreate", params)
# print f.read()


# params = urllib.urlencode({'location' : 0, "groupType" : 2, "mark" : 1, "title" : "f啊D8@#!  123123@(*&^&  &", 'content' : "111吐&&&&&&槽&dddd   32432!@#%^@#&@*@*"})
# f = urllib.urlopen("http://localhost:1234/commentCreate", params)
# print f.read()


# params = urllib.urlencode({'location' : 0, "groupType" : 2, "mark" : 0, "title" : "f啊D8@#!  123123@(*&^&  &", 'content' : "111吐&&&&&&槽&dddd   32432!@#%^@#&@*@*"})
# f = urllib.urlopen("http://localhost:1234/commentCreate", params)
# print f.read()


# params = urllib.urlencode({'location' : 0, "groupType" : 2, "mark" : 1, "title" : "f啊D8@#!  123123@(*&^&  &", 'content' : "111吐&&&&&&槽&dddd   32432!@#%^@#&@*@*"})
# f = urllib.urlopen("http://localhost:1234/commentCreate", params)
# print f.read()


# f = urllib.urlopen("http://localhost:1234/versionGet")
# print f.read()

params = urllib.urlencode({'index' : 0, 'location' : 0, "groupType" : 2, "mark" : 1, "title" : "f啊D8@#!  123123@(*&^&  &", 'content' : "111吐&&&&&&槽&dddd   32432!@#%^@#&@*@*"})
f = urllib.urlopen("http://localhost:1234/commentLikeQueryUpdated", params)
print f.read()


# params = urllib.urlencode({'1' : 1, 'comment' : "测试1", 'title' : "马原课好无聊"})
# params = urllib.urlencode({'id' : '546794844c0cdc2e1443095b', 'location' : 1, "groupType": 2, "title" : "快下课", "index" : 2})
# params = urllib.urlencode({'id' : '546794844c0cdc2e1443095b', 'location' : 1, "groupType": 2, "title" : "快下课", "index" : 7})
# params = urllib.urlencode({'location' : 0, 'locationName' : "醉头条"})
# params = urllib.urlencode({'location' : 1, "groupType": 0, "title" : "快下课", "index" : 2})
# params = urllib.urlencode({'location' : 1, "groupType": 0, "title" : "快下课", "index" : 4})
# params = urllib.urlencode({'location' : 1, "groupType": 1, "title" : "快下课", "content" : "新的测试"})
# params = urllib.urlencode({'location' : 1, "groupType": 1, "title" : "快下课", "index" : 7})
# params = urllib.urlencode({'location' : 1, "groupType": 1, "title" : "快下课", "index" : 7})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试10"})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试3"})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试4"})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试5"})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试6"})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试7"})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试8"})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试9"})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 1})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 1})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 2})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 2})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 2})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 3})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 4})
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 4})
# params = urllib.urlencode({'location' : 1, 'comment' : "测试2", 'title' : "快下课"})
# params = urllib.urlencode({'location' : 1, 'comment' : "测试4", 'title' : "饿死了"})
# params = urllib.urlencode({'location' : 1, 'title' : "1饿死了"})
# params = urllib.urlencode({'location' : 1, 'title' : "我们饿了", 'groupType' : 2, 'index' : 0, 'indexOld' : 2, 'indexNew' : 4})
# params = urllib.urlencode({'location' : 1, 'title' : "饿死了"})
# params = urllib.urlencode({'location' : 8, "locationName": "宿舍区"})
# print f.read()
# print f.read()
# print f.read()
# print f.read()
# print s
# query by id
# s=f.read()
#comment Like
#f = urllib.urlopen("http://182.92.243.187:1234/commentCreate",params)
#f = urllib.urlopen("http://localhost:1234/locationQuery")
# params = urllib.urlencode({'location' : 5, "locationName": "理教、理科楼"})
# params = urllib.urlencode({'version' : '1.15'})
# f = urllib.urlopen("http://localhost:1234/versionUpdate", params)
# print f.read()


# params = urllib.urlencode({'location' : 1, "locationName" : "天涯杂谈热门"})
# f = urllib.urlopen("http://182.92.243.187:1234/locationUpdate", params)
# print f.read()

# params = urllib.urlencode({'location' : 2, "locationName" : "清华水木bbs热门"})
# f = urllib.urlopen("http://182.92.243.187:1234/locationUpdate", params)
# print f.read()

# params = urllib.urlencode({'location' : 3, "locationName" : "北大未名bbs热门"})
# f = urllib.urlopen("http://182.92.243.187:1234/locationUpdate", params)
# print f.read()

# params = urllib.urlencode({'location' : 4, "locationName" : "美国米国"})
# f = urllib.urlopen("http://182.92.243.187:1234/locationUpdate", params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "locationName" : "啊啊啊啊"})
# f = urllib.urlopen("http://localhost:1234/locationCreate", params)

# params = urllib.urlencode({'location' : 0, "title" : "f啊D8@#!  123123@(*&^&  &"})
# f = urllib.urlopen("http://localhost:1234/groupCreate", params)
        

# params = urllib.urlencode({'location' : 0, "title" : "f啊D8@#!  123123@(*&^&  &"})
# f = urllib.urlopen("http://182.92.243.187:1234/groupCreate", params)
        
# params = urllib.urlencode({'location' : 0, "groupType" : 2, "title" : "f啊D8@#!  123123@(*&^&  &", 'content' : "111吐&&&&&&槽&dddd   32432!@#%^@#&@*@*"})
# f = urllib.urlopen("http://182.92.243.187:1234/commentCreate", params)
# print f.read()






#print f.read()

# print f.read()
# f = urllib.urlopen("http://182.92.243.187:1234/commentLikeQueryNew",params)
# f = urllib.urlopen("http://182.92.243.187:1234/commentLikeQueryNext",params)
# f = urllib.urlopen("http://182.92.243.187:1234/commentLikeQuerySection",params)
# f = urllib.urlopen("http://182.92.243.187:1234/commentLikeQueryUpdated",params)
# import urllib
# params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "啊啊啊", "index" : 4})
# params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "啊啊啊", "index" : 4})
# params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "啊啊啊", "index" : 4})
# params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "啊啊啊", "indexOld" : 1, "indexNew" : 4})
# print f.read()
# print f.read()
# print f.read()
# print f.read()
# ｀赞｀Ω｀｀｀｀｀｀｀｀