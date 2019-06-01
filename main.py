import requests
import webbrowser
import re
import tkinter as tk
url = 'http://www.qmaile.com/'
responed = requests.get(url)
reg = re.compile('<option value="(.*?)" selected="">')
res = re.findall(reg,responed.text)
root = tk.Tk()
root.title('vip_movie')
root.geometry('500x250')
l1 = tk.Label(root,text='播放接口:',font=12).grid(row = 0,column = 0)
var = tk.StringVar()
var.set(res[2])
l1 = tk.Label(root,text='播放接口:',font=12).grid(row = 0,column = 0)
r1 = tk.Radiobutton(root,text = '播放接口1' , variable = var , value = res[0]).grid(row = 0,column = 1)
r2 = tk.Radiobutton(root,text = '播放接口2' , variable = var , value = res[1]).grid(row = 1,column = 1)
r3 = tk.Radiobutton(root,text = '播放接口3' , variable = var , value = res[2]).grid(row = 2,column = 1)
r4 = tk.Radiobutton(root,text = '播放接口4' , variable = var , value = res[3]).grid(row = 3,column = 1)
r5 = tk.Radiobutton(root,text = '播放接口5' , variable = var , value = res[4]).grid(row = 4,column = 1)
l2 = tk.Label(root,text='播放链接:',font=12).grid(row = 6,column = 0)
e1 = tk.Entry(root, text = '',width = 50 )
e1.grid(row =6,column = 1)
def play():
    webbrowser.open(var.get()+e1.get())
b1 = tk.Button(root, text = '播放', font = 12 ,command = play).grid(row = 7,column =1)
root.mainloop()
