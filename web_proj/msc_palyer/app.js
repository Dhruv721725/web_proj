
// let crsong=new Audio(`./music/${songs[sng]}.mp3`)
let os = require('os');

let songs=['A_Dreamers_Rap','A_Thousand_Years','9_45','Aarambh_Hai','Achyutam_Keshavam','Aik_din_Aap']
let sng=0

let crsong=new Audio(`./music/${songs[sng]}.mp3`)

let sname=document.getElementById('sname')
let prev=document.getElementById('prev')
let play=document.getElementById('play')
let next=document.getElementById('next')
let pbar=document.getElementById('pbar')

sname.innerText=songs[sng]
pbar.value=0

function next_song(){
    sng++;
    if(sng>=songs.length){
        sng=0
    }
    sname.innerText=songs[sng]

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
        next_song()
    }
})

console.log(os.tmpdir)