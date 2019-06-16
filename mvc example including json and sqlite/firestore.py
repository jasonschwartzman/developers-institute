import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/home/jason/PycharmProjects/developers-institute/mvc example including json and sqlite/mvc-example-85de8-firebase-adminsdk-j8015-99aa57407c.json")
firebase_admin.initialize_app(cred, {
  'projectId': 'mvc-example-85de8',
})

db = firestore.client()

# Then query for documents
person_ref = db.collection(u'person')
docs = person_ref.get()

for doc in docs:
    #print(u'{} => {}'.format(doc.id, doc.to_dict()))
    person = doc.to_dict()
    print(person['first_name'], person['last_name'], person['phone'])
