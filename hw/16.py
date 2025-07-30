from collections import defaultdict

def maxSatisfaction():
    n, m = map(int, input().split())
    goods = [[]]
    rely = defaultdict(list)
    for no in range(1, m+1):
        v, w, i = map(int, input().split())
        goods.append([v//10, v * w, i])
        if i != 0:
            rely[i].append(no)
    
    
    relyValue = []
    relySatis = []

    for no in range(1, len(goods)):
        if goods[no][2] == 0:
            tempValue = [ goods[no][0] ]
            tempSatis = [ goods[no][1] ]
            if len(rely[no]) == 1:
                tempValue.append( goods[no][0] + goods[rely[no][0]][0] )
                tempSatis.append( goods[no][1] + goods[rely[no][0]][1] ) 
            if len(rely[no]) == 2:
                # bare part 0
                tempValue.append( goods[no][0] + goods[rely[no][0]][0] )
                tempSatis.append( goods[no][1] + goods[rely[no][0]][1] )

                # bare part 1
                tempValue.append( goods[no][0] + goods[rely[no][1]][0] )
                tempSatis.append( goods[no][1] + goods[rely[no][1]][1] )  

                # bare part 1 and 2
                tempValue.append( goods[no][0] + goods[rely[no][0]][0] + goods[rely[no][1]][0] )
                tempSatis.append( goods[no][1] + goods[rely[no][0]][1] + goods[rely[no][1]][1] )
            
            relyValue.append(tempValue)
            relySatis.append(tempSatis)


    dp = [ [0] * (n // 10 + 1) for _ in range(len(relyValue)) ]

    for j in range(1, n//10+1):
        for k in range(len(relyValue[0])):
            if j >= relyValue[0][k]:
                dp[0][j] = max(dp[0][j], relySatis[0][k])

    for i in range(1, len(relyValue)):
        for j in range(1, n//10+1):
            tempMax = dp[i-1][j]
            for k in range(len(relyValue[i])):
                if j >= relyValue[i][k]:
                    tempMax = max(tempMax, dp[i-1][j - relyValue[i][k]] + relySatis[i][k] )
            dp[i][j] = tempMax

    print(dp[-1][-1])


maxSatisfaction()


# 此题的难点在于捆绑销售，会产生很多问题
# 1.你不能重复计算主件
# 2.你不能把主件捆绑附件作为新的东西出售，这会导致另一种层面上的重复购买主件，这变成了多重背包
# 3.由于带附件的分组，我们并没有对其做排序，所以有可能产生1，3，2，4这种排序，而只与dp[i-1][j]做对比，
# 会造成满足条件的靠后的小值替代应有的位置，即能装下的时候没有选择组内的最大值。
# 且组内如果不满足最大值的时候，又用了dp[i-1][j]来填充dp[i][j]，这里有错
#  所以我们要拟一个tempMax来记录组内的情况。


from collections import defaultdict

def maxSatisfaction():
    n, m = map(int, input().split())
    goods = [[]]
    rely = defaultdict(list)
    for no in range(1, m+1):
        v, w, i = map(int, input().split())
        goods.append([v//10, v * w, i])
        if i != 0:
            rely[i].append(no)
    
    
    relyValue = []
    relySatis = []

    for no in range(1, len(goods)):
        if goods[no][2] == 0:
            tempValue = [ goods[no][0] ]
            tempSatis = [ goods[no][1] ]
            if len(rely[no]) == 1:
                tempValue.append( goods[no][0] + goods[rely[no][0]][0] )
                tempSatis.append( goods[no][1] + goods[rely[no][0]][1] ) 
            if len(rely[no]) == 2:
                # bare part 0
                tempValue.append( goods[no][0] + goods[rely[no][0]][0] )
                tempSatis.append( goods[no][1] + goods[rely[no][0]][1] )

                # bare part 1
                tempValue.append( goods[no][0] + goods[rely[no][1]][0] )
                tempSatis.append( goods[no][1] + goods[rely[no][1]][1] )  

                # bare part 1 and 2
                tempValue.append( goods[no][0] + goods[rely[no][0]][0] + goods[rely[no][1]][0] )
                tempSatis.append( goods[no][1] + goods[rely[no][0]][1] + goods[rely[no][1]][1] )
            
            relyValue.append(tempValue)
            relySatis.append(tempSatis)


    dp = [ [0] * (n // 10 + 1) for _ in range(len(relyValue)) ]

    for j in range(1, n//10+1):
        for k in range(len(relyValue[0])):
            if j >= relyValue[0][k]:
                dp[0][j] = max(dp[0][j], relySatis[0][k])

    for i in range(1, len(relyValue)):
        for j in range(1, n//10+1):
            tempMax = dp[i-1][j]
            for k in range(len(relyValue[i])):
                if j >= relyValue[i][k]:
                    tempMax = max(tempMax, dp[i-1][j - relyValue[i][k]] + relySatis[i][k] )
            dp[i][j] = tempMax

    print(dp[-1][-1])


maxSatisfaction()