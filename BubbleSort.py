#!/usr/bin/env python
# coding=utf-8

#   冒泡排序思想：检查数组中相邻的成对元素，一次查看一对，如果
#   前面个元素大于后面个元素，则交换他们的位置，否则继续移动
#
#   冒泡排序特点：每种情况下，性能最差的算法之一

def bullte_sort(input_list):
    n = len(input_list)
    #   记录最后一次交换元素的位置
    lastExchangeIndex = 0
    #   无序数组的边界
    sort = n - 1
    for i in range(n):
        #   有序数组的标记
        flag = True
        for j in range(0, sort):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                flag = False
                lastExchangeIndex = j
        sort = lastExchangeIndex
        if flag:
            break
    return input_list

a = [1,0,3,5,9,6,11,7,14,8,20,15]

print(bullte_sort(a))
