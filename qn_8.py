# 8. Program to find the numbers divisible by 5 or 7 in a list. Find the product of such numbers

a=input("Enter the  limit :")
l=[]
d=[]
for i in range(0,a):
	v=input("Enter the  value :")
	l.append(v)
print l
for i in range(0,a):
	if(l[i]%5==0 or l[i]%7==0):
		d.append(l[i])
print("Numbers divisible by 5 and 7 are : ")
print d
pro=d[0]
for i in range(1,len(d)):
	pro = pro * d[i]
print("product of numbers:")
print(pro)
