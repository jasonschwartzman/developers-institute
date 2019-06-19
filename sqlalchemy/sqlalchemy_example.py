import sqlalchemy as db
engine = db.create_engine('sqlite:////Users/yaakovschwartzman/PycharmProjects/d/flask/flask-example-master/database_file/users.db')
connection = engine.connect()
metadata = db.MetaData()
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
query2 = db.select([users]).where(users.columns.id == 'ADMIN')
ResultProxy = connection.execute(query2)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
