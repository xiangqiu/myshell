#!/bin/bash
echo ' 一键安装shadowsocks!';
echo ' 1)安装';
echo ' 2)启动';
echo ' 3)重启';
echo ' 4)停用';
read numid
case ${numid} in
	1 )
		yum install python-setuptools && easy_install pip;
		pip install shadowsocks;
		touch /etc/ss.json;
		echo '输入当前服务器外网IP';
		read ip
		echo '输入密码';
		read password
		echo '{"server":"'${ip}'","local_port":1080,"port_password":{"8388":"'${password}'"},"timeout":600,"method":"aes-128-cfb"}' > /etc/ss.json
		echo '安装完成!配置文件信息如下:';
		cat /etc/ss.json
		;;
	2)
		/usr/bin/python2.6 /usr/bin/ssserver -c /etc/ss.json -d start
		;;
	3)
		/usr/bin/python2.6 /usr/bin/ssserver -c /etc/ss.json -d restart
		;;
	4)
		/usr/bin/python2.6 /usr/bin/ssserver -c /etc/ss.json -d stop
		;;
esac

