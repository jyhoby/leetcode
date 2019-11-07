# Day05

### 一、上堂回顾

> git命令:
>
> 本地仓库：
>
> ​	git init  ： 创建本地仓库
>
> ​	git add :  将修改添加到暂存区
>
> ​	git commit -m "" ：将暂存区的所有内容添加到分支
>
> ​	git diff : 查看区别 
>
> ​	git status : 查看状态（工作区和仓库是否同步）
>
> 远程仓库：
>
> ​	git remote add origin http  :  添加远程仓库的关联
>
> ​	git remote rm origin: 移除远程仓库的关联
>
> ​	git push origin master : 将本地仓库推送到远程仓库（推送修改）
>
> ​	git pull origin master : 将远程仓库拉取到本地仓库
>
> ​	git clone http..  : 克隆仓库到本地（下载并自动建立关联）
>
> 版本回退：
>
> ​	git reset --hard HEAD^  : 版本跳转到上一个版本
>
> ​	git log : 查看提交记录
>
> ​	git log --pretty=oneline ： 一行的方式查看提交记录
>
> ​	git reflog : 查看执行记录
>
> 分支管理：
>
> ​	创建分支： git branch dev
>
> ​	创建并切换分支： git checkout -b dev
>
> ​	切换分支：git checkout dev
>
> ​	合并分支： git merge dev
>
> ​	删除分支： git branch -d dev	

### 二、git

#### 6.分支管理

##### 6.4bug分支

> 一般情况下，每个bug都需要使用一个分支来进行解决，解决后，分支删除
>
> git stash: 可以把当前工作现场储存起来，然后先进行其他的工作，完成工作之后，可以解封继续工作
>
> ```Python
> 演示命令：
> ijeff@Rock:~/Desktop/day5Text$ git checkout -b dev
> 切换到一个新分支 'dev'
>
> ijeff@Rock:~/Desktop/day5Text$ git branch
> * dev
> master
>
> ijeff@Rock:~/Desktop/day5Text$ git status
> 位于分支 dev
> 无文件要提交，干净的工作区
>
> ijeff@Rock:~/Desktop/day5Text$ vim README.md 
> ijeff@Rock:~/Desktop/day5Text$ git add README.md 
> ijeff@Rock:~/Desktop/day5Text$ git status
> 位于分支 dev
> 要提交的变更：
> （使用 "git reset HEAD <文件>..." 以取消暂存）
>
> 	修改：     README.md
>   
> ijeff@Rock:~/Desktop/day5Text$ git stash			#封存工作现场
> 保存工作目录和索引状态 WIP on dev: e742319 Initial commit
>   
> ijeff@Rock:~/Desktop/day5Text$ git status
> 位于分支 dev
> 无文件要提交，干净的工作区
>
> ijeff@Rock:~/Desktop/day5Text$ git checkout master
> 切换到分支 'master'
> 您的分支与上游分支 'origin/master' 一致。
>
> ijeff@Rock:~/Desktop/day5Text$ git checkout -b bug-01
> 切换到一个新分支 'bug-01'
>
> ijeff@Rock:~/Desktop/day5Text$ vim README.md 
> ijeff@Rock:~/Desktop/day5Text$ git add README.md 
> ijeff@Rock:~/Desktop/day5Text$ git commit -m "fixed a bug"
> [bug-01 235be14] fixed a bug
> 1 file changed, 2 insertions(+), 1 deletion(-)
>
> ijeff@Rock:~/Desktop/day5Text$ git checkout master
> 切换到分支 'master'
> 您的分支与上游分支 'origin/master' 一致。
>
> ijeff@Rock:~/Desktop/day5Text$ git merge --no-ff -m "merge bug-01" bug-01
> Merge made by the 'recursive' strategy.
> README.md | 3 ++-
> 1 file changed, 2 insertions(+), 1 deletion(-)
>
> ijeff@Rock:~/Desktop/day5Text$ git branch -d bug-01
> 已删除分支 bug-01（曾为 235be14）。
>
> ijeff@Rock:~/Desktop/day5Text$ git status
> 位于分支 master
> 您的分支领先 'origin/master' 共 2 个提交。
> （使用 "git push" 来发布您的本地提交）
> 无文件要提交，干净的工作区
>
> ijeff@Rock:~/Desktop/day5Text$ git stash list
> stash@{0}: WIP on dev: e742319 Initial commit
>     
> ijeff@Rock:~/Desktop/day5Text$ git stash pop      # 解封，有冲突，解决冲突
> 自动合并 README.md
> 冲突（内容）：合并冲突于 README.md
>
> ijeff@Rock:~/Desktop/day5Text$ git stash pop
> README.md: needs merge
> 无法刷新索引
>
> ijeff@Rock:~/Desktop/day5Text$ git commit -m "continue"
> U	README.md
> error: 无法提交，因为您有未合并的文件。
> 提示：请在工作区改正文件，然后酌情使用 'git add/rm <文件>' 命令标记
> 提示：解决方案并提交。
> fatal: 因为存在未解决的冲突而退出。
>   
> ijeff@Rock:~/Desktop/day5Text$ git add README.md 	#冲突解决之后需要再次add和commit
>   
> ijeff@Rock:~/Desktop/day5Text$ git commit -m "continue"
> 位于分支 master
> 您的分支领先 'origin/master' 共 2 个提交。
> （使用 "git push" 来发布您的本地提交）
> 无文件要提交，干净的工作区
>
> ijeff@Rock:~/Desktop/day5Text$ git branch
> dev
> * master
>
> ```
>
> 总结：
>
> ​	修复bug时，创建一个新的分支，进行bug的修复，然后合并，最后删除bug分支
>
> ​	当手头的工作没有完成的时候，使用git stash 将内容封存，然后去修复bug，当bug修复完成之后，则使用命令git stash pop解封

##### 6.5 feature分支

> ```Python
> 演示命令：
> ijeff@hhhhh:~/Desktop/day5Text$ git branch
>   dev
> * master
> ijeff@hhhhh:~/Desktop/day5Text$ git checkout dev
> ijeff@hhhhh:~/Desktop/day5Text$ git checkout -b feature1
> 切换到一个新分支 'feature1'
> ijeff@hhhhh:~/Desktop/day5Text$ touch a.txt
> ijeff@hhhhh:~/Desktop/day5Text$ git add a.txt 
> ijeff@hhhhh:~/Desktop/day5Text$ git commit -m "create a.txt"
> [feature1 120a22f] create a.txt
>  1 file changed, 0 insertions(+), 0 deletions(-)
>  create mode 100644 a.txt
> ijeff@hhhhh:~/Desktop/day5Text$ git status
> 位于分支 feature1
> 无文件要提交，干净的工作区
> ijeff@hhhhh:~/Desktop/day5Text$ vim a.txt 
> ijeff@hhhhh:~/Desktop/day5Text$ git add a.txt 
> ijeff@hhhhh:~/Desktop/day5Text$ git status
> 位于分支 feature1
> 要提交的变更：
>   （使用 "git reset HEAD <文件>..." 以取消暂存）
>
> 	修改：     a.txt
>
> ijeff@hhhhh:~/Desktop/day5Text$ git commit -m "add hello"
> [feature1 af31c25] add hello
>  1 file changed, 1 insertion(+)
> ijeff@hhhhh:~/Desktop/day5Text$ git checkout dev
> 切换到分支 'dev'
> ijeff@hhhhh:~/Desktop/day5Text$ git branch -d feature1	#正常删除
> error: 分支 'feature1' 没有完全合并。
> 如果您确认要删除它，执行 'git branch -D feature1'。
> ijeff@hhhhh:~/Desktop/day5Text$ git branch -D feature1	#强制删除
> 已删除分支 feature1（曾为 af31c25）。
> ```
>
> 总结：
>
> ​	每开发一个新的功能【版本迭代】，最好新建一个分支来进行操作
>
> ​	如果需要丢弃一个还没有被合并的分支，使用命令 git branch -D  branch-name

##### 6.6多人协作

> 当你从远程仓克隆时，实际上git将本地的master和远程的master对应起来了，并且远程仓库的默认的名字为origin
>
> ```Python
> 演示命令：
> ijeff@hhhhh:~/Desktop/day5Text$ git remote     #查看远程库的信息
> origin
> ijeff@hhhhh:~/Desktop/day5Text$ git remote -v
> origin	git@github.com:ijeff-git/day5Text.git (fetch)
> origin	git@github.com:ijeff-git/day5Text.git (push)
> ```

##### 1>推送分支 git push

> 推送分支：把该分支上的所有的本地提交推送到远程库，推送时，要指定本地分支
>
> ```Python
> 演示命令：
> ijeff@hhhhh:~/Desktop/day5Text$ git branch
> * dev
> master
>
> ijeff@hhhhh:~/Desktop/day5Text$ git push origin master
> 对象计数中: 4, 完成.
> Delta compression using up to 2 threads.
> 压缩对象中: 100% (2/2), 完成.
> 写入对象中: 100% (4/4), 340 bytes | 340.00 KiB/s, 完成.
> Total 4 (delta 1), reused 0 (delta 0)
> remote: Resolving deltas: 100% (1/1), done.
> To github.com:ijeff-git/day5Text.git
> e742319..cc4bef3  master -> master
>
> ijeff@hhhhh:~/Desktop/day5Text$ git push origin dev
> Total 0 (delta 0), reused 0 (delta 0)
> To github.com:ijeff-git/day5Text.git
>  * [new branch]      dev -> dev
>
> ijeff@hhhhh:~/Desktop/day5Text$ vim README.md 
> ijeff@hhhhh:~/Desktop/day5Text$ git add README.md 
> ijeff@hhhhh:~/Desktop/day5Text$ git commit -m "hello"
> [dev ae20ec5] hello
> 1 file changed, 2 insertions(+), 1 deletion(-)
>
> ijeff@hhhhh:~/Desktop/day5Text$ git checkout master
> 切换到分支 'master'
> 您的分支与上游分支 'origin/master' 一致。
>
> ijeff@hhhhh:~/Desktop/day5Text$ git merge dev
> 自动合并 README.md
> 冲突（内容）：合并冲突于 README.md
> 自动合并失败，修正冲突然后提交修正的结果。
>
> ijeff@hhhhh:~/Desktop/day5Text$ vim README.md 
> ijeff@hhhhh:~/Desktop/day5Text$ git add README.md 
> ijeff@hhhhh:~/Desktop/day5Text$ git commit -m "conflict"
> [master 56411e2] conflict
>
> ijeff@hhhhh:~/Desktop/day5Text$ git merge dev
> 已经是最新的。
>
> ijeff@hhhhh:~/Desktop/day5Text$ git push origin dev
> 对象计数中: 3, 完成.
> 写入对象中: 100% (3/3), 255 bytes | 255.00 KiB/s, 完成.
> Total 3 (delta 0), reused 0 (delta 0)
> To github.com:ijeff-git/day5Text.git
> e742319..ae20ec5  dev -> dev
> ```
>
> 总结：
>
> ​	并不是所有的分支都需要推送到远程仓库
>
> ​	a.master分支是主分支，因此要时刻与远程保持同步
>
> ​	b.dev是一个开发分支，团队所有的成员都在上面工作，所以也需要推送到远程仓库
>
> ​	c.bug分支只是修复一个bug，就没必要推送到远程

##### 2>抓取分支 git pull

> ```Python
> 演示命令：
> ijeff@hhhhh:~/Desktop/day5Text$ cd ..
> ijeff@hhhhh:~/Desktop$ mkdir other
> ijeff@hhhhh:~/Desktop$ cd other/
>   
> ijeff@hhhhh:~/Desktop/other$ git clone git@github.com:ijeff-git/day5Text.git
> 正克隆到 'day5Text'...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (3/3), done.
> remote: Total 10 (delta 2), reused 6 (delta 1), pack-reused 0
> 接收对象中: 100% (10/10), 完成.
> 处理 delta 中: 100% (2/2), 完成.
>   
> ijeff@hhhhh:~/Desktop/other$ cd day5Text/
> ijeff@hhhhh:~/Desktop/other/day5Text$ git branch
> * master
>   
> # 分支 'dev' 设置为跟踪来自 'origin' 的远程分支 'dev'。
> # 需要先在github创建dev分支
> ijeff@hhhhh:~/Desktop/other/day5Text$ git checkout -b dev origin/dev
> 切换到一个新分支 'dev'
>
> ijeff@hhhhh:~/Desktop/other/day5Text$ git branch
> * dev
> master
>
> ijeff@hhhhh:~/Desktop/other/day5Text$ touch b.txt
> ijeff@hhhhh:~/Desktop/other/day5Text$ vim b.txt 
> ijeff@hhhhh:~/Desktop/other/day5Text$ git add b.txt 
> ijeff@hhhhh:~/Desktop/other/day5Text$ git commit -m "b"
> [dev b08d6ec] b
> 1 file changed, 1 insertion(+)
> create mode 100644 b.txt
>
> ijeff@hhhhh:~/Desktop/other/day5Text$ git push origin dev    #推送分支
> 对象计数中: 3, 完成.
> Delta compression using up to 2 threads.
> 压缩对象中: 100% (2/2), 完成.
> 写入对象中: 100% (3/3), 274 bytes | 274.00 KiB/s, 完成.
> Total 3 (delta 0), reused 0 (delta 0)
> To github.com:ijeff-git/day5Text.git
> ae20ec5..b08d6ec  dev -> dev
>
> ijeff@hhhhh:~/Desktop/other/day5Text$ cd ../..
> ijeff@hhhhh:~/Desktop$ cd day5Text/
> ijeff@hhhhh:~/Desktop/day5Text$ git branch
> dev
> * master
>
> ijeff@hhhhh:~/Desktop/day5Text$ git checkout dev
> 切换到分支 'dev'
>
> ijeff@hhhhh:~/Desktop/day5Text$ git pull
> remote: Counting objects: 3, done.
> remote: Compressing objects: 100% (2/2), done.
> remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
> 展开对象中: 100% (3/3), 完成.
> 来自 github.com:ijeff-git/day5Text
> ae20ec5..b08d6ec  dev        -> origin/dev
> 当前分支没有跟踪信息。
> 请指定您要合并哪一个分支。
> 详见 git-pull(1)。
>
>  git pull <远程> <分支>
>
> 如果您想要为此分支创建跟踪信息，您可以执行：#抓取失败，根据提示操作，原因是没有指定本地dev分支与远程origin/dev分支的链接
>  git branch --set-upstream-to=origin/<分支> dev
>
> ijeff@hhhhh:~/Desktop/day5Text$ git branch --set-upstream-to=origin/dev dev
> 分支 'dev' 设置为跟踪来自 'origin' 的远程分支 'dev'	 # 设置跟踪
>
> ijeff@hhhhh:~/Desktop/day5Text$ git pull       #抓取分支
> 更新 ae20ec5..b08d6ec
> Fast-forward
> b.txt | 1 +
> 1 file changed, 1 insertion(+)
> create mode 100644 b.txt
>
> #此时，两个小伙伴之间就可以各自工作了，然后只需要将各自的修改每次提交到dev分支
> ijeff@hhhhh:~/Desktop/day5Text$ vim b.txt
> ijeff@hhhhh:~/Desktop/day5Text$ git add b.txt 
> ijeff@hhhhh:~/Desktop/day5Text$ git commit -m "hello"
> [dev 61c1d88] hello
> 1 file changed, 1 insertion(+)
> ijeff@hhhhh:~/Desktop/day5Text$ git push origin dev
> 对象计数中: 3, 完成.
> Delta compression using up to 2 threads.
> 压缩对象中: 100% (2/2), 完成.
> 写入对象中: 100% (3/3), 284 bytes | 284.00 KiB/s, 完成.
> Total 3 (delta 0), reused 0 (delta 0)
> To github.com:ijeff-git/day5Text.git
> b08d6ec..61c1d88  dev -> dev
> ijeff@hhhhh:~/Desktop/day5Text$ cd ..
> ijeff@hhhhh:~/Desktop$ cd other/day5Text/
> ijeff@hhhhh:~/Desktop/other/day5Text$ git pull
> remote: Counting objects: 3, done.
> remote: Compressing objects: 100% (2/2), done.
> remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
> 展开对象中: 100% (3/3), 完成.
> 来自 github.com:ijeff-git/day5Text
> b08d6ec..61c1d88  dev        -> origin/dev
> 更新 b08d6ec..61c1d88
> Fast-forward
> b.txt | 1 +
> 1 file changed, 1 insertion(+)
> ijeff@hhhhh:~/Desktop/other/day5Text$ cat b.txt 
> fghajdfja
> hello
>
> #注意：如果合并有冲突，需要手动解决，解决的方法和分支管理中的解决冲突完全一样。解决后，提交，再push
> #实际的工作流程是：先pull[抓取]，后push[推送]
> ```
>
> 总结：
>
> ​	a.查看远程库的信息，使用git remote -v
>
> ​	b.本地新建的分支如果不推送到远程，对其他人都是不可见的
>
> ​	c.从本地推送分支，使用命令git push origin branchname,如果推送失败，则先用git pull抓取
>
> ​	d.在本地创建于远程分支的连接，使用命令git checkout -b branchname origin/branchname
>
> ​	e. 从远程抓取分支，使用git pull，如果有冲突，则要先解决冲突	

#### 7.标签管理

##### 7.1创建标签

> ```Python
> 演示命令：
> ijeff@hhhhh:~/Desktop/day5Text$ git tag v1.0	#创建标签，默认创建的是当前最新提交的标签
> ijeff@hhhhh:~/Desktop/day5Text$ git tag
> v1.0
> ijeff@hhhhh:~/Desktop/day5Text$ git tag v0.2 ae20ec5	#为指定commit id创建标签
> ijeff@hhhhh:~/Desktop/day5Text$ git tag
> v0.2
> v1.0
> ```

##### 7.2操作标签

> ```Python
> 演示命令：
> ijeff@hhhhh:~/Desktop/day5Text$ git show v1.0	#查看指定标签的详细信息
> commit 61c1d8863fd7df3d20c156ace3bfa1d7882b636c (HEAD -> dev, tag: v1.0, origin/dev)
> Author: ijeff-git <18501970795@163.com>
> Date:   Mon Jul 2 10:52:50 2018 +0800
>
>     hello
>
> diff --git a/b.txt b/b.txt
> index 9022bb8..4bc9d07 100644
> --- a/b.txt
> +++ b/b.txt
> @@ -1 +1,2 @@
>  fghajdfja
> +hello
> ijeff@hhhhh:~/Desktop/day5Text$ git tag -a v0.1 -m "version 0.1" e7423195
>   #创建标签，携带标签的描述信息
> ijeff@hhhhh:~/Desktop/day5Text$ git tag	#查看当前分支下的标签
> v0.1
> v0.2
> v1.0
>
> # 删除标签
> ijeff@hhhhh:~/Desktop/day5Text$ git tag -d v0.1	
> 已删除标签 'v0.1'（曾为 97026a8）
> ijeff@hhhhh:~/Desktop/day5Text$ git push origin --tags	#将本地仓库中的标签推送到远程仓库
> Total 0 (delta 0), reused 0 (delta 0)
> To github.com:ijeff-git/day5Text.git
>  * [new tag]         v0.2 -> v0.2
>  * [new tag]         v1.0 -> v1.0
> ijeff@hhhhh:~/Desktop/day5Text$ git tag -d v0.2		#删除本地仓库中的标签
> 已删除标签 'v0.2'（曾为 ae20ec5）
> ijeff@hhhhh:~/Desktop/day5Text$ git push origin :refs/tags/v0.2
>     #删除远程仓库中的指定标签
> remote: warning: Deleting a non-existent ref.
> To github.com:ijeff-git/day5Text.git
>  - [deleted]         v0.2To
> ```

### 三、shell编程

#### 1.简介

##### 1.1什么是shell

> 把在终端运行的命令保存到文件中，这个文件就是shell程序
>
> 简单的说，shell编程就是第Linux命令的逻辑化处理

##### 1.2shell解析器的类型

> bash，ash，ksh等，默认使用bash
>
> ```
> 演示命令：
> echo $SHELL
> /bin/bash
> ```

##### 1.3shell的作用

> 如果需要反复执行某些Linux命令，则可以将这些命令写到一个shell脚本中，然后每次只需要运行一下这个脚本即可

#### 2.第一个shell程序

##### 2.1实现

> 打开文本编辑器(可以使用 touch命令来创建文件)，新建一个文件 test.sh，扩展名为 sh（sh代表shell），扩展名并不影响脚本执行，见名知意就好
>
> 代码演示：
>
> ```shell
> #!/bin/bash
> # 打印hello world
> echo "Hello World !"
> ```

##### 2.2运行

> 方式一：作为可执行程序
>
> ```Python
> touch test.sh
> vim test.sh
> chmod +x ./test.sh
> ./test.sh
> ```
>
> 方式二：作为解释器参数
>
> ```Python
> bin/bash test.sh 
> ```

#### 3.shell中的变量

##### 3.1变量的定义

> 定义：变量名=值
>
> ```shell
> 演示命令：
> your_name="zhangsan"
> echo $your_name
> num=10
> echo ${num}
>
> # 注意：变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界
> echo "his name is ${your_name}"
> ```

##### 3.2只读变量

> readonly：只读，将变量声明为readonly，只读变量的值不能发生改变
>
> ```shell
> myUrl="http://www.baidu.com"
> readonly myUrl
> myUrl="http://www.1000phone.com"
>
> #运行脚本,报错：/bin/sh: NAME: This variable is read only
> ```

##### 3.3删除变量

> unset：删除变量
>
> ```shell
> 代码演示：
> myUrl="http://www.baidu.com"
> unset myUrl
> echo $myUrl
>
> #变量被删除后不能再次使用。unset 命令不能删除只读变量。
> #以上实例执行将没有任何输出
> ```

#### 4.字符串和数组

##### 4.1字符串

> 双引号或者单引号
>
> 单引号的限制：
>
> ​	a.单引号中的任何字符都会原样输出，单引号字符串中的变量是无效的
>
> ​	b.单引号字符串中不能再出现单引号【对单引号进行转义后去不起作用】
>
> 总结：
>
> ​	双引号：可以包含除了$、`、\、‘‘之外的任意字符
>
> ​	单引号：其中的任意字符都不会被解析，都会原样输出
>
> ​	反引号：会将其中的内容作为命令执行 ``
>
> ​	反斜线：转义特定的字符，如：&、*、^、等  \
>
> 代码演示:
>
> ```shell
> 代码演示：
> #!/bin/bash
>
> #定义字符串
> your_name='qinjx'
> str="Hello, I know you are \"$your_name\"! \n"
>
> #拼接字符串
> your_name="qinjx"
> greeting="hello, "$your_name" !"
> greeting_1="hello, ${your_name} !"
> echo $greeting $greeting_1
>
> #获取字符串长度
> string="abcd"
> echo ${#string} #输出 4
>
> #提取子字符串
> string="1000phone is a great site"
> echo ${string:1:4}       #从下标1开始，长度为4
>
> #查找子字符串
> string="1000phone is a great company"
> echo `expr index "$string" is`  
>
> #注意： 以上脚本中 "`" 是反引号，而不是单引号 "'"，不要看错了哦
> ```

##### 4.2数组

> bash只支持一维数组，不支持多维数组
>
> 并没有限制数组的大小
>
> 数组元素的下标也是从0开始的，获取数组中的元素使用下标
>
> 定义数组：数组名=(值1 值2 值3....)
>
> 注意：shell中的数组元素之间使用空格分隔
>
> 代码演示：
>
> ```shell
> #数组的定义
> arr1=(10 20 30 40)
> echo $arr1
> arr2=(
> 10
> 20
> 30
> 40
> )
> echo $arr2
>
> #数组的使用
> #读取数组中的元素
> echo ${arr1[2]}
> #如果要读取数组中的全部元素
> echo ${arr2[@]}
>
> # 取得数组元素的个数
> length=${#arr1[@]}
> echo $length
> # 或者
> length=${#arr1[*]}
> echo $length
> # 取得数组单个元素的长度
> lengthn=${#arr1[3]}
> echo $lengthn
> ```

#### 5.shell中的运算符

> expr:是一款表达式计算工具，使用它能够完成表达式的求值操作
>
> 代码演示：
>
> ```shell
> val=`expr 1 + 2`
> echo "两数之和为 : $val"
>
> #1.算术运算符
> val=`expr $a + $b`
> echo "a + b : $val"
>
> val=`expr $a \* $b`
> echo "a * b : $val"
>
> #2.关系运算符
> ## []中，前后都需要空格
> if [ $a -eq $b ]
> then
>    echo "$a -eq $b : a 等于 b"
> else
>    echo "$a -eq $b: a 不等于 b"
> fi
>
> #3.逻辑运算符
> if [ 1 -lt 3 ] && [ 2 -lt 3 ]; 
> then
> 	echo "ok"
> fi
> ```

#### 6.echo、printf、test命令

> 1>echo
>
> ```shell
> echo -e "OK! \n" 		# -e 开启转义,\n 显示换行
> echo -e "OK! \c"		 # -e 开启转义 \c 不换行
>
> echo `date`    #显示命令执行结果
> #注意： 这里使用的是反引号 `, 而不是单引号 '。
> #结果为：Thu Jul 24 10:08:46 CST 2014
> ```
>
> 2> printf
>
> ```shell
> printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
> printf "%-10s %-8s %-4.2f\n" 张三 男 66.1234 
> printf "%-10s %-8s %-4.2f\n" 李四 男 48.6543 
> ```
>
> 注意：
>
> ​	%s %d %f都是格式替换符
>
> ​	-10s:指的是一个宽度为10的字符（-表示左对齐，没有则表示右对齐），任何字符都会填充在这10个字符内，如果不足则使用空格自动填充
>
> ​	-4.2f:指的是格式化为小数，其中.2表示保留小数点后两位
>
> 3> test
>
> ```shell
> #1.数值测试
> num1=100
> num2=100
> if test $[num1] -eq $[num2]
> then
>     echo '两个数相等！'
> else
>     echo '两个数不相等！'
> fi
>
> #2.字符串测试
> num1="hello"
> num2="hello11"
> if test $num1 = $num2
> then
>     echo '两个字符串相等!'
> else
>     echo '两个字符串不相等!'
> fi
>
> #3.文件测试
> cd /bin
> if test -e ./bash
> then
>     echo '文件已存在!'
> else
>     echo '文件不存在!'
> fi
> ```
>
> test命令用来监测某个条件是否成立，他可以进行数值，字符和文件的监测

#### 7.shell中的流程控制语句

##### 7.1分支语句

> if
>
> 代码演示：
>
> ```shell
> #if语句
> #单分支
> if [ 1 -lt 3 ] && [ 2 -lt 3 ]; 
> then
> 	echo "ok"
> fi
>
> #双分支
> num1=$[2*3]
> num2=$[1+5]
> #if else语句经常与test命令结合使用
> if test $[num1] -eq $[num2]
> then
>     echo '两个数字相等!'
> else
>     echo '两个数字不相等!'
> fi
>
> #多分支
> a=10
> b=20
> if [ $a == $b ]
> then
>    echo "a 等于 b"
> elif [ $a -gt $b ]
> then
>    echo "a 大于 b"
> elif [ $a -lt $b ]
> then
>    echo "a 小于 b"
> else
>    echo "没有符合的条件"
> fi
>
>
> #case语句
> echo '输入 1 到 4 之间的数字:'
> read aNum
> case $aNum in
>     1)  echo '你选择了 1'
>     ;;
>     2)  echo '你选择了 2'
>     ;;
>     3)  echo '你选择了 3'
>     ;;
>     4)  echo '你选择了 4'
>     ;;
>     *)  echo '你没有输入 1 到 4 之间的数字'
>     ;;
> esac
> ```

##### 7.2循环语句

> for 
>
> 代码演示：
>
> ```shell
> #for语句
> #需求：顺序输出当前列表中的数字
> for num in 1 2 3 4 5
> do
>     echo "The value is: $num"
> done
>
>
> #需求：顺序输出字符串中的字符
> for str in 'This is a string'
> do
>     echo $str
> done
>
> #需求：遍历数组中的所有元素
> a=(1 2 3)
>   for x in ${a[*]}
>   do 
>   	echo $x
>   done
>   
> ```

#### 8.函数

> 代码演示：
>
> ```shell
> #无参无返回值
> #定义函数
> demo()
> {
> 	echo 'hello world'
> }
> #调用函数
> demo
>
> #有返回值
> funWithReturn(){
>     echo "输入第一个数字: "
>     read aNum
>     echo "输入第二个数字: "
>     read anotherNum
>     return $(($aNum+$anotherNum))
> }
> funWithReturn
> echo  $? 
>
> #有参有返回值
> arg()
> {
> 	echo $1
> 	echo $2
> 	echo $#
> 	echo $*
> 	return 123
> }
>
> arg 1 2
> # $? 表示函数的返回值
> echo $?
> ```

