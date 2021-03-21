# -*- coding = utf - 8 -*-
#@Time : 2020/12/11 15:20
#@Author : sunzy
#@File : 仿射密码.py

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

def encode(a,b,s):
    result = ""
    s = s.upper()
    for i in range(0,len(s)):
        s2 = chr((a*(ord(s[i])-65)+b)%26 + 65)
        result = result +s2
    print(result.lower())

def decode(a,b,s):
    a1 = findModReverse(a,26)
    result = ""
    s = s.upper()
    for i in range(0, len(s)):
        s2 = chr((a1 * (ord(s[i]) - 65 - b)) % 26 + 65)
        result = result + s2
    print(result.lower())

def s_decode(a,b,s):
    letter ='abcdefghijklmnopqrstuvwxyz'
    letter = letter.upper()
    s = s.upper()
    result = ""
    for i in s:
        for j in range(0,len(letter)):
            if i == letter[(a*j+b)%26]:
                result = result+letter[j]
    print(result.lower())

def main():
    answer = input(f'请输入所需的操作：编码/E or 解码/D: ')
    try:
        if answer.upper() == 'E':
            a = int(input('请输入a:'))
            b = int(input('请输入b:'))
            s = input('请输入需要加密的字符:')
            encode(a, b, s)
        elif answer.upper() == 'D':
            a = int(input('请输入a:'))
            b = int(input('请输入b:'))
            s = input('请输入需要解密的字符：')
            decode(a, b, s)  # 利用逆元解密
            # s_decode(a,b,s)   # 暴力枚举每一个字符
        else:
            print('输入错误！')
    except KeyError:
        print('请勿输入空格！')

if __name__ == '__main__':
    main()

# letter = 'abcdefghijklmnopqrstuvwxyz'
# plain = firstthesentenceandthentheevidencesaidthequeen
# crypto = falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj
