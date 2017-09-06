#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: sanjicaidan.py

@time: 2017/9/6 20:15

@desc:三级菜单

'''
# 省市列表

caidan={'山东':{
    '威海':['乳山','环翠','经区','环翠','临港'],
    '烟台':['海阳','栖霞','莱阳','莱山']
},
    '河南':{
        '郑州':['zheng1','zhegn2']
    },
    '湖北':{
    '武汉':['hankou','jiujiang']
},

}
# 获取省份列表

provience=list(caidan.keys())
print('省：',provience)

# 省标志位
flag_sheng= True

while flag_sheng:
    # enumerate method
    for i,y in enumerate(provience,1):
        print(i,'>',y)

    # 市标志位，每次回到省级重新开始循环，标志位变为True
    flag_shi = True
    choice_sheng = input("请输入你的选择（省）；e退出 :")
    # 判断输入的字符是否像数字
    if choice_sheng.isdigit():

        if int(choice_sheng)>0 and int(choice_sheng) <=len(provience):
            #  获取市列表
            shi=list(caidan[provience[int(choice_sheng)-1]])
            # print('市',shi)
            while flag_shi:
                for j,erji in enumerate(shi,1):
                    print(j,'>>',erji)
                choice_shi=input('请输入你选择的市，输入q返回上一级,输入e退出程序 ：')
                if choice_shi.isdigit():
                    if int(choice_shi)>0 and int(choice_shi)<=len(shi):
                        # 县列表
                        xian= caidan[provience[int(choice_sheng)-1]][shi[int(choice_shi)-1]]
                        while True:
                            for h,f in enumerate(xian,1):
                                print(h,'>>>',f)
                            choice_xian= input('请输入你选择的县，输入q返回上一级,x返回上上级，输入e退出程序 ：')
                            if choice_xian.isdigit():
                                if int(choice_xian) >0 and int(choice_xian)<=len(xian):
                                    print('-----------------------------------------')
                                    print(xian[int(choice_xian)-1])
                                else:
                                    print('输入错，重新输入')
                            else:
                                choice_xian.lower()
                                # 根据输入判断
                                if choice_xian=='q':
                                    # 清空县列表
                                    xian=[]
                                    break
                                elif choice_xian=='x':
                                    # 清空县列表
                                    xian=[]
                                    # 标志位设置
                                    flag_shi=False
                                    break
                                elif choice_xian=='e':
                                    print('退出程序，bye！！！')
                                    # 清空县列表
                                    xian=[]
                                    flag_shi=False
                                    flag_sheng=False
                                    break
                                else:
                                    print('输入错误，请重新输入！！')
                    else:
                        print('输入错误，超出范围！')
                else:
                    choice_shi.lower()
                    if choice_shi=='q':
                        # 清空市列表退出
                        shi=[]
                        break
                    elif choice_shi=='e':
                        # 清空市列表退出
                        print('bye,exit')
                        shi=[]
                        flag_sheng=False
                        break
                    else:
                        print('输入错误，请重新选择')

        # else:
        #     print('输入错误，请重新输入！！')
    else :
        # 转换为小写为后面的比较做准备
        choice_sheng.islower()
        if choice_sheng=='e':
             print('bye,exit!!!')
             break
        # else:
        #     print('输入错误，请重新输入！！！')


