#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.22%)
# Total Accepted:    111.9K
# Total Submissions: 347.4K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def reverse1(st):
            return st[::-1]

        result = 0

        if x < 0:
            x = -x
            s = '{0}'.format(x)
            result = int(reverse1(s))*-1
        else:
            s = '{0}'.format(x)
            result = int(reverse1(s))
        if result < -2147483648 or result > 2147483647:
            return 0
        else:
            return result

