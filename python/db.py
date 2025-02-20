#importing the SQLite module

import sqlite3
from sqlite3.dbapi2 import Cursor
#this line of code prints the sqlite version.

print("sqlite version" + " " + sqlite3.sqlite_version)

#the line of code below creates a database and connects to that database

conn = sqlite3.connect(database.db)
c = conn.cursor()


#we had to comment this out to avoid recreating the table
try:
  db.execute(''' CREATE TABLE users(
    [generated_ID] INTEGER PRIMARY KEY, [first_name] text, [last_name] text, [email] blob, [phone] blob
) ''' )  
except _sqlite3.Error as error:
    print('Error creating table',error)    
 try:
  db.execute("INSERT INTO users VALUES ('2','john','kahenya', 'kahenyaa@gmail.com ','0700419377')")
  except _sqlite3.Error as error:
    print('Error creating table',error) 
#     save changes
conn.commit()
#fcommented for testing purpose

#conn.close()


#create query
search_query = """ SELECT * FROM users """

#execute query with cursor
c.execute(search_query)

#fetch all
records = c.fetchall()
print(records)


