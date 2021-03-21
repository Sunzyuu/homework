# -*- coding = utf - 8 -*-
#@Time : 2020/12/16 14:52
#@Author : sunzy
#@File : DES_ECB.py

# 两字符进行异或运算
def xor(str1, str2):
    res = ""
    for i in range(0, len(str1)):
        xor_res = int(str1[i], 10)^int(str2[i], 10)
        if xor_res == 1:
            res += '1'
        else:
            res += '0'
    return res

# 处理字符串，将每个字符串都转成八位二进制数
def str_process(str):
    res = ""
    for i in str:
        tmp = bin(ord(i))[2:]
        tmp = (8 - len(tmp)) * '0' + tmp  # 不够八位则在前面补 0
        res += tmp
    return res

# PC-1盒处理密钥
def key_change_1(str):
    change_table = [57,49,41,33,25,17,9,1,
                 58,50,42,34,26,18,10,
                 2,59,51,43,35,27,19,11,
                 3,60,52,44,36,63,55,47,
                 39,31,23,15,7,62,54,46,
                 38,30,22,14,6,61,53,45,
                 37,29,21,13,5,28,20,12,4]
    res = ""
    for i in change_table:
        res += str[i-1]
    return res

# PC-2盒处理密钥
def key_change_2(str):
    change_table = [14,17,11,24,1,5,3,28,
                 15,6,21,10,23,19,12,4,
                 26,8,16,7,27,20,13,2,
                 41,52,31,37,47,55,30,40,
                 51,45,33,48,44,49,39,56,
                 34,53,46,42,50,36,29,32]
    res = ""
    for i in change_table:
        res += str[i-1]
    return res


# 循环左移
def left_run(str, num):
    tmp_str = str[num:len(str)]
    tmp_str = tmp_str+str[0:num]
    return tmp_str


# 生成16个子密钥
def key_gen(str):
    key_list = []
    key_change_res = key_change_1(str)
    key_c = key_change_res[0:28]
    key_d = key_change_res[28:]
    num = [0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for i in range(1, 17): #共16轮
        key_c = left_run(key_c, num[i])
        key_d = left_run(key_d, num[i])
        key_yiwei = key_c + key_d
        key_res = key_change_2(key_yiwei)
        key_list.append(key_res)
    return key_list

# IP盒处理  明文置换
def begin_change(str):
    change_table = [58,50,42,34,26,18,10,2,
                   60,52,44,36,28,20,12,4,
                   62,54,46,38,30,22,14,6,
                   64,56,48,40,32,24,16,8,
                   57,49,41,33,25,17,9,1,
                   59,51,43,35,27,19,11,3,
                   61,53,45,37,29,21,13,5,
                   63,55,47,39,31,23,15,7]
    res = ""
    for i in change_table:
        res += str[i-1]
    return res


# E盒处理  32位->48位
def E_box(str):
    change_table = [32,1,2,3,4,5,4,5,
                    6,7,8,9,8,9,10,11,
                    12,13,12,13,14,15,16,17,
                    16,17,18,19,20,21,20,21,
                    22,23,24,25,24,25,26,27,
                    28,29,28,29,30,31,32,1]
    res = ""
    for i in change_table:
        res += str[i-1]
    return res

# s盒处理   48位->32位
def S_box(str):
    j = 0
    s_list = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
              [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
              [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
              [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
              [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
              [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
              [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
              [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
              ]
    res = ""
    for i in range(0, len(str), 6):
        begin_s = str[i:i + 6]
        row = int(begin_s[0] + begin_s[5], 2)  #第一位和第六位作为行
        col = int(begin_s[1:5], 2)             #中间四位作为列
        index = s_list[j][row * 16 + col]
        num = bin(index)[2:]                   #将匹配的数字转换位二进制数
        for k in range(0, 4 - len(num)):       #不够4位则补0
            num = "0" + num
        res += num
        j = j + 1
    return res

# p盒处理   置换操作
def P_box(str):
    res = ""
    change_table = [16,7,20,21,29,12,28,17,
                    1,15,23,26,5,18,31,10,
                    2,8,24,14,32,27,3,9,
                    19,13,30,6,22,11,4,25]
    for i in change_table:
        res += str[i - 1]
    return res

# F函数
def F_function(str, key):  # 明文右半部分R(32位) -> E盒扩展(48位) -> 与key的子密钥异或 -> S盒置换(32位) -> P置换
    str_e_res = E_box(str)            # 将 E 异或 S  P 集合到一个函数种，便于调用
    xor_res = xor(str_e_res, key)
    str_s_res = S_box(xor_res)
    str_p_res = P_box(str_s_res)
    return str_p_res

# 逆IP盒
def IP_re(str):
    res = ""
    ip_list = [40,8,48,16,56,24,64,32,
               39,7,47,15,55,23,63,31,
               38,6,46,14,54,22,62,30,
               37,5,45,13,53,21,61,29,
               36,4,44,12,52,20,60,28,
               35,3,43,11,51,19,59,27,
               34,2,42,10,50,18,58,26,
               33,1,41,9,49,17,57,25 ]
    for i in ip_list:
        res += str[i-1]
    return res


# DES加密操作
def DESencode(text, key):
    text_bin = str_process(text)     # 将字符转换为二进制数
    text_IP = begin_change(text_bin)  # 明文初始置换
    key_bin = str_process(key)      # 将密钥转换位二进制数
    key_list = key_gen(key_bin)     # key_list 数组中存放着十六个子密钥

    text_left = text_IP[0:32]     # R0
    text_right = text_IP[32:]     # L0

    for i in range(0, 15):      # 十五轮加密

        mes_tmp = text_right     # 临时变量用于左右两部分交换
        text_right = xor(F_function(text_right, key_list[i]) , text_left) #F 函数的作用 R(32位)->E盒(48位)->与key的子密钥异或(32位)->S盒(32位)->P置换(32位)
        text_left = mes_tmp
    fin_right = text_right       # 第十六轮加密
    fin_left = xor(F_function(text_right, key_list[15]), text_left)
    criph_text = fin_left + fin_right
    criph_text = IP_re(criph_text)     #  IP逆置换
    return criph_text

# 针对一组的解密程序
def DESdecode(text, key):  #密文直接输64位2进制
    key_bin = str_process(key)    # 将密钥转换为二进制数
    key_list = key_gen(key_bin)   # 生成的十六个子密钥
    text = begin_change(text)   # 先初始值换 与加密过程相反
    cipher_left = text[0:32]    # R16
    cipher_right = text[32:]    # L16
    i = 15
    while i > 0:                # 十五轮加密 反过来
        cipher_tmp = cipher_right   #设置一个临时变量用于后面的交换
        cipher_right = xor(cipher_left, F_function(cipher_right, key_list[i]))    # F 函数的作用 R(32位)->E盒(48位)->与key的子密钥异或(32位)->S盒(32位)->P置换(32位)
                                                                                  # F 函数处理完后与L(32位)异或
        cipher_left = cipher_tmp    # 左右交换完成
        i = i - 1
    left_text = xor(cipher_left, F_function(cipher_right, key_list[0])) # 一
    right_text = cipher_right                                           # 二 三 这三步是第十六轮加密
    plain_bin = left_text + right_text                                  #
    plain_bin = IP_re(plain_bin)                                        #
    plain_text = ""
    for i in range(0, len(plain_bin), 8):
        plain_text += chr(int(plain_bin[i:i + 8], 2))
    return plain_text

def bintohex(string):
    res = ''
    for i in range(0,len(string),4):
        i = int(i)
        res = res + str(hex(int(string[i:i+4],2))[2:])
    return res

def hextobin(string):
    res = ''
    for i in range(0,len(string)):
        tmp = str(bin(int(string[i],16))[2:])
        tmp = '0'*(4-len(tmp))+ tmp
        res = res + tmp
    return res


def Divide_text(order,text,key):    # 将明文或者明文分组 明文分成8个字符一组，密文则分成64bit一组
    block_text = []
    res = ""
    length = 0
    if order == "E":
        length = 8
    else:
        length = 64
    i = 0
    while text[i:i+length] != "":
        block_text.append(text[i:i+length])
        i += length

    if order == 'E':
        if len(block_text[-1]) != 8:       # 最后一组明文如果不够八个字符则添加 + 补齐八个  否则程序会报错
            block_text[-1] = block_text[-1] + '+' * (8 - len(block_text[-1]))
        for text in block_text:             # 分别对每组加密
            res += DESencode(text, key)
    else:
        for text in block_text:             # 对密文解密
            res += DESdecode(text, key)
    return res

def main():
    while 1:
        plaintext = ''
        ciphertext = ''
        key = ''
        order = input("加密请按E,解密请按D:")
        if order == 'E':
            plaintext = input("请输入明文：")
            key = input("请输入密钥：")
            ciphertext = Divide_text(order, plaintext, key)
            ciphertext = bintohex(ciphertext)
            print("密文是：")
            print(ciphertext)
        else:
            ciphertext = input("请输入密文：")
            ciphertext = hextobin(ciphertext)
            key = input("请输入密钥：")
            plaintext = Divide_text(order, ciphertext, key)
            print("明文是：")
            print(plaintext)

if __name__ == '__main__':
    while 1:
        main()