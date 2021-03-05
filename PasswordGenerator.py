from tkinter import *
import random, string
import pyperclip

char  = string.ascii_letters + string.digits + string.punctuation

#Password generator page
def password_generator_page():
    global generator_screen
    generator_screen = Toplevel(pwdgenerator_screen)
    generator_screen.title("Password Generator")
    generator_screen.geometry("400x250")
    
    global password_length
    global pwd_length_input
    global pwd_gen
    password_length = IntVar()
    pwd_gen = StringVar()
    
#int input for password length (minimum 12)
    Label(generator_screen, text="What is the desired password length? Please enter a number between 12 and 32", font=("Arial", 17), width=60, bg="orange").pack()
    Label(generator_screen, text="").pack()
    pwd_length_Label = Label(generator_screen, text="Password Length: ", font=("Arial", 16)).pack()
    pwd_length_input = Entry(generator_screen, textvariable=password_length)
    pwd_length_input.pack()
    
    Label(generator_screen, text="").pack()
    Button(generator_screen, text="Generate password", font=("Arial", 16), width=20, height=1, bg="orange", command = pwd_generator).pack()
    Entry(generator_screen , textvariable = pwd_gen).pack()
    Label(generator_screen, text="").pack()
    Button(generator_screen, text = 'COPY TO CLIPBOARD', command = copy_password).pack()

    
#Copy Password
def copy_password():
    pyperclip.copy(pwd_gen.get())


def pwd_generator():
    
    pwd_len = password_length.get()
    
    pwd_output = ([random.choice(char) for x in range(pwd_len - 4 )]
                 + [random.choice(string.ascii_lowercase
                          + string.ascii_uppercase
                          + string.punctuation
                          + string.digits) for i in range(4)])
    
    random.shuffle(pwd_output)
    password = ''.join(pwd_output)
    
    pwd_gen.set(password)


def pwdgenerator_screen():
    global pwdgenerator_screen
    pwdgenerator_screen = Tk()      # GUI window creation
    pwdgenerator_screen.geometry("400x300")     # size of the window
    pwdgenerator_screen.title("Password Generator")      # window title 
    Label(text="Password Generator", bg="Orange", width="300", height="2", font=("Arial", 23)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Generate Password", bg="orange", height="1", width="20", command = password_generator_page, font=("Arial", 16)).pack()       
    Label(text="").pack()
    Label(text="").pack()

    pwdgenerator_screen.mainloop() # intializes GUI 
 
 
pwdgenerator_screen()
