
var http = require('http');


var data = {
    locationName : "理科教学楼",
    comment : "放屁",
    groupName : "上毛概的进来"
};


// //var userJson=JSON.stringify(user);
// //varuserString='data='+userjson;//这种格式在服务器端解析的时候可解析为req.body.datda
// var userString = JSON.stringify(user);//转换为json字符格式,在服务器端直接解析req.body
// var headers = {
//     'Content-Type': 'application/json',
//     //如果使用的是varuserString='data='+userjson格式应将'Content-Type':设为'application/x-www-form-urlencoded'//form表单格式
//     'Content-Length': userString.length
// };

// var options = {
//     host: 'localhost',//'162.105.74.252',//主机：切记不可在前面加上HTTP://
//     port: 55555,//端口号
//     path: '/groupCreate',//路径
    
//     headers: headers,
//     method: 'POST'//提交方式
// };
// console.log("prepared");
// var body = "";
// var req = http.request(options, function ( res) {

// //    console.log('STATUS: ' + res.statusCode);
// //    console.log('HEADERS: ' + JSON.stringify(res.headers));
//     //  res.setEncoding('utf8');
//     //console.log(res);
//     res.on('data', function (data) {
//         body+=data;
//         //console.log('response : ' ,message);
//         //var ret= eval('(' + message + ')');
//     });
//     res.on('end', function () { req.send(200, body); console.log(body) });  

// });


// // write data to request body
// req.write(userString);//向req.body里写入数据
// req.end();


// exports.sendEmail = function (req, res) {



    data = JSON.stringify(data);
    console.log(data);
    var opt = {
        method: "POST",
        host: "localhost",
        port: 1234,
        path: "/groupCreate",
        headers: {
            "Content-Type": 'application/json',
            "Content-Length": data.length
        }
    };

    var req = http.request(opt, function (serverFeedback) {
        if (serverFeedback.statusCode == 200) {
            var body = "";
            serverFeedback.on('data', function (data) { body += data; })
                          .on('end', function () { res.send(200, body); });
        }
        else {
            res.send(500, "error");
        }
    });
    req.write(data + "\n");
    req.end();
