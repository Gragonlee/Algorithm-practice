#!/usr/bin/env python
# coding=utf-8
#
#   注意：仅当数组是有序数组时，二分查找才有意义
#   二分查找时间复杂度n个元素数组时间复杂度O(n)=logn
#
#

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_lst = [1,3,5,7,9,11,13,15,17,21,23,25,27]
print(binary_search(my_lst, 13))
