total = 0

multiples_three = []
multiples_five = []

for i in range(0,1000):
	if i % 3 == 0:
		print "%d is a multiple of 3" % i
		multiples_three.append(i)
	elif i % 5 == 0:
		print "%d is a multiple of 5" % i
		multiples_five.append(i)
	else:
		print "%d not a multiple of 3 or 5" % i

all_nums = multiples_three
all_nums.extend(multiples_five)

#print all_nums

for i in all_nums:
	total += i

print len(all_nums)
print total



# Alternative solution. See how the use of or is very helpful. 
# Also, no need to create lists and then sum. Can just directly add to result

result = 0
for i in range(0,1000):
	if i % 3 == 0 or i % 5 == 0:
		result += i

print result




