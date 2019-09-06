



### Docker的基本组成

- Docker Client 客户端
- Docker Daemon 守护进程
- Docker Image 镜像：docker镜像运行之后编程容器(docker run ...)
- Docker Container 容器
- Docker Registry 仓库: docker镜像的中央存储仓库（pull / push）

```
sudo apt install containerd
sudo apt-get install docker.io		# 版本低 ，不建议

whereis curl		# 有则不需要案子curl, 无 则 sudo apt-get install -y curl
curl -SSL https://get.docker.com/ | sudo sh

sudo groupadd docker 				# 添加docker名字的用户组
sudo gpasswd -a klaus docker		 # 将klaus用户添加到 docker 用户组
sudo service docker restart			# 重启docker服务，然后注销用户即可使用非root用户
```

command:
	ctrl + p, q: 退出容器且保持后台运行

```
# docker启动命令,docker重启命令,docker关闭命令
启动        systemctl start docker
守护进程重启   sudo systemctl daemon-reload
重启docker服务   systemctl restart  docker
重启docker服务  sudo service dcker restart
关闭docker   service docker stop   
关闭docker  systemctl stop docker
```

```
# 创建本地镜像
docker build -t <image_name>[:<image_tag>] .  
!!!  命令行最后的dot "." 一定不能少  !!!
	--tag, -t: 镜像的名字及标签，通常 name:tag 或者 name 格式；可以在一次构建中为一个镜像设置多个标签。
	-f :指定要使用的Dockerfile路径
	eg.:
		docker build -t runoob/ubuntu:v1 . 
		docker build -f /path/to/a/Dockerfile .

# 创建容器：docker run 之后生成container
docker run -i:   # 以交互模式运行容器，通常与 -t 同时使用；
		  -t: 	# 为容器重新分配一个伪输入终端，通常与 -i 同时使用
		  -d: 	# 后台运行容器，并返回容器ID
		  -p: 	# （小写）指定端口映射，格式为：主机(宿主)端口:容器端口
		  -P:	# （大写）随机端口映射，容器内部端口随机映射到主机的高端口 
		  --name="nginx-lb": 为容器指定一个名称
		  --volume , -v: 绑定一个卷 -v host_dir:container_dir
docker run -d -p 2222:22 --name base csphere/centos:7.1

# 查看容器
docker ps [OPTIONS]
    -a :显示所有的容器，包括未运行的。
    -f :根据条件过滤显示的内容。
    --format :指定返回值的模板文件。
    -l :显示最近创建的容器。
    -n :列出最近创建的n个容器。
    --no-trunc :不截断输出。
    -q :静默模式，只显示容器编号。
    -s :显示总的文件大小。
    
# 在运行的容器中执行命令  docker exec 
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
	-d :分离模式: 在后台运行
    -i :即使没有附加也保持STDIN 打开
    -t :分配一个伪终端
    eg.:
    	# 1) 在容器 mynginx 中开启一个交互模式的终端:
    	runoob@runoob:~$ docker exec -i -t  mynginx /bin/bash	
	    root@b1a0703e41e7:/#
	    # 2) 在容器 mynginx 中以交互模式执行容器内 /root/runoob.sh 脚本:
	    runoob@runoob:~$ docker exec -it mynginx /bin/sh /root/runoob.sh
		http://www.runoob.com/	
```



















