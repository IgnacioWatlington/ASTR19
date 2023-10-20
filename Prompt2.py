#Write a Python that prints the sum of two floating point numbers
#the difference between two integers
#the product of a floating point number and an integer. 
#In each case, have the program print out the data type of the resulting answer

Fnumber_a = 4.3
Fnumber_b = 5.7
Integer_a = 9
Integer_b = 6 

a = Fnumber_a - Fnumber_b
print (f"Diff of two floating numbers:{a:.1f}")
print(type(a))
b = Integer_a - Integer_b
print (f"Diff of two integers:{b}")
print(type(b))
c = (Fnumber_a*Integer_b)
print (f"Product of an integer and a floatprint {c:.1f}")
print(type(c))