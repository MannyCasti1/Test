import mysql.connector
import datetime
from datetime import date
connection = mysql.connector.connect(host="cis3368.coiz58yyxzqm.us-east-2.rds.amazonaws.com", user="mfcasti3", passwd="mcastillov101", database="cis3368db")



#tried using the code for class everything worked except the excute part
'''

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#from class
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
'''
ans=True
while ans:
    print("Menu")
    print("a - add contact")
    print('d - Remove contact')
    print('u - Update contact details')
    print('b - Output all contacts in alphabrtical order')
    print("c - Output all contacts creation date")
    print("o - Output all contacts")
    print("q - Quit")
    
    ans = input("Please enter letter: ") 
    
    if ans=="a":
      #source from w3schools creates the coonection and excute
      
      cursor = connection.cursor() # creates the connection to the database, its in every single input on the code this is because it made it simple to understand
      name = input("contactdetails:")
      val = date.today()
      
      #Had to make the excution my statemenet because other methods where not working
      #code from class and w3 schools inserts the values using the .format 
      cursor.execute("INSERT INTO contacts (contactDetails, creationDate) VALUES ('{}', '{}')".format(name, val)
      connection.commit()

      
      print(cursor.rowcount, "inserted.")
#deleting values from id 
    elif ans=="d":
      cursor = connection.cursor()
      name_id = int(input('Please, enter an ID: '))  #tried printing the data first to see which one to delete but had many errors but just simply type the number
      statmt = "DELETE FROM `contacts` WHERE id = %s" 
      cursor.execute(statmt, (name_id,))
      connection.commit()

      
#updating values tried implementing different methods but did not excute
'''
    elif ans == "u":
      cursor = connection.cursor()
      id = input("Please enter updadeted info:")
      ver = "UPDATE contacts SET contactDetails = {id}"
      cursor.execute(ver)
      connection.commit()
      print(cursor.rowcount, "record(s) affected")
'''      
      # order through ABC
    elif ans == "b": 
      cursor = connection.cursor()
      ver = "SELECT * FROM contacts ORDER BY contactDetails ASC"
      cursor.execute(ver)
      #used fetchall to return rows of the query later on printing results to view it
      result = cursor.fetchall()
      print(result)
    # ordering for creationDate
    elif ans == "c": 
      cursor = connection.cursor()
      ver = "SELECT * FROM contacts ORDER BY creationDate ASC"
      cursor.execute(ver)
            #used fetchall to return rows of the query later on printing results to view it

      result = cursor.fetchall()
      print(result)
      
    elif ans == "o":
     cursor = connection.cursor()
     cursor.execute("SELECT * FROM contacts")
     result = cursor.fetchall()#used fetchall to return rows of the query later on printing results to view it w3schools
     for x in result: #organizes the code to make it look good
        print(x)
     
#finally breaking the code after user input q
    elif ans == "q":
      print("Thank you")
      break
    

      
   