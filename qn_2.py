n=input("Enter the number to find factorial : ")
fact=1;
if n<0:
	print("factorial for negative number does not exist ")
elif n==0:
	print("factorial of 0 = 0 ")
else:
	for i in range(1,n+1):
		fact=fact*i
	print 'Factorial of ',n,'=',fact
