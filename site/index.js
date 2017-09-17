var express = require('express');
var app = require('express')();
var bodyParser = require('body-parser');
var fs = require('fs');
var PythonShell = require('python-shell');


app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.get('/', function (req, res) {
	console.log('requested root');
	res.sendFile( __dirname + '/public/index.html');
});


app.post('/get-prediction', function(req, res) {
	var options = {
		// mode: 'text',
		 pythonPath: '/usr/bin/python3',
		// pythonOptions: ['-u'],
		// scriptPath: 'path/to/my/scripts',
		args: [req.body.first_name, req.body.sex, req.body.address.latitude, req.body.address.longitude, req.body.dob_year, req.body.product, req.body.coverage, req.body.premium, req.body.plan],
	};

	PythonShell.run(('../models/predict.py'), options, function (err, results) {
		if (err) {
			console.log(err);
			return res.status(500).send('Error making prediction.');
		};
		return res.send(results[0]);
	});

});

var server = app.listen(80, function() {
	console.log('Server started.');
});
