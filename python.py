# add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175

big_list = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# x = 
# for a in a_list:
#     for b in a:
#         if 

overall_sum = 0
# for baby_list in big_list:
#     smallest = baby_list[0]
#     for number in baby_list:
#         if number < smallest:
#             smallest = number
#     overall_sum += number 


b = [sum(min(i) for i in big_list)] 
print(b[0])

overall_sum = 0
for baby_list in big_list:
    smallest = baby_list[0]
    for num in baby_list:
        if num < smallest:
            smallest = num
    overall_sum += smallest

print(overall_sum)
