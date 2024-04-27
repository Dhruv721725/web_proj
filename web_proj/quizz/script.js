const startbtn=document.querySelector('.start-btn')
const popupinfo=document.querySelector('.pop-info')
const exitbtn=document.querySelector('#extqz')
const main=document.querySelector('.main')
const cont=document.querySelector('#continue')
const home=document.querySelector('.home')
const next=document.querySelector('.next-btn')
const qsect=document.querySelector('.quiz-section')
const qbox=document.querySelector('.quiz-box')
const oplst=document.querySelector('.option-list')
const tques=document.querySelector('.total-question')
const scr=document.querySelector('.header-score')
const rslt=document.querySelector('.result-box')
const try_again=document.querySelector('.try-again')
const gohome=document.querySelector('.gohome')

let qcnt=0;
let score=0;
scr.textContent=`Score: 0/${questions.length}`

startbtn.addEventListener('click',()=>{
    popupinfo.classList.add('active')
    main.classList.add('active')
})

exitbtn.addEventListener('click',()=>{
    popupinfo.classList.remove('active')
    main.classList.remove('active')
})

cont.addEventListener('click',()=>{
    home.classList.add('inactive')
    qbox.classList.add('active')
    popupinfo.classList.remove('active')
    main.classList.remove('active')

    showQ(qcnt);
})  

next.addEventListener('click',()=>{
    if (qcnt<questions.length-1){
        oplst.innerHTML=null
        qcnt+=1
        showQ(qcnt)
        if (qcnt==questions.length-1){
            next.textContent='Finish'  
            next.classList.add('finish')
        }
    }
    else{
        if (next.classList.contains('finish')){
            rslt.classList.add('active')
            qbox.classList.remove('active')
            showresult()
        }
    }
})

try_again.addEventListener('click',()=>{
    rslt.classList.remove('active')
    qcnt=0;
    score=0;
    scr.textContent=`Score: 0/${questions.length}`
    oplst.innerHTML=null
    qbox.classList.add('active')
    showQ(qcnt)
})
gohome.addEventListener('click',()=>{
    home.classList.remove('inactive')
    rslt.classList.remove('active')
    qcnt=0;
    score=0;
    scr.textContent=`Score: 0/${questions.length}`
    oplst.innerHTML=null
  
})

function showQ(i){
    const questext=document.querySelector('.question-text')
    questext.textContent=`${questions[i].num}. ${questions[i].ques}`;
    for (const j of questions[i].options) {
        let optag=
            `<div class="option">
                <span>${j}</span>
            </div>`
        oplst.innerHTML+=optag    
    }
    tques.textContent=`${questions[i].num} of ${questions.length} Questions`

    const option=document.querySelectorAll('.option')
    for (const k of option) {
        k.setAttribute('onclick',`optionSelected(this)`) 
    }
    next.classList.remove('active')
    
}

function optionSelected(answer){
    let usrans=answer.textContent.trim()
    let crctans=questions[qcnt].ans
    if (usrans==crctans){
        score+=1;
        answer.classList.add('correct')
    }
    else{
        answer.classList.add('incorrect')
        console.log(false);
    }
    const option=document.querySelectorAll('.option')
    for (const k of option) {
        k.removeAttribute('onclick')
        let kans=k.textContent.trim()
        if (kans==crctans){
            k.classList.add('correct')
        }
    }
    scr.textContent=`Score: ${score}/${questions.length}`
    next.classList.add('active')
}

function showresult(){
    const pval=document.querySelector('.progress-value')
    const scrval=document.querySelector('.score-text')
    const pcrcl=document.querySelector('.progress-circle')
    scrval.textContent=`Your score ${score} out of ${questions.length}`
    
    let pstart=0;
    let pend=(score/questions.length)*100;
    let pspeed=20;

    let progress=setInterval(()=>{
        if (pstart<pend){
            pstart++;     
            pval.textContent=pstart+"%"
            let arch= (pstart/100)*360
            pcrcl.setAttribute('style',`background:conic-gradient(seagreen ${arch}deg, rgba(0,0,0,0.3)0deg)`)
        }        
    },pspeed)
}

