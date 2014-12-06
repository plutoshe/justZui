groupType为0时，为大组，即“第一教学楼”这种类型，当为2时，是没升级的小组。
len为显示的吐槽数量，默认为3

Post请求，/commentQueryNew(location(number), groupType(binary),  [title(string)])
查询某个地点某个组的最新的len条评论,title是缺省项，当为0时，不需要输入。
返回一个数组，数组类型为{ index : Number,  like : Number, body: String, date:Date }

Post请求，/commentQueryNext(location(number), groupType(binary),  [title(string)], index(Number))
查询某个地点某个组的某条吐槽之后的len条吐槽,title是缺省项，当为0时，不需要输入，index表示吐槽的编号。
返回一个数组,数组类型为{ index : Number, like : Number,  body: String, date:Date }


Post请求，/commentLike(location(number), groupType(Number), [title(String)], index(Number))
为某个组的某条吐槽点赞title是缺省项，当为0时，不需要输入

Post请求，/commentCreate(location(number), groupType(Number), [title(String)], content)
为某个组添加吐槽，groupName是缺省项，当为0时，不需要输入，返回{indexNew: Number}

Post请求，/groupQuery(location(number))
查询某个大组的所有小组，返回{_id:String, title : String, groupType : Number, lastComment : String, updateTime : Date}

Post请求，/groupCreate(location(number),  title(String))
为某个大组创建小组，

Get请求，/locationQuery()
查询所有大组，返回{_id:String, location : Number, title : String, groupType(Number), lastComment : String, updateTime : Date}



＃＃＃＃＃＃＃＃＃＃＃＃＃＃新加功能，可不用＃＃＃＃＃＃＃＃＃＃＃＃＃＃


post请求, /groupExist(location(number), title(String))
查看一个小组是否存在
返回{ exist : Number}，0为不存在，1为存在

post请求, /groupUpgrade(location(number), title(String))
为一个小组升级

post请求, /groupUpgrade(location(number), title(String))
为一个小组降级

post请求，/locationCreate(location(number), locationName(String))
创建一个新的大组，location为编号，locationName为名字

post请求，/locationUpdate(location(number), locationName(String))
更新一个新的大组的名字，location为编号，locationName为名字



＃＃＃＃＃＃＃＃＃＃＃＃新要求的三个功能＃＃＃＃＃＃＃＃＃＃＃＃＃＃

Post请求，/commentDislike(location(number), groupType(Number), [title(String)], index(Number))
为某个组的某条吐槽点赞title是缺省项，当为0时，不需要输入

Post请求，/commentQuerySection(location(number), groupType(binary),  [title(string)], indexNew(Number), indexOld(Number))
查询某个地点某个组的一段区间的吐槽,title是缺省项，当为0时，不需要输入，indexNew表示最新的index, indexOld表示最旧的区间，indexNew>indexOld。
返回一个数组,数组类型为{ index : Number, like : Number,  body: String, date:Date }

Post请求，/commentQueryUpdated(location(number), groupType(binary),  [title(string)], index(Number))
查询某个地点某个组的某条吐槽之后更新的吐槽,title是缺省项，当为0时，不需要输入，index表示查询吐槽的编号。
返回一个数组,数组类型为{ index : Number,  like : Number, body: String, date:Date }


＃＃＃＃＃＃＃＃＃＃＃＃新加的一个功能12/04/2014＃＃＃＃＃＃＃＃＃＃＃＃＃＃
Get请求，versionGet()
返回版本号{ version : String }


＃＃＃＃＃＃＃＃＃＃＃＃＃preference module 12/06/2014＃＃＃＃＃＃＃＃＃＃＃＃＃＃

Post请求，/commentLikeQuerySection(location(number), groupType(binary),  [title(string)], indexNew(Number), indexOld(Number))
查询某个地点某个组的一段区间的吐槽的赞,title是缺省项，当为0时，不需要输入，indexNew表示最新的index, indexOld表示最旧的区间，indexNew>indexOld。
返回一个数组,数组类型为{ index : Number,  body: String, date:Date }

Post请求，/commentLikeQueryNew(location(number), groupType(binary),  [title(string)])
查询某个地点某个组的最新的len条吐槽的赞,title是缺省项，当为0时，不需要输入。
返回一个数组，数组类型为{ index : Number,  like : Number, body: String, date:Date }

Post请求，/commentLikeQueryNext(location(number), groupType(binary),  [title(string)], index(Number))
查询某个地点某个组的某条吐槽之后的len条吐槽的赞,title是缺省项，当为0时，不需要输入，index表示吐槽的编号。
返回一个数组,数组类型为{ index : Number, like : Number }


Post请求，/commentLikeQueryUpdated(location(number), groupType(binary),  [title(string)], index(Number))
查询某个地点某个组的某条吐槽之后更新的吐槽的赞,title是缺省项，当为0时，不需要输入，index表示查询吐槽的编号。
返回一个数组,数组类型为{ index : Number,  like : Number }




