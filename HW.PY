import mysql.connector
import datetime
from datetime import date
connection = mysql.connector.connect(host="cis3368.coiz58yyxzqm.us-east-2.rds.amazonaws.com", user="mfcasti3", passwd="mcastillov101", database="cis3368db")




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
      
      
      cursor = connection.cursor()# creates the connection to the database it is in all the code for every entry
      name = input("contactdetails:")
      val = date.today()
      
      
      cursor.execute("INSERT INTO contacts (contactDetails, creationDate) VALUES ('{}', '{}')".format(name, val))#excute accepts the connection and creates it

      connection.commit()#commits the code to the datebase

      print(cursor.rowcount, "inserted.")
#deleting values from id 
    elif ans=="d":
      cursor = connection.cursor()
      name_id = int(input('Please, enter an ID: '))  #tried printing the data first to see which one to delete but had many errors but just simply type the number
      statement = "DELETE FROM `contacts` WHERE id = %s"
      cursor.execute(statement, (name_id,))
      connection.commit()

      
# could not figure it out
    elif ans == "u":
      cursor = connection.cursor()
      id = input("Please enter updadeted info:")
      statement = "UPDATE contacts SET contactDetails = %s"
      cursor.execute(statement)
      connection.commit()
      
      
      
    elif ans == "b": 
      cursor = connection.cursor()
      statement = "SELECT * FROM contacts ORDER BY contactDetails ASC" #acensding order for abc
      cursor.execute(statement)
      
      result = cursor.fetchall()#used fetchall to return rows of the query later on printing results to view it w3schools
      print(result)
    
    elif ans == "c": 
      cursor = connection.cursor()
      statement = "SELECT * FROM contacts ORDER BY creationDate ASC"
      cursor.execute(statement)
            

      result = cursor.fetchall() #used fetchall to return rows of the query later on printing results to view it w3schools
      print(result)
      
    elif ans == "o":
     cursor = connection.cursor()
     cursor.execute("SELECT * FROM contacts")
     result = cursor.fetchall() #used fetchall to return rows of the query later on printing results to view it w3schools
     '''
     for x in result:
         print(x)
    '''
     print(result)
     
     

    elif ans == "q":
      print("Thank you")
      break #end the code
    
