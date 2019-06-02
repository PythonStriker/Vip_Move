import requests
import webbrowser
import re
import tkinter as tk
from tkinter import ttk
import os

data = ["播放接口1","播放接口2",\
        "播放接口3","播放接口4",\
        "播放接口5"]

url = 'http://www.qmaile.com/'

def read():
    if os.path.exists('data.txt'):
        with open('data.txt', encoding='utf-8', mode='r') as file:
            if os.path.getsize('data.txt')==0:
                readlist = ['', '']
            else:
                lines = file.readlines()
                last_line = lines[-1]
                readlist = last_line.split(' ')
    else:
        file = open('data.txt',encoding='utf-8',mode='a')
        file.close()
        readlist = ['', '']
    return readlist

responed = requests.get(url)
reg = re.compile('<option value="(.*?)" selected="">')
res = re.findall(reg,responed.text)

root = tk.Tk()
root.title('vip_movie')
root.geometry('290x150')
l1 = tk.Label(root,text='播放接口:',font=12).grid(row = 0,column = 0)

var = tk.StringVar()
Var = tk.StringVar()
var.set(res[2])
reload_url = tk.StringVar()
reload_url.set(read()[-1])
reload_name = tk.StringVar()
reload_name.set(read()[0])

combo = ttk.Combobox(root ,textvariable=Var)
combo.grid(row = 0,column = 1)
combo["values"] = data
combo.current(0)

def choice(event):
    if combo.get()=="播放接口1":
        var.set(res[0])
    elif combo.get()=="播放接口2":
        var.set(res[1])
    elif combo.get()=="播放接口3":
        var.set(res[2])
    elif combo.get()=="播放接口4":
        var.set(res[3])
    else:
        var.set(res[4])

combo.bind("<<ComboboxSelected>>",choice)
l2 = tk.Label(root,text='播放链接:',font=12).grid(row = 1,column = 0)
e1 = tk.Entry(root ,textvariable =reload_url ,text = reload_url,width = 23 )

e1.grid(row =1,column = 1)
e2 = tk.Entry(root,text=reload_name,width = 23)
e2.grid(row =3,column=1)
l3 = tk.Label(root,text='链接名称',font=12).grid(row =3,column=0)

def play():
    webbrowser.open(var.get()+e1.get())

def save():
    with open('data.txt', encoding='utf-8', mode='a') as file:
        file.writelines([e2.get()+' ',e1.get()+'\n'])

b1 = tk.Button(root, text = '播放', font = 10 ,command = play).grid(row = 2,column =1)
b1 = tk.Button(root, text = '保存', font = 10 ,command = save).grid(row = 4,column =1)
root.mainloop()
