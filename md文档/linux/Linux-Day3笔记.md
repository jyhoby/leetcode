# Day03

### 一、回顾

> 

### 二、常用命令

#### 1.文件管理

> ##### 1>打包和压缩
>
> 见 《4.Linux命令.pdf》
>

#### 2.vi和vim编辑器

> **vi命令**是UNIX操作系统最通用的全屏幕纯文本编辑器。Linux中的vi编辑器叫vim，它是vi的增强版（vi Improved），与vi编辑器完全兼容，而且实现了很多增强功能
>
> vim编辑器工作模式有三种：命令模式，输入模式【编辑模式】，末行模式
>
> 输入模式：可以完成文本文档的编辑操作
>
> 命令模式：可以完成对文本的操作命令
>
> 掌握：掌握三种工作模式之间的任意切换
>
> ```Python
> 进入vim的命令 
>     vim filename :打开或新建文件，并将光标置于第一行首    ******
>     vim +n filename ：打开文件，并将光标置于第n行首 
>     vim + filename ：打开文件，并将光标置于最后一行首
>       
> 演示命令：
> ijeff@Rock:~/Desktop$ vim a1.txt
> ijeff@Rock:~/Desktop$ vim +3 a1.txt
> ijeff@Rock:~/Desktop$ vim + a1.txt
>
> 插入文本类命令 #在命令模式下使用
>   	i：在光标前       ******
>   	I：在当前行首 
>   	a：光标后        ******
>   	A：在当前行尾 
>   	o：在当前行之下新开一行        ******
>   	O：在当前行之上新开一行 
>   	r：替换当前字符 
>   	R：替换当前字符及其后的字符，直至按ESC键 
>   
> 移动光标 #在命令模式下使用
>   	j或下箭头 向下移动一行
>   	k或上箭头 向上移动一行
>   	h或左箭头 左移一个字符
>   	l或右箭头 右移一个字符
>   	w 　　　　右移一个词
>   	W 　　　　右移一个以空格分隔的词 
>   	b 　　　　左移一个词
>   	B 　　　　左移一个以空格分隔的词
>   	0 　　　　移到行首
>   	Ctrl+F　　向前翻页
>   	Ctrl+B　　向后翻页
>   	nG　　　　到第n行  ——> 先按下数字，再按下G
>   	G 　　　　到最后一行   
>   	gg	     第一行   ——> 先按下g，再按下g
>   	n+       光标下移n行 
>   	n-       光标上移n行
>     
> esc:退出输入模式      ******
>
> :set number：在命令模式下，用于在最左端显示行号；
> :set nonumber：在命令模式下，用于在最左端不显示行号；
>
> 保存退出 
>   	:wq		执行存盘退出操作； # 对内容做修改之后使用，保存退出   *****
>     :wq!	# 修改之后并且强制保存退出
> 	:w		执行存盘操作；
> 	:w！	   执行强制存盘操作；
> 	:q		执行退出vi操作；
> 	:q！	   执行强制退出vi操作； # 如果没有任何修改的时候使用  ******
> 	:n!		如果同时打开多个文件，则保存上个文件继续编辑下一个文件；
> 	:f		用于显示当前的文件名、光标所在行的行号以及显示比例；
> 	
> 删除操作【注意：和上面的插入文本类没有关系，进入vim后直接使用】  # 在命令模式下使用
>   	x		删除光标处的单个字符 
>   	dd		删除光标所在行 
>   	dw		删除当前字符到单词尾（包括空格）的所有字符 
>   	de		删除当前字符到单词尾（不包括单词尾部的空格）的所有字符 
>   	d$		删除当前字符到行尾的所有字符 
>   	d^		删除当前字符到行首的所有字符 （不包括当前字符）
>   	J		删除光标所在行行尾的换行符，相当于合并当前行和下一行的内容
>   	
> 替换操作
>   	:s/old/new 		将当前行中查找到的第一个字符“old” 串替换为“new”
>   	:#,#s/old/new 	在行号“#,#”范围内第一个匹配的替换所有的字符串“old”为“new”
>   	:%s/old/new	    在整个文件范围内所有行第一个匹配的替换所有的字符串“old”为“new”
>   	:s/old/new/c 	在替换命令末尾加入c命令，将对每个替换动作提示用户进行确认
>   	:%s/old/new/g 	全部替换
>   	
> 撤消操作 
> 	u 取消最近一次的操作，并恢复操作结果   *****
> 	#可以多次使用u命令恢复已进行的多步操作  
> 	Ctrl + r 对使用u命令撤销的操作进行恢复 
> ```

#### 3.用户管理

> 用户管理包括用户和组账号的管理
>
> 在Linux系统中，每个系统都必须有一个账号，并且对于不同的系统资源的使用权限
>
> root：超级管理员，通常用于系统的管理和维护，对Linux系统具有不受任何限制的操作权限

> ```
> linux使用文件保存用户信息 
> /etc/passwd 用户账户信息。
> /etc/shadow 安全用户账户信息。
> /etc/group 组账户信息。
> /etc/gshadow 安全组账户信息。
> /etc/default/useradd 账户创建的默认值。
> /etc/skel/ 包含默认文件的目录。
> /etc/login.defs Shadow 密码套件配置。
> ```

> ##### 1>whoami     查看当前系统当前用户的用户名
>
> ```Python
> 演示命令：
> ijeff@Rock:/$ su root
> 密码： 
> root@Rock:/# whoami
> root
> ```

> ##### 2>who     查看当前所有登录系统的用户信息
>
> ```Python
> -q:只显示用户的登录账号的和登录用户的数量
> -u:显示列标题
>
> 演示命令：
> root@Rock:/# su ijeff
> ijeff@Rock:/$ who
> ijeff tty7         2018-06-28 08:54 (:0)
> ijeff@Rock:/$ who -q
> ijeff
> # 用户数=1
> ijeff@Rock:/$ who -u
> ijeff tty7         2018-06-28 08:54 02:42        8992 (:0)
> ```

> ##### 3>exit	退出
>
> 如果切换后的用户，则返回上一个登录的账号
>
> ```Python
> 演示命令：
> ijeff@Rock:/$ su root
> 密码： 
> root@Rock:/# exit
> exit
> ijeff@Rock:/$ su root
> 密码： 
> root@Rock:/# su ijeff
> ijeff@Rock:/$ su
> 密码： 
> root@Rock:/# exit
> exit
> ijeff@Rock:/$ su - 
> 密码： 
> root@Rock:~# exit
> 注销
> ```

> ##### 4>su	切换用户
>
> 注意：如果不知名用户名，则默认切换到root用户
>
> 用法：
>
> ​	su  用户名
>
> ​	su  -   用户名
>
> ```Python
> 演示命令：
> ijeff@Rock:/$ su - root
> 密码： 
> root@Rock:~# su - ijeff
> ijeff@Rock:~$ pwd
> /home/ijeff
> ijeff@Rock:~$ 
> ```

> ##### 5>useradd       添加用户
>
> 注意：添加普通用户，只能通过root添加
>
> ```Python
> -g 主要组。设置用户所属的主要组  www.cit.cn           *******
> -m 强制建立用户主文件夹，并将/etc/skel/当中的文件复制到用户的根目录下      ****  
> -p 密码。输入该帐号的密码         
> -s shell。用户登录所使用的shell         
>
> 演示命令：
> # 添加用户
> ijeff@Rock:~$ sudo useradd -m -s /bin/bash lisi
> ijeff@Rock:~$ ls /home/
> lisi  ijeff  
> ijeff@Rock:~$ sudo useradd -m xiaoli
> ijeff@Rock:~$ ls /home/
> lisi  xiaoli  ijeff  
> ```
>

> ##### 6>userdel        删除用户
>
> ```Python
> userdel -rf zhangsan   ：删除普通用户，同时自动删除用户所在的主目录
> userdel zhangsan：只是删除普通用户，不会自动删除用户所在的主目录，需要手动 rm -rf zhangsan
>
> 演示命令：
> ijeff@Rock:~$ sudo userdel -r lisi
> [sudo] ijeff 的密码： 
> userdel: lisi 邮件池 (/var/mail/lisi) 未找到
> ijeff@Rock:~$ ls /home/
> ijeff
> ```

> ##### 7>passwd    设置密码
>
> 注意：一般配合useradd命令使用，当添加一个新的普通用户时，一般会紧接着设置该用户的密码
>
> ```Python
> 演示命令：
> ijeff@Rock:~$ sudo useradd -m -s /bin/bash wangwu   #添加用户
> ijeff@Rock:~$ sudo passwd wangwu
> 输入新的 UNIX 密码： 			#需要设置的密码
> 重新输入新的 UNIX 密码： 
> passwd：已成功更新密码
> ijeff@Rock:~$ su wangwu
> 密码：        #新用户的密码
> wangwu@Rock:~$ 
> ```

> ##### 8>查看用户组
>
> 用户组的作用：将多个用户管理在同一个组下，方便管理，可以让不同的用户享用同种权限
>
> ```Python
> 演示命令：
> ijeff@Rock:~$cat /etc/group
> ```

> ##### 9>groupadd    添加组
>
> ```Python
> 演示命令：
> ijeff@Rock:~$ sudo groupadd python2019
> ijeff@Rock:~$ sudo useradd -m python -g python2019
> ijeff@Rock:~$ sudo passwd python
> 输入新的 UNIX 密码： 
> 重新输入新的 UNIX 密码： 
> passwd：已成功更新密码
> ijeff@Rock:~$ su python
> 密码： 
> python@Rock:~$ ll
> 总用量 32
> drwxr-xr-x 2 python python2019 4096 6月  28 15:23 ./
> drwxr-xr-x 5 root   root       4096 6月  28 15:23 ../
> -rw-r--r-- 1 python python2019  220 9月   1  2015 .bash_logout
> -rw-r--r-- 1 python python2019 3771 9月   1  2015 .bashrc
> -rw-r--r-- 1 python python2019 8980 4月  20  2016 examples.desktop
> -rw-r--r-- 1 python python2019  655 6月  24  2016 .profile
> ```

> ##### 10>usermod    	修改modify用户的基本信息
>
> ```Python
> -g<群组> 　修改用户所属的群组。 
> -l<帐号名称> 　修改用户帐号名称。 
>
> 演示命令：
> angRock@Rock:~$ ls -l /home/
> 总用量 16
> drwxr-xr-x  2 abc      abc        4096 6月  28 14:59 abc
> drwxr-xr-x  2 jack     jack       4096 6月  28 15:30 jack
> drwxr-xr-x  2 python   python2019 4096 6月  28 15:23 python
> drwxr-xr-x 31 ijeff ijeff   4096 6月  28 14:36 ijeff
> ijeff@Rock:~$ sudo groupadd tom     # 创建用户组
> ijeff@Rock:~$ sudo usermod -g tom jack   # jack为用户名
> ijeff@Rock:~$ ls -l /home/
> 总用量 16
> drwxr-xr-x  2 abc      abc        4096 6月  28 14:59 abc
> drwxr-xr-x  2 jack     tom        4096 6月  28 15:30 jack
> drwxr-xr-x  2 python   python2019 4096 6月  28 15:23 python
> drwxr-xr-x 31 ijeff ijeff   4096 6月  28 14:36 ijeff
> ijeff@Rock:~$ sudo usermod -l newuser jack #修改用户名
> ijeff@Rock:~$ ls -l /home/
> 总用量 16
> drwxr-xr-x  2 abc      abc        4096 6月  28 14:59 abc
> drwxr-xr-x  2 newuser  tom        4096 6月  28 15:30 jack
> drwxr-xr-x  2 python   python2019 4096 6月  28 15:23 python
> ```
>

> ##### 11>groupdel 	删除组
>
> ```Python
> 演示命令：
> ijeff@Rock:~$ sudo groupdel abc
> groupdel：不能移除用户“abc”的主组
> ijeff@Rock:~$ sudo groupdel python2019
> groupdel：不能移除用户“python”的主组
> ijeff@Rock:~$ sudo groupadd user11   
> ijeff@Rock:~$ sudo groupdel user11  # 删除没有用户的组
> ijeff@Rock:~$ sudo userdel -r abc  # 删除对于有用户组
> userdel: user abc is currently used by process 13160 
> ijeff@Rock:~$ 注销   # 如果用户在使用中则使用ctrl+d注销
> ijeff@Rock:~$ sudo userdel -r abc   # 注销之后再删除
> userdel: user abc is currently used by process 13160
> ijeff@Rock:~$ 注销
> abc@Rock:~$ 注销
> ijeff@Rock:~$ sudo userdel -r abc
> userdel: abc 邮件池 (/var/mail/abc) 未找到  
> ```

> ##### 12>sudo      让当前用户暂时以管理员的身份root来执行命令

> ##### 13>chmod     修改文件权限
>
> ```Python
> drwxr-xr-x 31 ijeff ijeff   4096 6月  28 14:36 ijeff
>
> #权限的意义
> rwx           			r-x  			 			r-x
> 当前用户的权限			  同组内其他用户的权限		   其他组内用户的权限
> r w x -
> 4 2 1 0
>
> 0  000  ---  => 不可读，不可写，不可执行 
> 1  001  --x  => 不可读，不可写，可执行
> 2  010  -w-  => 不可读，可写，不执行
> 3  011  -wx  => 不可读，可写，可执行
> 4  100  r--  => 可读，不可写，不可执行
> 5  101  r-x  => 可读，不可写，可执行
> 6  110  rw-  => 可读，可写，不可执行
> 7  111  rwx  => 可读，可写，可执行
>
> 演示命令：
> #字母法修改文件权限
> ijeff@Rock:~/Desktop$ ll
> 总用量 12
> drwxr-xr-x  2 ijeff ijeff 4096 6月  28 15:47 ./
> drwxr-xr-x 31 ijeff ijeff 4096 6月  28 15:47 ../
> -rw-r--r--  1 ijeff rock       20 6月  28 15:47 a.txt
> ijeff@Rock:~/Desktop$ chmod u+x a.txt
> ijeff@Rock:~/Desktop$ ll
> 总用量 12
> drwxr-xr-x  2 ijeff ijeff 4096 6月  28 15:47 ./
> drwxr-xr-x 31 ijeff ijeff 4096 6月  28 15:47 ../
> -rwxr--r--  1 ijeff rock       20 6月  28 15:47 a.txt*
>   
> #数字法修改文件权限
> ijeff@Rock:~/Desktop$ touch b.txt
> ijeff@Rock:~/Desktop$ ll
> 总用量 12
> drwxr-xr-x  2 ijeff ijeff 4096 6月  28 15:52 ./
> drwxr-xr-x 31 ijeff ijeff 4096 6月  28 15:47 ../
> -rwxr--r--  1 ijeff rock       20 6月  28 15:47 a.txt*
> -rw-r--r--  1 ijeff rock        0 6月  28 15:52 b.txt
> ijeff@Rock:~/Desktop$ chmod 0764 b.txt
> ijeff@Rock:~/Desktop$ ll
> 总用量 12
> drwxr-xr-x  2 ijeff ijeff 4096 6月  28 15:52 ./
> drwxr-xr-x 31 ijeff ijeff 4096 6月  28 15:47 ../
> -rwxr--r--  1 ijeff rock       20 6月  28 15:47 a.txt*
> -rwxrw-r--  1 ijeff rock        0 6月  28 15:52 b.txt*
> ```

> ##### 14>chown       修改文件所有者
>
> 格式：chown   新的用户  文件名

> ##### 15>chgrp      修改文件所属组
>
> 格式：chgrp   新的组  文件名

#### 4.系统管理

> ##### 1>cal		显示一个日历
>
> ```
> 演示命令：
> ijeff@Rock:~/Desktop$ cal 
>       六月 2018         
> 日 一 二 三 四 五 六  
>                 1  2  
>  3  4  5  6  7  8  9  
> 10 11 12 13 14 15 16  
> 17 18 19 20 21 22 23  
> 24 25 26 27 28 29 30  
> ```

> ##### 2>ps	报告当前系统的进程状态
>
> ```
> 演示命令：
> ijeff@Rock:~/Desktop$ ps -u
> USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
> ijeff  13087  0.0  0.3  25248  6124 pts/4    Ss   14:56   0:00 bash
> ijeff  14078  0.0  0.1  39104  3284 pts/4    R+   16:42   0:00 ps -u
> ```
>

> ##### 3>kill	删除执行中的程序或工作
>
> ```python
> -l <信息编号>：若不加<信息编号>选项，则-l参数会列出全部的信息名称；
>
> 演示命令：
> ijeff@Rock:~/Desktop$ kill -l
>  1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
>  6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
> 11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
> 16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
> 21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
> 26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
> 31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
> 38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
> 43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
> 48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
> 53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
> 58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
> 63) SIGRTMAX-1	64) SIGRTMAX	
> ijeff@Rock:~/Desktop$ kill -9 12312  # 删除进程
>
> ```

> ##### 4>df      显示磁盘分区上的可使用的磁盘空间
>
> ​	注意：默认的单位为kb
>
> ```
> 演示命令：
> ijeff@Rock:~/Desktop$ df 
> df: /mnt/hgfs: 协议错误
> 文件系统          1K-块    已用    可用 已用% 挂载点
> udev             982640       0  982640    0% /dev
> tmpfs            201812    8928  192884    5% /run
> /dev/sda1      16381864 8263340 7263332   54% /
> tmpfs           1009040     280 1008760    1% /dev/shm
> tmpfs              5120       4    5116    1% /run/lock
> tmpfs           1009040       0 1009040    0% /sys/fs/cgroup
> tmpfs            201812      68  201744    1% /run/user/1000
> ijeff@Rock:~/Desktop$ df -h
> df: /mnt/hgfs: 协议错误
> 文件系统        容量  已用  可用 已用% 挂载点
> udev            960M     0  960M    0% /dev
> tmpfs           198M  8.8M  189M    5% /run
> /dev/sda1        16G  7.9G  7.0G   54% /
> tmpfs           986M  280K  986M    1% /dev/shm
> tmpfs           5.0M  4.0K  5.0M    1% /run/lock
> tmpfs           986M     0  986M    0% /sys/fs/cgroup
> tmpfs           198M   68K  198M    1% /run/user/1000
> ```

> ##### 5>du  	显示文件的内存大小
>
> 注意：与df命令不同的是du命令是对文件和目录磁盘使用的空间的查看

> ##### 6>free	显示当前系统未使用的和已使用的内存数目，还可以显示被内核使用的内存缓冲区
>
> ```
> 演示命令：
> free -m
>               total        used        free      shared  buff/cache   available
> Mem:           1970        1103         144          15         722         638
> Swap:          4093           5        4088
>
>
> 延时命令：
> total        used        free      shared  buff/cache   available
> Mem:           1970        1103         144          15         722         638
> Swap:          4093           5        4088
>
> 全部		  已使用的      剩余的  共享的    缓存
> total = used + free
>
> ```

> ##### 7>其他
>
> ```
> reboot:重启
> shutdown -h now   :立即关机
> shutdown -r now   :立即重启
> shutdown -h +1    ：1分钟之后重启
> clear   :清屏，作用类似于ctrl+l
>
> init 0: 关机
> init 6: 重启
> ```

> ##### 8>ping   检测网络的连通性
>
> ##### 9>ifconfig  查看网卡信息，ip地址等，相当于windows上的ipconfig
>
> ```
> 演示命令：
> ijeff@Rock:~/Desktop$ ifconfig
> ens33     Link encap:以太网  硬件地址 00:0c:29:8c:1e:35  
>           inet 地址:10.36.131.192  广播:10.36.131.255  掩码:255.255.255.0
>           inet6 地址: fe80::2025:7389:1aad:8cc8/64 Scope:Link
>           UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
>           接收数据包:73625 错误:0 丢弃:0 过载:0 帧数:0
>           发送数据包:29011 错误:0 丢弃:0 过载:0 载波:0
>           碰撞:0 发送队列长度:1000 
>           接收字节:9001772 (9.0 MB)  发送字节:2018148 (2.0 MB)
>
> lo        Link encap:本地环回  
>           inet 地址:127.0.0.1  掩码:255.0.0.0
>           inet6 地址: ::1/128 Scope:Host
>           UP LOOPBACK RUNNING  MTU:65536  跃点数:1
>           接收数据包:42021 错误:0 丢弃:0 过载:0 帧数:0
>           发送数据包:42021 错误:0 丢弃:0 过载:0 载波:0
>           碰撞:0 发送队列长度:1000 
>           接收字节:3381269 (3.3 MB)  发送字节:3381269 (3.3 MB)
> ```
>
####  5.安装软件

> ##### 1.apt
>
> 软件管理 apt ( Advanced Packaging Tool ) , 他可以自动下载、配置、安装软件包
>
>  ```python
>  sudo apt-get install package 安装包  *****
>  sudo apt-get install package –reinstall 重新安装包
>  sudo apt-get -f install 强制安装
>  sudo apt-get remove package 删除包
>  sudo apt-get remove package –purge 删除包，包括删除配置文件等
>  sudo apt-get autoremove package 自动删除不需要的包   *****
>  sudo apt-get update 更新源  *****
>  sudo apt-get upgrade 更新已安装的包   
>  sudo apt-get dist-upgrade 升级系统
>  sudo apt-get dselect-upgrade 使用 dselect 升级
>  
>  apt-cache search package 搜索包
>  apt-cache show package 获取包的相关信息，如说明、大小、版本等
>  apt-cache depends package 了解使用依赖
>  apt-cache rdepends package 了解某个具体的依赖
>  sudo apt-get build-dep package 安装相关的编译环境
>  apt-get source package 下载该包的源代码
>  sudo apt-get clean && sudo apt-get autoclean 清理下载文件的存档
>  sudo apt-get check 检查是否有损坏的依赖
>  ```
>
>  apt的配置文件
>
>  ```python
>  /etc/apt/sources.list 设置软件包的获取来源
>  /etc/apt/apt.conf apt配置文件
>  /etc/apt/apt.conf.d apt的零碎配置文件
>  /etc/apt/preferences 版本参数
>  /var/cache/apt/archives/partial 存放正在下载的软件包
>  /var/cache/apt/archives 存放已经下载的软件包
>  /var/lib/apt/lists 存放已经下载的软件包详细信息
>  /var/lib/apt/lists/partial 存放正在下载的软件包详细信息
>  ```
>
> ##### 2.dpkg
>
>  dpkg是Debian软件包管理器的基础，被用于安装、卸载和供给和.deb软件包相关的信息,dpkg本身是一个底层的工具，本身并不能从远程包仓库下载包以及处理包的依赖的关系，需要将包从远程下载后再安装
>
>  ```python
>  dpkg -i package.deb 安装包  *****
>  dpkg -r package 删除包  
>  dpkg -P package 删除包（包括配置文件）*****
>  dpkg -L package 列出与该包关联的文件
>  dpkg -l package 显示该包的版本
>  dpkg –unpack package.deb 解开 deb 包的内容
>  dpkg -S keyword 搜索所属的包内容
>  dpkg -l 列出当前已安装的包
>  dpkg -c package.deb 列出 deb 包的内容
>  dpkg –configure package 配置包
>  ```

#### 

#####  