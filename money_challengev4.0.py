# ！/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'CZH'
'''
    作者：陈自豪
    功能：52周存钱挑战
    版本：4.0
    日期：09/10/2018
    4.0灵活设置每周存款金额，增加存款数及存款周数
'''

import math
def saving_money_in_n_weeks(money_per_week,increase_money,total_week):
    saving = 0  # 账户累计
    money_list = []  # 记录每周存款数的列表
    for i in range(total_week):
        # 存钱操作
        # saving = saving + money_per_week
        # saving += money_per_week

        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))
        # 更新下一周存钱金额
        money_per_week += increase_money
    return saving,money_list

def main():
    '''
    主函数
    :return:
    '''
    money_per_week = float(input('请输入每周的存入金额：'))     # 每周存入的金额
    # i = 1  # 记录周数
    increase_money = float(input('请输入每周的递增金额：'))     # 递增金额
    total_week = int(input('请输入计划存钱总共的周数：'))       # 总共周数

    saving,money_list=saving_money_in_n_weeks(money_per_week,increase_money,total_week)
    print('存款总金额：',saving)
    print('存款列表：',money_list)

if __name__ == '__main__':
    main()

