var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});

//module.exports = router;
exports.route  = router;

exports.not_found = function(req, res) {
  res.statusCode = 404;
  res.render('index/404', {
    title: '错误'
  });
};

