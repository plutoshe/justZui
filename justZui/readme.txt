groupTypeΪ0ʱ��Ϊ���飬������һ��ѧ¥���������ͣ���Ϊ2ʱ����û������С�顣
lenΪ��ʾ���²�������Ĭ��Ϊ3

Post����/commentQueryNew(location(number), groupType(binary),�0�2 [title(string)])
��ѯĳ���ص�ĳ��������µ�len������,title��ȱʡ���Ϊ0ʱ������Ҫ���롣
����һ�����飬��������Ϊ{ index : Number,  like : Number, body: String, date:Date }

Post����/commentQueryNext(location(number), groupType(binary),�0�2 [title(string)], index(Number))
��ѯĳ���ص�ĳ�����ĳ���²�֮���len���²�,title��ȱʡ���Ϊ0ʱ������Ҫ���룬index��ʾ�²۵ı�š�
����һ������,��������Ϊ{ index : Number, like : Number,  body: String, date:Date }


Post����/commentLike(location(number), groupType(Number), [title(String)], index(Number))
Ϊĳ�����ĳ���²۵���title��ȱʡ���Ϊ0ʱ������Ҫ����

Post����/commentCreate(location(number), groupType(Number), [title(String)], content)
Ϊĳ��������²ۣ�groupName��ȱʡ���Ϊ0ʱ������Ҫ���룬����{indexNew: Number}

Post����/groupQuery(location(number))
��ѯĳ�����������С�飬����{_id:String, title : String, groupType : Number, lastComment : String, updateTime : Date}

Post����/groupCreate(location(number),�0�2 title(String))
Ϊĳ�����鴴��С�飬

Get����/locationQuery()
��ѯ���д��飬����{_id:String, location : Number, title : String, groupType(Number), lastComment : String, updateTime : Date}



�����������������������������¼ӹ��ܣ��ɲ��ã���������������������������


post����, /groupExist(location(number), title(String))
�鿴һ��С���Ƿ����
����{ exist : Number}��0Ϊ�����ڣ�1Ϊ����

post����, /groupUpgrade(location(number), title(String))
Ϊһ��С������

post����, /groupUpgrade(location(number), title(String))
Ϊһ��С�齵��

post����/locationCreate(location(number), locationName(String))
����һ���µĴ��飬locationΪ��ţ�locationNameΪ����

post����/locationUpdate(location(number), locationName(String))
����һ���µĴ�������֣�locationΪ��ţ�locationNameΪ����



��������������������������Ҫ����������ܣ���������������������������

Post����/commentDislike(location(number), groupType(Number), [title(String)], index(Number))
Ϊĳ�����ĳ���²۵���title��ȱʡ���Ϊ0ʱ������Ҫ����

Post����/commentQuerySection(location(number), groupType(binary),�0�2 [title(string)], indexNew(Number), indexOld(Number))
��ѯĳ���ص�ĳ�����һ��������²�,title��ȱʡ���Ϊ0ʱ������Ҫ���룬indexNew��ʾ���µ�index, indexOld��ʾ��ɵ����䣬indexNew>indexOld��
����һ������,��������Ϊ{ index : Number, like : Number,  body: String, date:Date }

Post����/commentQueryUpdated(location(number), groupType(binary),�0�2 [title(string)], index(Number))
��ѯĳ���ص�ĳ�����ĳ���²�֮����µ��²�,title��ȱʡ���Ϊ0ʱ������Ҫ���룬index��ʾ��ѯ�²۵ı�š�
����һ������,��������Ϊ{ index : Number,  like : Number, body: String, date:Date }


�������������������������¼ӵ�һ������12/04/2014����������������������������
Get����versionGet()
���ذ汾��{ version : String }


��������������������������preference module 12/06/2014����������������������������

Post����/commentLikeQuerySection(location(number), groupType(binary),�0�2 [title(string)], indexNew(Number), indexOld(Number))
��ѯĳ���ص�ĳ�����һ��������²۵���,title��ȱʡ���Ϊ0ʱ������Ҫ���룬indexNew��ʾ���µ�index, indexOld��ʾ��ɵ����䣬indexNew>indexOld��
����һ������,��������Ϊ{ index : Number, like : Number }

Post����/commentLikeQueryNew(location(number), groupType(binary),�0�2 [title(string)])
��ѯĳ���ص�ĳ��������µ�len���²۵���,title��ȱʡ���Ϊ0ʱ������Ҫ���롣
����һ�����飬��������Ϊ{ index : Number,  like : Number}

Post����/commentLikeQueryNext(location(number), groupType(binary),�0�2 [title(string)], index(Number))
��ѯĳ���ص�ĳ�����ĳ���²�֮���len���²۵���,title��ȱʡ���Ϊ0ʱ������Ҫ���룬index��ʾ�²۵ı�š�
����һ������,��������Ϊ{ index : Number, like : Number }


Post����/commentLikeQueryUpdated(location(number), groupType(binary),�0�2 [title(string)], index(Number))
��ѯĳ���ص�ĳ�����ĳ���²�֮����µ��²۵���,title��ȱʡ���Ϊ0ʱ������Ҫ���룬index��ʾ��ѯ�²۵ı�š�
����һ������,��������Ϊ{ index : Number,  like : Number }




===============================12/23/2014===============================
===============================version4.1===============================
updated Weibo, Weiming regular updater


===============================12/27/2014===============================
===============================version4.1===============================
########
Updated Version Module
current version type : { isCurrent : Number, version : String, download : Number, update_content : String, locationNum : Number }

Post request:
1.versionUpdate
in : { version : String, update_content : String }
out : None
function : ���°汾

2.downloadUpdate
in : { version : String }
out : None
function : ����һ���汾����������

3.specificVersion
in : { version : String }
out : { locationNum : Number, isCurrent : Number, version : String, download : Number, update_content : String } 
function: �õ��ض��汾����Ϣ

4.versionCreate
in : { version : String, update_content : String, locationNum : Number }
out : None
function: �����°汾


Get request:
1.versionGet
in : None
out : { locationNum : Number, isCurrent : Number, version : String, download : Number, update_content : String }
function : �õ���ǰ�汾��Ϣ



########
Updated Comment and Locatio Module

1.About comment 
current comment type : { mark : Number, index : Number, like : Number,  body: String, date:Date }
Description : 
a) ����commentQuery��commentLikeQuey��post����ķ��ص����۶���һ������mark���������۵�����

b) commentCreate��post������Ҫ�������м���mark����


2.About group 
Լ������Ϊ(��subclass��ʾ)
0:������Ⱥ
1:����BBSȺ
2:ֱ��BBSȺ
3:����Ⱥ

a) create
<1>.������Ⱥ����
Post request : locationCreate
in : { LocationName : String}
out : None

<2>.�����Ⱥ����
Post request : newLocationCreate
in : {subclass : Number, LocationName : String}
out : None

b) ��ѯ
����specificLargeGroupQuery���󣬲�ѯ�ض�subclass�Ĵ�Ⱥ
in : {subclass : Number }
out : {_id:String, subclass : Number, title : String, groupType : Number, lastComment : String, updateTime : Date}










