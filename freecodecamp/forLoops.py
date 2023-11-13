# finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9 , 12, 24, 18, 122, 23, 87] :
    if the_num > largest_so_far :
        largest_so_far = the_num
        break
    print(largest_so_far, the_num)
print('After', largest_so_far)