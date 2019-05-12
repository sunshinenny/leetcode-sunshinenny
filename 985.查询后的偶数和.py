#
# @lc app=leetcode.cn id=985 lang=python
#
# [985] 查询后的偶数和
#
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
#         result=[]
#         for index,item in enumerate(queries):
#             q_value=item[0]
#             q_index=item[1]
#             A_value=A[q_index]
#             A[q_index]=A_value+q_value
#             temp=[j for j in A if j%2==0]
#             result.append(sum(temp))
                
#         return result
        total=sum([i for i in A if i%2==0])
        result=[]
        for query in queries:
            if A[query[1]]%2==0:
                if (A[query[1]]+query[0])%2==0:
                    total+=query[0]
                else:
                    total-=A[query[1]]
            else:
                if (A[query[1]]+query[0])%2==0:
                    total+=(A[query[1]]+query[0])
            A[query[1]]+=query[0]
            result.append(total)
        return result
