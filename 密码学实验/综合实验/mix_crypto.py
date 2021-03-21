import sys
import random
import libnum


from DES_BOX import *
from DES import *
from RSA import *
from MD5 import *


# 生成随机对称密钥
def gen_key(): #num为希望产生伪素数的位数
    list = []
    for i in range(64):
        c = random.choice(['0','1'])
        list.append(c)
    res = "".join(list)
    return res
# 读取明文
def read_out_file():
    try:
        f = open('文章.txt','r',encoding = 'utf-8')
        mess = f.read()
        f.close()
        print("读取成功！")
        return mess
    except IOError:
        print('读取错误！')

