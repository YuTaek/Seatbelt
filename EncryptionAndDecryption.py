import sys 
import hashlib 

from Crypto.Cipher import AES
from SyncLocally import *
import os
cwd = os.getcwd()
print (cwd)

#This would be utilized to check the master password and username
def encrypt_master(plaintext):
    # create a sha3 hash object 
    hash_sha3_512 = hashlib.new("sha3_512", plaintext.encode()) 
    return (hash_sha3_512.hexdigest())



#this is utilized to encrypt and store pw locally
def encrypt_pw(website, username, data, master):
        """Encrypts the password using EAX and the master pw as the key
        
        Arguments:
            website: website for pw
            username: website for pw
            data: password to be encrypted
            master: the master password
        """        

        #add padding, just in case it is not 16 long
        padded = master + "++++++++++++++++"

        key = padded[:16].encode("utf-8")

        cipher = AES.new(key, AES.MODE_EAX)

    
        nonce = cipher.nonce.hex()
        data_to_encrypt = data.encode("utf-8")
        
        encrypted_data = cipher.encrypt(data_to_encrypt).hex()
        
        pw1 = (website, encrypted_data, nonce, username)

        database = r"%s\pythonsqlite.db" % cwd
        conn = create_connection(database)
        with conn:
            try:
                create_password(conn, pw1)
                return True
            except:
                return False

#access pw locally and decrypts
def decrypt_pw(website, username, master):
    """Returns the ciphertext decrypted.
    
    Arguments:
        website: the website to be accessed
        username: website for pw
        master: the master password
    """    
     #add padding, just in case it is not 16 long
    padded = master + "++++++++++++++++"
    master_pass_encoded = padded[:16].encode("utf-8")

    database = r"%s\pythonsqlite.db" % cwd

    print (database)
    conn = create_connection(database)
    
    with conn:
        ciphertext = find_encrypted(conn, website, username)
        nonce = find_nonce(conn, website, username)

    if (nonce is None):
        return False

    nonce = bytes.fromhex(nonce)
    password = bytes.fromhex(ciphertext)
    print (nonce)
    print (password)

    cipher = AES.new(master_pass_encoded, AES.MODE_EAX, nonce)
 
    plaintext = cipher.decrypt(password).decode("utf-8")

    return plaintext

def encrypt_firebase_pw(data, master):
        """Encrypts the password using EAX and the master pw as the key
        
        Arguments:
            data: password to be encrypted
            master: the master password
        """        

        #add padding, just in case it is not 16 long
        padded = master + "++++++++++++++++"

        key = padded[:16].encode("utf-8")

        cipher = AES.new(key, AES.MODE_EAX)

    
        nonce = cipher.nonce.hex()
        data_to_encrypt = data.encode("utf-8")
        
        encrypted_data = cipher.encrypt(data_to_encrypt).hex()
        return (nonce, encrypted_data)
       
def decrypt_firebase_pw(ciphertext, nonce, master):
    """Returns the ciphertext decrypted.
    
    Arguments:
        cipher: the cipher of the pw trying to be accessed
        nonce: the nonce of the cipher
        master: the master password
    """    
     #add padding, just in case it is not 16 long
    padded = master + "++++++++++++++++"
    master_pass_encoded = padded[:16].encode("utf-8")


    nonce = bytes.fromhex(nonce)
    password = bytes.fromhex(ciphertext)

    cipher = AES.new(master_pass_encoded, AES.MODE_EAX, nonce)
 
    plaintext = cipher.decrypt(password).decode("utf-8")

    return plaintext
