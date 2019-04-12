#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (43.04%)
# Total Accepted:    12K
# Total Submissions: 27.8K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if height==[]:
            return 0
        # 创建一个矩阵,形如题目中的表格
        length=len(height)
        m=max(height)
        l=[[0 for i in range(length)] for j in range(m)]
        temp=height
        for l_index in range(m):
            for index,item in enumerate(temp):
                if item >0:
                    temp[index]-=1
                    l[l_index][index]=1
        # 矩阵建立完成，接下来逐行分析可以接多少水
        # 定义总数为sum
        sum=0
        # 逐行遍历
        for i in l:
            # 存在两个指针，分别为slow和fast
            # 初始化的时候两个指针位置相同，且均从第一个开始
            s,f=0,0
            # 外循环，移动s指针
            while s <length:
                # f只会比s大，所以此处直接令其等于s
                f=s
                # 内循环，移动f指针
                while f<length-1:
                    #print('当前S指针处于：{0}'.format(s))
                    #print('当前F指针处于：{0}'.format(f))
                    # 如果s当前值为0，则说明这个坑没有价值，直接跳出内循环
                    if i[s]==0:
                        #print('value=0 S指针处于：{0}'.format(s))
                        break
                    # 如果出现了连续的1，则表明这几个格子里不可能有水，直接跳出内循环
                    if i[f]==1 and i[f+1]==1:
                        break
                    # 如果当前f指针的值为0，下一个f指针的值为1
                    # 则说明中间这部分可以蓄水
                    if i[f]==0 and i[f+1]==1:
                        # 此时蓄水量为两个指针的差值
                        sum+=(f-s)
                        #print('此时的sum是'+str(sum))
                        # 将s指针移动到f的下一个位置，保证两个指针可以遍历所有的点
                        s=f+1
                    # 隐藏了一个可能性为：如果此时的f和下一个f都为0，则说明这处于一个水坑中。不用在意，f指针继续移动即可，直到移动到水坑的边缘
                    # 此次+1用于内循环
                    f+=1
                #print('This time sum is {0}\nDown'.format(sum))
                # 此次+1用于外循环
                s+=1
        # 输出sum即为答案
        return sum

存在的问题='''
如果列表长度还可以,速度还行
但是如果测试用例过于庞大,速度将会非常非常慢

事实上LeetCode的检测也是超出时间限制
'''

其他人的算法1='''
思路:
1. 找出最高点
2. 分别从两边往最高点遍历：如果下一个数比当前数小，说明可以接到水
if len(height) <= 1:
            return 0
        
        max_height = 0
        max_height_index = 0
        
        # 找到最高点
        for i in range(len(height)):
            h = height[i]
            if h > max_height:
                max_height = h
                max_height_index = i
        
        area = 0
        
        # 从左边往最高点遍历
        tmp = height[0]
        for i in range(max_height_index):
            if height[i] > tmp:
                tmp = height[i]
            else:
                area = area + (tmp - height[i])
        
        # 从右边往最高点遍历
        tmp = height[-1]
        for i in reversed(range(max_height_index + 1, len(height))):
            if height[i] > tmp:
                tmp = height[i]
            else:
                area = area + (tmp - height[i])
        
        return area
'''
