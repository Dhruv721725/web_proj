let btns=document.getElementsByTagName("button");
let disp=document.getElementById("display");
let ac=0
let rt=0
let lst=['+','-','*','/','**']

for (let item of btns){
    item.addEventListener("click",(event)=>{
        if (event.target.innerText=="AC"){
            disp.value=0;
            ac+=1
        }
        else if(event.target.innerText=="="){
            try {
                if (rt>0){
                    exp=disp.value.slice(disp.value.indexOf('rt')+2)+`**(1/${num})`
                    rt=0
                    ans=eval(exp)
                }
                else{
                    ans=eval(disp.value)
                    }
                   disp.value=ans
                
            } catch (error) {
                disp.value="invalid input"
            }
        }
        else{
            if (ac>0){
                disp.value=""
                ac=0
            }
            if (event.target.innerText=="X"){
                disp.value+="*"
            }
            else if (event.target.innerText=="BACK SPACE"){
                disp.value=disp.value.slice(0,-1)
            }
            else if (event.target.innerText=="pw"){
                disp.value+='**'
            }
            else if (event.target.innerText=="rt"){
                disp.value+='rt'
                num=disp.value.slice(0,disp.value.indexOf('rt'))
                rt+=1
            }
            else{
                disp.value+=event.target.innerText
            }
            
        }
        
    })
}
console.log(eval(16**1/2))