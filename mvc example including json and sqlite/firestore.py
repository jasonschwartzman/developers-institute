import json
import sqlite3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def open_firebase():
    cred = credentials.Certificate("/home/jason/PycharmProjects/developers-institute/mvc example including json and sqlite/mvc-example-85de8-firebase-adminsdk-j8015-99aa57407c.json")
    firebase_admin.initialize_app(cred, {
        'projectId': 'mvc-example-85de8',
    })

    db = firestore.client()
    return db



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
    def getAllFirestore(self):
        db = open_firebase()
        # Then query for documents
        person_ref = db.collection(u'person')
        docs = person_ref.get()
        result = []
        for doc in docs:
            item = doc.to_dict()
            person = Person(item['last_name'], item['first_name'], item['phone'], doc.id)
            result.append(person)
        return result

