Seatbelt is a simple password manager that can be synced locally or using Firestore. This is a project created for COMP4109.


## Group Members:</p>
Yutaek Hwang: 101073993 </p>
Naveed Hossain: 101049011</p>
Zarish Owais: 100712733</p>
RC Syed: 101049886</p>

## Contents
1. [Overview](#Overview)
2. [Utilization](#Utilization)
3. [Credits](#Credits)

## Overview

This password generator acts as a tool that is able to generate a password that follow the guidelines a user sets. Additionally, the password manager would have a secure storage and management of passwords in an encrypted database and allow user to receive them on demand. 

### Step 1: Dependencies
This program is created utilizing python, so the user must have python downloaded in order to run the program. Additionally, this program utilizes pyrebase, so the user must run:

```pip install pyrebase```

### Step 1: Clone the Repo
```git clone https://github.com/YuTaek/Seatbelt.git```</p>

```cd Seatbelt```

### Step 2: Run the Program
``` python GUI_Manager.py```


## Utilization

</p>

## Credits


**RC Syed**

Roles:
Assisted in storing and retrieving passwords, implemented the login and registration capabalities with Firestore, implemented local syncing and storing and retrieving with SQLite, implemented the update feature and finding compromised passwords, implemented the sha3 hashing for user login and storage of login, and the block cipher method EAX for the storage of passwords, implemented the decryption of passwords when storing them 

**Yutaek Hwang**

Roles:
Implementing the GUI

**Naveed Hossain**

Roles:
Created Firestore database, implemented the storage and retrieval of passwords in Firestore

**Zarish Owais**

Roles:
Created password generating capabilities
