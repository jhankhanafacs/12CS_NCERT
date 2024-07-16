#Write a program with a user-defined function with string as a parameter 
#which replaces all vowels in the string with ‘*’.
def strep(str):

# convert string into list

     str_lst =list(str) 

# Iterate list                         

     for i in range(len(str_lst)):

# Each Character Check with Vowels                

          if str_lst[i] in 'aeiouAEIOU':

# Replace ith position vowel with'*'          

               str_lst[i]='*'  

#to join the characters into a new string.                   

               new_str = "".join(str_lst)   
     return new_str

def main():
     line = input("Enter string: ")
     print("Orginal  String")
     print(line)
     print("After replacing Vowels with '*'")
     print(strep(line))
main()
 