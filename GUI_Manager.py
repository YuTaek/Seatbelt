from tkinter import *
from tkinter import messagebox
import os
import pyrebase

useruid = ""

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

def store():
    global store_account
    store_account = Toplevel(login_success_screen)
    store_account.title("Store Acoount")
    store_account.geometry("400x250")

    # text variables
    global storename
    global storeword
    global website
    global storename_entry
    global storeword_entry
    global website_entry
    global iv
    global iv_entry
    storename = StringVar()
    storeword = StringVar()
    website = StringVar()
    iv = StringVar()

    Label(store_account, text="Please store information below", font=("Arial", 17), width=60,
          bg="orange").pack()
    Label(store_account, text="").pack()
    username_lable = Label(store_account, text="New Username: ", font=("Arial", 16)).pack()
    storename_entry = Entry(store_account, textvariable=storename)
    storename_entry.pack()
    Label(store_account, text="").pack()
    password_lable = Label(store_account, text="New Password: ", font=("Arial", 16)).pack()
    storeword_entry = Entry(store_account, textvariable=storeword)
    storeword_entry.pack()
    Label(store_account, text="").pack()
    site_lable = Label(store_account, text="Website: ", font=("Arial", 16)).pack()
    website_entry = Entry(store_account, textvariable=website)
    website_entry.pack()
    Label(store_account, text="").pack()
    site_lable = Label(store_account, text="IV: ", font=("Arial", 16)).pack()
    iv_entry = Entry(store_account, textvariable=iv)
    iv_entry.pack()
    Label(store_account, text="").pack()
    Button(store_account, text="Click here to store", font=("Arial", 16), width=20, height=1, bg="orange",
           command= storepassword).pack()




def storepassword():

    username_info = storename.get()
    password_info =storeword.get()
    website_info = website.get()
    exists = False

    storage_info = useruid
    all_users = db.child("Users").child(storage_info).get()
    #for users in all_users.each():
        #if (users.val()['website'] == username_info):
            #exists = True

    #print (master_dm)

    if len(username_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Empty", message="Please fill up every field")

    is_ok = messagebox.askokcancel(title="username info",message=f"Details entered : \nUserName: {username_info} \nPassword: {password_info} \nAre you sure you want to save this? ")
    if is_ok:
        if (exists == False):
            data = {"name": username_info, "password": password_info, "website": website_info}
            result = db.child("Users").child(storage_info).push(data)

            Label(store_account, text="Registration Successful", fg="orange", font=("calibri", 11)).pack()

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
    global useruid
    useruid = StringVar()
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
                all_users = db.child("Users").get()
                for user in all_users.each():
                    if (username1 == user.val()['name']):
                        useruid = user.key()
            else:
                password_not_recognised()

    print (useruid)
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
    Button(login_success_screen, text="Store Password", font=("Arial", 16), bg="orange", command=store).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Search", font=("Arial", 16), bg="orange", command=Search).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Exit", font=("Arial", 16), bg="orange", command=delete_login_success).pack()



def Search():
    global search

    global search_entry
    global site_entry
    global searchvar
    global sitevar
    searchvar = StringVar()
    sitevar = StringVar()
    search = Toplevel(login_success_screen)
    search.title("Search Username")
    Label(search, text="Search Username below", font=("Arial", 17), bg="orange", width=60).pack()
    Label(search, text="").pack()
    Label(search, text="Username: ", font=("Arial", 16)).pack()
    search_entry = Entry(search, textvariable= searchvar)
    search_entry.pack()
    Label(search, text="").pack()
    Label(search, text="Website: ", font=("Arial", 16)).pack()
    site_entry = Entry(search, textvariable=sitevar)
    site_entry.pack()
    Label(search, text="").pack()
    Button(search, text="Search", font=("Arial", 16), bg="orange", command=FoundUser).pack()

def FoundUser():
    storage_info = useruid
    username = searchvar.get()
    website = sitevar.get()

    if len(username) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure that each and every field is filled up")
    all_users = db.child("Users").child(storage_info).get()
    for users in all_users.each():

        if (users.val()['name'] == username and users.val()['website'] == website):


         Label(search, text=users.val()['password'], fg="orange", font=("calibri", 11)).pack()





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



    main_screen.mainloop()  # intializes GUI


main_account_screen()
