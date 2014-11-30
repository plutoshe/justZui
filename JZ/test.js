var doc = {name : '第二教学楼'};
locationModel.create(doc, function(error){
    if(error) {
        console.log(error);
    } else {
        console.log('save ok');
    }
    // 关闭数据库链接
    //db.close();
});
var doc = {name : '第一教学楼'};
locationModel.create(doc, function(error){
    if(error) {
        console.log(error);
    } else {
        console.log('save ok');
    }
    // 关闭数据库链接
    //db.close();
});
var doc = {name : '理科教学楼'};
locationModel.create(doc, function(error){
    if(error) {
        console.log(error);
    } else {
        console.log('save ok');
    }
    // 关闭数据库链接
    //db.close();
});
var doc = {name : '第三教学楼'};
locationModel.create(doc, function(error){
    if(error) {
        console.log(error);
    } else {
        console.log('save ok');
    }
    // 关闭数据库链接
    //db.close();
});
var doc = {name : '第四教学楼'};
locationModel.create(doc, function(error){
    if(error) {
        console.log(error);
    } else {
        console.log('save ok');
    }
    // 关闭数据库链接
    //db.close();
});
var doc = {name : '图书馆'};
locationModel.create(doc, function(error){
    if(error) {
        console.log(error);
    } else {
        console.log('save ok');
    }
    // 关闭数据库链接
    //db.close();
});

var doc = {name : '理科一号楼'};
locationModel.create(doc, function(error){
    if(error) {
        console.log(error);
    } else {
        console.log('save ok');
    }
    // 关闭数据库链接
    //db.close();
});
var doc = {name : '理科二号楼'};
locationModel.create(doc, function(error){
    if(error) {
        console.log(error);
    } else {
        console.log('save ok');
    }
    // 关闭数据库链接
    //db.close();
});


var new1=new locationModel({location : 西门, id : 1}); new1.save();
var new2=new locationModel({location : 未名湖, id : 2}); new2.save();
var new3=new locationModel({location : 百讲, id : 3}); new3.save();
var new4=new locationModel({location : 图书馆, id : 4}); new4.save();
var new5=new locationModel({location : 理科楼, id : 5}); new5.save();
var new6=new locationModel({location : 二三四教, id : 6}); new6.save();
var new7=new locationModel({location : 五四, id : 7}); new7.save();
var new8=new locationModel({location : 宿舍, id : 8}); new8.save();
var new9=new locationModel({location : 东门, id : 9}); new9.save();
var new10=new locationModel({location : 其它, id : 0}); new10.save();


var new1=new commentModel({location : "第二教学楼",comment : [], groupType : 0, groupName : ""}); new1.save();
var new2=new commentModel({location : "第一教学楼",comment : [], groupType : 0, groupName : ""}); new2.save();
var new3=new commentModel({location : "理科教学楼",comment : [], groupType : 0, groupName : ""}); new3.save();
var new4=new commentModel({location : "第三教学楼",comment : [], groupType : 0, groupName : ""}); new4.save();
var new5=new commentModel({location : "第四教学楼",comment : [], groupType : 0, groupName : ""}); new5.save();
var new6=new commentModel({location : "图书馆",comment : [], groupType : 0, groupName : ""}); new6.save();
var new7=new commentModel({location : "理科一号楼",comment : [], groupType : 0, groupName : ""}); new7.save();
var new8=new commentModel({location : "理科二号楼",comment : [], groupType : 0, groupName : ""}); new8.save();







 var new1=new commentModel({location : 1, title : "西门", comment : [], lastComment : "", id : 1, groupType : 0}); new1.save();
var new2=new commentModel({location : 2, title : "未名湖", comment : [], lastComment : "", id : 2, groupType : 0}); new2.save();
var new3=new commentModel({location : 3, title : "百讲", comment : [], lastComment : "", id : 3, groupType : 0}); new3.save();
var new4=new commentModel({location : 4, title : "图书馆", comment : [], lastComment : "", id : 4, groupType : 0}); new4.save();
var new5=new commentModel({location : 5, title : "理科楼", comment : [], lastComment : "", id : 5, groupType : 0}); new5.save();
var new6=new commentModel({location : 6, title : "二三四教", comment : [], lastComment : "", id : 6, groupType : 0}); new6.save();
var new7=new commentModel({location : 7, title : "五四", comment : [], lastComment : "", id : 7, groupType : 0}); new7.save();
var new8=new commentModel({location : 8, title : "宿舍", comment : [], lastComment : "", id : 8, groupType : 0}); new8.save();
var new9=new commentModel({location : 9, title : "东门", comment : [], lastComment : "", id : 9, groupType : 0}); new9.save();
var new10=new commentModel({location : 0, title : "其它", comment : [], lastComment : "", id : 0, groupType : 0}); new10.save();

