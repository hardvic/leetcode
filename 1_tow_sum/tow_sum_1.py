# !/usr/env/bin python
# -*- coding: utf-8 -*-

__author__ = 'mrhero'


class Solution(object):
    """
    16 / 16 test cases passed.
    Status: Accepted
    Runtime: 1052 ms
    Your runtime beats 26.79% of python submissions.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for key, value in enumerate(nums):
            the_other_one = target - value
            if key + 1 == len(nums):
                return []
            try:
                the_other_one_index = nums[key+1:].index(the_other_one) + key + 1
            except ValueError, e:
                continue

            return [key, the_other_one_index]
        return []
