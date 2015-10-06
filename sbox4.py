import math

# list = [898, 521, 8283, 93910, 813318, 919383, 393, 18393, 9009, 893189, 80208, 800008, 347743]
# list = sorted(list, reverse = True)

# print list

# bigNumList = []

# for i in list:
# 	if i / 100000 > 1:
# 		bigNumList.append(i)

# print bigNumList

# num_dict = {}
# pallindromes = []

# for number in bigNumList:
# 	num_dict[number] = str(number)
# 	if num_dict[number][0] == num_dict[number][-1] and num_dict[number][1] == num_dict[number][-2] and num_dict[number][2] == num_dict[number][-3]:
# 		pallindromes.append(num_dict[number])

# print pallindromes




# print x

# while True:
# 	for i in range(len(x)):
		
# 		if x[i][0] == x[i][-1] and x[i][1] == x[i][-2] and x[i][2] == x[i][-3]:
# 			print x[i]
# 	break





# If want to remove the middle number in an integer with odd number of digits, the code below works
# Note that when divide any number, it will round down the answer. eg. 39 / 40 gives 0.

# for key in num_dict:
# 	if len(num_dict[key]) % 2 != 0:
# 		midlen = len(num_dict[key]) / 2
# 		num_dict[key] = num_dict[key][:midlen] + num_dict[key][midlen+1:]



# Need to build a list of numbers that are the products of 3 digit numbers

bigNumList = []

for i in range(1, 1000):
	for j in range(1, 1000):
		if i * j / 100000 > 1:
			bigNumList.append(i*j)
		

print bigNumList






