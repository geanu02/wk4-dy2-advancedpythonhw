# taking in an input
# directly mutates inputs
#.sorted() vs sorted() is out-of-place

# def swap_indecies(alist, index1, index2):
#     index1_value = alist[index1]
#     alist[index1] = alist[index2]
#     alist[index2] = index1_value

# num_list = [9,10,1,2]
# swap_indecies(num_list, 1, 2)

# print(num_list)

# def swap_indexes(alist, index1, index2):
#     alist[index1], alist[index2] = alist[index2], alist[index1]
#     return alist

# new_list = swap_indexes([2, 5, 10, 3], 0, -1)
# print(new_list)

num_list = [9,10,1,2,3,5]

def swap_indexes(alist, index1, index2, index3):
    alist[index1], alist[index2], alist[index3] = alist[index3], alist[index2], alist[index1]
    return alist