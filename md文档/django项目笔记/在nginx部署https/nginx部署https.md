## 1.把下载的证书放到新建的cert文件夹内，将cert放置项目文件夹下--同级

![Snipaste_2019-07-27_11-12-52](.\Snipaste_2019-07-27_11-12-52.png)

![Snipaste_2019-07-27_11-14-23](.\Snipaste_2019-07-27_11-14-23.png)

## 2.配置nginx.conf文件

```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;
  	server {
   		listen 80;	
		server_name www.jyhoby.top 104.199.215.233;	#监听80端口所有域名和ip的请求
		charset utf-8;
		rewrite ^(.*)$ https://www.jyhoby.top$1 ; # 重定向到https的地址	
	}
	
	server{
		listen 443 ssl; # 监听443端口并开启ssl
		server_name www.jyhoby.top;  # localhost修改为您证书绑定的域名。
		charset utf-8;
		
		#ssl on;   #设置为on启用SSL功能。
		#root html;
		#index index.html index.htm;
		ssl_certificate cert/2392619.pem;   #将domain name.pem替换成您证书的文件名。
		ssl_certificate_key cert/2392619.key;   #将domain name.key替换成您证书的密钥文件名。
		ssl_session_timeout 5m;
		#ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;  				#使用此加密套件。
		#ssl_protocols TLSv1 TLSv1.1 TLSv1.2;   #使用该协议进行配置。
		#ssl_prefer_server_ciphers on; 

		location /static {
				alias /var/www/Moonbasa/static/; #设置为项目的静态文件夹
			}
		location / {
				include /etc/nginx/uwsgi_params;
				uwsgi_pass localhost:8010;  # uwsgi配置8010端口
			}			
    		}
	
	include /etc/nginx/conf.d/*.conf;
}

```

重启 nginx：

```
nginx -s stop
配置并运行：nginx -c /var/www/Moobasa/nginx.conf
/var/www/Moobasa/nginx.conf为配置文件的绝对路径
```

重载：

```
nginx -s reload
```

## 3.uwsgi配置

uwsgi.ini

```
[uwsgi]
# 使用nginx连接时 使用
socket=127.0.0.1:8010
# 直接作为web服务器使用
#http=127.0.0.1:8010
# 配置工程目录
chdir=/var/www/Moonbasa
# 配置项目的wsgi目录。相对于工程目录
wsgi-file=Moonbasa/wsgi.py

#配置进程，线程信息
processes=4
threads=2
enable-threads=True
master=True
pidfile=uwsgi.pid
daemonize=uwsgi.log
```

启动uwsgi服务

```
uwsgi --ini uwsgi.ini
```

关闭：

```
ps -ef | grep uwsgi : 查看进程
kill -9 5563 : 关闭进程(5563为进程号)
```

