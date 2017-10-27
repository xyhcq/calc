# -*- coding:utf-8 -*-
import random

print "四则运算计算器"

# 运算符
ops = ['+', '-', '*', '/']

# 用户的答案
answer = ""

# 题号
i = 1

#难度控制
hard = raw_input('请输入产生随机数的最大值：')

sw=1
while sw:
    if hard.isdigit():
        hard=int(hard)
        sw=0
    else :
        hard = raw_input('请输入产生随机数的最大值：')
        sw=1

# 题目数量
number = raw_input('请输入题目数量：')

sw1=1
while sw1:
    if number.isdigit():
        #number=int(number)
        sw1=0
    else :
        number = raw_input('请输入题目数量：')
        sw1=1

while int(number)> 4**hard:
    print '你输入的数将产生重复的题，请重新输入'
    number = raw_input('请输入题目数量：')       

# 计算正确和错误的数量
calc_true, calc_false= 0,0

eq=''
used_eq=[]

while i < int(number) + 1:
    # 生成第一个数和第二个数
    num1 = random.randint(1, hard)*1.0
    num2 = random.randint(1, hard)*1.0
    # 随机生成运算符
    op = random.randint(0, 3)
    # 产生算式和答案
    eq = str(num1) + ops[op] + str(num2)

    # 判断是否重复，重复则重新生成
    while eq in used_eq:
        # 生成第一个数和第二个数
        num1 = random.randint(1, hard)*1.0
        num2 = random.randint(1, hard)*1.0
        # 随机生成运算符
        op = random.randint(0, 3)
        # 产生算式和答案
        eq = str(num1) + ops[op] + str(num2)

    # 将算式添加到用过的算式列表
    used_eq.append(eq)

    value =eval(eq)

    # 显示问题
    print "问题%d: %s=" % (i, eq)
    # 接收用户的答案
    answer = raw_input("请输入答案: ")
    while answer == '':
        answer = raw_input("答案不能为空，请重新输入: ")
    # 判断正误
    if value == float(answer):
        print "回答正确！"
        calc_true+=1
    else:
        print "回答错误，正确答案是： %d" % value
        calc_false+=1
    # 刷新题号
    i += 1

print '共计算'+str(number)+'道题,\n计算正确'+str(calc_true)+'道题,\n计算错误'+str(calc_false)+'道题。'
