#!/usr/bin/env python
# coding=utf-8

#   实现要点：  正/负值绝对值大于数组长度则添加在数组末尾和首位，负数绝对值小于数组
#   长度，则用index_len(list)来处理；若插入位置刚好是None，则直接替换。
#
#   注意：  元素插入需要考虑扩容问题，如果原本数组已满，则需要扩容


class Array(object):
    def __init__(self, lst):
        self.size = len(lst)
        self.lst = lst

    def insert(self, index, e):
        count = 0   #   判断数组是否存在None值
        if index < 0:
            if (-index) > self.size:    #   下标处理
                index = 0
            else:
                index = index + self.size
        if index > self.size:
            print(index)
            index = self.size
            print(index)
        #   None值判断及优化
        if self.lst[index-1] is None:
            self.lst[index-1] = e
            return self.lst
        else:
            for i in range(self.size-1, index, -1):
                if self.lst[i] is None:
                    count += 1
        if count == 0:      #   没有None值，扩容数组
            self.resize()
        #   插入数据
        for i in range(self.size-2, index-1, -1):
            if (self.lst[i] is not None) and (self.lst[i+1] is None):
                self.lst[i+1] = self.lst[i]
                self.lst[i] = None
        self.lst[index] = e
        return self.lst

    def resize(self):
        self.size = self.size * 2
        lst1 = [None for i in range(self.size)]
        for i in range(len(self.lst)):
            lst1[i] = self.lst[i]
        #   self.lst = lst1.copy()  list.copy方法在Python2.x和Python3.x中都不起作用，母鸡为毛
        self.lst = lst1

if __name__ == "__main__":
    my_list = [0,1,2,3,4,5,6,7,8,9,None]
    my_array = Array(my_list)
    my_array.insert(10,88)
    print(my_array.lst)
