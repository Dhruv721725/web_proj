// setInterval(()=>{
//     console.log("hello world")
// },1000)


// const os=require('os');
// const user=os.userInfo();
// console.log(user);
// const crnt_os={
//     name: os.type(),
//     release: os.release(),
//     totmem: os.totalmem(),
//     freemem: os.freemem()
// } 
// console.log(crnt_os);


// const path=require('path')
// console.log (path.sep)
// const filePath=path.join('/cont','subfolder','notes.txt')
// console.log(filePath)
// const base=path.basename(filePath)
// console.log(base)
// const absolute = path.resolve(__dirname,'content','subfolder','test.txt')
// console.log(absolute)


// // __file handling__
// // __synchronous approach__
// // __here we will directly call functions__
// const {readFileSync,writeFileSync}=require('fs') //these are built-in functions readFileSync,writeFileSync
// // __reading data from files__
// const first = readFileSync('./notes.txt','utf-8')
// const sec = readFileSync('./sec.txt','ascii')
// // __creating or overwriting files__
// const cont='this data is written into this file from js file named 1.js with the help of file handling'+first+sec
// const third=writeFileSync('./module practice/fh2.txt',cont)

// // __asynchronous approach__
// const {readFile,writeFile}=require ('fs')
// // __reading data from file__
// readFile('./notes.txt','utf-8',(err,result)=>{
//     if (err){
//         console.log(err);
//         return;
//     }
//     const first=result;
//     // __creating or overwriting file__
//     writeFile('./module practice/fh2.txt',first,
//     (err,result)=>{
//         if (err){
//             console.log(err);
//             return;
//         }
//         else if (result==undefined){
//             console.log('data is inserted successfully') 
//         }
//     })
// })

// // __HTTP module__
// const http=require('http')
// // __here we are creating a server at port 5000__
// const server=http.createServer((req,res)=>{
//     // console.log(req)
//     const text='<h1>welcome to our homepage</h1>'
//     if (req.url ==='/home' || req.url ==='/'){
//         res.end(text)
//     }
//     res.end()
//     // console.log(req)
// })
// server.listen(5000)


// const load=require('lodash')
// const items=[1,[2,[3,[4]]]]
// const nitems=load.flattenDeep(items)
// console.log(nitems);
// --------------------------------------------------------
// const {readFile}=require('fs')
// const util=require('util')

// const readFilePromise=util.promisify(readFile)
// --------------------------------------------------------
// const getText=(path)=>{
//     return new Promise((resolve,reject)=>{
//         readFile(path,'ascii',(err,rslt)=>{
//             if (err){
//                 reject(err)
//             }else{
//                 resolve(rslt)
//             }
//         })
//     })
// }
// getText('./notes.txt')
//     .then((result)=>console.log(result))
//     .catch((err)=>console.log(err))
// --------------------------------------------------------
// const start=async ()=>{
//     try{
//         const first= await getText('./t1.txt')
//         const sec= await getText('./t2.txt')
//         console.log(first,sec)
//     }catch (error){
//         console.log(error)
//     }
// }
// start()

// // __EVENTS__
// const EventEmmiter = require('events')
// const customEmitter=new EventEmmiter()

// customEmitter.on('response',(name, id)=>{
//     console.log('data received '+name+" "+id)
// })
// // we can append logic to predefined events.
// customEmitter.on('response',()=>{
//     console.log('data is being received')
// })
// customEmitter.emit('response',"Dhruv",11)

// const {writeFileSync}=require('fs')
// for (let i=1;i<10001;i++){
//     writeFileSync('./t3.txt','hello world this is line no.:'+i+'\n',{flag:'a'})
// }

// const http=require('http')
// const {createReadStream}=require('fs')
// const server=http.createServer()
// server.on("request",(req,res)=>{
//     res.end("<h1>WELCOME</h1> <hr color=red>")
// })
// server.listen(8000)
// const stream = createReadStream('./t3.txt',{highWaterMark:50000,encoding:'utf8'})
// stream.on('data',(result)=>{
//     console.log(result)
// })

// in output we can easily see that data comes in the form of chunks.
// by default buffer size is 64 kbs
// we can define a size using ,{highWaterMark:9000} now the size would be 8950 bytes.
// we can add encoding type as well ,{encoding:'utf8'}


