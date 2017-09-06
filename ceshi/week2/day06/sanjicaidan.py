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

caidan={'山东':{
    '威海':['rushan','huancui','jingqu','lingang'],
    '烟台':['haiyang','qixia','muping','laishan']
},
    '河南':{
        'zhengzhou':['zheng1','zhegn2']
    },
    '湖北':{
    '武汉':['hankou','jiujiang']
}

}
# 获取省份列表
provience=list(caidan.keys())
print('省：',provience)


# 省标志位
flag_sheng= True

while flag_sheng:
    for i,y in enumerate(provience,1):
        print(i,'>',y)
    # 市标志位
    flag_shi = True
    choice_sheng = input("请输入你的选择（省）；e退出")
    if choice_sheng.isdigit():

        if int(choice_sheng)>0 and int(choice_sheng) <=len(provience):
            #  获取市列表
            shi=list(caidan[provience[int(choice_sheng)-1]])
            # print('市',shi)
            while flag_shi:
                for j,erji in enumerate(shi,1):
                    print(j,'>>',erji)
                choice_shi=input('请输入你选择的市，输入q返回上一级,输入e退出程序：')
                if choice_shi.isdigit():
                    if int(choice_shi)>0 and int(choice_shi)<=len(shi):
                        xian= caidan[provience[int(choice_sheng)-1]][shi[int(choice_shi)-1]]
                        while True:
                            for h,f in enumerate(xian,1):
                                print(h,'>>>',f)
                            choice_xian= input('请输入你选择的县，输入q返回上一级,x返回上上级，输入e退出程序：')
                            if choice_xian.isdigit():
                                if int(choice_xian) >0 and int(choice_xian)<=len(xian):
                                    print(xian[int(choice_xian)-1])
                                else:
                                    print('输入错，重新输入')
                            else:
                                choice_xian.lower()
                                if choice_xian=='q':
                                    xian=[]
                                    break
                                elif choice_xian=='x':
                                    xian=[]
                                    flag_shi=False
                                    break
                                elif choice_xian=='e':
                                    print('退出程序，bye！！！')
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

        else:
            print('输入错误，请重新输入！！')
    else :
        choice_sheng.islower()
        if choice_sheng=='e':
             break
        else:
            print('输入错误，请重新输入！！！')


