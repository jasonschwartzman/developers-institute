import sqlite3

def open_database_connection():
    conn = sqlite3.connect('/Users/yaakovschwartzman/Desktop/reservations.db')
    #conn = sqlite3.connect('/home/jason/PycharmProjects/developers-institute/reservations.db')
    return conn

def close_database_connection(c):
    c.close()
    return

def insert_new_user(conn, firstname, lastname, email, phone, address):
    c = conn.cursor()
    c.execute("insert into User (Lastname, Firstname, Phone, Email, Address) values (?, ?, ?, ?, ?)",
              (lastname, firstname, email, phone, address))
    new_user = c.execute("select * from User where Lastname = '"+ lastname +"' order by Userid desc limit 1").fetchone()
    conn.commit()
    return new_user

def insert_new_room(conn, location, entrycode, numbeds, numbaths):
    c = conn.cursor()
    c.execute("insert into Room (Location, Entrycode, Numbeds, Numbaths) values (?, ?, ?, ?)",
              (location, entrycode, numbeds, numbaths))
    new_room = c.execute(
        "select * from Room where Location = '" + location + "' order by Roomid desc limit 1").fetchone()
    conn.commit()
    return new_room

def insert_new_reservation(conn, userid, roomid, startdate, enddate):
    c = conn.cursor()
    c.execute("insert into Booking_info (RoomId, UserId, StartDate, EndDate) values (?, ?, ?, ?)",
              (roomid, userid, startdate, enddate))
    conn.commit()
    return

class User:

    def __init__(self):
        self.userid = ""
        self.firstname = ""
        self.lastname =""
        self.phone =""
        self.email =""
        self.address =""
        self.lastlogin =""
        return


    def store_user_in_db(self):
        connection = open_database_connection()
        new_user = insert_new_user(connection, self.firstname, self.lastname, self.phone, self.email, self.address)
        close_database_connection(connection)
        if len(new_user) > 0:
            self.userid = new_user[0]
            self.lastlogin = new_user[6]
        else:
            print("Your data was not saved.")
        return

    def add(self, firstname, lastname, phone, email, address):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address
        self.store_user_in_db()
        return

    def get(self, userid):
        #retrieve from db
        self.lastname = lastname

class Room:

    def __init__(self):
        self.roomid = ""
        self.location = ""
        self.entrycode = ""
        self.numbeds = ""
        self.numbaths = ""
        return

    def add(self, location, entrycode, numbeds, numbaths):
        self.location = location
        self.entrycode = entrycode
        self.numbeds = numbeds
        self.numbaths = numbaths
        self.store_room_in_db()
        return

    def store_room_in_db(self):
        connection = open_database_connection()
        new_room = insert_new_room(connection, self.location, self.entrycode, self.numbeds, self.numbaths)
        close_database_connection(connection)
        if len(new_room) > 0:
            self.roomid = new_room[0]
        return


class Reservation:


    def __init__(self):
        self.user = User()
        self.room = Room()
        self.startdate = ""
        self.enddate =""
        return

    def add(self, user, room, startdate, enddate):
        self.user = user
        self.room = room
        self.startdate = startdate
        self.enddate = enddate
        self.store_reservation_in_db()
        return

    def store_reservation_in_db(self):
        connection = open_database_connection()
        insert_new_reservation(connection, self.user.userid, self.room.roomid, self.startdate, self.enddate)
        close_database_connection(connection)
        return

my_user = User()
my_user.add("jason", "black", "0656666666", "abc@gmail.com", "123 main")
print("Your user is: ", my_user.userid, my_user.firstname, my_user.lastname)

my_room = Room()
my_room.add("123 main", "9999", 2, 2)
print("Your room is:", my_room.roomid, my_room.location)

my_reservation = Reservation()
my_reservation.add(my_user, my_room, "01/01/2020", "01/30/2020")
print("Your reservation is: ", my_reservation.user.lastname, my_reservation.room.location)
