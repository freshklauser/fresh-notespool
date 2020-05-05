# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-03-15 10:53:52
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-15 17:04:54

'''水果摊小买卖
小王手里有点闲钱，想着做点卖水果的小买卖，给出两个数组m，n，用m[i]表示第i个水果的成本价，
n[i]表示第i个水果能卖出的价钱，假如现在有本钱k元，试问最后最多能赚多少钱？

说明：
    1. 每种水果只能买一次，只能卖一次；
    2. 数组m,n大小不超过50；
    3. 数组元素为正整数，不超过1000

思路：
贪心算法
'''

while True:
    try:
        # 成本 卖价 本钱
        # cost_prices = list(map(int, input().split(",")))
        # sell_prices = list(map(int, input().split(",")))
        # money = int(input())
        cost_prices = [4, 2, 6, 4, 5, 17, 20, 7, 8, 33, 28, 35, 100, 80]
        sell_prices = [5, 3, 8, 7, 6, 15, 25, 9, 10, 39, 35, 40, 102, 89]
        # cost_prices = [4, 2, 6, 4]
        # sell_prices = [5, 3, 8, 7]
        money = 15

        length = len(cost_prices)

        # 构造利润表，降序排列，贪心算法
        profits = {}
        for i in range(length):
            profits[i] = sell_prices[i] - cost_prices[i]
        profits = sorted(profits.items(), key=lambda x: x[1], reverse=True)
        print(profits)

        cur_money = money
        max_profit = 0
        unvisited = []
        for index, profit in profits:
            if profit >= 0:
                if cost_prices[index] <= cur_money:
                    cur_money += profit                                         # 卖完 index 后剩余价钱 = cur + profit
                    max_profit += profit
                else:
                    unvisited.append((index, cost_prices[index], profit))       # unvisited: 等钱够了再回来买 (index, cost, profit)
        print("First Round End.")
        print("unvisited list:", unvisited)

        # 第一遍买不起的水果，再利用赚到后的总本金来买
        '关键： 跳出循环的条件, 如果存在一直都买不起的情况'
        updated_length = 0
        while unvisited:
            print("Remaining {} element: ".format(len(unvisited)), unvisited, "money_have:", max_profit + money)
            cur_length = len(unvisited)

            for _ in range(cur_length):
                head = unvisited[0]
                if head[2] >= 0:
                    if head[1] <= cur_money:
                        cur_money = cur_money + head[2]
                        max_profit += head[2]
                        unvisited.pop(0)                                        # 执行到此，说明visited，直接从unvisited列表中删除
                    else:
                        unvisited.append(unvisited.pop(0))                      # unvisted的第一个水果还是没买，则放到unvisited列表最后，等下次再买
                    updated_length = len(unvisited)

            if updated_length >= cur_length:                                    # 说明 一轮之后 还是不够钱买剩下的任何一个水果，退出
                break

        print("Total income:", max_profit + money)
        break

    except Exception:
        break
