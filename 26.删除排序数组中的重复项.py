#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (43.68%)
# Total Accepted:    105.1K
# Total Submissions: 240.6K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
# 
# 示例 1:
# 
# 给定数组 nums = [1,1,2], 
# 
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
# 
# 你不需要考虑数组中超出新长度后面的元素。
# 
# 示例 2:
# 
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# 
# 你不需要考虑数组中超出新长度后面的元素。
# 
# 
# 说明:
# 
# 为什么返回数值是整数，但输出的答案是数组呢?
# 
# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 
# 你可以想象内部操作如下:
# 
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
# 
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
# 
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 自己的写法:一边读取一边删除
        index=0
        # len(nums)随着数组的变化而变化,所以不能一开始就写死了
        while index < len(nums):
            if index!=len(nums)-1 and nums[index]==nums[index+1]:
                    nums.remove(nums[index])
                    index-=1
            index+=1
        return len(nums)
way='''
大佬的解法:
- 读取的时候判断是不是和前一个相同,如果相同,将后面的值向前推
        if not nums:
            return 0
        count = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count

        举个例子,如果是 1,1,2,3
        time1: nums[count=1]=1 nums[i=1]=1 不满足条件 nums=[1,1,2,3] count=1
        time2: nums[count=1]=1 nums[i=2]=2 满足条件 后面元素前移 nums=[1,2,3] count=2
        time3: nums[count=2]=3 nums[i=2]=3 不满足条件[感觉len(nums)的实时计算有点意思,此时可以不发生数组越界] nums=[1,2,3]
神仙算法:
- 快慢指针
    - 原理也是后面数组前移,就是实现的操作太骚气了
    - 便于理解,分析的时候需要一个例子!!!
class Solution {
    public int removeDuplicates(int[] nums) {
    if(nums.length < 2){
                    return nums.length;
                }
                boolean flag = true;
                int i = 0;
                int j = 0;
               for( i = 1; i < nums.length; i++){
                 if(nums[j] != nums[i]){
                     // 利用++j提前对j进行操作
                     nums[++j] = nums[i];
                 }
               }
               return j + 1;
    }
}
'''

