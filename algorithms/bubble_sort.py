list_1 = [10, 8, 1, 4, 9, 3, 12]

def bubble_sort(alist):
    is_not_sorted = True
    right_boundary = len(alist) - 1
    while is_not_sorted:
        is_not_sorted = False
        for i in range(right_boundary):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                is_not_sorted = True
        right_boundary -= 1

bubble_sort(list_1)
print(list_1)