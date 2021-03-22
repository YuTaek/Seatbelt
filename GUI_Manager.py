from tkinter import *
from tkinter import messagebox
import os
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyA4S4BmC0_dOuPbKLAJTKTzZIGCPXpeDuE",
    'authDomain': "fir-password-ef198.firebaseapp.com",
    'databaseURL': "https://fir-password-ef198-default-rtdb.firebaseio.com",
    'projectId': "fir-password-ef198",
    'storageBucket': "fir-password-ef198.appspot.com",
    'messagingSenderId': "923724720186",
    'appId': "1:923724720186:web:7ff9ffa57c054654e2ed03",
    'measurementId': "G-10S5GMG96Q"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

data2 = {"name": "JOHN", "password": "DINOSAUR"}
data3 = {"name": "j", "password": "123"}
#db.child("User").push(data3)

def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

# registration window
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Account Registration")
    register_screen.geometry("400x250")

    # text variables
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please input registration details below", font=("Arial", 17), width=60,
          bg="orange").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="New Username: ", font=("Arial", 16)).pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="").pack()
    password_lable = Label(register_screen, text="New Password: ", font=("Arial", 16)).pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Click here to register", font=("Arial", 16), width=20, height=1, bg="orange",
           command=register_user).pack()


# login window
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Account Login")
    login_screen.geometry("400x250")

    # text variables
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Please input login details below", font=("Arial", 17), bg="orange", width=60).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username: ", font=("Arial", 16)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password: ", font=("Arial", 16)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Click here to login", bg="orange", font=("Arial", 16), width=20, height=1,
           command=login_verify).pack()

def master():
    global register_master
    register_master = Toplevel(login_success_screen)
    register_master.title("Enter Master")
    register_master.geometry("400x250")

    # text variables
    global mastername
    global masterword
    global stor
    global mastername_entry
    global masterword_entry
    global storage_entry
    mastername = StringVar()
    masterword = StringVar()
    stor = StringVar()

    Label(register_master, text="Please store your passwords below", font=("Arial", 17), width=60,
          bg="orange").pack()
    Label(register_master, text="").pack()
    username_lable = Label(register_master, text="New Username: ", font=("Arial", 16)).pack()
    mastername_entry = Entry(register_master, textvariable=mastername)
    mastername_entry.pack()
    Label(register_master, text="").pack()
    password_lable = Label(register_master, text="New Password: ", font=("Arial", 16)).pack()
    masterword_entry = Entry(register_master, textvariable=masterword, show='*')
    masterword_entry.pack()
    Label(register_master, text="").pack()
    password_lable = Label(register_master, text="UID: ", font=("Arial", 16)).pack()
    storage_entry = Entry(register_master, textvariable=stor, show='*')
    storage_entry.pack()
    storage_entry.pack()
    Button(register_master, text="Click here to store", font=("Arial", 16), width=20, height=1, bg="orange",
           command= registermaster).pack()




def registermaster():

    username_info = mastername.get()
    password_info = masterword.get()
    storage_info = stor.get()

    print (username_info)
    if len(username_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Empty", message="Please fill up every field")

    is_ok = messagebox.askokcancel(title="username info",message=f"Details entered : \nUserName: {username_info} \nPassword: {password_info} \nAre you sure you want to save this? ")
    if is_ok:

            data = {"name": username_info, "password": password_info}
            result = db.child("Users").child(storage_info).push(data)

            Label(register_master, text="Registration Successful", fg="orange", font=("calibri", 11)).pack()

    else:
        messagebox.showerror("showerror", "Registration Unsuccessful, please choose a unique username")





def register_user():

    username_info = username.get()
    password_info = password.get()
    exists = False
    all_users = db.child("Users").get()
    for users in all_users.each():
        if (users.val()['name'] == username_info):
            exists = True

    if len(username_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure that each and every field is filled up")

    is_ok = messagebox.askokcancel(title=username_info,message=f"These are the details entered : \nUserName: {username_info} \nPassword: {password_info} \nAre you sure you want to save this? ")
    if is_ok:
        if (exists == False):
            data = {"name": username_info, "password": password_info}
            result = db.child("Users").push(data)
            #db.child(username_info).push(data)
            Label(register_screen, text="Registration Successful", fg="orange", font=("calibri", 11)).pack()

        else:
            messagebox.showerror("showerror", "Registration Unsuccessful, please choose a unique username")







# login button event handler
def login_verify():
    # retrieve login details
    username1 = username_verify.get()
    password1 = password_verify.get()
    # erase the login details after clicking login 
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    Userfound = False

    all_users = db.child("Users").get()

    for users in all_users.each():
        if (users.val()['name'] == username1):
            Userfound = True
            if (users.val()['password'] == password1):
                login_sucess()
            else:
                password_not_recognised()
    if (Userfound == False):
        user_not_found()


# Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("User Authenticated")
    login_success_screen.geometry("400x250")
    Label(login_success_screen, text="").pack()
    Label(login_success_screen, text="Login Authorized", font=("Arial", 16)).pack()
    Label(login_success_screen, text="").pack()




    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Register Password", font=("Arial", 16), bg="orange", command=master).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Search", font=("Arial", 16), bg="orange", command=Search).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Exit", font=("Arial", 16), bg="orange", command=delete_login_success).pack()

def display():
    global display
    display = Toplevel(main_screen)
    display.title("Find User")
    Label(display, text="Find UID details below", font=("Arial", 17), bg="orange", width=60).pack()
    Label(display, text="").pack()

    display.geometry("400x250")
    Label(display, text="").pack()

    all_users = db.child("Users").get()
    for user in all_users.each():
        #messagebox.showinfo(title="Oops", message=users.val())
       Label(display, text=user.val(), fg="orange", font=("calibri", 10)).pack()


def Search():
    global search

    global search_entry
    global searchvar
    searchvar = StringVar()
    search = Toplevel(login_success_screen)
    search.title("Search Username")
    Label(search, text="Search Username below", font=("Arial", 17), bg="orange", width=60).pack()
    Label(search, text="").pack()
    Label(search, text="Username: ", font=("Arial", 16)).pack()
    search_entry = Entry(search, textvariable= searchvar)
    search_entry.pack()
    Label(search, text="").pack()
    Button(search, text="Search", font=("Arial", 16), bg="orange", command=FoundUser).pack()

def FoundUser():
    username = searchvar.get()
    result = db.child("Users").order_by_child('name').equal_to(username).get()
    print(result.val())

    Label(search, text=result.val(), fg="orange", font=("calibri", 11)).pack()





# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Unsuccessful")
    password_not_recog_screen.geometry("400x250")
    Label(password_not_recog_screen, text="").pack()
    Label(password_not_recog_screen, text="Invalid Password", font=("Arial", 16)).pack()
    Label(password_not_recog_screen, text="").pack()
    Button(password_not_recog_screen, text="OK", font=("Arial", 16), bg="orange",
           command=delete_password_not_recognised).pack()


# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Unsuccessful")
    user_not_found_screen.geometry("400x250")
    Label(user_not_found_screen, text="").pack()
    Label(user_not_found_screen, text="User Does Not Exist", font=("Arial", 16)).pack()
    Label(user_not_found_screen, text="").pack()
    Button(user_not_found_screen, text="OK", font=("Arial", 16), bg="orange",
           command=delete_user_not_found_screen).pack()


# Deleting popups
def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# initial login window
def main_account_screen():
    global main_screen
    main_screen = Tk()  # GUI window creation
    main_screen.geometry("400x300")  # size of the window
    main_screen.title("Account Login")  # window title
    Label(text="Password Manager", bg="Orange", width="300", height="2", font=("Arial", 23)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="User Login", bg="orange", height="1", width="20", command=login,
           font=("Arial", 16)).pack()  # login button
    Label(text="").pack()
    Label(text="").pack()
    Button(text="User Registration", bg="orange", height="1", width="20", command=register,
           font=("Arial", 16)).pack()  # register button

    Label(text="").pack()
    Button(text="Find UID", bg="orange", height="1", width="20", command=display,
           font=("Arial", 16)).pack()  # register button
    Label(text="").pack()


    main_screen.mainloop()  # intializes GUI


main_account_screen()
