import sys 
import hashlib 

from Crypto.Cipher import AES
from SyncLocally import *


if sys.version_info < (3, 6): 
    import sha3 
  


#This would be utilized to check the master password 
def encrypt_master(plaintext):
    # create a sha3 hash object 
    hash_sha3_512 = hashlib.new("sha3_512", plaintext.encode()) 
    print("\nSHA3-512 Hash: ", hash_sha3_512.hexdigest()) 



#this is utilized to encrypt and store pw locally
def encrypt_pw(website, data, master):
        """Encrypts the password using EAX and the master pw as the key
        
        Arguments:
            website: website for pw
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
        
        pw1 = (website, encrypted_data, nonce)

        database = r"C:\Users\RC\Documents\Seatbelt\pythonsqlite.db"
        conn = create_connection(database)
        with conn:
            create_password(conn, pw1)

#access pw locally and decrypts
def decrypt_pw(website, master):
    """Returns the ciphertext decrypted.
    
    Arguments:
        website: the website to be accessed
        cipher: the cipher of the pw trying to be accessed
        master: the master password
    """    
     #add padding, just in case it is not 16 long
    padded = master + "++++++++++++++++"
    master_pass_encoded = padded[:16].encode("utf-8")

    database = r"C:\Users\RC\Documents\Seatbelt\pythonsqlite.db"
    conn = create_connection(database)
    
    with conn:
        ciphertext = find_encrypted(conn, website)
        nonce = find_nonce(conn, website)

    nonce = bytes.fromhex(nonce)
    password = bytes.fromhex(ciphertext)

    cipher = AES.new(master_pass_encoded, AES.MODE_EAX, nonce)
 
    plaintext = cipher.decrypt(password).decode("utf-8")

    return plaintext


print (decrypt_pw("google", "waseem54"))

