#15.	Remove all the lines that contain the character 'a' in a file 
#and write it to another file. 

f1 = open("Mydoc.txt")
f2 = open("copyMydoc.txt","w")
for line in f1:
     if 'a' not in line:
          f2.write(line)
print('## File Copied Successfully! ##')
f1.close()
f2.close()

f2 = open("copyMydoc.txt","r")
print(f2.read())