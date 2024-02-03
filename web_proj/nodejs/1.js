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

// __HTTP module__
const http=require('http')
// __here we are creating a server at port 5000__
const server=http.createServer((req,res)=>{
    // console.log(req)
    const text='<h1>welcome to our homepage</h1>'
    if (req.url ==='/home' || req.url ==='/'){
        res.end(text)
    }
    res.end()
    // console.log(req)
})
server.listen(5000)
