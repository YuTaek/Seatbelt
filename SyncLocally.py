#This is the logic behind saving information locally if the user requests syncing

import sqlite3
from sqlite3 import Error
import pyrebase
import os
cwd = os.getcwd()
#Cite:
#https://www.sqlitetutorial.net/sqlite-python/create-tables/


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


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_password(conn, password):
    """
    Create a new password
    :param conn:
    :param password:
    :return:
    """

    sql = ''' INSERT INTO passwords(website, password, nonce, username)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, password)
    conn.commit()
    return cur.lastrowid


def find_encrypted(conn, website, username):
    
    cur = conn.cursor()
    try:
        cur.execute("SELECT password FROM passwords WHERE website=? AND username=?", (website,username))
    except:
        return False
    rows = cur.fetchall()

    for row in rows:
        return row[0]

def update_pw(conn, website, username, newpw, nonce):
    cur = conn.cursor()
    cur.execute("UPDATE passwords SET password=? WHERE website=? AND username=?", (newpw,website,username))
    cur.execute("UPDATE passwords SET nonce =? WHERE website=? AND username=?", (nonce,website,username))
    
def update_password(conn, task):
    """
    update password
    """
    sql = ''' UPDATE passwords
              SET password = ? ,
                  nonce = ?
              WHERE username = ? AND website = ?'''
    cur = conn.cursor()
    try:
        cur.execute(sql, task)    
    except:
     return False
    conn.commit()

def find_nonce(conn, website, username):
    
    cur = conn.cursor()
    try:
        cur.execute("SELECT nonce FROM passwords WHERE website=? AND username=?", (website, username))
    except:
        return False

    rows = cur.fetchall()

    for row in rows:
        return row[0]

def delete (conn):
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE passwords")
    except:
        return False



def main(useruid, masterpw):
    database = r"%s\pythonsqlite.db" % cwd
    sql_create_passwords_table = """ CREATE TABLE IF NOT EXISTS passwords (
                                        website text,
                                        username text,
                                        password text NOT NULL,
                                        nonce text NOT NULL,
                                        PRIMARY KEY (website, username)
                                    ); """

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        create_table(conn, sql_create_passwords_table)
        all_users = db.child("Users").child(useruid).get()
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
                print (users.val())
                pw1 = (users.val()['website'], users.val()['password'], users.val()['nonce'], users.val()['name'])
                
                database = r"%s\pythonsqlite.db" % cwd
                conn = create_connection(database)
                with conn:
                    try:
                        create_password(conn, pw1)
                    except:
                        print ("dupe")
                current = current + 1
        print ("exit") 
        # this is where it would loop through the db to put into the local db
        #pw1 = ('google', encryptedpw, nonce)
        #create_password(conn, pw1)
        
#if __name__ == '__main__':
#    main()


