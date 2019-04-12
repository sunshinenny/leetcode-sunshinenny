#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (38.87%)
# Total Accepted:    31.2K
# Total Submissions: 80.3K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result=''
        for i in s:
            if i.isalnum():
                result+=i
        if len(result)==1 or len(result)==0:
            return True
        print(len(result)//2)
        result=result.lower()
        z=[i for i in result[0:len(result)//2]]
        f=[i for i in result[-(len(result)//2):]]
        f.reverse()
        print(z)
        print(f)
        
        if z==f:
            return True
        else:
            return False

