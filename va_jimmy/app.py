from func import *

#start of body
while True:
    try:
        st=lstn()    
        if "jimmy" in st.lower():
            u=""
            spk(f"{wish()} {u}, How can I help you.")
            s=" "
            queries=0
            while True:
                st=lstn()
                print(st)
                l=st.split(" ")
                if queries>0:
                    spk("anything else")
                    
                if "repeat" in l:
                    spk(s)

                elif "translate" in l:
                    i=l.index("translate")
                    st=" ".join(l[i+1:])
                    res=translate(st)
                    print(res)

                elif "open" in l:
                    n=l.index("open")
                    open(l[n+1:])

                elif "close" in l:
                    n=l.index("close")
                    # close(l[n+1:])
                
                elif "copy" in l:
                    copy()                

                elif "cut" in l:
                    cut()

                elif "paste" in l:
                    paste()
                
                elif "minimize" in l:
                    i=l.index("minimize")
                    if l[i+1]=="all":
                        min_all()
                
                elif "undo" in l:
                    undo()

                elif "redo" in l:
                    redo()

                elif "close" in l:
                    i=l.index("close")
                    if l[i+1]=="it":
                        close()
                    elif l[i+1]=="all":
                        for i in range(queries+1):
                            close()
                    else:
                        close()
                
                elif "select" in l:
                    i=l.index("select")
                    t=l[i+1] 
                    if t=="all":
                        sel_all()
                    else:
                        sel_all()

                elif "delete" in l:
                    spk("are you sure")
                    ans=lstn()
                    if str(ans).lower() == 'yes':
                        delete()
                    else:
                        spk("ok")
                                    
                elif "find" in l:
                    n=l.index("find")
                    file=l[n+1]
                    if "in" in l:
                        n=l.index("in")
                        path=l[n+1]
                        if len(str(path)) == 1:
                            fl=fin(f"{path}:\\",file)   
                        else:
                            fl=fin(f"{path}\\",file)
                    else:
                        fl=fin("C:\\",file)
                        fl+=fin("D:\\",file)
                    for i in fl:
                        print(i)
                        spk(i)

                elif "search" in l:
                    n=l.index("search")
                    fout(l[n+1])

                elif "tell" in l:
                    n=l.index("tell")
                    a=l[n+1:len(l)]
                    t=str(dt.datetime.now()).split(" ")
                    print(t)
                    if "time" in a:
                        lt=str(t[1]).split(":")
                        s=f"right now it is {lt[0]} hours, {lt[1]} minute,{lt[2]} seconds"
                    elif "date" in a:
                        mon=["january","february","march","april","may","june","july","august","october","november","december"]
                        lt=t[0].split("-")
                        m=int(lt[1])
                        s=f"today is {lt[2]} of {mon[m]} of {lt[0]}"
                    elif "day" in a:
                        wd=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
                        w=dt.datetime.isoweekday(dt.datetime.now())
                        s=f"today is {wd[w]}"
                    else:
                        s="what"

                elif "play" in l:
                    n=l.index("play")
                    a=l[n+1:len(l)]
                    msc=fin("D://",".mp3")
                    vdo=fin("D://",".mp4")
                    if "music" in a:
                        rfl=len(msc)
                        print(rfl)
                        r=random.randint(0,rfl)
                        os.startfile(msc[r])
                    elif "video" in a:
                        rfl=len(vdo)
                        print(rfl)
                        r=random.randint(0,rfl)
                        os.startfile(vdo[r])
                    else:                
                        for ad in msc:
                            for i in a:
                                if i.lower() in str(ad).lower():
                                    os.startfile(ad)
                                    break 
                        for ad in vdo:
                            for i in a:   
                                if i.lower() in str(ad).lower():
                                    os.startfile(ad)
                                    break

                else:
                    s=" "
                spk(s)
                queries+=1
    except Exception as e:
        print(e)