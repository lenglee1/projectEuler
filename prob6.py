import math

total = 0
number = 0

for i in range(1,101):
	total += i**2
	number += i

num_sq = number **2

print total
print num_sq

diff = num_sq - total

print diff



# Learnt that when summing numbers 1 to n, that equals n(n+1)/2 
# And that square of sums always equals the sum of cubes (ie. if change the 2 on line 7 to a 3) and this holds for all n





