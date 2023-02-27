from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()== '':
        messagebox.showerror('Error','All Fields Are Required')
    print('Hello')

def signup_page():
    login_window.destroy()
    import register_GUI

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
        
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='img/cl.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='img/op.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

login_window = Tk()
login_window.geometry('1280x720')
login_window.resizable(0,0)
bgImage = ImageTk.PhotoImage(file='img/bg2.jpg')

bgLabel = Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0) 
login_window.title("Sign in")

heading = Label(login_window,text='USER LOGIN',font=('Bebas',40,'bold'),bg='white',fg='gray1')
heading.place(x=600,y=150) # center heading

usernameEntry = Entry(login_window,width=15,font=('Bebas',30),bg='white',fg='gray1')
usernameEntry.place(x=570,y=250)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_window,width=260,height=4,bg='gold').place(x=570,y=300)

passwordEntry = Entry(login_window,width=15,font=('Bebas',30),bg='white',fg='gray1')
passwordEntry.place(x=570,y=330)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_window,width=260,height=4,bg='gold').place(x=570,y=380)

openeye = PhotoImage(file='img/cl.png')
eyeButton = Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=850,y=335)

loginButton = Button(login_window,text='Login' , font=('Bebas',20,'bold'),fg='white',bg='gray1',activeforeground='white',activebackground='gray1'
                        ,cursor='hand2',bd=0,width=22,command=login_user)
loginButton.place(x=570,y=400)

signupLabel = Label(login_window,text="Don't have an account?",font=('Bebas',20),bg='white',fg='gray1')
signupLabel.place(x=500,y=500)

NewButton = Button(login_window,text='Create new one',font=('Bebas',20,'underline'),bg='white',fg='gold',bd=0,activeforeground='blue'
                ,activebackground='white',cursor='hand2',command=signup_page)
NewButton.place(x=720,y=493)

login_window.mainloop()
