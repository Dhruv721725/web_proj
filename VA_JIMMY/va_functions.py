import os
import webbrowser as wb
import random
import pyttsx3 
import speech_recognition as sr
import datetime as dt
import time
import AppOpener as ao
import pyautogui as ptg
from englisttohindi.englisttohindi import EngtoHindi
def fin(p,f):
    l=[]
    dir=os.listdir(p)
    for i in dir:
        if f.lower() in i.lower():
            a=os.path.join(p,i)
            l.append(a)
        try: 
            p2=os.path.join(p,i) 
            d2=os.listdir(p2)
            for i in d2:
                if f.lower() in i.lower():
                    a = os.path.join(p2, i)
                    l.append(a)
                try:
                    fin(os.path.join(p2,i),f)
                except PermissionError as e:
                    pass
                except NotADirectoryError as e:
                    pass
        except PermissionError as e:
            pass
        except NotADirectoryError as e:
            pass
    return l

def fout(url):    
    if url=="youtube":
        url="http://www.youtube.com"
    elif url=="bing":
        url="http://www.bing.com"
    elif url=="google":
        url="http://www.google.com"
    elif url=="python":
        url="https://www.python.org"
    wb.open_new(url)
    
def spk(vc):
    e=pyttsx3.init()
    a=e.getProperty("voices")
    e.setProperty("voice", a[1].id)# setting voice
    e.setProperty("rate",125)# setting rate
    e.setProperty("volume",1.0)# setting volume
    e.say(vc)# speaking
    e.runAndWait()

def wish():
    t=str(dt.datetime.now())
    a=t.split(" ")
    h=int((a[1].split(":"))[0])
    m=int((a[1].split(":"))[1])
    if h>0 and h<12:
        return("Good morning")
    elif h>12 and h<18:
        return("Good afternoon")
    elif h>18 and m<1:
        return("Good evening")
    
def open(src):
    ao.open(src)

# def close(src):
#     ao.close(src)

def lstn():
    r= sr.Recognizer()
    with sr.Microphone() as src:
        print("listening...")
        r.pause_threshold=0.5
        r.energy_threshold=1500
        aud=r.listen(src)
    try:
        print("recognizing...")
        q=r.recognize_google(aud,language="en-in")
        print(q)
        return q
    except Exception:
        print("voivce not recognized")
        return "none"

def translate(st):
    res=EngtoHindi(st)
    return res.convert



# shortcuts
def write(st):
    time.sleep(2)
    ptg.write(st)

def shortcut_key(a,b):
    ptg.keyDown(a)
    ptg.keyDown(b)
    ptg.keyUp(a)
    ptg.keyUp(b)

def copy():
    shortcut_key("ctrl","c")
def cut():
    shortcut_key("ctrl","x")
def paste():
    shortcut_key("ctrl","v")
def close():
    shortcut_key("alt","f4")
def undo():
    shortcut_key("ctrl","z")
def redo():
    shortcut_key("ctrl","y")
def min_all():
    shortcut_key("win","d")
def sel_all():
    shortcut_key("ctrl","a")
def delete():
    ptg.keyDown("del")
    ptg.keyUp("del")

