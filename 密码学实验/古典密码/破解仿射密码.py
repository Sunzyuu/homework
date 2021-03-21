# -*- coding = utf - 8 -*-
#@Time : 2020/12/16 23:35
#@Author : sunzy
#@File : 破解仿射密码.py

def gcd(a,b):  # 求出最大公因数
    while a!=0:
        a,b = b%a,a
    return b

def findModReverse(a,m): #扩展欧几里得算法求模逆
    if gcd(a,m)!=1:
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3!=0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m

def findAllre():    # 找出所有小于26且与26互素的数
    re_all = []
    for i in range(1,26):
        if gcd(i,26) == 1:
            res = findModReverse(i,26)
            re_all.append(res)
    #re_all.sort()
    return re_all

def decode(s):
    re_all = findAllre()
    for k1 in re_all:
        for k2 in range(0, 26):
            result = ""
            for i in range(len(s)):
                s2 = chr(((int(k1) * (ord(s[i]) - 97 - k2)) % 26 + 97))
                result = result + s2
            print("k1=" + str(findModReverse(k1,26)) + ", k2=" + str(k2) + " plaintext = " + result)

def main():
   # criphertext = 'falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj'
    criphertext = input("请输入要破解的密文: ")
    criphertext = criphertext.lower()
    print("---------"*3+"strat attck"+"---------"*3)
    decode(criphertext)

if __name__ == '__main__':
     main()