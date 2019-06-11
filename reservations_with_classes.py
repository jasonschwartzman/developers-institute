import sqlite3

def open_database_connection():
    conn = sqlite3.connect('/Users/yaakovschwartzman/reservations.db')
    c = conn.cursor()
    return c

def close_database_connection(c):
    c.close()
    return

def insert_new_user(c, firstname, lastname, email, phone, address):
    c.execute("insert into User (Lastname, Firstname, Phone, Email, Address) values (?, ?, ?, ?, ?)",
              (lastname, firstname, email, phone, address))
    return

class User:

    def __int__(self):
        userid = ""
        firstname = ""
        lastname =""
        phone =""
        email =""
        address =""
        lastlogin =""


    def store_user_in_db(self):
        connection = open_database_connection()
        insert_new_user(connection, self.firstname, self.lastname, self.phone, self.email, self.address)
        close_database_connection(connection)


    def add(self, firstname, lastname, phone, email, address):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address
        # store in db



    def get(self, userid):
        #retrieve from db
        self.lastname = lastname




my_user = User()
my_user.add("jason", "black", "0656666666", "abc@gmail.com", "123 main")
