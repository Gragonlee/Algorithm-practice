#!/usr/bin/env python
# coding=utf-8

#   选择排序的思想：从第一个位置开始比较，找出最小的元素，
#   和第一个位置的元素进行交换，再开始下一轮
#
#   选择排序特点：选择排序是一种不稳定排序，但平均时间复杂度始终为O(n2)
#   时间复杂度可以使用堆排序进行优化

#   差性能版本选择排序算法，循环中找到最小元素就交换一次，增加内存占用
def select_sort_c(list1):
    n = len(list1)
    for i in range(n-1):    #   开启循环
        for j in range(i+1, n): #   假设第i个位置元素最小
            if list1[j] < list1[i]: #   找到比最小值还小的数，交换位置
                list1[i], list1[j] = list1[j], list1[i]
    return list1


#   较好性能版本选择排序算法
def select_sort_b(list1):
    n = len(list1)
    count = 0  #    统计更改次数
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if list1[j] < list1[min_index]: #   找到后面存在比最小值还小的元素
                min_index = j
        if min_index != i:  #   判断当前最小值是不是在i所在位置
            list1[i], list1[min_index] = list1[min_index], list1[i]
            count += 1
    print("交换次数：", count)
    return list1


#   性能更好的选择排序实现
def select_sort_a(list1):
    n = len(list1)
    for i in range(n//2):
        min_mark = i
        max_mark = n-i-1
        for j in range(i+1, n-i):
            if list1[j] < list1[min_mark]:
                min_mark = j
        if min_mark != i:
            list1[i], list1[min_mark] = list1[min_mark], list1[i]
        for j in range(n-i-2, i, -1):
            if list1[j] > list1[max_mark]:
                max_mark = j
        if max_mark != (n-i-1):
            list1[n-i-1], list1[max_mark] = list1[max_mark], list1[n-i-1]
    return list1

if __name__ == '__main__':
    a = [1,0,3,5,9,6,11,7,14,8,20,15]
    print(select_sort_a(a))
