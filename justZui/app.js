var express = require('express');
var path = require('path');
var favicon = require('static-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var http = require("http");

var routes = require('./routes/index');
var users = require('./routes/users');
var query = require('./routes/query');
var MongoStore = require('connect-mongo');

var app = express();
console.log("begin");
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.set('port',process.env.PORT || 1234)
app.use(favicon());
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

//app.use('/', routes.route);
//app.use('/users', users);

//download control
app.post('/versionUpdate', query);
app.post('/versionCreate', query);
app.post('/specificVersion', query);
app.post('/downloadUpdate', query);
app.get('/versionCurrentDelete',query);
// app.get('/getDownload', query);
app.get('/versionGet', query);
// comments query
app.post('/commentQueryNew', query);
app.post('/commentQueryNext', query);
app.post('/commentQuerySection', query);
app.post('/commentQueryUpdated', query);
// coments preference query
app.post('/commentLikeQueryNew', query);
app.post('/commentLikeQueryNext', query);
app.post('/commentLikeQuerySection', query);
app.post('/commentLikeQueryUpdated', query);


// comments query by id
app.post('/commentQueryNewById', query);
app.post('/commentQueryNextById', query);

// commments preference alteration
app.post('/commentLike', query);
app.post('/commentDislike', query);

// comments create
app.post('/commentCreate', query);

// large group opreation
app.post('/locationCreate', query);
app.post('/newlocationCreate', query);
app.post('/specificLocationQuery', query);
app.post('/locationUpdate', query);
app.get('/locationQuery', query);

// mini group opreation
app.post('/groupExist', query);
app.post('/groupQuery', query);
app.post('/groupCreate', query);
app.post('/groupUpgrade', query);
app.post('/groupDegrade', query);

// version query
app.get('/versionGet', query);

app.all('*', routes.not_found);

/// catch 404 and forwarding to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});
// app.use(express.session({
//     //secret: config.cookieSecret,
//     Store: new MongoStore({
//       db: 'justZui'
  
  
//     })
//   }));

/// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});

//console.log("!");
module.exports = app;
http.createServer(app).listen(app.get('port'), function(){
    console.log('Express server listening on port ' + app.get('port'));
});       
