const http=require('http')
const {readFileSync}=require('fs')

const style=readFileSync('./app/theme.css')
const server=http.createServer((req,res)=>{
    const url=req.url;
    if (url==='/'||url==='/home/'){
        const home=readFileSync('./app/home.html','ascii')
        res.writeHead(200,{'content-type':'text/html'})
        res.write(home)
        if (req.method=='POST'){
            // const data=req.POST.get('name')
            // console.log(data) 
        }        
    }
    else if (url==='/services/'){
        const services=readFileSync('./app/services.html','ascii')
        res.writeHead(200,{'content-type':'text/html'})
        res.write(services)        
    }
    else if (url==='/about/'){
        const about=readFileSync('./app/about.html','ascii')
        res.writeHead(200,{'content-type':'text/html'})
        res.write(about)        
    }
    else if (url==='/contact/'){
        const contact=readFileSync('./app/contact.html','ascii')
        res.writeHead(200,{'content-type':'text/html'})
        res.write(contact)        
    }
    else if (url==='/help/'){
        const help=readFileSync('./app/help.html','ascii')
        res.writeHead(200,{'content-type':'text/html'})
        res.write(help)        
    }
    else if (url==='/home/theme.css'||url==='/theme.css'){
        res.writeHead(200,{'content-type':'text/css'})
        res.write(style)        
    }
    else{
        res.writeHead(404,{'content-type':'text/html'})
        res.write("<h1><center>page not found</center></h1>")
    }
    console.log(req.url);
    console.log('user hit the server')
    res.end()
})

server.listen(8000)
