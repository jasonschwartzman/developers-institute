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

def insert_new_room(c, location, entrycode, numbeds, numbaths):
    c.execute("insert into Room (Location, Entrycode, Numbeds, Numbaths) values (?, ?, ?, ?)",
              (location, entrycode, numbeds, numbaths))
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

class Room:

    def __init__(self):
        location = ""
        entrycode = ""
        numbeds = ""
        numbaths = ""

    def add(self, location, entrycode, numbeds, numbaths):
        self.location = location
        self.entrycode = entrycode
        self.numbeds = numbeds
        self.numbaths = numbaths

    def store_room_in_db(self):
        connection = open_database_connection()
        insert_new_room(connection, self.location, self.entrycode, self.numbeds, self.numbaths)
        close_database_connection(connection)


class Reservation:


    def __init__self(self):
        user = User()
        room = Room()
        startdate = ""
        enddate =""

    def add(self, user, room, startdate, enddate):
        self.user = user
        self.room = room
        self.startdate = startdate
        self.enddate = enddate


my_user = User()
my_user.add("jason", "black", "0656666666", "abc@gmail.com", "123 main")

my_room = Room()
my_room.add("123 main", "9999", 2, 2)


my_reservation = Reservation()
my_reservation.add_new_booking(my_user, my_room, "01/01/2020", "01/30/2020")

what would this mean?
my_reservation.user.lastname
my_reservation.room.location













