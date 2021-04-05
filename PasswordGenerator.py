
#password generator page
def password_generator_page():
    global generator_screen
    generator_screen = Toplevel(login_success_screen)
    generator_screen.title("Password Generator")
    generator_screen.geometry("600x400")
    
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
    Label(generator_screen, text="Enter Desired password length: Number between 12 and 32", font=("Arial", 14), width=100, bg="orange").pack()
    Label(generator_screen, text="").pack()
    pwd_length_Label = Label(generator_screen, text="Password Length: ", font=("Arial", 16)).pack()
    pwd_length_input = Entry(generator_screen, textvariable=password_length, font=("Arial", 16), width=4)
    pwd_length_input.pack()
    
    Label(generator_screen, text="").pack()
    Label(generator_screen, text="I need this password to have:")
    
 
    c1 = Checkbutton(generator_screen, text="Special Characters", variable=SpecChar, onvalue = True, offvalue= False, command = addSpecChar)
    c1.pack()
    c2 = Checkbutton(generator_screen, text="Upper Case", variable=UpperChar, onvalue = True, offvalue = False, command = addUpperChar)
    c2.pack()
    c3 = Checkbutton(generator_screen, text="Lower Case", variable=LowerChar, onvalue = True, offvalue=False, command = addLowerChar)
    c3.pack()
    c4 = Checkbutton(generator_screen, text="Numbers", variable=NumChar, onvalue = True, offvalue = False, command = addNumChar)
    c4.pack()
    
    
    Label(generator_screen, text="").pack()
    Button(generator_screen, text="Generate password", font=("Arial", 16), width=20, height=1, bg="orange", command=pwd_generator).pack()
    Label(generator_screen, text="").pack()
    Entry(generator_screen , textvariable = pwd_gen, font=("Arial", 16), width=32).pack()
    Label(generator_screen, text="").pack()
    
    Button(generator_screen, text = 'Copy to Clipboard', font=("Arial", 16), width=32, height=1, bg="orange", command = copy_password).pack()
    Label(generator_screen, text="").pack()
    Button(generator_screen, text="Exit", font=("Arial", 16), bg="orange", command=delete_pwd_generator).pack()
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
    Button(Invalid_screen, text="OK", font=("Arial", 16), bg="orange",
           command=delete_Invalid_screen).pack()

def delete_Invalid_entry():
    Invalid_screen.destroy()  

def delete_pwd_generator():
    generator_screen.destroy()

#end of password generator
