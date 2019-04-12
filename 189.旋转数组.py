#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (36.95%)
# Total Accepted:    43.9K
# Total Submissions: 118.9K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 说明:
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。
# 
# 
#
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 第一种方法:截取后添加到头部再删除
        #temp=nums[-k:]
        #nums=[i for i in temp]+nums
        #del nums[-k:]
        
        # 第二种办法:循环的时候插入再pop
        l=len(nums)

        for i in range(k%l):
            nums.insert(0,nums.pop(-1))

        神仙解法='''
        # 获取nums的长度
        l = len(nums)
        # 拿k和l去取余操作,此处借以判断具体需要挪动几步
        # 如果一个列表长度为3,那么移动3次和6次是一样的,这一步很好的节约了时间开销
        k = k % len(nums)
        # 如果k==0,则就不需要旋转了
        if k != 0:
            # 将nums翻转
            nums.reverse()
            # 通过切片 获取到指定的值,设计的很精妙
            nums[:k]=nums[k-1::-1]
            nums[k:]=nums[:k-1:-1]
        '''
