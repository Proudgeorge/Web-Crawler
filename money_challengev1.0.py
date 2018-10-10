# ！/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'CZH'
'''
    作者：陈自豪
    功能：52周存钱挑战
    版本：1.0
    日期：08/10/2018
'''


def main():
    '''
    主函数
    :return:
    '''
    money_per_week = 10  # 每周存入的金额
    i = 1  # 记录周数
    increase_money = 10  # 递增金额
    total_week = 52  # 总共周数
    saving = 0  # 账户累计
    while i <= total_week:
        # 存钱操作
        # saving = saving + money_per_week
        saving += money_per_week

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))
        # 更新下一周存钱金额
        money_per_week += increase_money
        i += 1

    return saving, money_per_week


if __name__ == '__main__':
    main()

