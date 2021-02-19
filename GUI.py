from tkinter import *
import os


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
 
    Label(register_screen, text="Please input registration details below", font=("Arial", 17), width=60, bg="orange").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="New Username: ", font=("Arial", 16)).pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="").pack()
    password_lable = Label(register_screen, text="New Password: ", font=("Arial", 16)).pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Click here to register", font=("Arial", 16), width=20, height=1, bg="orange", command = register_user).pack()
 

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
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Click here to login", bg="orange", font=("Arial", 16), width=20, height=1, command = login_verify).pack()
 

# register button event handler
def register_user():
    username_info = username.get()
    password_info = password.get()
 
 # opens a file in write mode and writes username and password into it 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
 # successful registration message 
    Label(register_screen, text="Registration Successful", fg="orange", font=("calibri", 11)).pack()
 

# login button event handler
def login_verify():
    # retrieve login details
    username1 = username_verify.get()
    password1 = password_verify.get()
    # erase the login details after clicking login 
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
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
    Button(login_success_screen, text="OK", font=("Arial", 16), bg="orange", command=delete_login_success).pack()
 

# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("400x250")
    Label(password_not_recog_screen, text="").pack()
    Label(password_not_recog_screen, text="Invalid Password", font=("Arial", 16)).pack()
    Label(password_not_recog_screen, text="").pack()
    Button(password_not_recog_screen, text="OK", font=("Arial", 16), bg="orange", command=delete_password_not_recognised).pack()
 

# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("400x250")
    Label(user_not_found_screen, text="").pack()
    Label(user_not_found_screen, text="User Does Not Exist", font=("Arial", 16)).pack()
    Label(user_not_found_screen, text="").pack()
    Button(user_not_found_screen, text="OK", font=("Arial", 16), bg="orange", command=delete_user_not_found_screen).pack()
 

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
    main_screen = Tk()      # GUI window creation
    main_screen.geometry("400x300")     # size of the window
    main_screen.title("Account Login")      # window title 
    Label(text="Password Manager", bg="Orange", width="300", height="2", font=("Arial", 23)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="User Login", bg="orange", height="1", width="20", command = login, font=("Arial", 16)).pack()        # login button
    Label(text="").pack()
    Label(text="").pack()
    Button(text="User Registration", bg="orange", height="1", width="20", command=register, font=("Arial", 16)).pack()        # register button
 
    main_screen.mainloop() # intializes GUI 
 
 
main_account_screen()