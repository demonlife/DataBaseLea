# 使用lnmp安装 mysql #
* mysql 配置文件

> mysql的错误日志文件默认是在/usr/local/mysql/var/domain.err

* mysql 添加用户

> grant all privileges on *.* to 'username'@'*' identified by 'password'

> grant all privileges on *.* to 'username'@'localhost' identified by 'passwd'

> grant all privileges on 'dbname.tablename' to 'uname'@'*' identified by 'pwd'

# mysql 编码 #
* [原文地址](http://www.imcjd.com/?p=1310)

* 现在的字符编码主要有两大体系, ANSI和UNICODE

* ANSI是由一个母体（ASCII）出发，产生了多个不兼容平行分支（LATIN1、GBK、JIS）。
而UNICODE体系则将所有的字符统一于一种编码规范之下


