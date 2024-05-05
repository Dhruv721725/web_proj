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
            q=0
            while True:
                try:
                    st=lstn()
                    print(st)
                    print(translate(st))
                    l=st.split(" ")
                    spk(s)
                    if queries>0:
                        spk("anything else")

                    if "repeat" in l:
                        spk(s)
                    s=" "
                    if "translate" in l:
                        i=l.index("translate")
                        st=" ".join(l[i+1:])
                        res=translate(st)
                        print(res)
                        continue

                    elif "open" in l:
                        n=l.index("open")
                        open(str(l[n+1:]))
                        q+=1
                        continue

                    # elif "close" in l:
                    #     n=l.index("close")
                        # close(l[n+1:])

                    elif "copy" in l:
                        copy()
                        s="copied"  
                        continue               

                    elif "cut" in l:
                        cut()
                        s="cutted"
                        continue

                    elif "paste" in l:
                        paste()
                        s="pasted"
                        continue

                    elif "minimize" in l:
                        i=l.index("minimize")
                        min_all()

                        s="minimized"
                        continue

                    elif "undo" in l:
                        undo()
                        s="undone"
                        continue

                    elif "redo" in l:
                        redo()
                        s="redone"
                        continue

                    elif "close" in l:
                        i=l.index("close")
                        if l[i+1]=="it":
                            close()
                        elif l[i+1]=="all":
                            for i in range(q+1):
                                close()
                        else:
                            close()
                        s="closed"
                        continue

                    elif "select" in l:
                        i=l.index("select")
                        t=l[i+1] 
                        if t=="all":
                            sel_all()
                        else:
                            sel_all()
                        s="selected"
                        continue

                    elif "delete" in l:
                        spk("are you sure")
                        ans=lstn()
                        if str(ans).lower() == 'yes':
                            delete()
                        else:
                            spk("ok")
                        continue
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
                        continue
                    elif "search" in l:
                        n=l.index("search")
                        fout(l[n+1])
                        continue
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
                        continue

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
                        continue

                    else:
                        res=query(st)
                        # print (res)
                        txt=str(res).split('.')
                        print(txt)
                        spk(txt[1])
                        print(txt[1])
                    if st != " ":
                        queries+=1
                    else:
                        queries=0
                    spk(s)

                except Exception as e:
                    print(e)
                    continue              


    except Exception as e:
        print(e)
        continue