import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
#Create Datatbase
#mycursor.execute("CREATE DATABASE mydemo")


#Check if Database Exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)



