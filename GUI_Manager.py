from tkinter import *
from tkinter import messagebox
import os
import pyrebase
from EncryptionAndDecryption import *
import random, string
import pyperclip
#from PasswordGenerator import * 


useruid = ""
masterpw = ""

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
    register_screen.geometry("650x525")

    # text variables
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please input registration details", font=("Arial", 23), width=90, height=2, bg="orange").pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="New Username: ", font=("Arial", 18)).pack()
    username_entry = Entry(register_screen, textvariable=username, font=("Arial", 16),width=30)
    username_entry.pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    password_lable = Label(register_screen, text="New Password: ", font=("Arial", 18)).pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', font=("Arial", 16),width=30)
    password_entry.pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Click here to register", font=("Arial", 16), width=20, height=1, bg="orange", command=register_user).pack()


# login window
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Account Login")
    login_screen.geometry("650x525")

    # text variables
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Please input login details", font=("Arial", 23), bg="orange", width=90, height=2).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username: ", font=("Arial", 18)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, font=("Arial", 16),width=30)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password: ", font=("Arial", 18)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*', font=("Arial", 16),width=30)
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Click here to login", bg="orange", font=("Arial", 16), width=20, height=1,command=login_verify).pack()


def store():
    global store_account
    store_account = Toplevel(login_success_screen)
    store_account.title("Store Acoount")
    store_account.geometry("650x525")

    # text variables
    global storename
    global storeword
    global website
    global storename_entry
    global storeword_entry
    global website_entry
    
    storename = StringVar()
    storeword = StringVar()
    website = StringVar()
    iv = StringVar()

    Label(store_account, text="Please store information below", font=("Arial", 20), width=60,bg="orange", height=2).pack()
    Label(store_account, text="").pack()
    username_lable = Label(store_account, text="New Username: ", font=("Arial", 18)).pack()
    storename_entry = Entry(store_account, textvariable=storename, font=("Arial", 16),width=30)
    storename_entry.pack()
    Label(store_account, text="").pack()
    Label(store_account, text="").pack()
    password_lable = Label(store_account, text="New Password: ", font=("Arial", 18)).pack()
    storeword_entry = Entry(store_account, textvariable=storeword, font=("Arial", 16),width=30)
    storeword_entry.pack()
    Label(store_account, text="").pack()
    Label(store_account, text="").pack()
    site_lable = Label(store_account, text="Website: ", font=("Arial", 18)).pack()
    website_entry = Entry(store_account, textvariable=website, font=("Arial", 16),width=30)
    website_entry.pack()
    Label(store_account, text="").pack()
    Label(store_account, text="").pack()
    Label(store_account, text="").pack()
    Button(store_account, text="Click here to store", font=("Arial", 18), width=20, height=1, bg="orange",command= storepassword).pack()



def storepassword():
    username_info = storename.get()
    password_info = storeword.get()
    website_info = website.get()
    exists = False
    global useruid
    global masterpw
    print(useruid)
    storage_info = useruid
    all_users = db.child("Users").child(useruid).get()
    # for users in all_users.each():
    # if (users.val()['website'] == username_info):
    # exists = True

    # print (master_dm)

    p = Strength(password_info)
    print(p)

    length = 0
    if (all_users.each() is not None):
        for users in all_users.each():
            length = length + 1

    length = length - 2
    current = 0

    print(length)

    if (all_users.each() is not None):
        for users in all_users.each():
            if (current < length):
                if (users.val()['website'] == website_info):
                    if (users.val()['name'] == username_info):
                        exists = True
                current = current + 1

    if len(username_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Empty", message="Please fill up every field")

    if p == 0:
        messagebox.showinfo(title="Weak", message="Your password is too weak")

    elif p ==1:
        messagebox.showinfo(title="Medium", message="Your password is at medium strength")
    else:
         if (exists == False):
            nonce, encrypted = encrypt_firebase_pw(password_info, masterpw)
            data = {"name": username_info, "password": encrypted, "website": website_info, "nonce": nonce}
            result = db.child("Users").child(useruid).push(data)

            Label(store_account, text="Password Storage Successful", fg="orange", font=("calibri", 11)).pack()
         else:
            messagebox.showerror("showerror", "Data not stored")



def Strength(input):

    num = len(input)

    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

    for i in range(num):
        if input[i].islower():
            hasLower = True
        if input[i].isupper():
            hasUpper = True
        if input[i].isdigit():
            hasDigit = True
        if input[i] not in normalChars:
            specialChar = True

   
    if (hasLower and hasUpper and
            hasDigit and specialChar and num >= 8):
        return 2

    elif ((hasLower or hasUpper) and
          hasDigit and num >= 4):
        return 1
    else:
        return 0



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
    
    else:
 # writes to the database
        data = {
            'name': username_info,
            'password': password_info,
        }
        
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
        if (exists == False): 
            # successful registration message
            userhash = encrypt_master(username_info)
            passwordhash = encrypt_master(password_info)
            data = {"name": userhash, "password": passwordhash}
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
    global masterpw
    # erase the login details after clicking login
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    Userfound = False

    all_users = db.child("Users").get()

    hashuser = encrypt_master(username1)
    hashpass = encrypt_master(password1)

    for users in all_users.each():
        if (users.val()['name'] == hashuser):
            Userfound = True
            if (users.val()['password'] == hashpass):
                all_users = db.child("Users").get()
                for user in all_users.each():
                    if (hashuser == user.val()['name']):
                        global useruid
                        global masterpw
                        useruid = user.key()
                        masterpw = user.val()['password']
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
    login_success_screen.geometry("650x525")
    Label(login_success_screen, text="Login Authorized", width=90, height=2, bg="orange", font=("Arial", 20)).pack()

    Label(login_success_screen, text="").pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Store Password", font=("Arial", 16), bg="orange", command=store).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text=" Update Password", font=("Arial", 16), bg="orange", command=Update).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Search", font=("Arial", 16), bg="orange", command=Search).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Sync Locally", font=("Arial", 16), bg="orange", command=Sync).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Password Generator", font=("Arial", 16), bg="orange", command=password_generator_page).pack()
    Label(login_success_screen, text="").pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Exit", font=("Arial", 16), bg="orange", command=delete_login_success).pack()


#password generator page
def password_generator_page():
    global generator_screen
    generator_screen = Toplevel(login_success_screen)
    generator_screen.title("Password Generator")
    generator_screen.geometry("650x525")
    
    global password_length
    global pwd_length_input
    global pwd_gen
    global SpecChar
    global UpperChar
    global LowerChar
    global NumChar
    global pwd_space 

    password_length = IntVar()
    pwd_gen = StringVar()
    SpecChar = BooleanVar()
    UpperChar = BooleanVar()
    LowerChar = BooleanVar()
    NumChar = BooleanVar()
    pwd_space = ""
    
    
#int input for password length (minimum 12)
    Label(generator_screen, text="Enter desired password length: Number between 12 and 32", font=("Arial", 17), width=100, bg="orange", height=2).pack()
    Label(generator_screen, text="").pack()
    pwd_length_Label = Label(generator_screen, text="Password Length: ", font=("Arial", 14)).pack()
    pwd_length_input = Entry(generator_screen, textvariable=password_length, font=("Arial", 14), width=4)
    pwd_length_input.pack()
    
    Label(generator_screen, text="").pack()
    Label(generator_screen, text="I need this password to have:")
    
 
    c1 = Checkbutton(generator_screen, text="Special Characters", variable=SpecChar, onvalue = True, offvalue= False, command = addSpecChar, font=("Arial", 14))
    c1.pack()
    c2 = Checkbutton(generator_screen, text="Upper Case", variable=UpperChar, onvalue = True, offvalue = False, command = addUpperChar, font=("Arial", 14))
    c2.pack()
    c3 = Checkbutton(generator_screen, text="Lower Case", variable=LowerChar, onvalue = True, offvalue=False, command = addLowerChar, font=("Arial", 14))
    c3.pack()
    c4 = Checkbutton(generator_screen, text="Numbers", variable=NumChar, onvalue = True, offvalue = False, command = addNumChar, font=("Arial", 14))
    c4.pack()
    
    
    Label(generator_screen, text="").pack()
    Button(generator_screen, text="Generate password", font=("Arial", 14), width=20, height=1, bg="orange", command=pwd_generator).pack()
    Label(generator_screen, text="").pack()
    Entry(generator_screen , textvariable = pwd_gen, font=("Arial", 14), width=36).pack()
    Label(generator_screen, text="").pack()
    
    Button(generator_screen, text = 'Copy to Clipboard', font=("Arial", 14), width=20, height=1, bg="orange", command = copy_password).pack()
    Label(generator_screen, text="").pack()
    Button(generator_screen, text="Exit", font=("Arial", 14), bg="orange", command=delete_pwd_generator).pack()
    Label(generator_screen, text="").pack()
    

#Copy Password
def copy_password():
    pyperclip.copy(pwd_gen.get())

    
def addSpecChar():
    global pwd_space
    if SpecChar.get() == True:
        pwd_space+=random.choice(string.punctuation)
    else: 
        return pwd_space
        
        
def addUpperChar():     
    global pwd_space
    if UpperChar.get() == True:
        pwd_space+= string.ascii_uppercase
    else: 
        return pwd_space
        
def addLowerChar():
    global pwd_space
    if LowerChar.get() == True:
        pwd_space+= string.ascii_lowercase
    else: 
        return pwd_space
        
def addNumChar():
    global pwd_space
    if NumChar.get() == True:
        pwd_space+=string.digits 
    else: 
        return pwd_space
        
        
def pwd_generator():

    pwd_len = password_length.get()
    if pwd_len < 12 or pwd_len > 32:
        Invalid_entry()

    else:
        pwd_output = [random.choice(pwd_space) for x in range(pwd_len)]
    
        """pwd_output = ([random.choice(char) for x in range(pwd_len - 4 )]
                     + [random.choice(string.ascii_lowercase
                              + string.ascii_uppercase
                              + string.punctuation
                              + string.digits) for i in range(4)])"""
   
        random.shuffle(pwd_output)
        password = ''.join(pwd_output)
    
        pwd_gen.set(password)
   

def Invalid_entry():
    global Invalid_screen
    Invalid_screen = Toplevel(login_screen)
    Invalid_screen.title("Unsuccessful")
    Invalid_screen.geometry("400x250")
    Label(Invalid_screen, text="").pack()
    Label(Invalid_screen, text="Invalid entry, please enter a value between 12 and 32", font=("Arial", 16)).pack()
    Label(Invalid_screen, text="").pack()
    Button(Invalid_screen, text="OK", font=("Arial", 16), bg="orange", command=delete_Invalid_screen).pack()

def delete_Invalid_entry():
    Invalid_screen.destroy()  

def delete_pwd_generator():
    generator_screen.destroy()

#end of password generator


def Update():
    global update_account
    update_account = Toplevel(login_success_screen)
    update_account.title("Update Password Info")
    update_account.geometry("650x525")

    # text variables
    global updatename
    global updateword
    global updatewebsite
    global updatename_entry
    global updateword_entry
    global website_entry
    
    
    updatename = StringVar()
    updateword = StringVar()
    updatewebsite = StringVar()
    iv = StringVar()

    Label(update_account, text="Please update information below", font=("Arial", 20), width=60,bg="orange", height=2).pack()
    Label(update_account, text="").pack()
    username_lable = Label(update_account, text="Username: ", font=("Arial", 18)).pack()
    updatename_entry = Entry(update_account, textvariable=updatename, font=("Arial", 16), width=30)
    updatename_entry.pack()
    Label(update_account, text="").pack()
    Label(update_account, text="").pack()
    site_lable = Label(update_account, text="Website: ", font=("Arial", 18)).pack()
    website_entry = Entry(update_account, textvariable=updatewebsite, font=("Arial", 16), width=30)
    website_entry.pack()
    Label(update_account, text="").pack()
    Label(update_account, text="").pack()
    password_lable = Label(update_account, text="New Password: ", font=("Arial", 18)).pack()
    updateword_entry = Entry(update_account, textvariable=updateword, font=("Arial", 16), width=30)
    updateword_entry.pack()
    Label(update_account, text="").pack()
    Label(update_account, text="").pack()
    Label(update_account, text="").pack()

    Button(update_account, text="Click here to update", font=("Arial", 16), width=20, height=1, bg="orange", command=UpdatePassword).pack()


def listMessageBox(arr):
    window=Tk()
    window.title("Compromised Passwords")
    window.geometry("500x200")    
    listbox=Listbox(window)
    listbox.pack(fill=BOTH, expand=1) #adds listbox to window
    [listbox.insert(END, row) for row in arr] #one line for loop
    window.mainloop()

def UpdatePassword():

    username = updatename.get()
    website = updatewebsite.get()
    password = updateword.get()
    global useruid
    global masterpw
    global cwd
    storage_info = useruid 
    #update pw locally

    database = r"%s\pythonsqlite.db" % cwd
    conn = create_connection(database)

    nonce, encrypted = encrypt_firebase_pw(password, masterpw)
    with conn:
        update_password(conn, (encrypted, nonce, username, website))

    all_users = db.child("Users").child(storage_info).get()
    length = 0
    if (all_users.each() is not None):
        for users in all_users.each():
            length = length + 1
        
    length = length - 2
    current = 0 
    found = False
    decryptedold = ""

    if (all_users.each() is not None):
        for users in all_users.each():
            if (current < length):
                if (users.val()['website'] == website):
                    if (users.val()['name'] == username): 
                        found = True
                        decryptedold = decrypt_firebase_pw(users.val()['password'], users.val()['nonce'], masterpw)
                        print (users.key())
                        nonce, encrypted = encrypt_firebase_pw(password, masterpw)
                        db.child("Users").child(storage_info).child(users.key()).update({"password": encrypted, "nonce": nonce})
                current = current + 1
    if (found == False):
        messagebox.showinfo(title="Oops", message="There was no entry found.")
    else:
        all_users = db.child("Users").child(storage_info).get()
        length = 0
        if (all_users.each() is not None):
            for users in all_users.each():
                length = length + 1
            
        length = length - 2
        current = 0 
        found = False
        arr = ["placeholder"]
        if (all_users.each() is not None):
            for users in all_users.each():
                if (current < length):
                    decrypted = decrypt_firebase_pw(users.val()['password'], users.val()['nonce'], masterpw)
                    if (decrypted == decryptedold):
                        arr.append(users.val()['website'] + ": " + users.val()['name'])
                    current = current + 1

        arr[0] = "You have " + str(len(arr)-1) + " compromised passwords for the following websites and usernames:"
    
        listMessageBox(arr)
    

def Sync():
    global useruid
    global masterpw
    main(useruid, masterpw)
    messagebox.showinfo(title="Successful Sync", message="Your data has been successfully synced locally.")

def Search():
    global search
    global search_entry
    global site_entry
    global searchvar
    global sitevar
    searchvar = StringVar()
    sitevar = StringVar()
    search = Toplevel(login_success_screen)
    search.geometry("650x525")
    search.title("Search Username")
    Label(search, text="Search Username below", font=("Arial", 20), bg="orange", width=60, height=2).pack()
    Label(search, text="").pack()
    Label(search, text="").pack()
    Label(search, text="Username: ", font=("Arial", 18)).pack()
    search_entry = Entry(search, textvariable= searchvar, font=("Arial", 16), width=30)
    search_entry.pack()
    Label(search, text="").pack()
    Label(search, text="").pack()
    Label(search, text="Website: ", font=("Arial", 18)).pack()
    site_entry = Entry(search, textvariable=sitevar, font=("Arial", 16), width=30)
    site_entry.pack()
    Label(search, text="").pack()
    Label(search, text="").pack()
    Label(search, text="").pack()
    Label(search, text="").pack()
    Button(search, text="Search", font=("Arial", 18), bg="orange", command=FoundUser).pack()

def FoundUser():
    storage_info = useruid
    username = searchvar.get()
    website = sitevar.get()
    global masterpw

    found = False

    if len(username) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure that each and every field is filled up")
        
    # search locally first

    passwordfound = decrypt_pw(website, username, masterpw)

    if (passwordfound != False):
        print ("here")
        found = True
        Label(search, text=passwordfound, fg="orange", font=("calibri", 11)).pack()

    if (found == False):
        all_users = db.child("Users").child(storage_info).get()

        length = 0
        if (all_users.each() is not None):
            for users in all_users.each():
                length = length + 1
        
        length = length - 2
        current = 0 

        print (length)

        if (all_users.each() is not None):
            for users in all_users.each():
                if (current < length):
                    if (users.val()['website'] == website):
                        if (users.val()['name'] == username):
                            decrypted = decrypt_firebase_pw(users.val()['password'], users.val()['nonce'], masterpw)
                            found = True
                            Label(search, text=decrypted, fg="orange", font=("calibri", 11)).pack()
                    current = current + 1
    if (found == False):
        Label(search, text="Entry not found", fg="orange", font=("calibri", 11)).pack()

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
    main_screen.geometry("650x525")  # size of the window
    main_screen.title("Account Login")  # window title
    Label(text="Password Manager", bg="Orange", width="300", height="2", font=("Arial", 34)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="User Login", bg="orange", height="1", width="25", command=login,font=("Arial", 20)).pack()  # login button
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="User Registration", bg="orange", height="1", width="25", command=register,font=("Arial", 20)).pack()  # register button
    Label(text="").pack()


    main_screen.mainloop()  # intializes GUI


main_account_screen()
