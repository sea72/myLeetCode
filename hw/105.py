# n, q = map(int, input().split())
# s = list(input())
# t = list(input())
# template = 'red'

# def counting(str):
#     def dfs(str, i, j):
#         if i < n:
#             if j == len(template) - 1 and str[i] == template[j]:
#                 nonlocal res
#                 res += 1
#                 dfs(str, i+1, j)
#             elif j < len(template) - 1 and str[i] == template[j]:
#                 dfs(str, i+1, j)
#                 dfs(str, i+1, j+1)
#         else:
#             return

#     res = 0
#     dfs(str, 0, 0)
#     return res

# ans = []
# for _ in range(q):
#     no = int(input())-1
#     s[no], t[no] = t[no], s[no]
#     ans.append(counting(s) - counting(t))
# print(*ans, sep='\n')

# n, q = map(int, input().split())
# s = list(input())
# t = list(input())
# template = 'red'

# def counting(str):
#     dp = [[0] * (len(template)+1) for _ in range(n+1)]

#     for i in range(n+1):
#         dp[i][-1] = 1

#     for i in range(n-1, -1, -1):
#         for j in range(len(template)-1, -1, -1):
#             if str[i] == template[j]:
#                 dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
#             else:
#                 dp[i][j] = dp[i+1][j]
    
#     return dp[0][0]

# ans = []
# for _ in range(q):
#     no = int(input())-1
#     s[no], t[no] = t[no], s[no]
#     ans.append(counting(s) - counting(t))
# print(*ans, sep='\n')



class SegTree:
    class Seg:
        def __init__(self):
            self.l = 0
            self.r = 0
            self.rcnt = 0
            self.ecnt = 0
            self.dcnt = 0
            self.recnt = 0
            self.edcnt = 0
            self.redcnt = 0

    def __init__(self, maxn):
        self.seg = [self.Seg() for _ in range(maxn * 4)]

    def push_up(self, p):
        ls = p * 2
        rs = p * 2 + 1
        self.seg[p].rcnt = self.seg[ls].rcnt + self.seg[rs].rcnt
        self.seg[p].ecnt = self.seg[ls].ecnt + self.seg[rs].ecnt
        self.seg[p].dcnt = self.seg[ls].dcnt + self.seg[rs].dcnt

        self.seg[p].recnt = (
            self.seg[ls].recnt + self.seg[rs].recnt +
            self.seg[ls].rcnt * self.seg[rs].ecnt
        )
        self.seg[p].edcnt = (
            self.seg[ls].edcnt + self.seg[rs].edcnt +
            self.seg[ls].ecnt * self.seg[rs].dcnt
        )
        self.seg[p].redcnt = (
            self.seg[ls].redcnt + self.seg[rs].redcnt +
            self.seg[ls].recnt * self.seg[rs].dcnt +
            self.seg[ls].rcnt * self.seg[rs].edcnt
        )

    def build(self, l, r, s, p):
        self.seg[p].l = l
        self.seg[p].r = r
        if l == r:
            self.seg[p].rcnt = self.seg[p].ecnt = self.seg[p].dcnt = 0
            if s[l] == 'r':
                self.seg[p].rcnt = 1
            elif s[l] == 'e':
                self.seg[p].ecnt = 1
            elif s[l] == 'd':
                self.seg[p].dcnt = 1
            return
        mid = (l + r) // 2
        self.build(l, mid, s, p * 2)
        self.build(mid + 1, r, s, p * 2 + 1)
        self.push_up(p)

    def update(self, pos, c, p):
        if self.seg[p].l == self.seg[p].r == pos:
            self.seg[p].rcnt = self.seg[p].ecnt = self.seg[p].dcnt = 0
            if c == 'r':
                self.seg[p].rcnt = 1
            elif c == 'e':
                self.seg[p].ecnt = 1
            elif c == 'd':
                self.seg[p].dcnt = 1
            return
        mid = (self.seg[p].l + self.seg[p].r) // 2
        if pos <= mid:
            self.update(pos, c, p * 2)
        else:
            self.update(pos, c, p * 2 + 1)
        self.push_up(p)


import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
q = int(data[1])
s = " " + data[2]  # 1-based indexing
t = " " + data[3]

queries = list(map(int, data[4:]))

t1 = SegTree(n + 5)
t2 = SegTree(n + 5)

t1.build(1, n, s, 1)
t2.build(1, n, t, 1)

output = []
for x in queries:
    s_list = list(s)
    t_list = list(t)
    s_list[x], t_list[x] = t_list[x], s_list[x]
    s = "".join(s_list)
    t = "".join(t_list)
    t1.update(x, s[x], 1)
    t2.update(x, t[x], 1)
    output.append(str(t1.seg[1].redcnt - t2.seg[1].redcnt))

print("\n".join(output))





class Node(object):  # 线段树的结点类
    def __init__(self):
        self.ln = -1
        self.rn = -1  # 左子节点和右子节点，值为字符的索引
        self.r = 0  # 分别记录 r, e, d, re, ed, red 的个数
        self.e = 0
        self.d = 0
        self.re = 0
        self.ed = 0
        self.red = 0


class SegTree(object):  # 线段树类
    def __init__(self, data):
        self.n = len(data)
        # 初始化线段树，大小为4*n（因为最坏情况下是满二叉树）
        self.tree = [Node() for _ in range(self.n * 4)]
        self.build(data, 1, 0, self.n - 1)  # 树节点从1开始

    def build(self, data, node, start, end):  # 构建线段树
        # data 表示字符串， node 表示节点下标，start 和 end 表示 字符的索引
        self.tree[node].ln = start
        self.tree[node].rn = end
        if start == end:  # 如果当前节点是叶子节点
            self.tree[node].r = int(data[start] == 'r')
            self.tree[node].e = int(data[start] == 'e')
            self.tree[node].d = int(data[start] == 'd')
            return
        mid = (start + end) // 2
        self.build(data, node * 2, start, mid)  # 左子树
        self.build(data, node * 2 + 1, mid + 1, end)  # 右子树
        self.push_up(node)

    def push_up(self, node):  # 计算该节点的r e d re ed red 个数
        left = self.tree[node * 2]  # 左节点
        right = self.tree[node * 2 + 1]  # 右节点
        self.tree[node].r = left.r + right.r
        self.tree[node].e = left.e + right.e
        self.tree[node].d = left.d + right.d
        self.tree[node].re = left.re + right.re + left.r * right.e
        self.tree[node].ed = left.ed + right.ed + left.e * right.d
        self.tree[node].red = left.red + right.red + left.re * right.d + left.r * right.ed

    def update(self, node, pos, val):  # 单点更新，pos表示更新的索引，val表示更新的值
        if self.tree[node].ln == self.tree[node].rn and self.tree[node].ln == pos:  # 递归到叶子节点
            self.tree[node].r = int(val == 'r')
            self.tree[node].e = int(val == 'e')
            self.tree[node].d = int(val == 'd')
            return
        mid = (self.tree[node].ln + self.tree[node].rn) // 2
        if pos <= mid:
            self.update(node * 2, pos, val)
        else:
            self.update(node * 2 + 1, pos, val)
        self.push_up(node)


n, q = map(int, input().split())
s = input()
t = input()
seg_s = SegTree(s)
seg_t = SegTree(t)
opt = []
for _ in range(q):
    x = int(input()) - 1
    opt.append(x)
for x in opt:
    seg_s.update(1, x, t[x])
    seg_t.update(1, x, s[x])
    s, t = s[:x] + t[x] + s[x + 1:], t[:x] + s[x] + t[x + 1:]
    print(seg_s.tree[1].red - seg_t.tree[1].red)
  