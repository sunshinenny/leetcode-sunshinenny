#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (52.44%)
# Total Accepted:    15.7K
# Total Submissions: 30K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数是不是“快乐数”。
# 
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到
# 1。如果可以变为 1，那么这个数就是快乐数。
# 
# 示例: 
# 
# 输入: 19
# 输出: true
# 解释: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # from functools import reduce

        # def calc(a,b):
        #     return a**2+b**2

        # def detail(num):
        #     # 将数字转为str类型
        #     # 例如 123,转为1 2 3
        #     if 1 < num < 5:
        #         return False
        #     s=str(num)
        #     # 将1 2 3 加入到一个临时的列表中
        #     l1=[int(i) for i in s]
        #     # 通过reduce方法,递归计算结果,123的计算结果为 14
        #     result=reduce(calc,l1)
        #     #  4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
        #     # 如果答案为 1 ,说明这个数字是快乐数
        #     if result is 1:
        #         return True
        #     # 如果答案不是1,则将这个数字参与递归,直至得出结论
        #     else:
        #         return detail(result)
        #         # print('result={0}'.format(result))

        # return detail(n)
        comment='''
        暴力递归方法失败,没有加上重复判断,这个代码可能会无限死循环下去
        于是改了一个思路
        '''
        # m = {}
        # while n not in m.keys():
        #     m[n] = 0
        #     if 1 in m.keys():return True
        #     n = sum([int(x)**2 for x in list(str(n))])
        # return False

        god='''
        if n==1:
            return True
        if n>1 and n<5:
            return False
        
        s = 0
        while n:
            a = n%10
            n = n/10
            s += a*a
            #print s
        return self.isHappy(s)
        '''

