# 7. Program to count the number of even numbers and odd numbers in a list
oddc=0
evenc=0
a=input("Enter the  limit :")
l=[]
for i in range(0,a):
	v=input("Enter the  value :")
	l.append(v)
print l
for i in l:
	if(i%2==0):
		evenc=evenc+1
	else:
		oddc=oddc+1
print "Total odd number in the list is : ",oddc
print "Total even number in the list is : ",evenc


