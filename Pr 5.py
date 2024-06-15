#Find the largest/smallest number in a list/tuple
# creating empty list 
list1 = [] 
  
# asking number of elements to put in list 
num = int(input("Enter number of elements in list: ")) 
  
# iterating till num to append elements in list 
for i in range(1, num + 1): 
    ele= int(input("Enter elements: ")) 
    list1.append(ele) 
      
# print maximum element 
print("Largest element is:", max(list1))

# print minimum element 
print("Smallest element is:", min(list1)) 