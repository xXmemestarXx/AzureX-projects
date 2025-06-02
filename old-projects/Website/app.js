const path = require ('path');
const express = require('express');
const app = express();
const port = 3000

//Specifing folder for css and stuff
//Image and Css files
app.use(express.static(__dirname + '/public/'));
//Specifing where JS files are 
app.use(express.static(__dirname + '/JS/'));
//Rerouting
app.get('/', (req, res) => res.sendFile(path.join(__dirname + '/views/index.html')));

app.get('/memes', (req, res) => res.sendFile(path.join(__dirname + '/views/memes.html')));

app.get('/about', (req, res) => res.sendFile(path.join(__dirname + '/views/about.html')));

app.listen(port, () => console.log(`Listening on 127.0.0.1 with port ${port}!`));
