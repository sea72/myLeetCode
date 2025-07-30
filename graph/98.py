from collections import defaultdict

def findAllPath():
    n, m = map(int, input().split())
    
    nodes = [ [] for _ in range(n)]
    nodes = defaultdict(list)  # 邻接表可以用defaultDict, 用字典存比用list存节约空间
    ans = []
    for _ in range(m):
        start, end = map(int, input().split())
        nodes[start-1].append(end)

    def backTrace(i, temp):
        if i == n:
            temp.append(i)
            ans.append(temp.copy())
            temp.pop()
            return
        
        if not nodes[i-1]:  
            return
        
        temp.append(i)
        for j in nodes[i-1]:
            backTrace(j, temp)
        temp.pop() 
        
    backTrace(1, [])
    if not ans:
        print(-1)
    else:
        for line in ans:
            print(*line)
        # print(" ".join(map(str, line)))
    





if __name__ == "__main__":
    findAllPath()
    


    



    
    


