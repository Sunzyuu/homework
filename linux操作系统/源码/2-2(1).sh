#!/bin/bash
#
#********************************************************************
#Author:         Sunzy
#FileName:     block.sh
#********************************************************************

#[[ $1 == "" ]] && echo "please enter a parameter" || echo $(grep "^$" $1 | wc -l)
if [ $# -eq 0 ]
then 
    echo "至少应该给一个参数!"
elif [ $# -eq 1 ]
then  
	# 使用grep匹配空行
    sum_file=$(grep "^$" $1 | wc -l)
    echo "该文件的空行数为:$sum_file"
elif [ $# -eq 2 ]
then
    sum_file1=$(grep "^$" $1 | wc -l)
    sum_file2=$(grep "^$" $2 | wc -l)
    sum=$[$sum_file1+$sum_file2]
    echo "第一个文件的空行数:$sum_file1"
    echo "第二个文件的空行数:$sum_file2"
    echo "两个文件的空行数总数为:$sum"
else
    echo "参数数量不对!"
fi