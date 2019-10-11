# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:18:53 2019

@author: keai
"""
#给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#如果你最多只允许完成一笔交易（即买入和卖出一支股票），
#设计一个算法来计算你所能获取的最大利润。
#注意你不能在买入股票前卖出股票。

#暴力解法
def maxProfit(prices):
        re=0
        for i in range(len(prices)-1):
            re=max(re,max(prices[i+1:])-prices[i])
        return re

#动态规划
def maxProfit1(prices):
    if len(prices)<2:
        return 0
    re=0
    pmin = prices[0]
    for i in range(1,len(prices)):
        if prices[i]<pmin:
            pmin=prices[i]
        else:re=max(re,prices[i]-pmin)
    return re

#给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#设计一个算法来计算你所能获取的最大利润。
#你可以尽可能地完成更多的交易（多次买卖一支股票）。
#注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

def maxProfit2(prices):
        if len(prices)<2:
            return 0
        re=0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                re+=prices[i]-prices[i-1]
        return re
    
def maxProfit3(prices):
        if len(prices)<2:
            return 0
        re=[]
        pmax = prices[0]
        pmin = prices[0]
        i=1
        while i<len(prices):
            while i<len(prices) and prices[i]<=prices[i-1]:
                i+=1
            pmin=prices[i-1]
            while i<len(prices) and prices[i]>prices[i-1]:
                i+=1
            pmax=prices[i-1]
            re.append(pmax-pmin)
        if len(re)==1:
            R=re[0]
        else:
            re.sort()
            R=re[-1]+re[-2]
        return R

def maxPro(prices):
    if not prices: return 0
    n = len(prices)
    dp = [[0] * n for _ in range(3)]
    for k in range(1, 3):
        pre_max = -prices[0]
        for i in range(1, n):
            pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
            dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
    return dp[-1][-1]

P = list(map(int,input().split()))
def maxP(P):
    n = len(P)
    deal1 = [0] * n
    deal2 = [0] * n
    min_price1 = - P[0]
    for i in range(1,n):
        min_price1 = max(-P[i],min_price1)
        deal1[i] = max(deal1[i-1],min_price1 + P[i])
    min_price2 = - P[0]
    for j in range(1,n):
        min_price2 = max(deal1[j-1]-P[j], min_price2)
        deal2[j] = max(deal2[j - 1], min_price2 + P[j])
    return deal2[-1]
re = maxP(P)
print(re)



# state = [[0]*n for i in range(3)]
# for i in range(2):
#     profits = - P[0]
#     for j in range(1,n):
#         profits = max(profits , state[i][j - 1] - P[j])
#         state[i + 1][j] = max(state[i + 1][j - 1], P[j] + profits)
