# Write a program to input n numbers from the user.
# Store these numbers in a tuple. Print the maximum,
# minimum, sum and mean of number from this tuple.

numbers = tuple() #create an empty tuple 'numbers'
n = int(input("How many numbers you want to enter?: "))
print("Enter any ",n," numbers")
for i in range(0,n):
     num = int(input())
#it will assign numbers entered by user to tuple 'numbers'
     numbers = numbers +(num,)
print('\nThe numbers in the tuple are:')
print(numbers)
print("\nThe maximum number is: ")
print(max(numbers))
print("The minimum number is: ")
print(min(numbers))
print("The sum of numbers is: ")
print(sum(numbers))
print("The mean of numbers is: ")
mean = sum(numbers)/(i+1)
print(mean)
ele=int(input("Enter the element to be searched: "))
if ele in numbers:
     print("Element found")
else:
     print("Element not found")