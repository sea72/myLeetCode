# from copy import deepcopy

# ques = []
# for _ in range(9):
#     ques.append(list(map(int, input().split())))

# spaces = {}

# def remain(cur):
#     row = ques[cur[0]]
#     column = [ ques[k][cur[1]] for k in range(9)]
#     area = [ ques[m][n] for m in range(cur[0]//3*3, (cur[0]//3+1)*3) for n in range(cur[1] // 3 * 3, (cur[1]//3+1)*3)]
#     return (set(range(1,10)) - set(row) ) & (set(range(1, 10)) - set(column)) & (set(range(1, 10)) - set(area))

# def isRelated(p1, p2):
#     return p1[0] == p2[0] or p1[1] == p2[1] or (p1[0]//3*3 == p2[0]//3*3 & p1[1]//3 * 3 == p2[1]//3*3)

# for i in range(9):
#     for j in range(9):
#         if ques[i][j] == 0:
#             spaces[(i, j)] = remain((i,j))
            

# decided = []

# def dfs(decided, spaces):
#     if len(decided) == len(spaces):
#         for k, v in spaces.items():
#             ques[k[0]][k[1]] = list(v)[0]
#         for line in ques:
#             print(*line)
#         return True
#     for key, values in spaces.items():
#         if key not in decided:
#             decided.append(key)
#             for v in values:
#                 tempSapces = deepcopy(spaces)
#                 for alterKey, alterValue in tempSapces.items():
#                     if alterKey != key and isRelated(alterKey, key) and v in alterValue:
#                         alterValue.remove(v)
#                     if len(spaces[alterKey]) < 1:
#                         break
#                 else:
#                     if dfs(decided, tempSapces):
#                         break
#             else:
#                 decided.pop(-1)
            
# dfs([], spaces)


# from copy import deepcopy

# ques = []
# for _ in range(9):
#     ques.append(list(map(int, input().split())))

# spaces = {}

# def remain(cur):
#     row = ques[cur[0]]
#     column = [ques[k][cur[1]] for k in range(9)]
#     area = [ques[m][n] for m in range(cur[0]//3*3, (cur[0]//3+1)*3) for n in range(cur[1]//3*3, (cur[1]//3+1)*3)]
#     return (set(range(1,10)) - set(row)) & (set(range(1,10)) - set(column)) & (set(range(1,10)) - set(area))

# def isRelated(p1, p2):
#     return p1[0] == p2[0] or p1[1] == p2[1] or (p1[0]//3*3 == p2[0]//3*3 and p1[1]//3*3 == p2[1]//3*3)

# for i in range(9):
#     for j in range(9):
#         if ques[i][j] == 0:
#             spaces[(i, j)] = remain((i,j))

# def dfs(visited, spaces):
#     if len(visited) == len(spaces):
#         for k, v in spaces.items():
#             ques[k[0]][k[1]] = list(v)[0]
#         for line in ques:
#             print(*line)
#         return True
#     for key, values in list(spaces.items()):  # 使用list()避免字典修改问题
#         if key not in visited:
#             visited.append(key)
#             for v in list(values):  # 避免集合修改问题
#                 tempSpaces = deepcopy(spaces)
#                 # 固定当前空格的值
#                 tempSpaces[key] = {v}
#                 # 更新相关空格的可能值
#                 found_empty = False
#                 for alterKey, alterValue in tempSpaces.items():
#                     if alterKey != key and isRelated(alterKey, key) and v in alterValue:
#                         alterValue.remove(v)
#                         if len(alterValue) == 0:
#                             found_empty = True
#                             break
#                 if not found_empty:
#                     if dfs(visited, tempSpaces):
#                         return True
#             visited.pop()
#     return False

# dfs([], spaces)


from copy import deepcopy

# 输入数独谜题
ques = []
for _ in range(9):
    ques.append(list(map(int, input().split())))

spaces = {}

# 计算某个空格的可能值
def remain(cur):
    i, j = cur
    row = ques[i]
    col = [ques[k][j] for k in range(9)]
    box_i, box_j = i//3*3, j//3*3
    box = [ques[m][n] for m in range(box_i, box_i+3) for n in range(box_j, box_j+3)]
    return set(range(1, 10)) - set(row) - set(col) - set(box)

# 检查两个格子是否相关（同行/同列/同宫）
def isRelated(p1, p2):
    return p1[0] == p2[0] or p1[1] == p2[1] or (p1[0]//3 == p2[0]//3 and p1[1]//3 == p2[1]//3)

# 初始化空格及其可能值
for i in range(9):
    for j in range(9):
        if ques[i][j] == 0:
            spaces[(i, j)] = remain((i, j))

def dfs(visited, spaces):
    # 所有空格已填满，打印解
    if len(visited) == len(spaces):
        for (i, j), vals in spaces.items():
            ques[i][j] = next(iter(vals))
        for row in ques:
            print(*row)
        return True
    
    # MRV启发式：选择可能值最少的空格
    min_key = None
    min_size = float('inf')
    for key, vals in spaces.items():
        if key not in visited:
            size = len(vals)
            if size < min_size:
                min_size = size
                min_key = key
    
    if min_key is None:
        return False  # 所有空格都已访问
    
    key = min_key
    visited.append(key)
    
    # 尝试所有可能值
    for val in list(spaces[key]):  # 创建副本防止迭代中修改
        tempSpaces = deepcopy(spaces)
        # 固定当前空格的值
        tempSpaces[key] = {val}
        
        # 传播约束：更新相关空格的可能值
        found_empty = False
        for alterKey, alterVals in tempSpaces.items():
            if alterKey == key or not isRelated(key, alterKey):
                continue
            if val in alterVals:
                alterVals.remove(val)
                if len(alterVals) == 0:
                    found_empty = True
                    break
        
        # 如果没有冲突，递归搜索
        if not found_empty:
            if dfs(visited, tempSpaces):
                return True
    
    visited.pop()
    return False

dfs([], spaces)