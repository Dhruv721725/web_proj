
// let crsong=new Audio(`./music/${songs[sng]}.mp3`)
<<<<<<< HEAD
// import {b} from "./songs.py";

=======
let os = require('os');
>>>>>>> b1

let songs=['A_Dreamers_Rap','A_Thousand_Years','9_45','Aarambh_Hai','Achyutam_Keshavam','Aik_din_Aap']
let sng=0

let crsong=new Audio(`./music/${songs[sng]}.mp3`)

<<<<<<< HEAD
// let volm=document.getElementById('volm')
=======
>>>>>>> b1
let sname=document.getElementById('sname')
let prev=document.getElementById('prev')
let play=document.getElementById('play')
let next=document.getElementById('next')
let pbar=document.getElementById('pbar')
<<<<<<< HEAD
let vbar=document.getElementById('vbar')
let shfl=document.getElementById('shfl')
let cycl='repeat'

sname.innerText=songs[sng]
pbar.value=0
vbar.value=50
=======

sname.innerText=songs[sng]
pbar.value=0
>>>>>>> b1

function next_song(){
    sng++;
    if(sng>=songs.length){
        sng=0
    }
<<<<<<< HEAD
    if (cycl=='shuffle'){
        sng=Math.round((Math.random(0,1)*(songs.length-1)))
        console.log(sng);
    }
    sname.innerText=songs[sng]
=======
    sname.innerText=songs[sng]

>>>>>>> b1
    crsong.src=`./music/${songs[sng]}.mp3`
    crsong.play()
    play.classList.replace('fa-play','fa-pause')
}

play.addEventListener('click',()=>{
    console.log('play');
    if (play.classList.contains('fa-play')) {
        play.classList.replace('fa-play','fa-pause')
        crsong.play()
    }
    else{
        play.classList.replace('fa-pause','fa-play')
        crsong.pause()
    }
})

prev.addEventListener('click',()=>{
    console.log('prev')
    sng--;
    if(sng<0){
        sng=songs.length-1
    }
    sname.innerText=songs[sng]

    crsong.src=`./music/${songs[sng]}.mp3`
    crsong.play()
    play.classList.replace('fa-play','fa-pause')   
})

next.addEventListener('click',next_song)

pbar.addEventListener('change',()=>{
    crsong.currentTime=(pbar.value/100)*crsong.duration
})

crsong.addEventListener('timeupdate',()=>{
    pbar.value=(crsong.currentTime/crsong.duration)*100
    if (crsong.currentTime>=crsong.duration){
<<<<<<< HEAD
        if (cycl=='1'){
            crsong.currentTime=0
            crsong.play()
        }
        else{
            next_song()
        }
    }
})

vbar.addEventListener('change',()=>{
    crsong.volume=vbar.value/100
})

shfl.addEventListener('click',()=>{
    if (shfl.classList.contains('fa-repeat')){
        cycl='shuffle'
        console.log('shuffle');
        shfl.classList.replace('fa-repeat','fa-shuffle')
    }
    
    else if (shfl.classList.contains('fa-shuffle')){
        cycl='1'
        console.log('1');
        shfl.classList.replace('fa-shuffle','fa-1')
    }
    
    else{
        cycl='repeat'
        console.log('repeat');
        shfl.classList.replace('fa-1','fa-repeat')
    }
})


// volm.addEventListener('click',()=>{
//     vbar.hidden=false
// })

// volm.addEventListener('mouseenter',()=>{
//     vbar.hidden=false
//     console.log('hi')
// })

// console.log(json.parse(b))
=======
        next_song()
    }
})

console.log(os.tmpdir)
>>>>>>> b1
