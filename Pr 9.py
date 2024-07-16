#WAP to store students’ details like admission number, roll number, name and percentage in a dictionary and display information on the basis of admission number.

record = dict ()
i=1
n= int (input ("How many records u want to enter: "))
while(i<=n):
     Adm = input("Enter Admission number: ")
     roll = input("Enter Roll Number: ")
     name = input("Enter Name :")
     perc = float(input("Enter Percentage : "))
     t = (roll,name, perc)
     record[Adm] = t
     i = i + 1
Nkey = record.keys() 
for i in Nkey:
     print("\nAdmno- ", i, " :")
     r = record[i]
     print("Roll No\t", "Name\t", "Percentage\t")
     for j in r:
          print(j, end = "\t")