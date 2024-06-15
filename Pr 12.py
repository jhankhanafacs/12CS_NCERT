
# WAP to display frequencies of all the elements of a list.
L= [3, 21, 5, 6, 3, 8, 21, 6] 
L1= [ ] 
L2= [ ] 
print ('Element' , ' \t' , 'frequency' )

for i in L: 
     if i not in L2: 
          x=L.count(i) 
          L1.append(x) 
          L2.append(i) 
     
for i in range(len(L1)): 
     print (L2[i],'\t\t\t',L1[i])