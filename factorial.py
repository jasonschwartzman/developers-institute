def new_factorial_way(n):
	if n<2:
		return 1
	else:
		return (n*new_factorial_way(n-1))


def factorial(n):
	total = 1
	for i in range(1,n):
		total*=i
	return total

n = int(input("What is the n to calculate: "))
#print("factorial:", factorial(n))
print("New Factorial way", new_factorial_way(n))
