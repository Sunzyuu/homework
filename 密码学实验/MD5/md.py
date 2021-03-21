# -*- coding = utf - 8 -*-
#@Time : 2020/12/18 21:50
#@Author : sunzy
#@File : md.py
import math
# 定义初始向量abcd,并将其转换成2进制,且补0到32位

ABCD_list = ['67452301','efcdab89','98badcfe','10325476']
for i in range(len(ABCD_list)):
    tmp = bin(int(ABCD_list[i], 16))[2:]
    if len(tmp) < 32:
        tmp = (32 - len(tmp)) * '0' + tmp
    ABCD_list[i] = tmp

A0,B0,C0,D0 = ABCD_list[0], ABCD_list[1], ABCD_list[2], ABCD_list[3]

# 定义第1-64个式子的第i个32比特常数
y = {}
for i in range(0, 64):
    result = (int(4294967296 * abs(math.sin(i + 1)))) & 0xffffffff
    result = bin(result)[2:]
    if len(result) < 32:
        result = (32 - len(result)) * '0' + result
    y[i] = result
    print(y[i])

# 实现x,y的逐比特与
def and1(x, y):
    z = ''
    for i in range(0, len(x)):
        z += str(int(x[i]) & int(y[i]))
    return z

# 实现x,y的逐比特或
def or1(x, y):
    z = ''
    for i in range(0, len(x)):
        z += str(int(x[i])|int(y[i]))
    return z
# 实现x,y的逐比特异或
def xor(x, y):
    z = ''
    for i in range(0, len(x)):
        z += str(int(x[i])^int(y[i]))
    return z

# 实现x的逐比特逻辑反
def reverse(x):
    z = ''
    for i in range(0, len(x)):
        z += str((int(x[i], 2) + 1) % 2)
    return z

# 实现x的循环左移
def shift(x, i):
    z = ''
    for t in range(0, len(x) - i):
        z = z + x[t + i:t + i + 1]
    for y in range(0, i):
        z = z + x[y:y + 1]
    return z

# 实现整数模2的三十二次方加法
def add(x, y):
    a = int(x,2)
    b = int(y,2)
    res = (a + b)%(2**32)
    res = str(bin(res)[2:])
    if len(res) != 32:
        res = (32-len(res))*'0'+res
    return res

# 定义f,g,h,i函数
def ffunc(x, y, z):
    t = and1(x, y)
    t1 = reverse(x)
    t2 = and1(t1, z)
    return or1(t, t2)

def gfunc(x, y, z):
    t = and1(x, z)
    t1 = reverse(z)
    t2 = and1(y, t1)
    return or1(t, t2)

def hfunc(x, y, z):
    t1 = xor(x, y)
    t2 = xor(t1, z)
    return t2

def ifunc(x, y, z):
    t = reverse(z)
    t1 = or1(x, t)
    return xor(y, t1)

# 填充算法
def fill(text):
    text1 = ''
    for i in text:
        t = str(ord(i))
        t = bin(int(t, 10)).replace("0b", "")
        t = str(t)
        if len(t) < 8:
            for num in range(8 - len(t)):
                t = '0' + t
        text1 = text1 + t
    length = len(text1)
    length1 = 512 - len(text1) - 65
    text1 = text1 + '1'
    for i in range(length1):
        text1 = text1 + '0'
    text2 = bin(length).replace('0b', '')
    # 填充后面64位
    if len(text2) < 8:
        for i in range(8 - len(text2)):
            text2 = '0' + text2
    length2 = 64 - len(text2)
    for t in range(length2):
        text2 = text2 + '0'
    return text1 + text2


# 将最后得到的ABCD逆序输出
def reverse_order(a):
    new_a = a[24:32] + a[16:24] + a[8:16] + a[0:8]
    return new_a

# 输入要加密的明文
password = input("请输入要加密的信息")
# 填充算法
x = fill(password)
# 处理数据,这里设计到大端序和小端序的问题,大家百度哈
M0 = x[0:32]
M0 = M0[24:32] + M0[16:24] + M0[8:16] + M0[0:8]
M1 = x[32:64]
M1 = M1[24:32] + M1[16:24] + M1[8:16] + M1[0:8]
M2 = x[64:96]
M2 = M2[24:32] + M2[16:24] + M2[8:16] + M2[0:8]
M3 = x[96:128]
M3 = M3[24:32] + M3[16:24] + M3[8:16] + M3[0:8]
M4 = x[128:160]
M4 = M4[24:32] + M4[16:24] + M4[8:16] + M4[0:8]
M5 = x[160:192]
M5 = M5[24:32] + M5[16:24] + M5[8:16] + M5[0:8]
M6 = x[192:224]
M6 = M6[24:32] + M6[16:24] + M6[8:16] + M6[0:8]
M7 = x[224:256]
M7 = M7[24:32] + M7[16:24] + M7[8:16] + M7[0:8]
M8 = x[256:288]
M8 = M8[24:32] + M8[16:24] + M8[8:16] + M8[0:8]
M9 = x[288:320]
M9 = M9[24:32] + M9[16:24] + M9[8:16] + M9[0:8]
M10 = x[320:352]
M10 = M10[24:32] + M10[16:24] + M10[8:16] + M10[0:8]
M11 = x[352:384]
M11 = M11[24:32] + M11[16:24] + M11[8:16] + M11[0:8]
M12 = x[384:416]
M12 = M12[24:32] + M12[16:24] + M12[8:16] + M12[0:8]
M13 = x[416:448]
M13 = M13[24:32] + M13[16:24] + M13[8:16] + M13[0:8]
M14 = x[448:480]
M14 = M14[24:32] + M14[16:24] + M14[8:16] + M14[0:8]
M15 = x[480:512]
M15 = M15[24:32] + M15[16:24] + M15[8:16] + M15[0:8]

# md5算法的第一步
A = A0
B = B0
C = C0
D = D0

# md5算法的第二步
AA = A
BB = B
CC = C
DD = D

# md5算法的第三步
# 第一轮
A = add(B, shift(add(A, add(add(ffunc(B, C, D), M0), y[0])), 7))
D = add(A, shift(add(D, add(add(ffunc(A, B, C), M1), y[1])), 12))
C = add(D, shift(add(C, add(add(ffunc(D, A, B), M2), y[2])), 17))
B = add(C, shift(add(B, add(add(ffunc(C, D, A), M3), y[3])), 22))

A = add(B, shift(add(A, add(add(ffunc(B, C, D), M4), y[4])), 7))
D = add(A, shift(add(D, add(add(ffunc(A, B, C), M5), y[5])), 12))
C = add(D, shift(add(C, add(add(ffunc(D, A, B), M6), y[6])), 17))
B = add(C, shift(add(B, add(add(ffunc(C, D, A), M7), y[7])), 22))

A = add(B, shift(add(A, add(add(ffunc(B, C, D), M8), y[8])), 7))
D = add(A, shift(add(D, add(add(ffunc(A, B, C), M9), y[9])), 12))
C = add(D, shift(add(C, add(add(ffunc(D, A, B), M10), y[10])), 17))
B = add(C, shift(add(B, add(add(ffunc(C, D, A), M11), y[11])), 22))

A = add(B, shift(add(A, add(add(ffunc(B, C, D), M12), y[12])), 7))
D = add(A, shift(add(D, add(add(ffunc(A, B, C), M13), y[13])), 12))
C = add(D, shift(add(C, add(add(ffunc(D, A, B), M14), y[14])), 17))
B = add(C, shift(add(B, add(add(ffunc(C, D, A), M15), y[15])), 22))

# 第二轮
A = add(B, shift(add(A, add(add(gfunc(B, C, D), M1), y[16])), 5))
D = add(A, shift(add(D, add(add(gfunc(A, B, C), M6), y[17])), 9))
C = add(D, shift(add(C, add(add(gfunc(D, A, B), M11), y[18])), 14))
B = add(C, shift(add(B, add(add(gfunc(C, D, A), M0), y[19])), 20))

A = add(B, shift(add(A, add(add(gfunc(B, C, D), M5), y[20])), 5))
D = add(A, shift(add(D, add(add(gfunc(A, B, C), M10), y[21])), 9))
C = add(D, shift(add(C, add(add(gfunc(D, A, B), M15), y[22])), 14))
B = add(C, shift(add(B, add(add(gfunc(C, D, A), M4), y[23])), 20))

A = add(B, shift(add(A, add(add(gfunc(B, C, D), M9), y[24])), 5))
D = add(A, shift(add(D, add(add(gfunc(A, B, C), M14), y[25])), 9))
C = add(D, shift(add(C, add(add(gfunc(D, A, B), M3), y[26])), 14))
B = add(C, shift(add(B, add(add(gfunc(C, D, A), M8), y[27])), 20))

A = add(B, shift(add(A, add(add(gfunc(B, C, D), M13), y[28])), 5))
D = add(A, shift(add(D, add(add(gfunc(A, B, C), M2), y[29])), 9))
C = add(D, shift(add(C, add(add(gfunc(D, A, B), M7), y[30])), 14))
B = add(C, shift(add(B, add(add(gfunc(C, D, A), M12), y[31])), 20))

# 第三轮
A = add(B, shift(add(A, add(add(hfunc(B, C, D), M5), y[32])), 4))
D = add(A, shift(add(D, add(add(hfunc(A, B, C), M8), y[33])), 11))
C = add(D, shift(add(C, add(add(hfunc(D, A, B), M11), y[34])), 16))
B = add(C, shift(add(B, add(add(hfunc(C, D, A), M14), y[35])), 23))

A = add(B, shift(add(A, add(add(hfunc(B, C, D), M1), y[36])), 4))
D = add(A, shift(add(D, add(add(hfunc(A, B, C), M4), y[37])), 11))
C = add(D, shift(add(C, add(add(hfunc(D, A, B), M7), y[38])), 16))
B = add(C, shift(add(B, add(add(hfunc(C, D, A), M10), y[39])), 23))

A = add(B, shift(add(A, add(add(hfunc(B, C, D), M13), y[40])), 4))
D = add(A, shift(add(D, add(add(hfunc(A, B, C), M0), y[41])), 11))
C = add(D, shift(add(C, add(add(hfunc(D, A, B), M3), y[42])), 16))
B = add(C, shift(add(B, add(add(hfunc(C, D, A), M6), y[43])), 23))

A = add(B, shift(add(A, add(add(hfunc(B, C, D), M9), y[44])), 4))
D = add(A, shift(add(D, add(add(hfunc(A, B, C), M12), y[45])), 11))
C = add(D, shift(add(C, add(add(hfunc(D, A, B), M15), y[46])), 16))
B = add(C, shift(add(B, add(add(hfunc(C, D, A), M2), y[47])), 23))

# 第四轮
A = add(B, shift(add(A, add(add(ifunc(B, C, D), M0), y[48])), 6))
D = add(A, shift(add(D, add(add(ifunc(A, B, C), M7), y[49])), 10))
C = add(D, shift(add(C, add(add(ifunc(D, A, B), M14), y[50])), 15))
B = add(C, shift(add(B, add(add(ifunc(C, D, A), M5), y[51])), 21))

A = add(B, shift(add(A, add(add(ifunc(B, C, D), M12), y[52])), 6))
D = add(A, shift(add(D, add(add(ifunc(A, B, C), M3), y[53])), 10))
C = add(D, shift(add(C, add(add(ifunc(D, A, B), M10), y[54])), 15))
B = add(C, shift(add(B, add(add(ifunc(C, D, A), M1), y[55])), 21))

A = add(B, shift(add(A, add(add(ifunc(B, C, D), M8), y[56])), 6))
D = add(A, shift(add(D, add(add(ifunc(A, B, C), M15), y[57])), 10))
C = add(D, shift(add(C, add(add(ifunc(D, A, B), M6), y[58])), 15))
B = add(C, shift(add(B, add(add(ifunc(C, D, A), M13), y[59])), 21))

A = add(B, shift(add(A, add(add(ifunc(B, C, D), M4), y[60])), 6))
D = add(A, shift(add(D, add(add(ifunc(A, B, C), M11), y[61])), 10))
C = add(D, shift(add(C, add(add(ifunc(D, A, B), M2), y[62])), 15))
B = add(C, shift(add(B, add(add(ifunc(C, D, A), M9), y[63])), 21))

# 第五步
A = add(A, AA)
B = add(B, BB)
C = add(C, CC)
D = add(D, DD)

# 输出得到的密文
answer = reverse_order(A) + reverse_order(B) + reverse_order(C) + reverse_order(D)
print(hex(int(answer, 2))[2:])
