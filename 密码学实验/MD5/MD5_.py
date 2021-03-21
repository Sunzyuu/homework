# -*- coding = utf - 8 -*-
#@Time : 2020/12/18 21:50
#@Author : sunzy
#@File : MD5.py

import math
# 定义初始向量abcd,并将其转换成2进制,且补0到32位
# 标准的幻数（物理顺序）是（A=(01234567)16，B=(89ABCDEF)16，C=(FEDCBA98)16，D=(76543210)16）。如果在程序中定义应该是:
# （A=0X67452301L，B=0XEFCDAB89L，C=0X98BADCFEL，D=0X10325476L）
ABCD_list = ['67452301','efcdab89','98badcfe','10325476']
for i in range(len(ABCD_list)):
    tmp = bin(int(ABCD_list[i], 16))[2:]
    if len(tmp) < 32:
        tmp = (32 - len(tmp)) * '0' + tmp
    ABCD_list[i] = tmp
A0,B0,C0,D0 = ABCD_list[0], ABCD_list[1], ABCD_list[2], ABCD_list[3]

# 生成第1-64个式子的第i个32比特常数
Ti = []
for i in range(0, 64):
    result = (int(4294967296 * abs(math.sin(i + 1)))) & 0xffffffff
    result = bin(result)[2:]
    if len(result) < 32:
        result = (32 - len(result)) * '0' + result
    Ti.append(result)

# 实现x,y的逐比特与
def and1(x, y):
    res = ''
    for i in range(0, len(x)):
        res += str(int(x[i])&int(y[i]))
    return res
# 实现x,y的逐比特或
def or1(x, y):
    res = ''
    for i in range(0, len(x)):
        res += str(int(x[i])|int(y[i]))
    return res
# 实现x,y的逐比特异或
def xor(x, y):
    res = ''
    for i in range(0, len(x)):
        res += str(int(x[i])^int(y[i]))
    return res
# 实现x的逐比特逻辑反
def reverse(x):
    res = ''
    for i in range(0, len(x)):
        res += str((int(x[i], 2) + 1) % 2)
    return res

# 实现x的循环左移
def shift(x, i):
    res = ''
    for t in range(0, len(x) - i):
        res = res + x[t + i:t + i + 1]   # 先保存 x[i:]  再保存x[:i]
    for y in range(0, i):
        res = res + x[y:y + 1]
    return res

# 实现整数模2的三十二次方加法
def add(x, y):
    a = int(x,2)  #先将二进制转换成十进制
    b = int(y,2)
    res = (a + b)%(2**32)
    res = str(bin(res)[2:])
    if len(res) != 32:    # 补充到32位
        res = (32-len(res))*'0'+res
    return res

# 定义f,g,h,i函数
def ffunc(x, y, z):  # ((x&y)|((~x)&z))
    t = and1(x, y)
    t1 = reverse(x)
    t2 = and1(t1, z)
    return or1(t, t2)

def gfunc(x, y, z):  # ((x&z)|(y&(~z)))
    t = and1(x, z)
    t1 = reverse(z)
    t2 = and1(y, t1)
    return or1(t, t2)

def hfunc(x, y, z): # (x^y^z)
    t1 = xor(x, y)
    t2 = xor(t1, z)
    return t2

def ifunc(x, y, z): # (y^(x|(~z)))
    t = reverse(z)
    t1 = or1(x, t)
    return xor(y, t1)

def fill(text):
    text1 = ''
    for i in text:
        t = str(ord(i))
        t = str(bin(int(t, 10))[2:])
        if len(t) < 8:                 # 将每个字符转换成8位二进制数
            for num in range(8 - len(t)):
                t = '0' + t
        text1 = text1 + t
    length = len(text1)
    length1 = 512 - len(text1) - 65    # length1是要填充0的位数
    text1 = text1 + '1'                # 第一位添加 0
    text1 = text1 + '0'*length1        # 将其补充到 N*512+448  N可以为0
    text2 = bin(length)[2:]            # 将字符长度转换成二进制数
    if len(text2) < 8:                 #  填充后面64位,先填充字符串的长度,再补0
        text2 = '0'*(8 - len(text2)) + text2

    length2 = 64 - len(text2)
    text2 = text2 + '0'*length2        # 填充后面64位,先填充字符串的长度,再补0
    return text1 + text2

# 将最后得到的ABCD逆序输出  最后一步使用
def reverse_order(a):
    res = a[24:32] + a[16:24] + a[8:16] + a[0:8]
    return res

# 输入要加密的明文
password = input("请输入要加密的信息:")
# 填充算法
x = fill(password)


j = 0
M = []
for i in range(0,len(x),32):   # 将512位分成十六组
    M.append(x[i:i+32])
    M[j] = M[j][24:32] + M[j][16:24] + M[j][8:16] + M[j][0:8]
    j+=1

# md5算法的第一步
A,B,C,D= A0,B0,C0,D0  #为第五步 相加原始的A,B,C,D做备份

# md5算法的第二步
AA,BB,CC,DD = A,B,C,D

# md5算法的第三步
# 第一轮     每轮A,B,C,D都处理四次，四轮就是十六次，一共六十四次
for i in range(4):                  # f函数
    A = add(B, shift(add(A, add(add(ffunc(B, C, D), M[4*i]), Ti[4 * i])), 7))
    D = add(A, shift(add(D, add(add(ffunc(A, B, C), M[4*i+1]), Ti[4 * i + 1])), 12))
    C = add(D, shift(add(C, add(add(ffunc(D, A, B), M[4*i+2]), Ti[4 * i + 2])), 17))
    B = add(C, shift(add(B, add(add(ffunc(C, D, A), M[4*i+3]), Ti[4 * i + 3])), 22))

# 第二轮
k = 1
j = 16
for i in range(4):
    A = add(B, shift(add(A, add(add(gfunc(B, C, D), M[(k+5*(4*i))%16]), Ti[j + i * 4])), 5))
    D = add(A, shift(add(D, add(add(gfunc(A, B, C), M[(k+5*(4*i+1))%16]), Ti[j + i * 4 + 1])), 9))
    C = add(D, shift(add(C, add(add(gfunc(D, A, B), M[(k+5*(4*i+2))%16]), Ti[j + i * 4 + 2])), 14))
    B = add(C, shift(add(B, add(add(gfunc(C, D, A), M[(k+5*(4*i+3))%16]), Ti[j + i * 4 + 3])), 20))

# 第三轮
k = 5
j = 32
for i in range(4):
    A = add(B, shift(add(A, add(add(hfunc(B, C, D), M[(k+i*4*3)%16]), Ti[j + i * 4])), 4))
    D = add(A, shift(add(D, add(add(hfunc(A, B, C), M[(k+(i*4+1)*3)%16]), Ti[j + i * 4 + 1])), 11))
    C = add(D, shift(add(C, add(add(hfunc(D, A, B), M[(k+(i*4+2)*3)%16]), Ti[j + i * 4 + 2])), 16))
    B = add(C, shift(add(B, add(add(hfunc(C, D, A), M[(k+(i*4+3)*3)%16]), Ti[j + i * 4 + 3])), 23))

# 第四轮
k = 0
j = 48
for i in range(4):
    A = add(B, shift(add(A, add(add(ifunc(B, C, D), M[(k+(i*4)*7)%16]), Ti[j + i * 4])), 6))
    D = add(A, shift(add(D, add(add(ifunc(A, B, C), M[(k+(i*4+1)*7)%16]), Ti[j + i * 4 + 1])), 10))
    C = add(D, shift(add(C, add(add(ifunc(D, A, B), M[(k+(i*4+2)*7)%16]), Ti[j + i * 4 + 2])), 15))
    B = add(C, shift(add(B, add(add(ifunc(C, D, A), M[(k+(i*4+3)*7)%16]), Ti[j + i * 4 + 3])), 21))
# 第五步  将计算出的A,B,C,D与初始的相加，并赋值
A,B,C,D = add(A, AA),add(B, BB),add(C, CC),add(D, DD)
# 输出得到的密文

ciphertext = reverse_order(A) + reverse_order(B) + reverse_order(C) + reverse_order(D)
cipher = ciphertext
ciphertext = str(hex(int(ciphertext, 2))[2:])   # 将二进制数转换为十六进制数
ciphertext = '0'*(32-len(ciphertext))+ciphertext # 为了避免第一个数字为零时无法显示出来
print("hash值(小写):",ciphertext)
print("hash值(大写):",ciphertext.upper())

