import sqlalchemy as db
# Creates an object with the connection to the PHYSICAL DATABASE
engine = db.create_engine('sqlite:////Users/yaakovschwartzman/PycharmProjects/d/flask/flask-example-master/database_file/users.db')
# Create a bridge (or connection) with the database through the engine object
connection = engine.connect()
# Get all the schema and database information
metadata = db.MetaData()
# Make a object with the metadata from the specific table that you want
users = db.Table('users', metadata, autoload=True, autoload_with=engine)
# Print the column names
print(users.columns.keys())
# Print full table metadata
print(repr(metadata.tables['users']))
# This is like the Select *
query = db.select([users])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
# Here it is compacted to one HARD TO READ LINE
ResultSet = connection.execute(db.select([users])).fetchall()
print(ResultSet)
query2 = db.select([users]).where(users.columns.id == 'ADMIN')
ResultProxy = connection.execute(query2)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
results = connection.execute(query)
#Example of an update
query = db.update(users).values(id="YAAKOV").where(users.columns.id=='YAAKOV2')
results = connection.execute(query)
#Example of an insert
#Inserting record one by one
query = db.insert(users).values(id='NEWUSER', pw='jhksdhkdhfkjhsd')
ResultProxy = connection.execute(query)


