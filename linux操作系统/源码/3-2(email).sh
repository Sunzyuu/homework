#!/bin/bash
#script name : sendemail.sh
account='2632338423@qq.com' #发件箱
password='gk***********d' #发件箱授权码不是密码
SMTP_server='smtp.qq.com' #发件箱对应的stmp服务器
to='08183039@cumt.edu.cn' #第一个参数(收件箱)
subject='你的网站正在被攻击' #第二个参数(主题)
content='危险IP如下' #第三个参数(内容)
appendix='/tmp/ddos_check.log'
sendemail -f $account -t $to -s $SMTP_server -u $subject -o message-content-type=html -o message-charset=utf-8 -xu $account -xp $password -m $content -a $appendix -o tls=no