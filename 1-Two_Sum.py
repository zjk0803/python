# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:21:03 2018

@author: 抖抖飞
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,num in enumerate(nums):
            if target-num in d:
                return [d[target-num],i]
            d[num]=i
    
twoSum()