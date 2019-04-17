#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (21.82%)
# Total Accepted:    48.3K
# Total Submissions: 221.5K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        # 复制nums，以防直接对nums操作
        temp=nums[:]
        # 临时列表l1，存储temp去掉当前遍历剩下的内容
        l1=temp
        # 临时列表l2，存储l1去掉当前遍历剩下的内容
        l2=l1
        r=[]
        for index1,i in enumerate(nums):
            # 通过排序,如果此时的遍历到的值大于0了,那么肯定不会有与之相加等于0的数了
            if i > 0:
                break
            l1=temp[index1+1:]
            for index2,j in enumerate(l1):
                l2=l1[index2+1:]
                for k in l2:
                    if i+j+k==0:
                        # 直接在append的时候去重,进一步提高效率
                        if [i,j,k] not in r:
                            r.append([i,j,k])
                            break
        return r
    result='''
    一共314个用例,只通过了311个.超出时间限制
    '''    
    god='''
        o = []
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        pos = [i for i in d if i>0]
        neg = [i for i in d if i<0]
        if 0 in d and d[0]>=3:
            o.append([0,0,0])
        for i in pos:
            for j in neg:
                k = -i-j
                if k in d:
                    if (k==i or k==j) and d[k]>=2:
                        o.append([i,j,k])
                    elif j<k<i:
                        o.append([i,k,j])
        return o
        
        使用了字典计数,再将正负数分开分别遍历,提升速度
        思路比较奇特
        '''
    god2='''
    res = []
        nums.sort()#先排序可以去重复
        length = len(nums)
        for i in xrange(length-2): #最后的两个，和倒数第三个组成组合
            if nums[i]>0: 
                break #因为已经排序了，所以到大于零的位置，之后的数字都是大于零的，肯定没有符合条件的组合了
            if i>0 and nums[i]==nums[i-1]: 
                continue #这种就是说，前面已经尝试过，如果成功了这次会重复，没成功，这次也没必要做了
            l, r = i+1, length-1 #双指针开始遍历
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total<0: #因为排序了，所以如果小于零，那么我们移动到更大的地方
                    l+=1
                elif total>0: #排序的，所以我们往更小的方向移动
                    r-=1
                else: #等于0符合要求
                    res.append([nums[i], nums[l], nums[r]])
                    #方式重复操作，左右都移动到不重复的数字
                    while l<r and nums[l]==nums[l+1]: #[6]
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6]
                        r-=1
                    l+=1
                    r-=1
        return res

    指针对撞的解法
    '''
