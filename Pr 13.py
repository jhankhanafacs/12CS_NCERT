#Read a text file line by line and display each word separated by a #.
filein = open("Mydoc.txt",'r')
line =" "
while line:
     line = filein.readline()
     #print(line)
     for w in line:
          if w == ' ':
               print('#',end = '')
          else:
               print(w,end = '')
filein.close()


'''
#-------------OR------------------

filein = open("Mydoc.txt",'r')
for  line in filein:
     word= line .split()
     for w in word:
          print(w + '#',end ='')
     print()
filein.close()

'''