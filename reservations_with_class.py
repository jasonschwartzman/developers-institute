import sqlite3

class Reservation:

class User:

class Room:

class Payment:

class BookingInfo:

class BookingHistory:



def open_database_connection():
	conn = sqlite3.connect('/Users/yaakovschwartzman/reservations.db')
	c = conn.cursor()
	return c

def close_database_connection(c):
	c.close()
	return

def not_paid_users():
	c = open_database_connection()
	results = c.execute('''Select User.* From User Where User.UserId Not in (Select Userid from Payments)''').fetchall()
	close_database_connection(c)
	return results

def add_new_user(first, last, phone, email, address):
	c = open_database_connection()
	# do something
	close_database_connection(c)
	return

def add_new_booking(userid, roomid, startdate, enddate):
	c = open_database_connection()
	# do something
	close_database_connection(c)
	return

def add_new_booking_history(userid, roomid, arrivaldate, departuredate):
	c = open_database_connection()
	# do something
	close_database_connection(c)
	return

def change_user_information(userid, first, last, phone, email, address):
	c = open_database_connection()
	# do something
	close_database_connection(c)
	return

def add_new_payment(userid, lastdigits, cardtype, paymentdate, amount, currency):
	c = open_database_connection()
	# do something
	close_database_connection(c)
	return

my_results = not_paid_users()
print("First", "Last Name", "Phone", "Email")
for line in my_results:
	print(line[1], line[2], line[3], line[4])


