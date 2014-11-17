var mongoose = require('mongoose');
var location = new mongoose.Schema ({
    name : String
});

//var entity = new Schema({ index : Number, title : String, body: String, date: Date, like : Number });

var comment = new mongoose.Schema ({
	location : String,
	comment: [{ index : Number,  body: String, date: {type:Date,default:Date.now}, like : {type : Number, default : 0} }],
	updateTime: { type: Date, default: Date.now },
	groupType : Number,
	groupName : String,
	sum : { type : Number, default : 0},
	lastComment : {type:String, default : "无"}
	
});
//mongoose.model('entity', entity);
mongoose.model('location', location);
mongoose.model('comment', comment);

exports.location = mongoose.model('location', location);;
exports.comment = mongoose.model('comment', comment); 
