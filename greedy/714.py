# from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         if len(prices) < 2:
#             return 0
#         res = []
#         for n in range(len(prices)-1):
#             if prices[n] < prices[n+1]:
#                 lastBuy = prices[n]
#                 lastSell = prices[n+1]
#                 res.append(lastSell - lastBuy - fee)
#                 break
#         for no in range(n+1, len(prices)-1):
#             if prices[no] < prices[no+1]:
#                 # if prices[no+1] - prices[no] + lastSell - lastBuy - 2 * fee < prices[no+1] - lastBuy - fee:
#                 if  -prices[no] + lastSell - fee < 0:
#                     res.pop()
#                     res.append(prices[no+1] - lastBuy - fee)
#                 else:
#                     res.append(prices[no+1] - prices[no] - fee)
#                     lastBuy = prices[no]
#                 lastSell = prices[no+1]
#         interest = 0
#         # for item in res:
#         #     interest += max(item, 0)
#         interest = sum(res)
#         return max(interest, 0)
            

# sol = Solution()
# print(sol.maxProfit(prices = [10,1,8,7,10], fee = 2))
                    
            


def maxProfit1(prices, fee):
    n = len(prices)
    buy = prices[0] + fee
    profit = 0
    for i in range(1, n):
        if prices[i] + fee < buy:
            buy = prices[i] + fee
        elif prices[i] > buy:
            profit += prices[i] - buy
            buy = prices[i]
    return profit


def maxProfit2(prices, fee):
    if len(prices) < 2:
        return 0
    res = []
    for n in range(len(prices)-1):
        if prices[n] < prices[n+1]:
            lastBuy = prices[n]
            lastSell = prices[n+1]
            res.append(lastSell - lastBuy - fee)
            break
    for no in range(n+1, len(prices)-1):
        if prices[no] < prices[no+1]:
            lastProfit = max(0, res[-1])
            thisProfit = max(0, prices[no+1] - prices[no] - fee)
            cancelProfit = max(0, prices[no+1] - lastBuy - fee)
            if lastProfit + thisProfit <= cancelProfit:
                res.pop()
                res.append(cancelProfit)
            else:
                res.append(thisProfit)
                lastBuy = prices[no]
            lastSell = prices[no+1]
    interest = 0
    for item in res:
        interest += max(item, 0)
    return max(interest, 0)

def main():
    import random
    while True:
        prices = []
        fee = random.randint(1,10)
        for _ in range(random.randint(1, 6)):
            prices.append(random.randint(0, 10))
        res1 = maxProfit1(prices, fee)
        res2 = maxProfit2(prices, fee)
        if res1 != res2:
            print(prices, fee, res1, res2)
            break

if __name__  == "__main__":
    #main()
    print(maxProfit2([7,8,0,2,4,8], 2))
    

                
                



