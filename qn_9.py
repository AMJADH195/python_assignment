"""
9. Program to create a list of numbers and find their average. Change the list by changing all numbers greater than
   or equal to average by 1 and others to 0
"""
a=input("Enter the  number of elements in the list :")
avg=0
s=0
l=[]
for i in range(0,a):
	v=input("Enter the  value :")
	l.append(v)
	s=s+v
avg=s/a
print l
for i in range(0,len(l)):
	if l[i]>=avg:
		l[i]=1
	else:
		l[i]=0
print("list after change")
print l




