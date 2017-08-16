# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_035.py
@time: 2017/7/11 16:24
"""
# 合唱队
def lower_bound(nums, target):
    low, high = 0, len(nums) - 1
    pos = len(nums)
    while low<high:
        mid = (low+high)/2
        if nums[mid]<target :
            low = mid+1
        else :
            high = mid
            pos  = high
    return pos

def deal(l, res):
    b = [9999]*len(l)
    b[0]= l[0]
    res = res+[1]
    for i in range(1, len(l)):
        pos = lower_bound(b, l[i]) - 0
        res+=[pos+1]
        b[pos]=l[i]
    return res

while True:
    try:
        n = int(input())
        q = [int(i) for i in raw_input().strip().split()]
        dp_1 = []
        dp_2 = []
        dp_1= deal(q, dp_1)
        q.reverse()
        dp_2 = deal(q, dp_2)
        dp_2.reverse()
        a = max([dp_1[i]+dp_2[i] for i in range(n)])
        print n-a+1
    except:
        break

