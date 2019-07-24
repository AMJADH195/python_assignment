"""
3. Take input of age of 3 people by user and determine oldest and youngest among them.
"""
a=input("Enter the age of A :")
b=input("Enter the age of B :")
c=input("Enter the age of C :")

if(a>b and a>c):
	print("The oldest person is A")
elif(b>a and b>c):
	print("The oldest person is B")
else:
	print("The oldest person is C")

if(a<b and a<c):
	print("The youngest person is A")
elif(b<a and b<c):
	print("The youngest person is B")
else:
	print("The youngest person is C")




