# WAP to input any two tuples and swap their values.
t1 = tuple()
n = int (input("Total no of values in First tuple: "))
for i in range(n):
     a = input("Enter Elements : ")
     t1 = t1 + (a,)
t2 = tuple()
m = int (input("Total no of values in Second tuple: "))
for i in range(m):
     a = input("Enter Elements : ")
     t2 = t2 + (a,)
print("First Tuple : ")
print(t1)
print("Second Tuple : ")
print(t2)

t1,t2 = t2, t1

print("After Swapping: ")
print("First Tuple : ")
print(t1)
print("Second Tuple : ")
print(t2)