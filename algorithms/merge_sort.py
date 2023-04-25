list_1 = [10, 1, 5, 9, 100, 1, 4, 39, 10, 11, 2]

def merge_sort(alist):
    middle = len(alist) // 2
    left_half = alist[:middle]
    right_half = alist[middle:]

    #recursively call merge until groups of 1
    if len(alist) > 1:
        merge_sort(left_half)
        merge_sort(right_half)

    # compare the elements from left half and right half plugging into list sorted
    left_point = right_point = main_point = 0

    while left_point < len(left_half) and right_point < len(right_half):
        if left_half[left_point] < right_half[right_point]:
            alist[main_point] = left_half[left_point]
            left_point += 1
        else: 
            alist[main_point] = right_half[right_point]
            right_point += 1
        main_point += 1

    # add any remaining elements from each list
    while left_point < len(left_half):
        alist[main_point] = left_half[left_point]
        left_point += 1
        main_point += 1

    while right_point < len(right_half):
        alist[main_point] = right_half[right_point]
        right_point += 1
        main_point += 1
        
merge_sort(list_1)

print(list_1)