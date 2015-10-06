# To find lowest common multiple, go through from 2 to 20 and list the prime factors of each number.
# Then multiply each factor the greatest number of times it occurs in either number. 
# If the same factor occurs more than once in both numbers, you multiply the factor the greatest number of times it occurs.


# answer = 2*2*2*2 * 3*3 * 5 * 7 * 11 * 13 * 17 * 19

# print answer



# If want to use Python code, this is from the forum

i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print i