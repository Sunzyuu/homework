#!/bin/bash
#
#********************************************************************
#Author:        Sunzy
#FileName:      usermanager.sh
#********************************************************************

# 定义一个显示菜单，根据用户输入的数字进行不同的操作
menu()
{
	echo "Please choose the number for the function you need!"
	echo "Input 1 : Add a user!"
	echo "Input 2 : Delete a user!"
	echo "Input 3 : Find a user and show information!"
	echo "Input 4 : Quit!"
	echo ""
}

func()
{
	# 读取用户的选项 num
	read -p "Please input your choice: " num
	case $num in
		"1")                                     #Add user
			read -p "Please input the username you want to add：" username1
			sudo useradd $username1   # 如果是root用户登录可以不加sudo调用useradd添加用户
			sudo mkdir /home/$username1 # 创建用户的家目录
			echo "Add success!"
			;;
		"2")                                     #Delete user
			read -p "Please input the username you want to delete：" username2
			grep "$username2" /etc/passwd >/dev/null    # 将匹配到的内容重定向到垃圾桶，即删除信息
			if [ $? -eq 0 ]; then
				userdel $username2  	# 调用userdel删除用户
				rm -r /home/$username2  # 调用rm 删除用户的家目录
				echo "Delete success!"
			else		
				echo "The user does not exist!"
			fi
			;;
		"3")                                     #Find user
			read -p "Please input the username you want to find：" username3
			grep -n "$username3" /etc/passwd         # 将匹配到的信息打印显示
					if [ $? -eq 1 ]; then        	 # 没有匹配到?为1,即不存在
							echo "The user does not exist!"
					fi
			;;
		"4")									# Quit
			echo "Qiut!"
			exit 0
			;;
		*)    # 使用通配符 * 处理其它情况的输入
			echo "Please input 1,2,3 or 4!"
			;;
	esac
}
# 设置一个循环，实现重复调用mem和func
for i in $( seq 1 100)
do
menu
func
done