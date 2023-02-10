# Python program to print 
# odd Prime numbers 

# Function to check prime 
def isPrime(n) : 
	
	# Corner cases 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True
	
	# This is checked so that we can skip 
	# middle five numbers in below loop 
	if (n % 2 == 0 or n % 3 == 0) : 
		return False
	
	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6
	
	return True

# Driver Program to test above function 
count = 0 
n = 2 
while (count < 1000): 
	if (isPrime(n) and n % 2 != 0): 
		print(n, end = " ") 
		count += 1
	n += 1
