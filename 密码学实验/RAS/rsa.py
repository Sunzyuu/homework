# -*- coding = utf - 8 -*-
#@Time : 2020/12/23 14:24
#@Author : sunzy
#@File : rsa.py

from Crypto.Util.number import *
import random

# 模重复平方法
def fast_mod(p,q,n):     # p为底数，p为指数
    res = 1
    while q:
        if q & 1:
            res = (res * p) % n
        q >>= 1             # 右移1位
        p = (p * p) % n
    return res

# 计算出d
#这个扩展欧几里得算法求模逆,用于求d
def caculateD(a, m):
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3!=0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m


# 将字符转化为十六进制字符串
def str2Hex(m):
    return "".join("{:02x}".format(ord(x)) for x in m)

# 素性检验：采用 Miler-Rabin 检验法
# 所有的𝑟 ∈ [0, 𝑠 − 1]，若𝑎^𝑑 ≠ 1(𝑚𝑜𝑑 𝑛)且𝑎^((2^𝑟)*𝑑) ≠ −1(𝑚𝑜𝑑 𝑛)，则𝑛是合数。否则，𝑛有 3/4的概率为素数
def miller_rabin(n):
    s = n - 1
    t = 0
    while s % 2 == 0:  # n,s,t之间的关系为 n = 2^s * t
        s = s // 2
        t += 1
    for trials in range(10):   # 可以多增加几轮保证大概率为素数
        a = random.randrange(2, n - 1) # 随机生成a
        v = pow(a, s, n)               # 验证 a^(n-1) mod n
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % n
    return True
# 生成素数 先生成1024位的奇数，再进行素性检验，通过则生成该素数
def genPrime(b=1024):
    while True:                             # 设置死循环直到生成素数才退出
        res = "1"
        for i in range(b-2):
            res += str(random.randint(0,1))
        res += "1"                              # 最后一位为1保证为奇数
        res = int(res,2)
        if miller_rabin(res):
            return res                          # 直到该数通过素数检验才推出循环

def genE(phi_n):
    while True:
        e = genPrime(b=random.randint(3,13))  #随机生成e
        if e < 2000 :                  # e不能太小
            continue
        if phi_n%e != 0:               # 保证e不能被phi整除
            return e

def RSAEncode(m, e, n):               # 加密公式 m^e mod n
    m = int(str2Hex(m), 16)           # 将字符转换为二进制
    c = fast_mod(m, e, n)
    return c

def RSADecode(c, d, n):                 # 加密公式 c^d mod n
    plaintext = fast_mod(c,d,n)
    plaintext = str(long_to_bytes(plaintext).decode()) # 将数字转换为字符
    return plaintext


def main():
    # 生成两个大素数p和q
    print("Generate p,q and e, please wait... ")
    p = genPrime()
    q = genPrime()
    print ("p = "+str(p))
    print ("q = "+str(q))
    n = p*q
    print ("n = "+str(n))
    # 用欧拉定理计算 phi_n
    phi_n = (p-1)*(q-1)
    # 生成e
    e = genE(phi_n)
    print ("e = "+str(e))
    # m = "Hello world!"
    m = str(input('请输入明文: '))
    # 加密算法
    Cryphtext = RSAEncode(m, e, n)
    print ("The Ciphertext is: "+str(Cryphtext))
    # 解密算法
    d = caculateD(e, phi_n)
    Plaintext = RSADecode(Cryphtext, d, n)
    print ("The Plaintext is: "+Plaintext)
if __name__ == '__main__':
    main()