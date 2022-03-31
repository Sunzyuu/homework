#!/bin/bash
#
#********************************************************************
#Author:        Sunzy
#FileName:      Service.sh
#********************************************************************
password=123456

#密钥分发函数
Distribute(){
which sshpass &>/dev/null     #首先用which命令判断本地sshpass是否安装
if [ $? -ne 0 ]               # 安装了则$?返回值为 0
then                          #$?不为0时，则没有安装
echo "******************* install sshpass...*******************"
apt install sshpass 
echo "******************* install finished  *******************"
echo "******************* 传输密钥 *******************"

#使用sshpass工具和-o参数实现避免交互输入yes和密码
#使用scp远测传输命令，传输密钥文件
#将本地密钥文件/root/.ssh/id_rsa.pub，传输到对应服务器上/tmp/目录下，此时不能直接传到/root/.ssh目录下，避免其他机器同样操作覆盖文件。
sshpass -p $password scp -p -o StrictHostKeyChecking=no /root/.ssh/id_rsa.pub 192.168.42.$i:/tmp/       
sshpass -p $password ssh -o StrictHostKeyChecking=no 192.168.42.$i "cat /tmp/id_rsa.pub >> /root/.ssh/authorized_keys"           
#ssh连接服务器，将/tmp/下密码文件写如入/root/.ssh/authorized_keys
sshpass -p $password ssh -o StrictHostKeyChecking=no 192.168.42.$i "chmod 600 /root/.ssh/authorized_keys"           #修改文件权限，保证只有root用户可以查看修改内容
sshpass -p $password ssh -o StrictHostKeyChecking=no 192.168.42.$i "rm -rf /tmp/id_rsa.pub"             echo "******************* 密钥传输成功 *******************"

else                                  #如果sshpass工具安装，则直接执行。
echo "******************* 传输密钥 *******************"
#sshpass -p $password ssh-copy-id 192.168.42.$i
sshpass -p $password scp -p -o StrictHostKeyChecking=no /root/.ssh/id_rsa.pub 192.168.42.$i:/tmp/
sshpass -p $password ssh -o StrictHostKeyChecking=no 192.168.42.$i "cat /tmp/id_rsa.pub >> /root/.ssh/authorized_keys" 
sshpass -p $password ssh -o StrictHostKeyChecking=no 192.168.42.$i "chmod 600 /root/.ssh/authorized_keys"
sshpass -p $password ssh -o StrictHostKeyChecking=no 192.168.42.$i "rm -rf /tmp/id_rsa.pub"
echo "******************* 密钥传输成功 *******************"
fi
}
#main函数中主要三个功能
# 1.密钥的生成
# 2.检查主机间的通信
# 3.密钥分发 使用sshpass的-o参数避免交互

MAIN(){                
for i in {101..201}
do
#检查是否可以通信
ping -c 1 192.168.42.$i &>/dev/null
if [ $? -eq 0 ]                    	 	#当上ping命令返回值为0是说明可以通信，接着生成密钥然后分发密钥
then									# 检查密钥是否创建
    if [ -f /root/.ssh/id_rsa.pub ]  
    then
       Distribute                        	#执行TRACE函数，分发秘钥
    else
       ssh-keygen -f /root/.ssh/id_rsa -P ""  # ssh-keygen创建秘钥并写入对应的文件中
       Distribute                        	#分发秘钥
    fi
else                  					#不通时
echo " 192.168.42.$i is unreachable..."
fi
done 
}

MAIN