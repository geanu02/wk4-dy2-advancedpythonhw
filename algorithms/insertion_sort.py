list_a = [10, 1, 9, 111, 5, 9, 10]

def insertion_sort(alist):
    for i in range(1, len(alist)):
        current_value = alist[i]
        j = i - 1
        while current_value < alist[j] and j >= 0:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = current_value

insertion_sort(list_a)
print(list_a)

