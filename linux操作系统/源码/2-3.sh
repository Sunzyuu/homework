#!/bin/bash
#
#********************************************************************
#Author:        Sunzy
#FileName:      IPv4.sh
#********************************************************************

#ipv4地址的正则匹配表达式
ipaddr='(\<([0-9]|[1-9][0-9]|1[0-9]{2}|2([0-4][0-9]|5[0-5]))\>\.){3}\<([0-9]|[1-9][0-9]|1[0-5][1-9]|2([0-4][0-9]|5[0-4]))\>'
    read -p "请输入一个IPv4地址: " ipv4
    if [[ $ipv4 =~ $ipaddr ]];then 
        echo "This a legal IP."
        ping -c 4 $ipv4  && echo "The ip is access" ||echo "Cant't access the ip address" 
        # 执行ping命令，-c参数是发送的包数 如果ping命令成功则执行&&后的echo命令 否则执行||后的echo命令
        # 如果觉得ping命令的结果显示太多也可以直接将结果重定向到 垃圾桶 （/dev/null）中
        # ping -c 4 $ipv4 &> /dev/null && echo "The ip is access" ||echo "Cant't access the ip address"
    else
        echo "This an unlegal IP"
        echo "请输入正确的地址"
        exit
    fi