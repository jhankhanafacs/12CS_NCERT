
'''
Write a program to input percentage marks of a student and find the grade as per following criterion:
Marks           Grade
>=90             A
75-90            B 
60-75            C     
Below 60         D
'''
a=float(input('Enter the percentage marks:'))
if a>=90:
     print('The student has got an A grade')
elif a>=75 and a<90:
     print('The student has got a B grade')
elif a>=60 and a<75:
     print('The student has got a C grade')
else:
     print('The student has got a D grade')