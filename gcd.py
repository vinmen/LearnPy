
def gcd(m, n):
	low = m
	if n < m:
		low = n
	
	for i in range(low, 0, -1):		
		if m % i == 0 and n % i == 0:
			return i	
	
def euclid_gcd(m, n):	

	if m % n == 0:
		return n
	else:		
		return euclid_gcd(n, m % n)

if __name__ == "__main__":
	print(gcd(5, 16))
	print(euclid_gcd(8, 12))