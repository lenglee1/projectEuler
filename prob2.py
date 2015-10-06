x = [1,2]

while x[-1] < 4000000:
		x.append( x[-1] + x[-2])

if x[-1] > 4000000:
	x.pop()

result = 0
elements = []

for i in x:
	if i % 2 == 0:
		elements.append(i)
		result += i

print elements
print result


