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



var new1=new commentModel({location : "第二教学楼",comment : [], groupType : 0, groupName : ""}); new1.save();
var new2=new commentModel({location : "第一教学楼",comment : [], groupType : 0, groupName : ""}); new2.save();
var new3=new commentModel({location : "理科教学楼",comment : [], groupType : 0, groupName : ""}); new3.save();
var new4=new commentModel({location : "第三教学楼",comment : [], groupType : 0, groupName : ""}); new4.save();
var new5=new commentModel({location : "第四教学楼",comment : [], groupType : 0, groupName : ""}); new5.save();
var new6=new commentModel({location : "图书馆",comment : [], groupType : 0, groupName : ""}); new6.save();
var new7=new commentModel({location : "理科一号楼",comment : [], groupType : 0, groupName : ""}); new7.save();
var new8=new commentModel({location : "理科二号楼",comment : [], groupType : 0, groupName : ""}); new8.save();
