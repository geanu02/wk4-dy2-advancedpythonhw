# Auxilary variables are made, only accessible within the function
# Return is required

def swap_out_of_place(alist, index1, index2):
    alist_copy = alist[:]
    alist_copy[index1], alist_copy[index2] = alist_copy[index2], alist_copy[index1]
    return alist_copy

swapped_list = swap_out_of_place([1,2,3,4,5,10], 2, -1)
print(swapped_list)