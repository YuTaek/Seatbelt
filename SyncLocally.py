#This is the logic behind saving information locally if the user requests syncing

import sqlite3
from sqlite3 import Error

#Cite:
#https://www.sqlitetutorial.net/sqlite-python/create-tables/


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

    sql = ''' INSERT INTO passwords(website, password, nonce)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, password)
    conn.commit()
    return cur.lastrowid


def find_encrypted(conn, website):
    
    cur = conn.cursor()
    cur.execute("SELECT password FROM passwords WHERE website=?", (website,))

    rows = cur.fetchall()

    for row in rows:
        return row[0]

def find_nonce(conn, website):
    
    cur = conn.cursor()
    cur.execute("SELECT nonce FROM passwords WHERE website=?", (website,))

    rows = cur.fetchall()

    for row in rows:
        return row[0]


def main():
    database = r"C:\Users\RC\Documents\Seatbelt\pythonsqlite.db"
    sql_create_passwords_table = """ CREATE TABLE IF NOT EXISTS passwords (
                                        website text PRIMARY KEY,
                                        password text NOT NULL,
                                        nonce text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        create_table(conn, sql_create_passwords_table)
        # this is where it would loop through the db to put into the local db
        #pw1 = ('google', encryptedpw, nonce)
        #create_password(conn, pw1)
        
if __name__ == '__main__':
    main()


