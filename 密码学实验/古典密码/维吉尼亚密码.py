# -*- coding = utf - 8 -*-
#@Time : 2020/12/11 14:14
#@Author : sunzy
#@File : 维吉尼亚密码.py

# 将密钥处理成和密文/明文一样长
def solve_key(s,key):
    nkey = key
    while len(nkey) < len(s):
        nkey = nkey+key
    nkey = nkey[:len(s)]
    return nkey

# 加密函数
def encode(s,key):
    print('加密后的结果： ',end='')
    s1 = s.upper()
    key1 = solve_key(s, key)
    key1 = key1.upper()

    result = ""
    for i in range(0,len(s)):
        s2 = chr(abs(((ord(s1[i])-65)+(ord(key1[i])-65)) % 26) + 65)
        result = result + s2
    print(result.lower())

# 解密函数
def decode(s,key):
    print('解密后的结果： ', end='')
    s1 = s.upper()
    key1 = solve_key(s, key)
    key1 = key1.upper()

    result = ""
    for i in range(0, len(s)):
        s2 = chr(((ord(s1[i]) - 65) - (ord(key1[i]) - 65)) % 26 + 65)
        result = result + s2
    print(result.lower())

def main():
    while 1:
        # 函数入口
        answer = input(f'请输入所需的操作：编码/E or 解码/D:  ')
        try:
            if answer.upper() == 'E':
                key = input('请输入密钥: ')
                key = "".join(filter(str.isalpha, key))
                s = input('请输入明文: ')
                s = "".join(filter(str.isalpha, s))  # 将字符串中的非字母字符去掉
                # print(s)
                encode(s, key)
            elif answer.upper() == 'D':
                key = input('请输入密钥: ')
                key = "".join(filter(str.isalpha, key))
                s = input('请输入密文: ')
                s = "".join(filter(str.isalpha, s))
                decode(s, key)
            else:
                print('输入错误！')
        except KeyError:
            print('请检查输入是否正确！')

if __name__ == '__main__':
    main()