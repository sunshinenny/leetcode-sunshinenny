#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (34.43%)
# Total Accepted:    47.8K
# Total Submissions: 138.7K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        l.sort()
        length=len(l)
        mid=length//2
        if length%2==1:
            return float(l[mid])
        else:
            return float((l[mid-1]+l[mid])/2)
神仙='''
class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> float:
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        mid = l//2
        if l%2:
            output = nums[mid]
        else:
            output = (nums[mid-1] + nums[mid])/2
        return output
解法和我的类似,不过忘记怎么计算时间复杂度了
不清楚我们的答案是否符合时间复杂度要求
'''
