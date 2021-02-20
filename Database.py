import pyrebase

# This is a firebase database with some examples of it's functions
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

# Push Data
data = {"name": "JOHN", "password": "DINOSAUR"}
# db.push(data)

# Create Key
data2 = {"password": "DINOSAUR"}
db.child("John").set(data2)

# Create key and path with child
data3 = {"password": ["DINO", "SAUR"]}
db.child("User").child("John").set(data2)
db.child("User").child("Sam").set(data2)
db.child("User").child("John").set(data3)

# Receive Data
john = db.child("User").child("John").get()
print(john.val())

# receive All keys replace .key() with .value() to receive all data

users = db.child("User").get()
for user in users.each():
    print(user.key())

# delete item with known key
# db.child("User").child("John").remove()

# Update Data
#db.child("User").child("John").update({"password": "T-rex"})

# Update data in multiple location
data = {"Users/John": {"password": "Test"}, "Users/Sam": {"password": "dog"}}
db.update(data)







