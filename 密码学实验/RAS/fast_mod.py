# -*- coding = utf - 8 -*-
#@Time : 2020/12/29 20:04
#@Author : sunzy
#@File : fast_mod.py

n = 100000000001121212111111111111112212220202212112121
# helle
c = 4483782032471122121342342423423423423432
    # 448378203247
e = 65537
e_bin = bin(e)[2:]
e_bin = str(e_bin)
print(e_bin)
res = 1
for i in range(len(e_bin)):
    res = res ** 2
    if e_bin[i] == "1":
        res = c * res

res = res % n
print(res)
print(pow(c,e,n))

def fast_mod(c,e,n):
    res = 1
    for i in range(len(e_bin)):
        res = res ** 2
        if e_bin[i] == "1":
            res = c * res
    res = res % n
    return res