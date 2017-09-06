
#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: lesson_dict.py

@time: 2017/9/2 22:11

@desc:

'''


#dic={1:'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
# dic={'age':'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}

# print(dic)

#字典两大特点：无序，键唯一（不能使用可变的做键）


#字典的创建方式
#  方法一：
# dic={'name':'alex'}
# 方法二：
# dic1={}
#可以是元祖的形式赋值
# dic2=dict((('name','alex'),))
# print(dic2)
# 也可以是列表的形式赋值
# dic3=dict([['name','alex'],])
# print(dic3)
# 值修改赋予的方式
# dic1={'name':'alex'}
# dic1['age']=18
# print(dic1)

#setdefault方法
# 键存在，不改动，返回字典中相应的键对应的值，这只默认键的方法
# ret=dic1.setdefault('age',34)
# print(ret)

# #键不存在，在字典中中增加新的键值对，并返回相应的值
# ret2=dic1.setdefault('hobby','girl')
# print(dic1)
# print(ret2)

#查  通过键去查找
# dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'}
#
# print(dic3['name'])
#获取键列表
# print(list(dic3.keys()))
# 返回键值列表
# print(list(dic3.values()))
#返回键值对
# print(list(dic3.items()))

# li=[1,2,34,4]
# li[2]=5
# dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'}
# dic3['age']=55
# print(dic3)

# dic4={'age': 18, 'name': 'alex', 'hobby': 'girl'}
# # dic5={'1':'111','2':'222'}
# dic5={'1':'111','name':'222'}
#更新dic5的内容到dic4中去，无则加，有则覆盖
# dic4.update(dic5)
# print(dic4)
# print(dic5)


# dic5 = {'name': 'alex', 'age': 18, 'class': 1}

# dic5.clear() # 清空字典
# print(dic5)
# del dic5['name'] #删除字典中指定键值对
# print(dic5)


# print(dic5.pop('age')) #删除字典中指定键值对，并返回该键值对的值
# ret=dic5.pop('age')
# print(ret)
# print(dic5)

# a = dic5.popitem() #随机删除某组键值对，并以元组方式返回值
# print(a, dic5)

# del dic5        #删除整个字典
# print(dic5)


#5 其他操作以及涉及到的方法

# fromkeys基本不用，有问题的，特别是在键值对，值为列表或者字典的时候
# dic6=dict.fromkeys(['host1','host2','host3'],'test')
# 值为字符串的时候没问题
# print(dic6)#{'host3': 'test', 'host1': 'test', 'host2': 'test'}
#
# dic6['host2']='abc'
# print(dic6)
# 如果值为可变的时候，会出现问题的
# dic6=dict.fromkeys(['host1','host2','host3'],['test1','tets2'])
# print(dic6)#{'host2': ['test1', 'tets2'], 'host3': ['test1', 'tets2'], 'host1': ['test1', 'tets2']}
#
# dic6['host2'][1]='test3'
# print(dic6)#{'host3': ['test1', 'test3'], 'host2': ['test1', 'test3'], 'host1': ['test1', 'test3']}



#  字典嵌套
# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }

# av_catalog['欧美']["www.youporn.com"][1]='高清午马'


dic={5:'555',2:'666',4:'444'}
# dic.has_keys(5)
# print(5 in dic)
# 字典的排序
# print(sorted(dic.items()))  # 可以指定排序的列
# dic5={'name': 'alex', 'age': 18}

# 打印键值
# 法一 推荐
# for i in dic5:
#  i 取出来的是键
#     print(i,dic5[i])+
# 法二
# for i,v in dic5.items():  #item方法对性能有影响
#     print(i,v)



#String 操作

# a="Let's go "
# print(a)
# 1   * 重复输出字符串
# print('hello'*20)

# 2 [] ,[:] 通过索引获取字符串中字符,这里和列表的切片操作是相同的,具体内容见列表
# print('helloworld'[2:])

#关键字 in  是否在列表里边
# print(123 in [23,45,123])
# print('e2l' in 'hello')

# 4 %   格式字符串
# print('alex is a good teacher')
# print('%s is a good teacher'%'alex')

#5 字符串的拼接  非常重要
# a='123'
# b='abc'
# d='44'
# # # c=a+b
# # # print(c)
# #
# c= ''.join([a,b,d])  #  前边''设个字符串
# print(c)



# String的内置方法

# st='hello kitty {name} is {age}'
#
# print(st.count('l'))       #  统计元素个数
# print(st.capitalize())     #  首字母大写
# print(st.center(50,'#'))   #  居中，补齐50字符
# print(st.endswith('tty3')) #  判断是否以某个内容结尾
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.expandtabs(tabsize=20)) # 设置tab空格的数量，长度
# print(st.find('t'))        #  查找到第一个元素，并将索引值返回
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print(st.format_map({'name':'alex','age':22}))
# print(st.index('t'))  # 查询到输出，不存在报错
# print('asd'.isalnum())
# print('12632178'.isdecimal())
# print('1269999.uuuu'.isnumeric())
# print('abc'.isidentifier())  # 是否一个非法的字符（变量）
# print('Abc'.islower())
# print('ABC'.isupper())
# print('  e'.isspace())
# print('My title'.istitle())
# print('My tLtle'.lower())
# print('My tLtle'.upper())
# print('My tLtle'.swapcase())
# print('My tLtle'.ljust(50,'*'))
# print('My tLtle'.rjust(50,'*'))
# print('\tMy tLtle\n'.strip()) # 去掉左右的空格和换行符
# print('\tMy tLtle\n'.lstrip())
# print('\tMy tLtle\n'.rstrip())
# print('ok')
# print('My title title'.replace('itle','lesson',1))
# print('My title title'.rfind('t'))  # 取到的是真实的索引值
# print('My title title'.split('i',1))
# print('My title title'.title())


#摘一些重要的字符串方法
#1 print(st.count('l'))  # 字符串中字母出现的次数
# print(st.center(50,'#'))   #  居中
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.find('t')) #  查找到第一个元素，并将索引值返回
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print('My tLtle'.lower())  # 变小写
# print('My tLtle'.upper()) # 变大写
# print('\tMy tLtle\n'.strip()) # 去除字符串的空格和特殊字符
# print('My title title'.replace('itle','lesson',1))  # 替换
# print('My title title'.split('i',1)) # 分割