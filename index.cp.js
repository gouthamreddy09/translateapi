const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const {translate} = require('bing-translate-api');
const morgan = require('morgan');
const db = require('./queries')

const app=express();
const port=3000;

app.use(cors());

app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json());
app.use(morgan('tiny'));


app.get('/',(req,res)=>{
res.send('Hello from MyTranslate World');
});


app.post('/translate', (req,res)=>{

    
    
    if(req.header("Content-Type")!="application/json"){
        res.status(400).send({"message":"Bad Request Only application/json allowed"});
    }
    else{
        
        const book = req.body;
        console.log(book.to)
        console.log( book['to']===undefined);
        if( book['text']===undefined || 
         book['to']===undefined ||
         book['from']===undefined ||
        book['from']=='' ||
        book['to']=='' ||
        book['text']==''){
            console.log(book)
            res.status(400).send({"message":"Bad Request,bad formatted JSON"});
        }
     db.searchText({
    
        "text":book['text'],
    
        "from":book['from'],
    
        "to":book['to']
    },req,res);
    }
})

var server=app.listen(port,()=>console.log(`Hello World app listening on port ${port}!`))

module.exports =server;