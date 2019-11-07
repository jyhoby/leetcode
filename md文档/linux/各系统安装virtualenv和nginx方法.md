### 1.ubuntu安装virtualenv 

#### 1.1 ubuntu安装pip		

```
【请使用普通用户】
a. 查看pip版本
查看pip版本: pip ‐V
查看pip3版本: pip3 ‐V
b. 安装pip(如果存在则不需要安装)
安装pip3: apt install python3‐pip
安装pip2: apt install python‐pip
c. 更新pip
更新pip (如果pip版本高于9.0则不需要更新):
更新pip3: pip3 install --upgrade pip
更新pip: pip install --upgrade pip

```

```
注意: 更新后如出现以下错误（这是pip 10.0.0版本的BUG）：
	Traceback (most recent call last):
	File “/usr/bin/pip”, line 9, in
	from pip import main
解决方法：修改对应pip文件中的代码(pip和pip3类似)
	例如更新pip时报错则需要修改 /usr/bin/pip 文件中的代码，
	使用: sudo vim /usr/bin/pip 打开pip文件
将：
	from pip import main
	if __name__ == '__main__':
		sys.exit(main())
	改成：
	from pip import __main__
	if __name__ == '__main__':
		sys.exit(__main__._main())

```

```
 让pip默认使用python3, 执行命令：
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
```

#### 1.2 ubuntu下virtualenv和virtualenvwrapper 的安装和使用

```
1.3, virtualenv和virtualenvwrapper 的安装和使用
【请使用普通用户】
a. 安装虚拟环境
sudo apt update
sudo pip3 install virtualenv virtualenvwrapper
安装后如果不能使用虚拟环境命令，则需要配置环境变量：
1,进入家目录: cd ~
2, 使用vim打开 .bashrc
3,定位到最后:shift+g，并添加以下2行代码(注意修改自己Ubuntu的用户名)

export WORKON_HOME=/home/自己Ubuntu的用户名/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh 

在家目录创建.virtualenvs目录: mkdir .virtualenvs
加载修改后的设置，使之生效：source .bashrc


```

#### 创建虚拟环境:

```
 	mkvirtualenv env
 	mkvirtualenv env2 ‐p /usr/bin/python3 (指定python路径)
```

#### 退出虚拟环境: 

```
	deactivated
```

#### 进入虚拟环境: 

```
	workon 虚拟环境名称
```

#### 删除虚拟环境:

```
	 rmvirtualenv env
```



### 2.windows下安装virtualenv

```
2.1,安装和创建virtualenv
a,安装虚拟环境：
	pip install virtualenv
				
b,创建虚拟环境：
	virtualenv 虚拟环境名称 [-p python版本的路径]
	如：virtualenv env1 
	如：virtualenv env1 -p C:\Python36\python.exe

```

#### 启动虚拟环境:

```
	进入Script文件夹下：
	activate
```

​		

#### 退出虚拟环境：

```
	(进入真实系统环境): 
	deactivate  
	(如果报错则使用:env1\Scripts\deactivate)
```

#### 2.1 virtualenvwrapper 的安装和使用  

（virtualenvwrapper是virtualenv的包装版，以后用这个，更加方便）
	

	Windows: pip install virtualenvwrapper-win
	(Linux：pip install virtualenvwrapper)
	
	创建:mkvirtualenv    虚拟环境名称  -p  python的路径 
	删除:rmvirtualenv    虚拟环境名称
	(注意：创建的虚拟环境放在用户目录下的Envs中)
	
	进入:workon 虚拟环境名称
	退出:deactivate 
	使用方法和linux下是一样的


### 3.安装nginx

      在虚拟机和腾讯云中安装nginx
    1，访问：http://nginx.org/en/linux_packages.html
    2，点击'this key' 查看官网提供的公钥, 并在Ubuntu下载这个公钥：
    	wget http://nginx.org/keys/nginx_signing.key
    3，添加key: 
    	apt-key add nginx_signing.key
    4, 进入/etc/apt/sources.list文件：
    	vim /etc/apt/sources.list
          并在最后添加软件包源: 
    	deb http://nginx.org/packages/ubuntu/ xenial nginx
    	deb-src http://nginx.org/packages/ubuntu/ xenial nginx
    5，更新：apt update
    6，安装nginx：apt install nginx
    7，启动nginx: nginx
    8, 在浏览器访问nginx服务器，查看是否安装好nginx
### 

### 4.导出导入虚拟环境的包

#### 导入:

```
pip freeze > a.txt(文件名自己定义)
```

#### 导出：

```
pip install -r a.txt （要进入a.txt目录下和workon进入虚拟环境下）
```

