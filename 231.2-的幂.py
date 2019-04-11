#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (44.89%)
# Total Accepted:    16.1K
# Total Submissions: 35.9K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        # 将输入的数字转为二进制,同时转为字符串
        temp="{0:b}".format(n)

        # 如果二进制字符串只有一个1,那么这个数就是2的幂
        if temp.count('1')==1:
            return True
        else:
            return False

神仙='''
def isPowerOfTwo(self, n):
    return (n>0) and (n & (n-1))==0
神仙题。。没见过就不会，见过就会了。

重点在于对位运算符的理解
解法 1：& 运算，同 1 则 1。 return (n > 0) && (n & -n) == n;
解释：2 的幂次方在二进制下，只有 1 位是 1，其余全是 0。例如：8---00001000。负数的在计算机中二进制表示为补码 (原码 -> 正常二进制表示，原码按位取反 (0-1,1-0)，最后再 + 1。然后两者进行与操作，得到的肯定是原码中最后一个二进制的 1。例如 8&(-8)->00001000 & 11111000 得 00001000，即 8。 建议自己动手算一下，按照这个流程来一遍，加深印象。
解法 2：移位运算：把二进制数进行左右移位。左移 1 位，扩大 2 倍；右移 1 位，缩小 2 倍。 return (n>0) && (1<<30) % n == 0;
解释：1<<30 得到最大的 2 的整数次幂，对 n 取模如果等于 0，说明 n 只有因子 2。
'''
