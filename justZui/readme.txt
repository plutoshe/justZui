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
����һ������,��������Ϊ{ index : Number,  body: String, date:Date }

Post����/commentLikeQueryNew(location(number), groupType(binary),�0�2 [title(string)])
��ѯĳ���ص�ĳ��������µ�len���²۵���,title��ȱʡ���Ϊ0ʱ������Ҫ���롣
����һ�����飬��������Ϊ{ index : Number,  like : Number, body: String, date:Date }

Post����/commentLikeQueryNext(location(number), groupType(binary),�0�2 [title(string)], index(Number))
��ѯĳ���ص�ĳ�����ĳ���²�֮���len���²۵���,title��ȱʡ���Ϊ0ʱ������Ҫ���룬index��ʾ�²۵ı�š�
����һ������,��������Ϊ{ index : Number, like : Number }


Post����/commentLikeQueryUpdated(location(number), groupType(binary),�0�2 [title(string)], index(Number))
��ѯĳ���ص�ĳ�����ĳ���²�֮����µ��²۵���,title��ȱʡ���Ϊ0ʱ������Ҫ���룬index��ʾ��ѯ�²۵ı�š�
����һ������,��������Ϊ{ index : Number,  like : Number }




