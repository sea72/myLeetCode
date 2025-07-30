# from collections import defaultdict
# import math

# def strChain():

#     def howClose(a, b):
#         diff = 0
#         for i in range(len(a)):
#             if a[i] != b[i]:
#                 diff += 1
#             else:
#                 continue
#         return diff
    
#     def dfs(cur, road):
#         if cur in road:
#             return 
#         road.append(cur)
#         if cur == end:
#             nonlocal res
#             res = min(res, len(road))
#             return
#         else:
#             for word in grids[cur]:
#                 dfs(word, road.copy())


#     n = int(input())
#     begin, end = input().split()
#     strList = []
#     for _ in range(n):
#         strList.append(input())
#     strList = [begin] + strList + [end]
#     grids = defaultdict(list)

#     for i in range(n+2):
#         for j in range(n+2):
#             if howClose(strList[i], strList[j]) == 1:
#                 grids[strList[i]].append(strList[j])
    
#     res = math.inf
#     dfs(begin, [])
#     if res > len(grids) + 2:
#         print(0)
#     else:
#         print(res)

# if __name__ == "__main__":
#     strChain()

from collections import defaultdict

def strChain():
    def howClose(a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff == 1


    n = int(input())
    begin, end = input().split()
    strList = []
    for _ in range(n):
        strList.append(input())
    strList = [begin] + strList + [end]
    grids = defaultdict(list)

    for i in range(n+2):
        for j in range(n+2):
            if howClose(strList[i], strList[j]):
                grids[strList[i]].append(strList[j])
    
    visited = set()
    bfsQue = [(begin, 1)]
    while bfsQue:
        cur, step = bfsQue.pop(0)
        if cur == end:
            print(step)
            exit()
        else:
            for word in grids[cur]:
                if word not in visited:
                    visited.add(word)
                    bfsQue.append((word, step+1))
    print(0)


if __name__ == "__main__":
    strChain()

# def judge(s1,s2):
#     count=0
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             count+=1
#     return count==1

# if __name__=='__main__':
#     n=int(input())
#     beginstr,endstr=map(str,input().split())
#     if beginstr==endstr:
#         print(0)
#         exit()
#     strlist=[]
#     for i in range(n):
#         strlist.append(input())
    
#     # use bfs
#     visit=[False for i in range(n)]
#     queue=[[beginstr,1]]
#     while queue:
#         str,step=queue.pop(0)
#         if judge(str,endstr):
#             print(step+1)
#             exit()
#         for i in range(n):
#             if visit[i]==False and judge(strlist[i], str):
#                 visit[i]=True
#                 queue.append([strlist[i],step+1])
#     print(0)