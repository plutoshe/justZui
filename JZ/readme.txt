groupTypeΪ0ʱ��Ϊ���飬������һ��ѧ¥���������ͣ���Ϊ2ʱ����û������С�顣
lenΪ��ʾ���²�������Ĭ��Ϊ3

Post����/commentQueryNew(location(number), groupType(binary),�0�2 [title(string)])
��ѯĳ���ص�ĳ��������µ�len������,title��ȱʡ���Ϊ0ʱ������Ҫ���롣
����һ�����飬��������Ϊ{ index : Number,  body: String, date:Date }

Post����/commentQueryNext(location(number), groupType(binary),�0�2 [title(string)], index(Number))
��ѯĳ���ص�ĳ�����ĳ���²�֮���len���²�,title��ȱʡ���Ϊ0ʱ������Ҫ���룬index��ʾ�²۵ı�š�
����һ������,��������Ϊ{ index : Number,  body: String, date:Date }


Post����/commentLike(location(number), groupType(Number), [title(String)], index(Number))
Ϊĳ�����ĳ���²۵���title��ȱʡ���Ϊ0ʱ������Ҫ����

Post����/commentCreate(location(number), groupType(Number), [title(String)])
Ϊĳ��������²ۣ�groupName��ȱʡ���Ϊ0ʱ������Ҫ����

Post����/groupQuery(location(number))
��ѯĳ�����������С�飬����{id:String, title : String, groupType : Number, lastComment : String, updateTime : Date}

Post����/groupCreate(location(String),�0�2 title(String), commment(String))
Ϊĳ�����鴴��С�鲢����һ���²�

Get����/locationQuery()
��ѯ���д��飬����{id:String, location : String, groupType(Number), lastComment : String, updateTime : Date}


