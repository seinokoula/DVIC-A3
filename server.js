const express = require('express')
const app = express()
const port = 3000
const IP = require('ip');
const ipAddress = IP.address();
let bodyParser = require('body-parser');


let scores = 0;

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
}
)
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send({ "score": scores })
})

app.post('/scores', (req, res) => {
    console.log(req.body)
    res.send({ "name": ipAddress })
})

app.post('/', (req, res) => {
    scores = req.body;
    console.log(scores);
    res.json(scores)
});

app.use(express.static('public'))

app.listen(port, () => {
    console.log(`Example app listening at http://${ipAddress}:${port}`)
})

