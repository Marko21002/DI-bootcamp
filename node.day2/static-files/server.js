const express = require('express')

const app = express()
app.listen(3001, ()=>{
    console.log('run on port 3001')
})

//static file

app.use('/')