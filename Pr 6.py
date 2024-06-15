
# WAP to accept values from user and create a tuple.
t=tuple()
n=int(input("How many values you want to enter: "))
for i in range(n): 
     a=input("Enter Number: ")
     t=t+(a,) 
print("Entered Numbers are: ")
print(t)