#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (53.45%)
# Total Accepted:    41.3K
# Total Submissions: 77.3K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 一边删除一边添加,即可达成效果
        # 1. 只操作原数组
        # 2. 少用遍历
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
最快的解法='''
冒泡排序
if not nums:
            return []
        zi = len(nums)
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0 and not flag:
                zi = i
                flag = True
            elif zi < len(nums):
                nums[i], nums[zi] = nums[zi], nums[i]
                while zi<len(nums) and  nums[zi]:
                    zi += 1

'''