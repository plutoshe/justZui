groupType为0时，为大组，即“第一教学楼”这种类型，当为2时，是没升级的小组。
len为显示的吐槽数量，默认为3

Post请求，/commentQueryNew(location(number), groupType(binary),  [title(string)])
查询某个地点某个组的最新的len条评论,title是缺省项，当为0时，不需要输入。
返回一个数组，数组类型为{ index : Number,  body: String, date:Date }

Post请求，/commentQueryNext(location(number), groupType(binary),  [title(string)], index(Number))
查询某个地点某个组的某条吐槽之后的len条吐槽,title是缺省项，当为0时，不需要输入，index表示吐槽的编号。
返回一个数组,数组类型为{ index : Number,  body: String, date:Date }


Post请求，/commentLike(location(number), groupType(Number), [title(String)], index(Number))
为某个组的某条吐槽点赞title是缺省项，当为0时，不需要输入

Post请求，/commentCreate(location(number), groupType(Number), [title(String)])
为某个组添加吐槽，groupName是缺省项，当为0时，不需要输入

Post请求，/groupQuery(location(number))
查询某个大组的所有小组，返回{id:String, title : String, groupType : Number, lastComment : String, updateTime : Date}

Post请求，/groupCreate(location(String),  title(String), commment(String))
为某个大组创建小组并带有一条吐槽

Get请求，/locationQuery()
查询所有大组，返回{id:String, location : String, groupType(Number), lastComment : String, updateTime : Date}


