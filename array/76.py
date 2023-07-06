import collections

# 手写了太多初始条件，判断条件，不够抽象，没有找准循环的关键点
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         counter = Counter()
#         myQue = deque()
#         rhs = 0
#         res = s + 'a'
#         while len(counter) < len(t) and rhs < len(s):
#             if s[rhs] in t:
#                 counter[s[rhs]] += 1
#                 myQue.append(rhs)
#             rhs += 1
#         if rhs == len(s) and len(counter) < len(t):
#             return ''
#         rhs -= 1
#         while rhs < len(s) or len(counter) > len(t):
#             while len(counter) >= len(t):
#                 lhs = myQue.popleft()
#                 counter[s[lhs]] -= 1
#                 if counter[s[lhs]] == 0:
#                     counter.pop(s[lhs])

#             res = s[lhs:rhs + 1] if rhs - lhs + 1 < len(res) else res
#             while rhs < len(s):
#                 if s[rhs] in t:
#                     counter[s[rhs]] += 1
#                     myQue.append(rhs)
#                     if s[rhs] == s[lhs]:
#                         break
#                 rhs += 1
#         return res
    
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         need=collections.defaultdict(int)
#         for c in t:
#             need[c]+=1
#         needCnt=len(t)
#         i=0
#         res=(0,float('inf'))
#         for j,c in enumerate(s):
#             if need[c]>0:
#                 needCnt-=1
#             need[c]-=1           
#             if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
#                 while True:      #步骤二：增加i，排除多余元素
#                     c=s[i] 
#                     if need[c]==0:
#                         break
#                     need[c]+=1
#                     i+=1
#                 if j-i<res[1]-res[0]:   #记录结果
#                     res=(i,j)
#                 need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
#                 needCnt+=1
#                 i+=1
#         return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needWords = len(t)
        need = collections.defaultdict(int)
        for _ in t:
            need[_] += 1
        lhs = 0
        res = [0, len(s) + 1]   # represent result in s[s, e] including both ends 

        for rhs, char in enumerate(s):
            if need[char] > 0:
                needWords -= 1
            need[char] -= 1
            if needWords == 0:
                while needWords == 0:
                    if need[s[lhs]] == 0:
                        needWords += 1
                    need[s[lhs]] += 1
                    lhs += 1
                res = res if (res[1] - res[0]) < (rhs - lhs + 1) else [lhs - 1, rhs]
        return '' if res[1] == len(s) + 1 else s[res[0]: res[1]+1]
                

                         




s = "ADOBECODEBANC"
t = "ABC"
sd = Solution()
res = sd.minWindow(s, t)
print(res)


        
        







        