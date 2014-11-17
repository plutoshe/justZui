var express = require('express');
var router = express.Router();
// var mongodb = require("mongodb");
var mongoose = require('mongoose');
var db = mongoose.connect('localhost', 'justZui');
// mongoose.connect('mongodb://localhost/justZui');
var models = require('../models/comment');


var locationModel = models.location;
//console.log(models.comment);
var commentModel = db.model("comment", models.comment);
//var groupModel = db.model("group", models.comment);
//locationModel.save()
var len = 10;



//commentModel.save(doc);


router.post('/commentQueryNew', function(req, res) {
	var requirement;
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, groupName: req.body.groupName};
	}
	commentModel.findOne(requirement, function (err, data) {
  		if (err) return console.error(err);
  		var result = [];
  		for (var i = data.comment.length - 1; i >= data.comment.length - len; i--) {
  			result.push(data.comment[i]);
  		}
  		res.send(result);
  		
  		res.end();
	});
});

router.post('/commentQueryNext', function(req, res) {
	var requirement;
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		console.log("!");
		requirement = {location : req.body.location, groupType : req.body.groupType, groupName: req.body.groupName};
	}
	commentModel.findOne(requirement,  function (err, data) {

  		if (err) return console.error(err);
  		var result = [];
  		for (var i = req.body.index - 1; i >= req.body.index - len && i >= 0; i--) {
  			result.push(data.comment[i]);
  		}
  		res.send(result);
  		
  		res.end();
	});
});


router.post('/commentQueryNewById', function(req, res) {
	console.log(req.body.id);
	commentModel.findById(req.body.id,  function (err, data) {
		console.log(data);
  		if (err) return console.error(err);
  		var result = [];
  		for (var i = data.comment.length - 1; i >= data.comment.length - len; i--) {
  			result.push(data.comment[i]);
  		}
  		res.send(result);
  		
  		res.end();
	});
});

router.post('/commentQueryNextById', function(req, res) {
	commentModel.findById(req.body.id,  function (err, data) {
  		if (err) return console.error(err);
  		var result = [];
  		for (var i = req.body.index - 1; i >= req.body.index - len && i >= 0; i--) {
  			result.push(data.comment[i]);
  		}
  		res.send(result);
  		
  		res.end();
	});
});



router.post('/commentLike', function(req, res) {
	var requirement;
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, groupName: req.body.groupName};
	}
	commentModel.findOne(requirement,  function (err, data) {
  		if (err) return console.error(err);
  		
  		data.comment[req.body.index].like++;
  		data.save();
  		res.end();
	});
});

router.post('/commentCreate', function(req, res) {
	var requirement;
	
	if (req.body.groupType == 0) {
		requirement = {location : req.body.location, groupType : req.body.groupType};
	}
	else {
		requirement = {location : req.body.location, groupType : req.body.groupType, groupName: req.body.groupName};
	}
	
	commentModel.findOne(requirement, function (err, data) {
  		if (err) return console.error(err);
  		data.comment.push({ index : data.comment.length, body: req.body.content, updateTime: new Date(), like : 0 });
  		data.updateTime = new Date();
  		data.lastComment = req.body.content;
  		data.sum++;
  		data.save();
  		//res.send(data);
  		res.end();
	});
});

router.post('/groupQuery', function(req, res) {
	console.log(req);
	commentModel.find({location : req.body.location, groupType : 1, updateTime : {"$gt": new Date() - 3*24*60*60*1000/*3*24*60*60*1000*/}}, '_id groupName lastComment updateTime', function (err, data) {
		console.log(data);
		if (err) return console.error(err);

  		res.send(data);
  		res.end();
	});
});


router.post('/groupCreate', function(req, res) {
	
	var newGroup = new commentModel({location : req.body.location, comment : [{index : 0, body : req.body.comment}], groupType : 1, groupName : req.body.groupName, lastComment : req.body.comment});
	
	console.log(newGroup);
	newGroup.save();
	res.end();
});

router.get('/locationQuery', function(req, res) {

	commentModel.find({groupType : 0}, '_id location lastComment updateTime', function (err, data) {
		if (err) return console.error(err);

  		res.send(data);
  		res.end();
	});
	
});
module.exports = router;
