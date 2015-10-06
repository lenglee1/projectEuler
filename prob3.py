import math

all_factors = []

limit = int(math.floor(math.sqrt(600851475143))) + 1

for i in range(1, limit):
	if 600851475143 % i == 0:
		all_factors.append(i)

print all_factors

primes = []

def is_prime(num):
	if num % 2 == 0:
		print "{0} is not a factor of 2".format(num)
		return False
	for i in range(3, int(math.floor(math.sqrt(num))), 2):
		if num % i == 0:
			print "{0} is a factor of {1}".format(i, num)
			print "{0} is not a prime".format(num)
			return False
	else:
		print "{0} is a prime".format(num)
		primes.append(num)
		return True
		


for i in all_factors:
	is_prime(i)

print primes

result = primes[-1]

print result






