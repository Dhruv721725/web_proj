from tkinter import *
import time
# i=4
root=Tk()
root.title('Jimmy')
root.iconbitmap('./img/1.ico')
root.configure(background='orange')
root.geometry('400x200')
root.maxsize(400,200)
root.minsize(400,200)

# animation
frameCnt = 240
frames = [PhotoImage(file='./img/va0_gif.gif',format = 'gif -index %i' %(i)) for i in range(0,frameCnt,10)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == (frameCnt//10):
        ind = 0
    label.configure(image=frame,background="purple",height=200,width=200)
    root.after(85, update, ind)

label = Label(root)
label.pack()
root.after(0, update, 0)


text="asdfghjk"
t1=Label(root,text=text,fg="white")
t1.pack()
root.mainloop()

