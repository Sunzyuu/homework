#!/bin/bash
#
#********************************************************************
#Author:        Sunzy
#FileName:      file.sh
#********************************************************************

# 统计/etc, /var, /usr目录中共有多少个一级子目录和文件
etcnum=$(ls -d /etc/* |wc -l)
varnum=$(ls -d /var/* |wc -l)
usrnum=$(ls -d /usr/* |wc -l)

echo "sum_etc: $etcnum"
echo "sum_var: $varnum"
echo "sum_usr: $usrnum"

sum=$[$etcnum+$varnum+$usrnum]
echo "etc_var_usr_sum:$sum"

# 计算参数A到B所有数字的总和
read -p "第一个参数A:" A
read -p "第二个参数B:" B
if [[ $A -le $B ]]then;
echo $(seq $A $B) |tr ' ' + |bc
else
echo $(seq $B $A) |tr ' ' + |bc
fi