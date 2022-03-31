#!/bin/bash
#
#********************************************************************
#Author:        Sunzy
#FileName:      systeminfo.sh
#********************************************************************
# 为了让显示内容更加的清楚，加了颜色突出重点
BEGINCOLOR="\e[1;35m"
ENDCOLOR="\e[0m"
 
echo -e "My hostname is ${BEGINCOLOR}`hostname`$ENDCOLOR"
echo -e "IP address is ${BEGINCOLOR}`ifconfig ens33 |grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}'|head -n1`$ENDCOLOR"

echo -e "OS version is ${BEGINCOLOR}`cat /etc/os-release`$ENDCOLOR"
echo -e "Kernel version is ${BEGINCOLOR}`uname -r`$ENDCOLOR"
echo -e "CPU type is ${BEGINCOLOR}`cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c`$ENDCOLOR"
echo -e "Memtotol is ${BEGINCOLOR}`cat /proc/meminfo |head -n1 |grep -Eo '[0-9]+.*'`$ENDCOLOR"
echo -e "Disk space is ${BEGINCOLOR}`lsblk |grep 'sda\>'|grep -Eo '[0-9]+[[:upper:]]'`$ENDCOLOR"