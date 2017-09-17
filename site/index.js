var express = require('express');
var app = require('express')();
var bodyParser = require('body-parser');
var fs = require('fs');
var PythonShell = require('python-shell');


app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.get('/', function (req, res) {
	res.sendFile( __dirname + '/public/index.html');
});


app.post('/get-prediction', function(req, res) {
	var options = {
		// mode: 'text',
		// pythonPath: 'path/to/python',
		// pythonOptions: ['-u'],
		// scriptPath: 'path/to/my/scripts',
		args: [req.marital_status, req.sex, req.first_name, req.address.latitude, req.address.longitude, req.dob_year, req.product, req.coverage, req.premium, req.plan],
	};

	PythonShell.run((__dirname + '/../models/predict.py'), options, function (err, results) {
		if (err) {
			return res.status(500).send('Error making prediction.');
		};
		return res.send(results[0]);
	});

});

var server = app.listen(8081, function() {
	console.log('Server started.');
});
