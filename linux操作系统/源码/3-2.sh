#!/bin/bash
#
#********************************************************************
#Author:        Sunzy
#FileName:      DDos.sh
#********************************************************************

Info_File=/tmp/ddos_check.log #检查信息的保存文件
Log_file=/root/dos.log		  #服务器日志文件
#一般的服务器日志文件路径(apache和nginx)
#/var/log/apache/access.log
#/var/log/httpd/access.log
#/var/log/apache2/access.log
#/var/logs/nginx-access.log
#从连接数获取
#netstat -lant|awk -F "[ :]+" '/180:80/{clsn[$6]++}END{for(pol in clsn)print pol,clsn[pol]}' >$Info_File
# 从日志获取 统计IP重复数量
awk '{hotel[$1]++}END{for(pol in hotel)print pol,hotel[pol]}' $Log_file|sort -nk2 -r|column -t >$Info_File

# 按行对取文件中的IP和重复次数
while read line
do  
	Ip_Add=`echo $line |awk '{print $1}'` 
	Num=`echo $line |awk '{print $2}'`
	if [[ $Num -ge 100 ]] # 如果次数大于100 打印IP地址并加入防火墙
	then 
		echo "$Ip_Add :危险IP,将被加入防火墙"
		iptables -I INPUT -s $Ip_Add -j DROP
	fi
done <$Info_File