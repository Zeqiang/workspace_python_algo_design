#!/bin/python
# -*- coding: utf8 -*-
import pandas as pd

def knapsack_dynamic(w, p, m):

    w.insert(0,0)
    p.insert(0,0)

    x = []   #装入背包的物体
    n = len(w) - 1   #计算n的个数

    #optp[i][j]表示在前i个物体中，能够装入载重量为j的背包中的物体的最大价值
    #optp 相当于做了一个n*m的全零矩阵的赶脚，n行为物件，m列为自背包载重量
    optp = [[0 for col in range(m + 1)] for raw in range(n + 1)]

    #计算optp[i][j]
    for i in range(1, n + 1):       # 物品一件件来
        for j in range(1, m + 1):   # j为子背包的载重量，寻找能够承载物品的子背包
            if (j >= w[i]):         # 当物品的重量小于背包能够承受的载重量的时候，才考虑能不能放进去
                optp[i][j] = max(optp[i - 1][j], optp[i - 1][j - w[i]] + p[i])    # optp[i - 1][j]是上一个单元的值， optp[i - 1][j - w[i]]为剩余空间的价值
            else:
                optp[i][j] = optp[i - 1][j]

    #递推装入背包的物体,寻找跳变的地方，从最后结果开始逆推
    j = m
    for i in range(n, 0, -1):
        if optp[i][j] > optp[i - 1][j]:
            x.append(i)
            j = j - w[i]  

    #返回最大价值，即表格中最后一行最后一列的值
    v = optp[n][m]

    return optp, v, x


if __name__ == '__main__':
    
    w = [4, 3, 2, 3]   #n个物体的重量
    p = [3, 2, 4, 4]   #n个物体的价值
    m = 6   #背包的载重量

    # w = [1, 4, 3, 1]   #n个物体的重量
    # p = [1500, 3000, 2000, 2000]   #n个物体的价值
    # m = 4   #背包的载重量

    chart, v, x = knapsack_dynamic(w, p, m)

    print(v)
    print(x)
    print(pd.DataFrame(chart))
    












