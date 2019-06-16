import json

class Person(object):
    def __init__(self, first_name=None, last_name=None, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

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