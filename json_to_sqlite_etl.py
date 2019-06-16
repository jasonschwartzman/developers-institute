import json
import sqlite3

def open_db():
    conn = sqlite3.connect('/Users/yaakovschwartzman/people.db')
    return conn

def close_db(conn):
    conn.close()
    return

def read_from_json():
    #open json file and add to json_list
    with open('db.json', 'r') as file:
        json_list = json.load(file)
    result = []
    for item in json_list:
        person = {"first_name": item['first_name'],
                  "last_name": item['last_name'],
                  "phone": item['phone']}
        result.append(person)
    return result

def save_to_db(json_list):
    conn = open_db()
    c = conn.cursor()
    # loop through json_list and save
    for item in json_list:
        c.execute("insert into person2 (first_name, last_name, phone) values (?, ?, ?)",
                  (item['first_name'], item['last_name'], item['phone']))
    conn.commit()
    close_db(conn)

    return

def main():
    json_list = read_from_json()
    save_to_db(json_list)
