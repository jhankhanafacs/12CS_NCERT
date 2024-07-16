#14.	Read a text file and display the number of vowels/consonants/uppercase
#/lowercase characters in the file. 

filein = open("Mydoc1.txt",'r')
line = filein.read()
count_vow = 0
count_con = 0
count_low = 0
count_up = 0
count_digit = 0
count_other = 0
print(line)
for ch in line:
     if ch.isupper():
          count_up +=1
     if ch.islower():
          count_low += 1
     if ch in 'aeiouAEIOU':
          count_vow += 1
     if ch.isalpha():
          count_con += 1
     if ch.isdigit():
          count_digit += 1
     if not ch.isalnum() and ch !=' ' and ch !='\n':
          count_other += 1
          
print("Digits",count_digit)          
print("Vowels: ",count_vow)
print("Consonants: ",count_con-count_vow)
print("Upper Case: ",count_up)
print("Lower Case: ",count_low)
print("other than letters and digit: ",count_other)

filein.close()