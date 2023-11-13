smallest_so_far = 4
print(smallest_so_far)
for the_num in [9, 10, 23, 3, 74] :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)