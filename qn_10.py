"""
 10.Program to create a new list by getting input from the user. Create another list containing the cube of numbers
  in the given list
"""
a=input("Enter the  number of elements in the list :")
l=[]
cu=[]
for i in range(0,a):
	v=input("Enter the  value :")
	l.append(v)
	p = pow(v,3)
	cu.append(p)
print(cu)
	