#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:pitmaner
# Datetime:2019/5/15 5:47 PM
# Software: PyCharm
# Project: practise-ml
# Filename: greedy


def large_coun_sum(arr):

    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:

        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


arr = [1, 2, -1, 3, 4, 10, 10, -10, -1, -1]

print large_coun_sum(arr)