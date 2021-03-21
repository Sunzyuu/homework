# -*- coding = utf - 8 -*-
#@Time : 2020/12/15 16:28
#@Author : sunzy
#@File : LFSR.py

def lfsr(inti, top):
    sum = 0
    inti2 = "0"*len(inti)
    inti2 = list(inti2)             # 初始化出一个与原始序列等长的列表，便于后面的计算
    inti1 = ''
    for i in range(len(inti)):
        if top[i] == "1":
            sum += int(inti[i])     # 计算本原多项式中1的个数
    sum = sum % 2                   # 计算出第一位的值
    for i in range(len(inti)):      # 实现左移
        if i == 0:
            inti2[i] = str(sum)
        else:
            inti2[i] = inti[i - 1]
    inti1 = inti1.join(inti2)       # 将数组转成字符串
    return inti1

def main():
    inti_str = str(input("请输入初始化序列："))
    inti_str_backup = inti_str          # 备份初始化序列，用于后面的比较
    top = str(input("请输入本原多项式："))
    top = top[::-1]
    for i in range(2 ** len(inti_str) + 1):
        if inti_str_backup == inti_str and i != 0 and i == 2 ** len(inti_str) - 1:
            print("第{0}次".format(i), inti_str_backup)
            print("是本原多项式且周期是" + str(i))
            break
        elif inti_str_backup == inti_str and i != 0 and i != 2 ** len(inti_str) - 1:
            print("第{0}次".format(i), inti_str_backup)
            print("不是本原多项式且周期是" + str(i))
            break
        print("第{0}次".format(i), inti_str_backup)
        inti_str_backup = lfsr(inti_str_backup, top)

if __name__ == '__main__':
    main()

'''
lst = 011100010100100101
key = 011100010100100101
本原多项式,周期为2^18-1=262143

key = 1000100000000101

key = 1010100000000001  

key = 10000000000000100
key = 10000000000000000100
lst = 111
key = 101
本原多项式,周期为2^3-1=7

lst = 1111
key = 1111
非本原多项式,周期为5 
'''
# 1010100000000001