# 6. Take 10 integers from keyboard using loop and print their average value on the screen.
s=0
for i in range(1,11):
	n=input("Enter the number ")
	s=s+n
avg=s/10
print 'average of the numbers is = ',avg