# Day02

### 一、目录结构

#### 1.Windows文件系统

> 看到的是一个个驱动器盘符，例如：C盘，D盘等
>
> 每个驱动器都有自己的根目录结构，形成了树结构

#### 2.Linux文件系统

> ubuntu没有盘符这个概念，只有一个根目录 ：/,   所有目录和文件都存放在/的下面
>
> 注意：在Linux系统下所有的内容都被视为文件，目录也被视为文件
>
> ```
> ls -l       #查看当前路径下文件的详细信息
> ls -l  /    #查看根目录下的详细信息
> ```
>
> ```Python
> Linux目录结构： 
>
> / ： 根目录  # Linux下的根目录，根目录只有一个
> /boot : boot配置文件、内核和其它启动时所需的文件
> /etc ：存放系统配置有关的文件   # 用户信息都放在这【用户名修改，密码修改等】
> /home ：存放普通用户目录  # 家目录，普通用户目录 ，普通用户存放在这里，
> /mnt ：硬盘上手动挂载的文件系统	# 默认是空的
> /media ：自动挂载（加载）的硬盘分区以及类似CD、数码相机等可移动介质。	
> /cdrom ：挂载光盘 
> /opt ： 存放一些可选程序,如某个程序测试版本,安装到该目录的程序的所有数据,库文件都存在同个目录下
> /root ：系统管理员的目录，对于系统来说，系统管理员好比上帝
> 		# 超级管理员用户，可以对系统做任何操作，比如删除文件，安装文件等.
>     	# 普通用户也可以使用root用户的权限：使用sudo
> /bin ：存放常用的程序文件， # binary 二进制程序或命令文件
> /sbin ：系统管理命令，这里存放的是系统管理员使用的管理程序 
> /tmp ：临时目录，存放临时文件   # temp 暂存，临时存储
> 	# 是存放一些命令或程序执行过程中产生的一些临时数据或文件，系统会定期清理 
> /usr ：在这个目录下，你可以找到那些不适合放在/bin或/etc目录下的额外的工具。比如游戏、打印工具等。/usr目录包含了许多子目录： 
> 	/usr/bin目录用于存放程序;
> 	/usr/share用于存放一些共享的数据，比如音乐文件或者图标等等;
> 	/usr/lib目录用于存放那些不能直接 运行的，但却是许多程序运行所必需的一些函数库文件。
> 	/usr/local ： 这个目录一般是用来存放用户自编译安装软件的存放目录；
>     			一般是通过源码包安装的软件，如果没有特别指定安装目录的话，一般是安装在这个目录中。
> 	/usr/bin/ 非必要可执行文件 (在单用户模式中不需要)；面向所有用户。
> 	/usr/include/ 标准包含文件。
> 	/usr/lib/ /usr/bin/和/usr/sbin/中二进制文件的库。
> 	/usr/sbin/ 非必要的系统二进制文件，例如：大量网络服务的守护进程。
> 	/usr/share/ 体系结构无关（共享）数据。
> 	/usr/src/ 源代码,例如:内核源代码及其头文件。
> 	/usr/X11R6/ X Window系统 版本 11, Release 6.
> 	/usr/local/ 本地数据的第三层次，具体到本台主机。通常而言有进一步的子目录， 
>     			例如：bin/、lib/、share/.
>
> /var ：该目录存放那些经常被修改的文件，包括各种日志、数据文件；
>     /var/cache/ 应用程序缓存数据。这些数据是在本地生成的一个耗时的I/O或计算结果。
>     			应用程序必须能够再生或恢复数据。缓存的文件可以被删除而不导致数据丢失。
>     /var/lib/ 状态信息。 由程序在运行时维护的持久性数据。 例如：数据库、包装的系统元数据等。
>     /var/lock/ 锁文件，一类跟踪当前使用中资源的文件。
>     /var/log/ 日志文件，包含大量日志文件。
>     /var/mail/ 用户的电子邮箱。
>     /var/run/ 自最后一次启动以来运行中的系统的信息，例如：当前登录的用户和运行中的守护进程。
>     		  现已经被/run代替[13]。
>     /var/spool/ 等待处理的任务的脱机文件，例如：打印队列和未读的邮件。
>     /var/spool/mail/ 用户的邮箱(不鼓励的存储位置)
>     /var/tmp/ 在系统重启过程中可以保留的临时文件。
>     
> /lib : 目录是根文件系统上的程序所需的共享库，存放了根文件系统程序运行所需的共享文件。这些文件包含了可被许多程序共享的代码，以避免每个程序都包含有相同的子程序的副本，故可以使得可执行文件变得更小，节省空间。
> /lib32 : 同上
> /lib64 ： 同上
> /lost+found ： 该目录在大多数情况下都是空的。但当突然停电、或者非正常关机后，有些文件就临时存放在；
> /dev : 存放设备文件 
> /run ：代替/var/run目录，
> /proc : 虚拟文件系统，可以在该目录下获取系统信息，这些信息是在内存中由系统自己产生的，该目录的内容不在硬盘上而在内存里；
> 	cat /proc/cpuinfo
> 	
> /sys ： 和proc一样，虚拟文件系统，可以在该目录下获取系统信息，这些信息是在内存中由系统自己产生的，该目录的内容不在硬盘上而在内存里；
> ```
>
> 补充：
>
> ```python
> .   代表当前目录
> ..  代表上一级目录
> 注意：根目录下.和..都代表当前目录
>
> 相对路径和绝对路径
> 相对路径：从当前位置开始描述的路径
> 绝对路径：从/目录开始描述的路径
> ```

> ```Python
> 演示命令：
> ijeff@Rock:~$ ls -l
> 总用量 40
> drwxr-xr-x 3 ijeff rock 4096 6月  26 02:23 Desktop
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Documents
> drwxr-xr-x 2 ijeff rock 4096 3月  25 22:05 Downloads
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Music
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Pictures
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Public
> drwxrwxr-x 3 ijeff rock 4096 3月  25 22:43 PycharmProjects
> drwxrwxr-x 3 ijeff rock 4096 3月  25 22:37 Software
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Templates
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Videos
> ijeff@Rock:~$ pwd  # 查看当前目录的绝对路径
> /home/ijeff
> ijeff@Rock:~$ ls -l /
> 总用量 100
> drwxr-xr-x   2 root root  4096 3月  25 22:26 bin
> drwxr-xr-x   3 root root  4096 6月  26 18:01 boot
> drwxrwxr-x   2 root root  4096 7月  18  2017 cdrom
> drwxr-xr-x  19 root root  4020 6月  26 18:01 dev
> drwxr-xr-x 137 root root 12288 6月  26 18:10 etc
> drwxr-xr-x   3 root root  4096 6月  26 17:58 home
> lrwxrwxrwx   1 root root    33 3月  25 22:28 initrd.img -> boot/initrd.img-4.13.0-37-generic
> ijeff@Rock:~$ ls /mnt/
>
> ijeff@Rock:~$ pwd
> /home/ijeff
> ijeff@Rock:~$ cd Desktop/     
> ijeff@Rock:~/Desktop$ cd .
> ijeff@Rock:~/Desktop$ cd ..
> ijeff@Rock:~$ cd /home/ijeff/Desktop/   #绝对路径
> ijeff@Rock:~/Desktop$ cd ..
> ijeff@Rock:~$ cd Desktop/      #相对路径
> ijeff@Rock:~/Desktop$
> ```

### 二、快捷键

> ```python
> ctrl + shift +  + :放大字体，放大终端窗口
> ctrl + - : 缩小字体
>
> ctrl  +  alt: 显示鼠标  # 
> ctrl + alt + t :快速打开终端
>
> tab  :命令行自动补全  # 
> 箭头上下键：翻看已经执行过的命令  #
>
> ctrl + f: 前进一个字符
> ctrl + b：后退一个字符
> ctrl + a: 回到行首
> ctrl + e: 回到行尾
>
> ctrl + w: 向左删除一个单词
> ctrl + u: 向左删除全部单词
> ctrl + k: 向右删除全部单词
>
> ctrl + y: 将ctrl + w，ctrl + u，ctrl + k删除的结果恢复
> ctrl + l: 清屏【并不是真正意义上的清屏，只是将历史记录向上翻一页】  #
> ctrl + c: 中断执行  # 
> ctrl + d: 退出终端
> ```


### 三、常用命令

#### 1.概述

> 语法：
>
> command    options    parameters
>
> ls   /home -a 
>
> command    :命令名称
>
> options    ：选项，可以对命令进行控制，根据具体需求可写可不写
>
> parameters：传给命令的参数，根据具体需求可写可不写，也可以写多个

#### 2.查看帮助文档

> ##### 1>--help
>
>  作用：Linux命令自带的帮助信息
>
> ```Python
> 演示命令：
> ijeff@Rock:~$ ls --help
> ```

> ##### 2>man
>
> 作用：相当于一个手册，包含了大多数的命令以及命令的使用方式
>
> ```Python
> man命令中常用的按键
> 空格键		向下翻页
> 上下方向键    向上或者向下翻一行
> fn + 左方向键		回到首页
> fn + 右方向键       回到尾页
>
> /xxx        从上到下进行搜索和指定关键字有关的内容
> ?xxx	    从上到下进行搜索和指定关键字有关的内容
> n	      定位到下一个搜索到的关键字
> N		  定位到上一个搜索到的关键字
> q		  退出帮助文档
>
> 演示命令：
> ijeff@Rock:~$ man ls 
> ```

> ##### 3>history   查看执行过的命令
>
> 当系统执行过一些命令之后，可以通过上下键翻看以前的命令，history将执行过的命令列举出来
>
> history   显示最近1000条记录
>
> history   5   显示最后5条命令
>
> !number    number 是history每条命令前面的编号，直接使用表示执行对应的命令
>
> ```Python
> 演示命令：
> ijeff@Rock:~$ history        #显示最近1000条记录
> ijeff@Rock:~$ history  5     #显示最后5条命令
>   958  cd ..
>   959  ls
>   960  pwd
>   961  history 
>   962  history  5
> ijeff@Rock:~$ !951            #指定编号对应的命令
> cd Desktop/
> ijeff@Rock:~/Desktop$ 
> ```

> 补充：
>
> ```Python
> #查看历史命令的记录
> #命令不会一直保存下去，最多只会显示1000条，查看信息：
> 演示命令：
> angRock@Rock:~/Desktop$ cat ~/.bashrc | grep -i hist
> # don't put duplicate lines or lines starting with space in the history.
> HISTCONTROL=ignoreboth
> # append to the history file, don't overwrite it
> shopt -s histappend
> # for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
> HISTSIZE=1000        #最多显示的条数
> HISTFILESIZE=2000		#执行过的命令都会存放在一个文件中，这个文件中最多存放2000条
> alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
> ```
>
> ```Python
> #查看命令保存的位置
> 演示命令：
> ijeff@Rock:~/Desktop$ ls -a ~/.bash*
> /home/ijeff/.bash_history         #存放历史命令的文件
> /home/ijeff/.bashrc				#存放详细信息的文件
> /home/ijeff/.bash_logout          #存放日志的文件
> ijeff@Rock:~/Desktop$ gedit /home/ijeff/.bash_history         #打开文件
> ijeff@Rock:~/Desktop$ 
> ```

#### 3.文件管理

> ##### 1>ls: 列举出当前工作目录的内容【list】
>
> ```Python
> -a 用于显示所有文件和子目录(包括隐藏文件)
> -A 同-a，但不列出“.”(表示当前目录)和“..”(表示当前目录的父目录)
> -l 除了文件名之外，还将文件的权限、所有者、文件大小等信息详细列出来。 (文件大小是字节)
> -lh 与-l 类似  只不过文件大小显示的是 KB [默认是按照文件名的 abcd 排序的]
> -lht 与-l -lh 类似  排序是按照修改时间降序排的
> -lhtr 按照时间升序排
> -r 将目录的内容清单以英文字母顺序的逆序显示
> -t 按文件修改时间进行排序
> ll : ls -a -l
>
> 补充
> drwxr-xr-x 2 ijeff rock 4096 6月   5 21:41 Desktop
> 一、文件类型
> #第一位代表的是文件类型：
> 	- 代表是文件
> 	d 代表目录
>     b 块设备文件
>     c  字符设备文件
>     l  链接文件
>     p  管道文件
>     s  socket文件
>
> 二、文件权限
> #第二位到十位是文件的权限
> 权限共九位，分三组，每三个一组
> 	rwx		
> 	r  read  可读权限，可以用数字4表示
> 	w  write   可写权限，可以用数字2表示
> 	x  execute	可执行权限，可以用数字1表示
> 	-  表示没有相应权限，可以用数字0表示
>     
>     rwx二进制表示：
>     	0表示没有该权限，1表示有该权限
>     rwx   r-x  r-x
>     rwx : 111
>     r-x : 101
>     
>     取值范围为0-7
> 	-0  代表什么权限都没有   000 => ---
> 	-1	文件只能执行		  001 => --x 
> 	-2	文件只有写权限      010 => -w-
> 	-3	文件可写可执行      011 => -wx
> 	-4	只读权限            100 => r--
> 	-5	可读可执行          101 => r-x
> 	-6	可读可写		    110 => rw-
> 	-7 可读可写可执行       111 => rwx
>     
> 三、文件和目录的权限类型	
> 对于文件而言：
> 	可读权限表示允许读其内容，禁止对其做任何的更改操作
> 	可写权限表示可以修改编辑文件的内容或者删除文件（要有文件所在目录的写权限）
> 	可执行表示允许将文件作为一个程序执行
>
> 对目录而言：
> 	可读权限表示允许显示该目录中的内容
> 	可写权限表示可以在该目录中新建，删除，重命名文件
> 	可执行权限表示可以进入该目录，可执行是基本权限，如果没有它，就进不了目录	
>         
> 四、硬链接的个数
> #第二列一位代表硬链接的个数
> 	
> 五、表示组
> #第三列表示组
> 	分三个组：
> 	代表当前用户的权限[user]
> 	代表用户所属组的权限[group]
> 	代表其他组的权限[other]
> ```

> ```Python
> 演示命令：
> ijeff@Rock:~$ ls
> Desktop    Downloads  Pictures  PycharmProjects  Templates
> Documents  Music      Public    Software         Videos
> ijeff@Rock:~$ ls /home/ijeff
> Desktop    Downloads  Pictures  PycharmProjects  Templates
> Documents  Music      Public    Software         Videos
> ijeff@Rock:~$ ls Desktop/
> vmware-tools-distrib            VNC-Server-6.1.1-Linux-x64.deb
> VNC-6.1.1-Linux-x64-DEB.tar.gz
> ijeff@Rock:~$ ls -a
> .                   Documents      .mysql_history    .sogouinput
> ..                  Downloads      .nano             .sudo_as_admin_successful
> .apport-ignore.xml  .gconf         .pam_environment  .sunpinyin
> .bash_history       .gnome         Pictures          Templates
> .bash_logout        .gnupg         .pki              Videos
> .bashrc             .ICEauthority  .presage          .viminfo
> .cache              .java          .profile          .virtualenvs
> .compiz             .lesshst       Public            .vnc
> .config             .local         .PyCharm2017.3    .Xauthority
> .dbus               .mozilla       PycharmProjects   .xinputrc
> Desktop             Music          .python_history   .xsession-errors
> .dmrc               .mysql         Software          .xsession-errors.old
> ijeff@Rock:~$ ls -A
> .apport-ignore.xml  .java             .python_history
> .bash_history       .lesshst          Software
> .bash_logout        .local            .sogouinput
> .bashrc             .mozilla          .sudo_as_admin_successful
> .cache              Music             .sunpinyin
> .compiz             .mysql            Templates
> .config             .mysql_history    Videos
> .dbus               .nano             .viminfo
> Desktop             .pam_environment  .virtualenvs
> .dmrc               Pictures          .vnc
> Documents           .pki              .Xauthority
> Downloads           .presage          .xinputrc
> .gconf              .profile          .xsession-errors
> .gnome              Public            .xsession-errors.old
> .gnupg              .PyCharm2017.3
> .ICEauthority       PycharmProjects
> ijeff@Rock:~$ ls -l
> 总用量 40
> drwxr-xr-x 3 ijeff rock 4096 6月  26 02:23 Desktop
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Documents
> drwxr-xr-x 2 ijeff rock 4096 3月  25 22:05 Downloads
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Music
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Pictures
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Public
> drwxrwxr-x 3 ijeff rock 4096 3月  25 22:43 PycharmProjects
> drwxrwxr-x 3 ijeff rock 4096 3月  25 22:37 Software
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Templates
> drwxr-xr-x 2 ijeff rock 4096 7月  18  2017 Videos
> ijeff@Rock:~$ ls -h
> Desktop    Downloads  Pictures  PycharmProjects  Templates
> Documents  Music      Public    Software         Videos
> ijeff@Rock:~$ ls -r
> Videos     Software         Public    Music      Documents
> Templates  PycharmProjects  Pictures  Downloads  Desktop
> ijeff@Rock:~$ ls -t
> Desktop          Software   Documents  Pictures  Templates
> PycharmProjects  Downloads  Music      Public    Videos
> ijeff@Rock:~$ ls -F
> Desktop/    Downloads/  Pictures/  PycharmProjects/  Templates/
> Documents/  Music/      Public/    Software/         Videos/
> ijeff@Rock:~$ ls -R
> .:
> Desktop    Downloads  Pictures  PycharmProjects  Templates
> Documents  Music      Public    Softw
> ```

> ##### 2>pwd	查看当前的工作目录[print working directory]
>
> ```Python
> 演示命令：
> ijeff@Rock:~$ pwd
> /home/ijeff
> ```

> ##### 3>查看文件
>
> ```Python
> cat：查看完整的文件内容        ********
> 	-n	:显示每一行的行号，包括空行
> 	-b	:显示每一行的行号，不包括空行
> #使用文件内容较少的情况下使用cat
> head：查看文件内容, 头10行
> 	head -3 a.txt  前3行
> tail：查看文件内容，尾10行
> 	tail -3 a.txt 尾3行
>     
> less：查看文件
> more：查看文件
> #使用文件内容较少的情况下使用more
>
> wc：一次显示文件行数，字节数以及文件名信息
> stat：查看文件详细信息，可以获取文件的文件名、大小、权限，最近访问以及最近更改的时间，stat命令的输出信息比ls命令还要详细
> file：查看文件的类型
> echo：用于在终端输出字符串或变量的值
>
> |: 管道，作用：将一个命令的输出作为另一个命令的输入，格式：命令1 | 命令2  ****
> >：输出重定向，Linux允许将执行结果重定向到一个文件，本应显示在终端上的内容保存到指定文件中     
> 		#清空源文件
>     cat a.txt > a_1.txt  复制
> >>：输出重定向，Linux允许将执行结果重定向到一个文件，本应显示在终端上的内容保存到指定文件中 
>   		#追加不清空
> 演示命令：
> ijeff@Rock:~$ cd Desktop/
> ijeff@Rock:~/Desktop$ ls
> aaa.txt               VNC-6.1.1-Linux-x64-DEB.tar.gz
> vmware-tools-distrib  VNC-Server-6.1.1-Linux-x64.deb
> ijeff@Rock:~/Desktop$ cat aaa.txt 
> hfuiewhg
> less：查看文件
> head：查看文件内容
> tail：查看文件内容
> less：查看文件
> more：查看文件
> wc：一次显示文件行数，字节数以及文件名信息
> stat：查看文件详细信息，可以获取文件的文件名、大小、权限，最近访问以及最近更改的时间，stat命令的输出信息比ls命令还要详细
> file：查看文件的类型
> echo：用于在终端输出字
> ijeff@Rock:~/Desktop$ cat -n aaa.txt 
>      1	hfuiewhg
>      2	less：查看文件
>      3	head：查看文件内容
>      4	tail：查看文件内容
>      5	less：查看文件
>      6	more：查看文件
>      7	wc：一次显示文件行数，字节数以及文件名信息
>      8	stat：查看文件详细信息，可以获取文件的文件名、大小、权限，最近访问以及最近更改的时间，stat命令的输出信息比ls命令还要详细
>      9	file：查看文件的类型
>     10	echo：用于在终端输出字
> ijeff@Rock:~/Desktop$ cat -b aaa.txt 
>      1	hfuiewhg
>      2	less：查看文件
>      3	head：查看文件内容
>      4	tail：查看文件内容
>      5	less：查看文件
>      6	more：查看文件
>      7	wc：一次显示文件行数，字节数以及文件名信息
>      8	stat：查看文件详细信息，可以获取文件的文件名、大小、权限，最近访问以及最近更改的时间，stat命令的输出信息比ls命令还要详细
>      9	file：查看文件的类型
>     10	echo：用于在终端输出字
> ijeff@Rock:~/Desktop$ head aaa.txt 
> hfuiewhg
> less：查看文件
> head：查看文件内容
> tail：查看文件内容
> less：查看文件
> more：查看文件
> wc：一次显示文件行数，字节数以及文件名信息
> stat：查看文件详细信息，可以获取文件的文件名、大小、权限，最近访问以及最近更改的时间，stat命令的输出信息比ls命令还要详细
> file：查看文件的类型
> echo：用于在终端输出字
> ijeff@Rock:~/Desktop$ head -2 aaa.txt 
> hfuiewhg
> less：查看文件
> ijeff@Rock:~/Desktop$ tail aaa.txt 
> hfuiewhg
> less：查看文件
> head：查看文件内容
> tail：查看文件内容
> less：查看文件
> more：查看文件
> wc：一次显示文件行数，字节数以及文件名信息
> stat：查看文件详细信息，可以获取文件的文件名、大小、权限，最近访问以及最近更改的时间，stat命令的输出信息比ls命令还要详细
> file：查看文件的类型
> echo：用于在终端输出字
> ijeff@Rock:~/Desktop$ tail -2 aaa.txt 
> file：查看文件的类型
> echo：用于在终端输出字
> ijeff@Rock:~/Desktop$ less aaa.txt 
> ijeff@Rock:~/Desktop$ more aaa.txt 
> hfuiewhg
> less：查看文件
> head：查看文件内容
> tail：查看文件内容
> less：查看文件
> more：查看文件
> wc：一次显示文件行数，字节数以及文件名信息
> stat：查看文件详细信息，可以获取文件的文件名、大小、权限，最近访问以及最近更改的
> 时间，stat命令的输出信息比ls命令还要详细
> file：查看文件的类型
> echo：用于在终端输出字
> ijeff@Rock:~/Desktop$ wc aaa.txt 
>  10  10 421 aaa.txt
> ijeff@Rock:~/Desktop$ stat aaa.txt 
>   文件：'aaa.txt'
>   大小：421       	块：8          IO 块：4096   普通文件
> 设备：801h/2049d	Inode：572338      硬链接：1
> 权限：(0644/-rw-r--r--)  Uid：( 1000/ijeff)   Gid：( 1000/    rock)
> 最近访问：2018-06-27 11:35:53.174601466 +0800
> 最近更改：2018-06-27 11:34:31.286596606 +0800
> 最近改动：2018-06-27 11:34:31.290596607 +0800
> 创建时间：-
> ijeff@Rock:~/Desktop$ file aaa.txt 
> aaa.txt: UTF-8 Unicode text
> ijeff@Rock:~/Desktop$ echo "today is a good day"
> today is a good day
> ijeff@Rock:~/Desktop$ ls
> aaa.txt               VNC-6.1.1-Linux-x64-DEB.tar.gz
> vmware-tools-distrib  VNC-Server-6.1.1-Linux-x64.deb
> ijeff@Rock:~/Desktop$ ls > bbb.txt 
> ijeff@Rock:~/Desktop$ cat aaa.txt 
> hfuiewhg
> less：查看文件
> head：查看文件内容
> tail：查看文件内容
> less：查看文件
> more：查看文件
> wc：一次显示文件行数，字节数以及文件名信息
> stat：查看文件详细信息，可以获取文件的文件名、大小、权限，最近访问以及最近更改的时间，stat命令的输出信息比ls命令还要详细
> file：查看文件的类型
> echo：用于在终端输出字
> ijeff@Rock:~/Desktop$ cat aaa.txt > bbb.txt 
> ijeff@Rock:~/Desktop$ 
> ```

> ##### 4>tree       以树形结构去显示目录结构
>
> ​	注意：默认情况下是当前路径下的所有文件的显示
>
> ```Python
> -d 	只显示文件夹
> -f	显示文件的完整路径
> -L 2	：只看前两级的内容
>
> 演示命令：
> ijeff@Rock:~/Desktop$  tree
> ijeff@Rock:~/Desktop$  tree -d
> ijeff@Rock:~/Desktop$  tree -f 
> ijeff@Rock:~/Desktop$  tree -L 2
> ```

> ##### 5>cd	切换工作目录【change  diretory】
>
> ```Python
> 用法：cd  路径[此处可以是相对路径，也可以是绝对路径]       ******
> 特殊用法： 
> cd	切换到当前用户的主目录，用户登录的时候，默认的目录就是用户的主目录
> cd ~	切换到当前用户的主目录
> cd .	切换到当前目录
> cd ..	切换到上一级目录			*******
> cd - 	返回上一次切换的目录
> cd #	回到当前用户的主目录
>
> 演示命令：
> ijeff@Rock:~/Desktop$ cd /home/ijeff
> ijeff@Rock:~$ cd
> ijeff@Rock:~$ cd ~
> ijeff@Rock:~$ cd Desktop/
> ijeff@Rock:~/Desktop$ cd -
> /home/ijeff
> ijeff@Rock:~$ cd Desktop/
> ```

> ##### 6>mv	移动或者重命名文件或者目录
>
> 注意：如果目标是文件，则表示重命名
>
> ​	   如果目标是目录，则表示移动
>
> ```Python
> 命令格式：mv [参数] 源文件  [目标路径|目标文件名]    ------》可以cd到【文件所在路径下】或者【直接通过路径指明文件】
> -i	在目标文件存在的时候会询问是否要覆盖
> -b	当目标文件存在的时候，不会进行询问直接覆盖
>
> 演示命令：
> ijeff@Rock:~/Desktop$ mv aaa.txt  abc.txt
> ijeff@Rock:~/Desktop$ mv bbb.txt bbb1.txt  bbb2.txt  dir1/
> ijeff@Rock:~/Desktop$ mv -i abc.txt  dir1/
> mv：是否覆盖'dir1/abc.txt'？ y
> ijeff@Rock:~/Desktop$ mv -b abc.txt  dir1/
> ```

> ##### 7>cp	复制文件或者目录
>
> ```Python
> 命令格式：cp [参数] 源文件 目标文件
>
> -i 在目标文件存在的时候会询问是否要覆盖【交互式复制】
> -r 若给出的源文件是一目录文件，此时cp将递归复制该目录下所有的子目录和文件。此时目标文件必须为一个目录名
> -a 复制的时候保持文件原有属性
> -f 对于已经存在的目标文件不提示
> -v 显示拷贝进度
>
> 演示命令：
> ijeff@Rock:~$ cd Desktop/
> ijeff@Rock:~/Desktop$ cp -i  abc.txt  dir1/
> cp：是否覆盖'dir1/abc.txt'？ n      #交互式复制
> ijeff@Rock:~/Desktop$ cp dir1 dir2/
> cp: 略过目录'dir1'
> ijeff@Rock:~/Desktop$ cp dir1 dir2
> cp: 略过目录'dir1'
> ijeff@Rock:~/Desktop$ cp -r  dir1 dir2/
> ijeff@Rock:~/Desktop$ cp -v  abc.txt dir2/
> 'abc.txt' -> 'dir2/abc.txt'
> ```

> ##### 8>创建文件或者目录
>
> ```Python
> 8.1>mkdir	创建一个新的目录   【make directory】
> 	-p：创建出具有嵌套层关系的文件目录
> 8.2>touch	创建空白文件，可以设置文件的时间
> 	名词解释：
> 	atime: 最后一次访问文件或目录的时间【access time】
> 	mtime：最后一次修改内容的时间【modify time】
> 	ctime：最后一次改变属性的时间【change time】
> 	参数：
> 	-a  修改atime
> 	-m	修改mtime
> 	-c	修改ctime
> 	-d	同时修改atime与mtime
> 	-t	同时修改atime与mtime，格式{YYYYMMDDhhmm}
> 	注意：只有-d和-t后面可以指定时间，其他的只能把时间修改为当前时间
> 	
> 演示命令：
> ijeff@Rock:~/Desktop$ mkdir check   #创建单层目录
> ijeff@Rock:~/Desktop$ mkdir -p a/b/c/d  #创建多级目录
> ijeff@Rock:~/Desktop$ mkdir -p b/{c,d}/{e,f,g}
> ijeff@Rock:~/Desktop$ touch file1.txt  
> ijeff@Rock:~/Desktop$ touch -m file2.txt
> ijeff@Rock:~/Desktop$ touch -t 202011221213 file3.txt
> ```

> ##### 9>删除文件或者目录
>
> ```Python
> 9.1>rmdir  删除给定的目录,注意：只能删除空文件夹
> 9.2>rm	删除文件或者目录，可以删除一个目录中的一个或多个文件或目录，也可以将某个目录及其下面所有子文件和目录都删掉
>
> 	-r	删除目录，否则删不掉
> 	-ri	交互式删除，每次删除都会进行询问
> 	-rf	强制删除文件或目录
>
> 演示命令：
> angRock@Rock:~/Desktop$ rmdir check
> ijeff@Rock:~/Desktop$ rmdir b
> rmdir: 删除 'b' 失败: 目录非空
> ijeff@Rock:~/Desktop$ rm -r dir1
> ijeff@Rock:~/Desktop$ rm -ri dir2
> rm：是否进入目录'dir2'? y          #交互式删除
> rm：是否进入目录'dir2/dir1'? y
> rm：是否删除普通文件 'dir2/dir1/bbb1.txt'？ y
> rm：是否删除普通文件 'dir2/dir1/abc.txt'？ ^C     #control + c中断执行
> ijeff@Rock:~/Desktop$ rm -rf a       #强制删除目录
>   ijeff@Rock:~/Desktop$ rm -rf file1.txt #强制删除文件
> ```

> ##### 10>ln         建立链接文件
>
> 注意：建立链接文件相当于windows上创建一个快捷方式
>
> 分类：
>
> ​	软链接 、符号链接：不占用磁盘空间的，源文件删除则软连接失效【-s】
>
> ​	硬链接：可以占用磁盘空间，源文件删除对硬链接没有影响，
>
> ​		注意：只能链接普通文件，不能链接目录
>
> ```Python
> 演示命令：
> #软连接
> ijeff@Rock:~/Desktop$ rm -rf *
> ijeff@Rock:~/Desktop$ touch a.txt
> ijeff@Rock:~/Desktop$ ls
> a.txt
> ijeff@Rock:~/Desktop$ ll
> 总用量 8
> drwxr-xr-x  2 ijeff rock 4096 6月  27 15:19 ./
> drwxr-xr-x 31 ijeff rock 4096 6月  27 14:35 ../
> -rw-r--r--  1 ijeff rock    0 6月  27 15:19 a.txt
> ijeff@Rock:~/Desktop$ ln -s a.txt a
> ijeff@Rock:~/Desktop$ ll
> 总用量 8
> drwxr-xr-x  2 ijeff rock 4096 6月  27 15:21 ./
> drwxr-xr-x 31 ijeff rock 4096 6月  27 14:35 ../
> lrwxrwxrwx  1 ijeff rock    5 6月  27 15:21 a -> a.txt
> -rw-r--r--  1 ijeff rock    0 6月  27 15:19 a.txt
> ijeff@Rock:~/Desktop$ cat a.txt 
> fhuwegjawhg
> hello
> html
> linux
> fjeehdgjsehdg
> ijeff@Rock:~/Desktop$ cat a
> fhuwegjawhg
> hello
> html
> linux
> fjeehdgjsehdg
> ijeff@Rock:~/Desktop$ cat a.txt 
> fhuwegjawhg
> hello
> html
> linux
> fjeehdgjsehdg
> 462527568357628
> ijeff@Rock:~/Desktop$ rm a.txt
> ijeff@Rock:~/Desktop$ cat a
> cat: a: 没有那个文件或目录
>
> #硬链接
> ijeff@Rock:~/Desktop$ touch a.txt
> ijeff@Rock:~/Desktop$ rm a
> ijeff@Rock:~/Desktop$ ln a.txt a
> ijeff@Rock:~/Desktop$ cat a.txt 
> hfijehgwahg
> hgjehgjwagd
> hjaehdg
> ijeff@Rock:~/Desktop$ cat a
> hfijehgwahg
> hgjehgjwagd
> hjaehdg
> ijeff@Rock:~/Desktop$ cat a.txt 
> hfijehgwahg
> hgjehgjwagd
> hjaehdg
> 64723882
> ijeff@Rock:~/Desktop$ cat a
> hfijehgwahg
> hgjehgjwagd
> hjaehdg
> 64723882
> ijeff@Rock:~/Desktop$ ll
> 总用量 16
> drwxr-xr-x  2 ijeff rock 4096 6月  27 15:27 ./
> drwxr-xr-x 31 ijeff rock 4096 6月  27 14:35 ../
> -rw-r--r--  2 ijeff rock   41 6月  27 15:28 a
> -rw-r--r--  2 ijeff rock   41 6月  27 15:28 a.txt
> ijeff@Rock:~/Desktop$ rm a.txt 
> ijeff@Rock:~/Desktop$ cat a
> hfijehgwahg
> hgjehgjwagd
> hjaehdg
> 64723882
>
> 【总结】
> 对于软连接而言，如果软连接和源文件不在同一个目录下，则原文件使用绝对路径
> 对于硬链接而言，两个文件占用相同大小的磁盘空间，如果源文件被删除，硬链接不受任何影响，正常使用
> 软连接是常见的形式
>
> ```

> ##### 11>grep	      文本搜索
>
> ```Python
> 强大的文本搜索工具，grep允许对文本文件进行模式查找，如果找到匹配模式，grep打印包含模式的所有行
> 注意：搜索内容串可以是正则表达式
>
> -c：返回匹配到的数目
> -i：忽略大小写	
> -n：显示匹配行以及行号
> -v：反向选择，列出没有关键词的行【求反】
>
> 演示命令：
> ijeff@Rock:~$ cd Desktop/
> ijeff@Rock:~/Desktop$ touch a.txt
> ijeff@Rock:~/Desktop$ touch a1.txt
> ijeff@Rock:~/Desktop$ touch a2.txt
> ijeff@Rock:~/Desktop$ ls
> a  a1.txt  a2.txt  a.txt
> ijeff@Rock:~/Desktop$ ls | grep a1.txt
> a1.txt								#以ls的输出作为grep的输入
> ijeff@Rock:~/Desktop$ ls | grep a
> a									#检索桌面上文件名中包含a的文件
> a1.txt
> a2.txt
> a.txt
> ijeff@Rock:~/Desktop$ touch b.txt
> ijeff@Rock:~/Desktop$ ls
> a  a1.txt  a2.txt  a.txt  b.txt
> ijeff@Rock:~/Desktop$ ls | grep a
> a
> a1.txt
> a2.txt
> a.txt
> ijeff@Rock:~/Desktop$ ls | grep -c a
> 4
> ijeff@Rock:~/Desktop$ ls | grep -n a
> 1:a
> 2:a1.txt
> 3:a2.txt
> 4:a.txt
> ijeff@Rock:~/Desktop$ ls | grep -v a
> b.txt									#反向检索【否定】
> ijeff@Rock:~/Desktop$ cat a.txt 
> yuieqwhfije
> fhhjeanf
> hfjaehdgj
> hello
>
> ijeff@Rock:~/Desktop$ cat a.txt | grep a
> fhhjeanf								#检索a.txt文件中包含a的内容
> hfjaehdgj
> ```

> ##### 12>which  查找其他命令所在的位置
>
> 注意：显示其他指定命令的路径
>
> ```Python
> 演示命令：
> ijeff@Rock:~/Desktop$ which ls
> /bin/ls
> ijeff@Rock:~/Desktop$ which cd
> ijeff@Rock:~/Desktop$ which cat
> /bin/cat
> ijeff@Rock:~/Desktop$ which pwd
> /bin/pwd
> ijeff@Rock:~/Desktop$ which ll
>
> #注意：如果是封装的命令，查找不到位置，比如上面的cd和ll
> ```

> ##### 13>type   寻找命令所在的位置，包括命令别名
>
> ```Python
> -a：可以找到所有，包括别名和位置
>
> #type和which的区别：type列出别名和位置，which列出位置
>
> 演示命令：
> ijeff@Rock:~/Desktop$ type ls
> ls 是 `ls --color=auto' 的别名
> ijeff@Rock:~/Desktop$ type -a ls
> ls 是 `ls --color=auto' 的别名
> ls 是 /bin/ls
> ```

> ##### 14>find	  按照指定条件来查找文件
>
> ```Python
> 格式：find  【查找路径】 【查找方式】 【查找条件】
>
> -name：匹配名称，默认是精确匹配 
> -size：匹配文件大小
> -empty
>
> 演示命令：
> ijeff@Rock:~/Desktop$ ls
> a  a1.txt  a2.txt  a.txt  b.txt
> ijeff@Rock:~/Desktop$ find -name a1.txt
> ./a1.txt								#查找文件名为a1.txt的文件
> ijeff@Rock:~/Desktop$ find -size 1k
> ./a.txt									#查找文件大小等于1k的文件
> ./a
> ijeff@Rock:~/Desktop$ find -size +1k
> . 									   #查找文件大小大于1k的文件
> ijeff@Rock:~/Desktop$ find -size -1k
> ./b.txt        							#查找文件大小小于1k的文件
> ./a2.txt
> ./a1.txt
> ijeff@Rock:~/Desktop$ find -empty     #查找空文件
> ./b.txt
> ./a2.txt
> ./a1.txt
> ```

> ##### 15>locate   查找数据
>
> ```Python
> -i:忽略大小写
> -c：不输出寻找结果，仅计算找到的文件数量
> -l：仅输出指定的几行，  例如：-l 8，输出8行
>
> 演示命令：
> ijeff@Rock:~/Desktop$ locate hello
> /boot/grub/i386-pc/hello.mod				#全局查找包含hello的内容
> /usr/lib/grub/i386-pc/hello.mod
> /usr/lib/python2.7/__phello__.foo.py
> /usr/lib/python2.7/__phello__.foo.pyc
> /usr/lib/python3.5/__phello__.foo.py
>
> ijeff@Rock:~/Desktop$ locate /etc/sh
> /etc/shadow
> /etc/shadow-
> /etc/shells
> ```

> ##### 16>sort    给文件内容排序
>
> ```Python
> -f：忽略大小写的差异，例如 A 与 a 视为编码相同；
> -b：忽略最前面的空格符部分；
> -n：使用『纯数字』进行排序(默认是以文字型态来排序的)；
> -r：反向排序；
> -u：就是 uniq，表示唯一的，相同的数据中，仅出现一行代表；
> -t：分隔符，默认是用 [tab] 键来分隔；
> -k：以哪个区间 (field) 来进行排序的意思
>
> 演示命令：
> ijeff@Rock:~/Desktop$ cat a.txt
> yuieqwhfije
> fhhjeanf
> hfjaehdgj
> hello
>
> ijeff@Rock:~/Desktop$ sort a.txt
> 									#默认按照升序排序
> fhhjeanf
> hello
> hfjaehdgj
> yuieqwhfije
> ijeff@Rock:~/Desktop$ sort -t ":" -k 2 a.txt
> 									#以：为分隔符，按照指定区间排序
> hfj:aehd:gj
> fhhj:ean:f
> hello:fhedg:fhjdg
> yuieq:whfij:e
> ```

> ##### 17>cut       可以从一个文本文件或者文本流中提取文本列
>
> ```Python
> -d ：后面接分隔字符。与 -f 一起使用；
> -f ：依据 -d 的分隔字符将一段信息分割成为数段，用 -f 取出第几段的意思；
> -c ：以字符 (characters) 的单位取出固定字符区间；( -连接区间  ,取的是和的意思)
>
> 演示命令：
> ijeff@Rock:~/Desktop$ cat a.txt
> yuieq:whfij:e
> fhhj:ean:f
> hfj:aehd:gj
> hello:fhedg:fhjdg
>
> ijeff@Rock:~/Desktop$ cut -d ":" -f 1 a.txt
> yuieq								#提取以：为分隔符的第1个区间的数据
> fhhj		
> hfj
> hello
>
> ijeff@Rock:~/Desktop$ cut -c 1 a.txt
> y									#提取第一个字符
> f
> h
> h
>
> ijeff@Rock:~/Desktop$ cut -c 1,3 a.txt
> yi									#提取第1个和第3个字符
> fh
> hj
> hl
>
> ijeff@Rock:~/Desktop$ cut -c 1-3 a.txt
> yui									#提取第1到第3个字符
> fhh
> hfj
> hel
> ```

> ##### 18>tee    读取标准输入的数据，并将其内容输出成文件【向指定文件中写入内容】
>
> ```Python
> -a：读取原文件内容，并追加新的内容,如果不设置该选项，则新的内容直接覆盖旧的内容
>
> 演示命令：
> ijeff@Rock:~/Desktop$ tee a.txt 
> ^C
> ijeff@Rock:~/Desktop$ tee -a a.txt
> fhajhf								#向指定文件中追加内容
> fhajhf
> gjfg
> gjfg
> jghqj
> jghqj
> gjrgh
> gjrgh
> ^C
> ijeff@Rock:~/Desktop$ cat a1.txt 
> ijeff@Rock:~/Desktop$ tee a1.txt
> tuwit								#向指定文件中写入内容
> tuwit
> grehwjgh
> grehwjgh
> ^C
> ijeff@Rock:~/Desktop$ cat a1.txt
> tuwit		
> grehwjgh
> ijeff@Rock:~/Desktop$ tee a1.txt a2.txt
> uuuu								#向多个指定文件中写入内容
> uuuu
> ppppp
> ppppp
> ^C
> ```

> ##### 19>gedit	打开Linux下的文本编辑器
>
> ```Python
> 演示命令：
> ijeff@Rock:~/Desktop$ gedit      #打开一个新的文本文件
> ijeff@Rock:~/Desktop$ gedit a1.txt	#打开一个现有的文本文件
> ```

