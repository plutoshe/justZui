var mongoose = require('mongoose');
// var location = new mongoose.Schema ({
//     name : String,
//     id : Number 
// });

//var entity = new Schema({ index : Number, title : String, body: String, date: Date, like : Number });

var comment = new mongoose.Schema ({
        location : Number,
        comment: [{ index : Number,  body: String, date: {type:Date,default:Date.now}, like : {type : Number, default : 0} }],
        updateTime: { type: Date, default: Date.now },
        groupType : Number,
        title : {type : String, default : 0},
        sum : { type : Number, default : 0},
        lastComment : {type:String, default : ""}

});


var version = new mongoose.Schema ({
        version : String,
        download : Number
});

//mongoose.model('entity', entity);
// mongoose.model('newLocation', location);
mongoose.model('newComment', comment);
mongoose.model('newVersion', version);


// exports.location = mongoose.model('newLocation', location);;
exports.comment = mongoose.model('newComment');
exports.newVersion = mongoose.model('newVersion');


