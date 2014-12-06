# coding=utf-8 
import urllib
# params = urllib.urlencode({'1' : 1, 'comment' : "测试1", 'title' : "马原课好无聊"})
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# print f.read()
# import urllib
# params = urllib.urlencode({'location' : 1, 'comment' : "测试2", 'title' : "快下课"})
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, 'comment' : "测试4", 'title' : "饿死了"})
# f = urllib.urlopen("http://localhost:1234/groupCreate",params)
# print f.read()

# params = urllib.urlencode({'location' : 1, 'title' : "我们饿了", 'groupType' : 2, 'index' : 0, 'indexOld' : 2, 'indexNew' : 4})
# f = urllib.urlopen("http://182.92.243.187:1234/commentQueryUpdated/",params)
# print f.read()


# params = urllib.urlencode({'location' : 1, 'title' : "饿死了"})
# f = urllib.urlopen("http://localhost:1234/groupDegrade/",params)
# print f.read()



# f = urllib.urlopen("http://182.92.243.187:1234/locationQuery/")
# print f.read()

# params = urllib.urlencode({'location' : 0, 'locationName' : "醉头条"})
# f = urllib.urlopen("http://182.92.243.187:1234/locationUpdate/",params)
# print f.read()


# params = urllib.urlencode({'location' : 1, 'title' : "1饿死了"})
# f = urllib.urlopen("http://localhost:1234/groupExist/",params)
# print f.read()

# #params = urllib.urlencode({'location' : 1, 'title' : "1饿死了"})
 #f = urllib.urlopen("http://localhost:1234/locationQuery/")
 #print f.read()

# commentCreate

#params = urllib.urlencode({'location' : 5, "locationName": "理教、理科楼"})
#f = urllib.urlopen("http://localhost:1234/locationQuery")
#print f.read()

# params = urllib.urlencode({'location' : 8, "locationName": "宿舍区"})
# f = urllib.urlopen("http://182.92.243.187:1234/locationUpdate",params)
# print f.read()

#params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "阿拉拉1", "content" : "测试www"})
#f = urllib.urlopen("http://182.92.243.187:1234/commentCreate",params)
#print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试3"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试4"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试5"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试6"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试7"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试8"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试9"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "content" : "测试10"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()

#comment Like
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 1})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 1})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 3})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()
# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 4})
# f = urllib.urlopen("http://localhost:1234/commentLike",params)
# print f.read()


# commentQueryNew
# params = urllib.urlencode({'location' : 1, "groupType": 0, "title" : "快下课", "index" : 4})
# f = urllib.urlopen("http://localhost:1234/commentQueryNew",params)
# print f.read()

# params = urllib.urlencode({'location' : 1, "groupType": 2, "title" : "快下课", "index" : 4})
# f = urllib.urlopen("http://localhost:1234/commentQueryNew",params)
# print f.read()

params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "啊啊啊", "index" : 4})
f = urllib.urlopen("http://182.92.243.187:1234/commentLikeQueryNew",params)
print f.read()

params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "啊啊啊", "index" : 4})
f = urllib.urlopen("http://182.92.243.187:1234/commentLikeQueryNext",params)
print f.read()


params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "啊啊啊", "indexOld" : 1, "indexNew" : 4})
f = urllib.urlopen("http://182.92.243.187:1234/commentLikeQuerySection",params)
print f.read()


params = urllib.urlencode({'location' : 9, "groupType": 2, "title" : "啊啊啊", "index" : 4})
f = urllib.urlopen("http://182.92.243.187:1234/commentLikeQueryUpdated",params)
print f.read()






# commentQueryNext

# params = urllib.urlencode({'location' : 1, "groupType": 1, "title" : "快下课", "index" : 7})
# f = urllib.urlopen("http://localhost:1234/commentQueryNext",params)
# print f.read()


# params = urllib.urlencode({'location' : 1, "groupType": 0, "title" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentQueryNext",params)
# print f.read()

# params = urllib.urlencode({'location' : 1, "groupType": 1, "title" : "快下课", "index" : 7})
# f = urllib.urlopen("http://localhost:1234/groupQuery",params)
# print f.read()


# query by id

# params = urllib.urlencode({'id' : '546794844c0cdc2e1443095b', 'location' : 1, "groupType": 2, "title" : "快下课", "index" : 7})
# f = urllib.urlopen("http://localhost:1234/commentQueryNewById",params)
# print f.read()

# params = urllib.urlencode({'id' : '546794844c0cdc2e1443095b', 'location' : 1, "groupType": 2, "title" : "快下课", "index" : 2})
# f = urllib.urlopen("http://localhost:1234/commentQueryNextById",params)
# print f.read()

# params = urllib.urlencode({'location' : 1, "groupType": 1, "title" : "快下课", "content" : "新的测试"})
# f = urllib.urlopen("http://localhost:1234/commentCreate",params)
# print f.read()


# f=urllib.urlopen("http://localhost:1234/locationQuery")
# s=f.read()
# print s
