import math

bigNumList = []

for i in range(100, 1000):
	for j in range(100, 1000):
		if i * j / 100000 > 1:
			bigNumList.append(i*j)

num_dict = {}
pallindromes = []

for number in bigNumList:
	num_dict[number] = str(number)
	if num_dict[number][0] == num_dict[number][-1] and num_dict[number][1] == num_dict[number][-2] and num_dict[number][2] == num_dict[number][-3]:
		pallindromes.append(num_dict[number])

for i in range(len(pallindromes)):
	pallindromes[i] = int(pallindromes[i])

pallindromes.sort()
print pallindromes

print "The answer is {0}!!!".format(pallindromes[-1])


