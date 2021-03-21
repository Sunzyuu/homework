# -*- coding = utf - 8 -*-
#@Time : 2020/12/23 21:01
#@Author : sunzy
#@File : RC4.py

import hashlib
import base64
'''
初始化T向量
for i = 0 to 255 do
    S[i] = i;
    T[i] = K[i mod keylen]
'''

# S盒初始化置换,Key为密钥
def Rc4_init(S, Key):
    j = 0
    Key = Key.encode('UTF-8')
    Key = hashlib.md5(Key).hexdigest()      # 生成长度为32的字符串作为新的密钥
    t = []
    for i in range(256):      # S中为0-255
        S.append(i)
        t.append(Key[i % len(Key)])
    for i in range(256):      # 打乱 S 中的顺序
        j = (j + S[i] + ord(t[i])) % 256
        S[i], S[j] = S[j], S[i]             # 交换S[i],S[j]

def rc4_Encode(S, plaintext):
    i = j = 0
    result = ''
    for a in plaintext:    # 对明文中的每一位进行加密
        i = (i + 1) % 256       # 经过变换后得到密文
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = chr(ord(a) ^ S[t])  # 明文与密钥异或得到密文
        result += k
    result = base64.b64encode(result.encode('UTF-8'))  #因为加密后会有不可见字符故使用base64编码
    result = result.decode()
    return result


def rc4_Decode(S, criphtext):  # 解密过程就是加密过程的逆过程 原理就是 a^b^b = a
    i = j = 0
    criphtext = base64.b64decode(criphtext)
    criphtext = str(criphtext.decode())
    result = ''
    for a in criphtext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = chr(ord(a) ^ S[t])
        result += k
    return result

def main():
    while 1:
        order = input("请输入指令,加密/E,解密/D :")
        if order.upper() =='E':
            plaintext = input('请输入明文: ')
            key = input("请输入密钥: ")
            s = []
            Rc4_init(s, key) # 加密之前初始化S盒和T
            cryphtext = rc4_Encode(s, plaintext)
            print("密文为: ", cryphtext)
            print('\n')

        else:
            cryphtext = input("请输入密文: ")
            key = input("请输入密钥: ")
            s = []
            Rc4_init(s, key)    # 解密之前也是需要先初始化S盒
            plaintext = rc4_Decode(s, cryphtext)
            print("明文为: ", plaintext)
            print('\n')
if __name__ == '__main__':
    main()

