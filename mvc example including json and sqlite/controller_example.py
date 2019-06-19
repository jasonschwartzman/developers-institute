from model_example import Person
import view_example as view

def showAll():
   #gets list of all Person objects
   #people_in_db = Person.getAll()
   #people_in_db = Person.getAllDB()
   people_in_db = Person.getAllDBSQLALCHEMY()
   #people_in_db = Person.getAllFirestore()
   #calls view
   return view.showAllView(people_in_db)

def start():
   view.startView()
   answer = input("")
   if answer == 'y':
      return showAll()
   else:
      return view.endView()

if __name__ == "__main__":
   #running controller function
   start()