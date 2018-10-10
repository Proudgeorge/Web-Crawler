#！/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'CZH'
'''
作者：陈自豪
功能：BMR计算器
版本：1.0
日期：10/06/2018
'''
def main():
    '''
    主函数
    :return:
    '''
    y_or_n = input('是否退出程序（y/n）?')
    #性别
    while y_or_n != 'y':
        input_str = input('性别 体重（kg） 身高（cm） 年龄：')
        str_list = input_str.split(' ')

        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':
            #男性
            bmr = (13.7*weight)+(5.0*height)-(6.8*age)+66
        elif gender== '女':
            #女性
            bmr = (9.6*weight)+(1.8*height)-(4.7*age)+65.5
        # else:
        #     bmr = -1
        # if bmr != -1:

        else:
            print('暂不支持该性别')

        print('您的性别：{}，体重：{}公斤，身高{}厘米，年龄：{}岁'.format(gender, weight, height, age))
        print('您的基础代谢率：{}大卡'.format(bmr))
        print()  # 输出空行
        y_or_n = input('是否退出程序（y/n）?')
if __name__ == '__main__':
    main()