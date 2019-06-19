import json
import sqlite3
import sqlalchemy as db
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore

#def open_firebase():
#    #cred = credentials.Certificate("/Users/yaakovschwartzman/PycharmProjects/new_developers-institute/mvc example including json and sqlite/mvc-example-85de8-firebase-adminsdk-j8015-99aa57407c.json")
#    cred = credentials.Certificate("/Users/yaakovschwartzman/PycharmProjects/new_developers-institute/mvc example including json and sqlite/my-new-cloud-database-firebase-adminsdk-mdx7u-c463d4be88.json")
#    #firebase_admin.initialize_app(cred, {
#    #    'projectId': 'mvc-example-85de8',
#    #})
#    firebase_admin.initialize_app(cred, {
#       'projectId': 'my-new-cloud-database',
#    })

#    db = firestore.client()
#    return db


def open_rds_connection():
    conn = mysql.connector.connect(
        host="di-test.cluster-cuaie290qfbf.eu-west-1.rds.amazonaws.com:3306",
        user="diadmin",
        passwd="diadmin613!"
    )
    return conn

def open_database_connection():
    conn = sqlite3.connect('people.db')

    return conn

def close_database_connection(c):
    c.close()
    return


class Person(object):
    def __init__(self, first_name=None, last_name=None, phone=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.id = id

    # returns Person name, ex: John Doe
    def name(self):
        #return str(self.first_name)+" "+str(self.last_name)
        return ("%s %s" % (self.first_name, self.last_name))

    @classmethod
    # returns all people inside db.json as list of Person objects
    def getAll(self):
        with open('db.json', 'r') as file:
            json_list = json.load(file)
        result = []
        for item in json_list:
            person = Person(item['first_name'], item['last_name'], item['phone'])
            result.append(person)
        return result



    @classmethod
    def getAllDB(self):
        conn = open_database_connection()
        c = conn.cursor()
        record_list = c.execute(
            '''Select first_name, last_name, phone, id from person''').fetchall()
        close_database_connection(c)
        result = []
        for item in record_list:
            person = Person(item[0], item[1], item[2], item[3])
            result.append(person)
        return result

    @classmethod
    def getAllDBSQLALCHEMY(self):
        engine = db.create_engine('sqlite:///people.db')
        # Create a bridge (or connection) with the database through the engine object
        connection = engine.connect()
        metadata = db.MetaData()
        persons = db.Table('person', metadata, autoload=True, autoload_with=engine)
        query = db.select([persons])
        record_list = connection.execute(query).fetchall()
        result = []
        #  PSST:   You really don't need to use the object person anymore... you have record_list with everything....
        # Take a look
        for item in record_list:
            person = Person(item[0], item[1], item[2], item[3])
            result.append(person)
        return result



#    @classmethod
#    def getAllFirestore(self):
#        db = open_firebase()
#        # Then query for documents
#        person_ref = db.collection(u'person')
#        docs = person_ref.get()
#        result = []
#        for doc in docs:
#            item = doc.to_dict()
#            person = Person(item['last_name'], item['first_name'], item['phone'], doc.id)
#            result.append(person)
#        return result

#    def addNewFirestore(self, last_name, first_name):
#        db = open_firebase()
#        person_ref = db.collection(u'person')
#        doc_ref = person_ref.document()
#        doc_ref.set({u'first_name': first_name, u'last_name': last_name})
