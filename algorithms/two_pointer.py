def reverse_list(alist):
    left, right = 0, len(alist) - 1
    while left < right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

reverse_list(alist)

print(alist)

str1 = 'racecar'
str2 = 'racercar'

def check_palindrome(astring):
    left, right = 0, len(astring) - 1
    while left < right:
        if astring[left] == astring[right]:
            left += 1
            right -= 1
        else:
            return f"{astring} is not a palindrome."
    return f"{astring} is a palindrome."

print(check_palindrome(str2))
