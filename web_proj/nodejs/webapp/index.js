// __loading home page html file__ 
const {readFileSync}=require('fs')
const cont=readFileSync('./home.html','ascii')

// __creating server and sending response__
const http=require('http')
const server=http.createServer((req,res)=>{
    const text='<h1>UNDER CONSTRUCTION</H1>'
    if (req.url==='/'||req.url==='/home/'){
        res.write(cont)
    }
    if (req.url==='/services/'){
        res.write(text)
    }
    if (req.url==='/about/'){
        res.write(text)
    }
    if (req.url==='/contact/'){
        res.write(text)
    }
    if (req.url==='/help/'){
        res.write(text)
    }
    
    res.end()
})
server.listen(5000)