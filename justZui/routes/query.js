var groupPeriod = 3*24*60*60*1000;
var newTrans = [0,1,2,3,4,5];
var trans=[0,5,6,8,4,3,9,1,7,2];
var version = '1.14';

var express = require('express');
var router = express.Router();
// var mongodb = require("mongodb");
var mongoose = require('mongoose');
var db = mongoose.connect('localhost', 'justZui');
// mongoose.connect('mongodb://localhost/justZui');
var models = require('../models/comment');

// var locationModel = models.location;
//console.log(models.comment);
var commentModel = models.comment;//db.model("comment", models.comment);
// var versionModel = models.newVersion;
var versionModel = models.newVersion;
// var versionModel = mongoose.model("version");
//var groupModel = db.model("group", models.comment);
//locationModel.save()
var len = 10;
 //commentModel.find({groupType : {"$ge" : 0}}).remove().exec();
// /commentModel.save(doc);

// var inW = new versionModel();
// inW.version = 1.14;
// inW.download = 0;
// inW.save();

router.post('/versionUpdate', function(req, res){
	versionModel.findOne({isCurrent:1},function (err,data){
		data.isCurrent = 0;
		data.save();
		newVersion = new versionModel();
		newVersion.version = req.body.version;
		newVersion.isCurrent = 1;
		newVersion.download = 0;
		newVersion.update_content = req.body.update_content;
		newVersion.locationNum = data.locationNum;
		newVersion.save();
		res.end();
	});
});

router.get('/versionCurrentDelete', function(req, res){
	versionModel.find({isCurrent:1},function (err,data){
		for (var i = 0; i < data.length; i++) {
			data[i].isCurrent = 0;
			data[i].save();
		}
		
		res.end();
	});
});


router.post('/versionCreate', function(req, res) {
	newVersion = new versionModel();
	newVersion.version = req.body.version;
	newVersion.isCurrent = 1;
	newVersion.download = 0;
	newVersion.update_content = req.body.update_content;
	newVersion.locationNum = req.body.locationNum;
	// console.log(req.body.update_content);
	newVersion.save();
	res.end();
});

        
        


router.get('/versionGet', function(req, res) {
	versionModel.findOne({isCurrent : 1}, function (err,data){
		res.send(data);
		res.end();
	});
});

router.post('/downloadUpdate', function(req, res){
	versionModel.findOne({version:req.body.version}, function (err,data){		
		if (data) {
			data.download++;
			data.save();
		}
		
		res.end();
	});
});

router.post('/specificVersion', function(req, res){
	versionModel.findOne({version:req.body.version}, function (err,data){
		// console.log(data);
		res.send(data);
		res.end();
	});
});





router.post('/commentQueryNew', function(req, res) {
	var requirement;
	//console.log(req);
	//console.log(req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	commentModel.findOne(requirement, function (err, data) {
  		if (err) return console.error(err);
  		var result = [];
  		if (data) {
	  		for (var i = data.comment.length - 1; i >= data.comment.length - len && i >= 0; i--) {
	  			result.push(data.comment[i]);
	  		}
	  	}
  		res.send(result);
  		
  		res.end();
	});
});

router.post('/commentQueryNext', function(req, res) {
	var requirement;
	//console.log(req);
	// console.log(req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	commentModel.findOne(requirement,  function (err, data) {

  		if (err) return console.error(err);
  		var result =[];
  		if (data) {
	  		for (var i = req.body.index - 1; i >= req.body.index - len && i >= 0; i--) {
	  			result.push(data.comment[i]);
	  		}
	  	}
  		res.send(result);
  		
  		res.end();
	});
});




router.post('/commentQuerySection', function(req, res) {
	var requirement;
	//console.log(req);
	//console.log("!", req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	
	commentModel.findOne(requirement,  function (err, data) {

  		if (err) return console.error(err);
  		var result =[];
  		if (data) {

	  		for (var i = req.body.indexNew; i >= req.body.indexOld && i >= 0; i--) {
	  			result.push(data.comment[i]);
	  		}
	  	}
  		res.send(result);
  		
  		res.end();
	});
});






router.post('/commentQueryUpdated', function(req, res) {
	var requirement;
	//console.log(req);
	// console.log(req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	commentModel.findOne(requirement,  function (err, data) {
		// console.log(requirement);
		// console.log(data);
  		if (err) return console.error(err);
  		var result =[];
  		if (data) {
	  		for (var i = data.comment.length - 1; i >= req.body.index && i >= 0; i--) {
	  			result.push(data.comment[i]);
	  		}
	  	}
	  	// console.log(result);
  		res.send(result);
  		
  		res.end();
	});
});


// router.post('/commentQueryNewById', function(req, res) {
// 	console.log(req.body.id);
// 	commentModel.findById(req.body.id,  function (err, data) {
// 		console.log(data);
//   		if (err) return console.error(err);
//   		var result = {data:[]};
//   		for (var i = data.comment.length - 1; i >= data.comment.length - len && i >= 0; i--) {
//   			result.data.push(data.comment[i]);
//   		}
//   		res.send(result);
  		
//   		res.end();
// 	});
// });

// router.post('/commentQueryNextById', function(req, res) {
// 	commentModel.findById(req.body.id,  function (err, data) {
//   		if (err) return console.error(err);
//   		var result = {data:[]};
//   		for (var i = req.body.index - 1; i >= req.body.index - len && i >= 0; i--) {
//   			result.data.push(data.comment[i]);
//   		}
//   		res.send(result);
  		
//   		res.end();
// 	});
// });



router.post('/commentLike', function(req, res) {
	var requirement;
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	commentModel.findOne(requirement,  function (err, data) {
  		if (err) return console.error(err);
  		if (data) {
	  		data.comment[req.body.index].like++;
	  		data.save();
	  		res.end();
	  	}
	});
});


router.post('/commentDislike', function(req, res) {
	var requirement;
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	commentModel.findOne(requirement,  function (err, data) {
  		if (err) return console.error(err);
  		if (data) {
	  		data.comment[req.body.index].like--;
	  		data.save();
	  		res.end();
	  	}
	});
});

router.post('/commentCreate', function(req, res) {
	var requirement;
	console.log(req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	console.log(requirement);
	
	commentModel.findOne(requirement, function (err, data) {
  		if (err) return console.error(err);
  		 console.log(data);
  		var indexPre;
  		if (data) {
  			indexPre = {indexNew : data.comment.length};

  			data.comment.push({ mark : req.body.mark, index : data.comment.length, body: req.body.content, updateTime: new Date(), like : 0 });

	  		data.updateTime = new Date();
	  		data.lastComment = req.body.content;
	  		data.sum++;
	  		data.save();
	  		res.send(indexPre);
  			res.end();
	  		

	  	} else res.end();
	  	
  		//res.send(data);
  		
	});
});

router.post('/groupQuery', function(req, res) {
	// console.log(req);
	commentModel.find({location : req.body.location, groupType : 2, updateTime : {"$gt": new Date() - groupPeriod/*3*24*60*60*1000*/}}, '_id title groupType lastComment updateTime').sort({updateTime : 1}).exec(function (err, data) {
		// console.log(data);
		if (err) return console.error(err);

  		res.send(data);
  		res.end();
	});
});


router.post('/groupExist', function(req, res) {
	commentModel.findOne({location : req.body.location, title : req.body.title}, function(err, data) {
		if (err) return console.error(err);
		if (data) res.send({ exist : 1}); else res.send({ exist : 0});
		res.end();
	});
});


router.post('/groupCreate', function(req, res) {
	
	commentModel.findOne({ location : req.body.location, title : req.body.title}, function(err, data) {
		var returnJson;
		
		if (data) {
			console.log("!!");
			returnJson = {status : "existed"};
			data.updateTime = new Date();
			data.save();
			res.send(returnJson);
			res.end();
		}
		else {
			returnJson = {status : "success"};
			var newGroup = new commentModel({sum : 0, location : req.body.location, comment : [], groupType : 2, title : req.body.title, lastComment : ""});
			newGroup.save();
			res.send(returnJson);
			res.end();
		}
		
	});
	// console.log(newGroup);
});

router.get('/locationQuery', function(req, res) {

	 commentModel.find({groupType : {"$lt" : 2}}, '_id location subclass title groupType lastComment updateTime').sort({location : 1}).exec(function (err, data) {
	 	if (err) return console.error(err);
	 	
	 	// var sdata = new Array();

	 	// for (var i = 0; i < newTrans.length; i++) 
	 	// 	sdata.push(data[newTrans[i]]);
   // 		res.send(sdata);
   		var sdata =  new Array();
   		for (var c = 0; c < 4; c++)
	   		for (var i = 0; i < data.length; i++)
	   			if (data[i].subclass == c)
	   				sdata.push(data[i]);
   		res.send(sdata);
   		
   		res.end();
	 });
	
});

router.post('/specificLocationQuery', function(req, res) {
	// console.log(req);
	
	commentModel.find({subclass : req.body.subclass, groupType : 0}, '_id location subclass title groupType lastComment updateTime').sort({updateTime : 1}).exec(function (err, data) {
		// console.log(data);
		if (err) return console.error(err);

  		res.send(data);
  		res.end();
	});
});



// router.post('/locationCreate', function(req, res) {
// 	var newGroup = new commentModel({location : req.body.location, comment : [], groupType : 0, title : req.body.locationName, lastComment : ""});
// 	newGroup.save();
// 	res.end();
// });

router.post('/locationCreate', function(req, res) {
	versionModel.findOne({isCurrent : 1}, function(err, data) {
		var newGroup = new commentModel({subclass : 0, location : data.locationNum+1, comment : [], groupType : 0, title : req.body.locationName, lastComment : ""});
		data.locationNum++;
		data.save();
		newGroup.save();
		res.end();
	});
});


router.post('/newLocationCreate', function(req, res) {
	versionModel.findOne({isCurrent : 1}, function(err, data) {
		var newGroup = new commentModel({subclass : req.body.subclass, location : data.locationNum+1, comment : [], groupType : 0, title : req.body.locationName, lastComment : ""});
		data.locationNum++;
		data.save();
		
		newGroup.save();
		res.end();
	});
});

router.post('/locationUpdate', function(req, res) {
	commentModel.findOne({location : req.body.location, groupType : 0}, function(err,data) {
		data.title = req.body.locationName;
		data.save();
		res.end();
	})
});

router.post('/groupUpgrade', function(req, res) {
	//console.log(req.body.location, req.body.title);
	commentModel.findOne({location : req.body.location, groupType : 2,title : req.body.title}, function(err,data) {
		if (data) {
			data.groupType = 1;
			data.save();

		}
		res.end();
	});
});

router.post('/groupDegrade', function(req, res) {
	commentModel.findOne({location : req.body.location, groupType : 1,title : req.body.title}, function(err,data) {
		if (data) {
			data.groupType = 2;
			data.save();
		}
		res.end();
	});
});





// Like Module



router.post('/commentLikeQueryNew', function(req, res) {
	var requirement;
	//console.log(req);
	//console.log(req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	commentModel.findOne(requirement, function (err, data) {
  		if (err) return console.error(err);
  		var result = [];
  		if (data) {
	  		for (var i = data.comment.length - 1; i >= data.comment.length - len && i >= 0; i--) {
	  			result.push({mark : data.comment[i]['mark'], index:data.comment[i]['index'], like :data.comment[i]['like']});
	  		}
	  	}
  		res.send(result);
  		
  		res.end();
	});
});

router.post('/commentLikeQueryNext', function(req, res) {
	var requirement;
	//console.log(req);
	// console.log(req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	commentModel.findOne(requirement,  function (err, data) {

  		if (err) return console.error(err);
  		var result =[];
  		if (data) {
			// console.log(data.comment);
	  		for (var i = req.body.index - 1; i >= req.body.index - len && i >= 0; i--) {
	  			result.push({mark : data.comment[i]['mark'], index:data.comment[i]['index'], like :data.comment[i]['like']});
	  		}
	  	}
  		res.send(result);
  		
  		res.end();
	});
});




router.post('/commentLikeQueryUpdated', function(req, res) {
	var requirement;
	//console.log(req);
	// console.log(req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	commentModel.findOne(requirement,  function (err, data) {

  		if (err) return console.error(err);
  		var result =[];
  		if (data) {
	  		for (var i = data.comment.length - 1; i >= req.body.index && i >= 0; i--) {
	  			result.push({mark : data.comment[i]['mark'], index:data.comment[i]['index'], like :data.comment[i]['like']});
	  		}
	  	}
  		res.send(result);
  		
  		res.end();
	});
});

router.post('/commentLikeQuerySection', function(req, res) {
	var requirement;
	//console.log(req);
	//console.log("!", req.body);
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, title: req.body.title};
	}
	
	commentModel.findOne(requirement,  function (err, data) {

  		if (err) return console.error(err);
  		var result =[];
  		if (data) {

	  		for (var i = req.body.indexNew; i >= req.body.indexOld && i >= 0; i--) {
	  			result.push({mark : data.comment[i]['mark'], index:data.comment[i]['index'], like :data.comment[i]['like']});
	  		}
	  	}
  		res.send(result);
  		
  		res.end();
	});
});


module.exports = router;
