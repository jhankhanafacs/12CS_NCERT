#Insert a record in the "customers" table:
#mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

#mydb.commit()

print(mycursor.rowcount, "record inserted.")
