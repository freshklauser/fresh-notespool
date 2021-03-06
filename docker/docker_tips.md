本文内容

[TOC]

# 一、Docker基础

- Docker Client 客户端
- Docker Daemon 守护进程
- Docker Image 镜像：docker镜像运行之后编程容器(docker run ...)
- Docker Container 容器
- Docker Registry 仓库: docker镜像的中央存储仓库（pull / push）

## 1、Docker安装(ubuntu)和启动

### 1. Docker安装

[`refer1: Get Docker Engine - Community for Ubuntu`](<https://docs.docker.com/install/linux/docker-ce/ubuntu/>)
[`refer2:Docker快速安装以及换镜像源`](<https://www.jianshu.com/p/34d3b4568059>)

- 方法1：

```
# 推荐ubuntu系统安装docker方式  具体参考refer1的官方文档
# 1. 如果存在旧版本docker，先按此方法卸载
sudo apt-get remove docker docker-engine docker.io containerd runc
# 2. Install using the repository
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
# 3. Add Docker’s official GPG key：确认所下载软件包的合法性，需添加软件源的`GPG`密匙
# 官方：curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -	# 中科大源的密匙
# 4. 向 source.list 中添加 Docker 软件源
# 官方：第二行用 "deb [arch=amd64] https://download.docker.com/linux/ubuntu \  替换
sudo add-apt-repository \
    "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
        # 忘了下面两行代码是什么情况下执行的		
        # whereis curl		# 有则不需要案子curl, 无 则 sudo apt-get install -y curl
        # curl -SSL https://get.docker.com/ | sudo sh
# 5. 安装 Docker CE： 更新 apt 软件包缓存，并安装 docker-ce
sudo apt-get update
sudo apt-get install docker-ce
# 6. 测试 Docker 是否安装正确
docker run hello-world		# 无权限则加　sudo

# 卸载
sudo apt-get remove docker-ce
```

- docker无权限，如何赋予管理员权限，避免每次使用sudo [`refer`](https://blog.csdn.net/u013948858/article/details/78429954)

```
cat /etc/group | grep docker # 查找 docker 组，确认其是否存在
>>> docker:x:999:			 # docker组已存在  

groups # 列出自己的用户组，确认自己在不在 docker 组中
>>> klaus adm cdrom sudo dip plugdev lpadmin sambashare

# 如果 docker 组不存在，则添加之：（已存在，可省略）
sudo groupadd docker
>>> groupadd：“docker”组已存在

# 将当前用户 klaus 添加到 docker 组
sudo gpasswd -a klaus docker
>>> 正在将用户“klaus”加入到“docker”组中

# 检查用户是否加入
cat /etc/group | grep docker
>>> docker:x:999:klaus		# klaus加入到了docker组中，此时直接docker 仍是无权限

# 重启服务，以便让 klaus　的权限生效
sudo service docker restart

# 如果提示如下错误：
    Server:
    ERROR: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/info: dial unix /var/run/docker.sock: connect: permission denied
    errors pretty printing info
 ---> 则修改 /var/run/docker.sock 权限
sudo chmod a+rw /var/run/docker.sock
docker info
>>> ......  # ok

# ------- 以下为另一个人的解决方法，尝试了下不起作用 ------------
# 切换一下用户组（刷新缓存）
newgrp - docker;
newgrp - `groups ${USER} | cut -d' ' -f1`; # TODO：必须逐行执行，不知道为什么，批量执行时第二条不会生效
# 或者，注销并重新登录
pkill X
```

- 方法2：

```
在测试或开发环境中 Docker 官方为了简化安装流程，提供了一套便捷的安装脚本，Ubuntu 系统上可以使用这套脚本安装：
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
执行这个命令后，脚本就会自动的将一切准备工作做好，并且把 Docker CE 的 Edge 版本安装在系统中。
```

### 2. 镜像加速

- 官方镜像加速：http://www.docker-cn.com/registry-mirror

- 国内镜像加速：

  中科大镜像：https://docker.mirrors.ustc.edu.cn
  `Azure`中国镜像： https://dockerhub.azk8s.cn
  七牛加速器：https://reg-mirror.qiniu.com
  `daocloud`镜像：https://get.daocloud.io/daotools/set_mirror

### 3. docker换镜像源

配置方法：
	新版的 Docker 使用` /etc/docker/daemon.j:son（Linux）`` 或者 %programdata%\docker\config\daemon.json（Windows） `来配置` Daemon`。
	请在该配置文件中加入下列代码（没有该文件的话，请先建一个）：
	`{"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]}`
亦即：$~ sudo vim /etc/docker/daemon.json  写入：

```
sudo vim /etc/docker/daemon.json
# 写入以下内容，然后重启docker服务即可 （中科大的源镜像）
{"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]}
```

### 4. 启动Docker CE

```
# 方法1安装好后貌似不需要这两步，方法2没试过  （centos系統中需要）
sudo systemctl enable docker
sudo systemctl start docker
```

### 5. 建立 docker 用户组

```
# 添加用户组
sudo groupadd docker 				# 添加docker名字的用户组
sudo gpasswd -a klaus docker		 # 将klaus用户添加到 docker 用户组
sudo service docker restart			# 重启docker服务，然后注销用户即可使用非root用户
```

### 6. 启动和关闭docker命令	

```
# docker启动命令,docker重启命令,docker关闭命令
启动        systemctl start docker
守护进程重启   sudo systemctl daemon-reload
重启docker服务   systemctl restart  docker
重启docker服务  sudo service dcker restart
关闭docker   service docker stop   
关闭docker  systemctl stop docker
```

## 2、日常docker命令

### 1. 创建镜像

1、从仓库拉取创建镜像

```
# 创建镜像（从仓库拉取）
docker pull python:3.6	
# 拉取aspnetcore的sdk和runtime环境
docker pull  microsoft/dotnet:2.2-sdk
docker pull  microsoft/dotnet:2.2-aspnetcore-runtime
```

2、利用`Dockerfile`文件创建镜像

```
# 创建本地镜像(利用Dockerfile文件创建)
docker build -t <image_name>[:<image_tag>] .  
!!!  命令行最后的dot "." 一定不能少 , 表示在当前文件夹中查找dockerfile !!!
	--tag, -t: 镜像的名字及标签，通常 name:tag 或者 name 格式；可以在一次构建中为一个镜像设置多个标签。
	-f :指定要使用的Dockerfile路径
	eg.:
		docker build -t runoob/ubuntu:v1 . 
		docker build -f /path/to/a/Dockerfile .
```

### 2. 删除镜像

```
# 删除镜像
docker rmi <image_id or tag>
# 删除虚悬镜像
docker rmi [-f] $(docker images -f "dangling=true" -q)   # [-f] 可选，强制删除
# 批量清理临时镜像文件
docker image prune -a -f  # 也可以
```

### 3. 镜像下创建容器及容器相关操作

```
# 在镜像下创建容器（新建并启动container）：docker run 之后生成container
docker run -i:   # 以交互模式运行容器，通常与 -t 同时使用；
		  -t: 	# 为容器重新分配一个伪输入终端，通常与 -i 同时使用
		  -d: 	# 后台运行容器，并返回容器ID
		  -p: 	# （小写）指定端口映	射，格式为：主机(宿主)端口:容器端口
		  -P:	# （大写）随机端口映射，容器内部端口随机映射到主机的高端口 
		  --name="nginx-lb": 为容器指定一个名称
		  --volume , -v: 绑定一个卷 -v host_dir:container_dir
		  --rm  # Automatically remove the container when it exits(容器存在的话自动删除原容器再重新创建，即覆盖)
docker run -d -p 2222:22 --name base csphere/centos:7.1
# 交互模式在continuumio/anaconda3镜像下创建容器(命名：ananconda3)并进入容器
docker run -it --name anaconda3 continuumio/anaconda3
# 退出后重新进入容器，并进入anaconda3环境bash环境
docker start anaconda3
docker exec -it anaconda3 /bin/bash
# 退出容器且保持后台运行： ctrl + p, q


# 重新启动一个已停止的容器
docker container start <container ID or NAMES>
# 终止运行中的容器
docker container stop <container ID or NAMES>
# 将一个运行态的容器终止，然后再重新启动
docker container restart <container ID or NAMES>

# 查看容器
docker container ls  # 查看正在运行的容器  docker ps 
docker ps [OPTIONS]
    -a :显示所有的容器，包括未运行的。
    -f :根据条件过滤显示的内容。
    --format :指定返回值的模板文件。
    -l :显示最近创建的容器。
    -n :列出最近创建的n个容器。
    --no-trunc :不截断输出。
    -q :静默模式，只显示容器编号。
    -s :显示总的文件大小。
 # 查看容器自身的信息
 docker inspect <container ID or NAMES>
 # 获取容器的输出日志信息
 docker container logs <container ID or NAMES>
    
# 进入容器，在运行的容器中执行命令  docker exec 
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
		
# 删除容器
docker rm <container_id or tag>
# 删除容器同时删除挂载的数据卷
docker rm -v docker rm <container_id or tag>
# 清理所有处于终止状态的容器
docker container prune

# docker容器与宿主机之间传输文件
# See 'docker cp --help'.
Usage:  docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
	docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH
Copy files/folders between a container and the local filesystem
eg.:
	# 宿主主机文件发送到docker容器中
 	sudo docker cp lock_problem.sh 1f1825ced322:/home/
	# docker容器中文件发送到宿主主机中
	sudo docker cp 1f1825ced322:/home/testfiletra.txt /home/Jun/
```

### 4. Docker镜像迁移

将Docker 放置到其他机器运行很简单，直接保存镜像，然后复制镜像到其他机器，然后使用docker 命令load 既可。

```
docker save dockerapi/tgdataflow > tgdataflow.tar 	# 将镜像保存为tar压缩文件
```

将`tgdataflow.tar`复制到其他机器中，然后加载命令：

```
docker load < tgdataflow.tar

# 若有挂载，先新建挂载目录
```

然后就可以使用`docker run` 运行程序了，无需关心程序需要哪些依赖。

## 3、创建Dockerfile文件

[`refer: 中文官方文档--Dockerfile介绍 `](<http://www.dockerinfo.net/dockerfile%e4%bb%8b%e7%bb%8d>)

<div align=center><img src='./img/dockerfile.png' width=80%></div>
<div align=center><img src='./img/dockerfile1.png' width=80%></div>
- **docker的层级结构**

<div align=center><img src='./img/layers.png' width=80%></div>
其中，`Image Layers`层的 `source code`不能修改，如果想不改变该层的内容的基础上，创建区别于`source code`的`container`如改变`Image Layers`中的`app.py`创建不同的python依赖包，可以直接在`Container Layer`层重新建立并修改`app.py`来建立容器；除此之外，就只能通过重新`build`  `Image Layers`层来实现。如下：

<div align=center><img src='./img/layers1.png' width=80%></div>
## 4、Docker 容器数据卷

### 1. 数据卷

数据卷 是一个可供一个或多个容器使用的特殊目录，它绕过 UFS，可以提供很多有用的特性：

- 数据卷 可以在容器之间共享和重用;
- 对 数据卷 的修改会立马生效
- 对 数据卷 的更新，不会影响镜像
- <font color=coral>数据卷 默认会一直存在，即使容器被删除</font>

注意：数据卷 的使用，类似于 Linux 下对目录或文件进行 mount，镜像中的被指定为挂载点的目录中的文件会隐藏掉，能显示看的是挂载的 数据卷。

### 2. 常用命令

####  1）创建和查询数据卷

```
# 创建一个数据卷
docker volume create my-vol
# 查看所有的 数据卷
docker volume ls
# 查看指定 数据卷 的信息
docker volume inspect my-vol
>>>
    [
        {
            "CreatedAt": "2019-09-19T01:19:02-07:00",
            "Driver": "local",
            "Labels": {},
            "Mountpoint": "/var/lib/docker/volumes/my-vol/_data", # 挂载点
            "Name": "my-vol",
            "Options": {},
            "Scope": "local"
        }
    ]
```

#### 2）启动挂载带有数据卷的容器
在用 docker run 命令的时候，使用 --mount 标记来将 数据卷 挂载到容器里。在一次 docker run 中可以挂载多个 数据卷。

```
$ docker run -d -p 8080:8080 \
    --name web \
    --mount source=my-vol,target=/webapp \
    training/webapp \
    python app.py
>>> 数据卷信息里面的"Mounts"的  "Type":"volumn"
    
# 也可直接挂载在主机的目录下，如下：
$ docker run -d -p 8080:8080 \
    --name web \
    --mount type=bind,source=my-vol,target=/webapp \
    training/webapp \
    python app.py
>>> 数据卷信息里面的"Mounts"的  "Type":"bind"
```

#### 3）删除数据卷

```
# 删除数据卷
docker volume rm my-vol
# 清理无主的数据卷
docker volume prune
```

​		数据卷 是被设计用来**持久化数据**的，它的生命周期**独立于容器**，**Docker 不会在容器被删除后自动删除 数据卷，并且也不存在垃圾回收这样的机制来处理没有任何容器引用的 数据卷**。如果需要在删除容器的同时移除数据卷。可以在删除容器的时候使用 docker rm -v 这个命令。

### 3. 修改容器挂载

- 方式一：修改配置文件（需停止docker服务）

  ```
  # 1、停止docker服务 （关键，修改之前必须停止docker服务）
  systemctl stop docker.service
  # 2、修改配置文件中的目录位置，然后保存退出
  vim /var/lib/docker/containers/container-ID/config.v2.json
    # 内容如下：
   "MountPoints":{"/home":{"Source":"/docker","Destination":"/home","RW":true,"Name":"","Driver":"","Type":"bind","Propagation":"rprivate","Spec":{"Type":"bind","Source":"//docker/","Target":"/home"}}}
  
  ```

  



## 4、Docker 网络配置

### 1. 外部访问容器

#### 1) 端口映射及说明

启动容器时，使用 -P 或 -p 参数来制定端口映射

（1）`-P:`随机映射一个 `49000~49900` 的端口到内部容器开放的网络端口

（2）`-p:`手动指定主机端口映射容器端口 ， 在一个指定端口上只可以绑定一个容器，可以多次使用`-p`来绑定多个端口
	支持的格式有` ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort`

```
$ docker run -d \
    -p 5000:5000 \
    -p 3000:80 \
    training/webapp \
    python app.py
```

- **映射所有接口地址**

使用<font color=coral> `hostPort:containerPort `</font>格式本地的 5000 端口映射到容器的 5000 端口，可以执行

```
docker run -d -p 5000:5000 training/webapp python app.py
```

此时默认会绑定本地所有接口上的所有地址

- **映射到指定地址的任意端口**

使用 <font color=coral> `ip::containerPort `</font>绑定 localhost 的任意端口到容器的 5000 端口，本地主机会自动分配一个端口。

```
docker run -d -p 127.0.0.1::5000 training/webapp python app.py
# 使用 udp 标记来指定 udp 端口
docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
```

- **映射到指定地址的指定端口**

可以使用<font color=coral>` ip:hostPort:containerPort`</font> 格式指定映射使用一个特定地址

```
docker run -d -p 192.168.1.152:5000:5000 training/webapp python app.py
```

#### 2）查看容器端口信息及端口映射配置

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                              NAMES
a2693e99c896        training/webapp     "python app.py"     35 minutes ago      Up 35 minutes       5000/tcp, 0.0.0.0:8080->8080/tcp   web
```

```
$ docker logs -f -t web
2019-09-19T08:53:15.617440593Z  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

# docker logs --help:
Options:
      --details        Show extra details provided to logs
  -f, --follow         Follow log output
      --since string   Show logs since timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes)
      --tail string    Number of lines to show from the end of the logs (default "all")
      
  -t, --timestamps     Show timestamps
      --until string   Show logs before a timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes)
```

```
$ docker port web
8080/tcp -> 0.0.0.0:8080
```

### 2. 容器互联

#### 1）新建网络 及 docker network 命令

```
$ docker network create -d bridge my-net    
c85934fbfefafdf59df269696db88bfb71ac5dfd37c2104321153f6d7d6f2224
```

​	其中，参数 `-d` 指定 `Docker`网络类型，有 bridge(常用)  overlay。其中 overlay 网络类型用于 Swarm mode

- `docker network` 命令

  ```
  $ docker network
  
  Manage network
  Commands:
    connect     Connect a container to a network
    create      Create a network
    disconnect  Disconnect a container from a network
    inspect     Display detailed information on one or more networks
    ls          List networks
    prune       Remove all unused networks
    rm          Remove one or more networks
  ```

#### 2）连接容器

创建镜像： `docker pull busybox`

1. terminal 1中运行一个容器如下，并连接到新建的 my-net 网络:

```
$ docker run -it --rm --name busybox1 --network my-net busybox
/ # ifconfig
/ # ...... ip1 address ......
/ # 
```

2. terminal 2中运行一个容器如下，并连接到新建的 my-net 网络:

```
$ docker run -it --rm --name busybox2 --network my-net busybox
/ # ifconfig
/ # ...... ip2 address ......
/ # 
```

3. terminal 3中 查看运行中的container, 两个容器都在运行中

```
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
67bd42758cf4        busybox             "sh"                52 seconds ago       Up 51 seconds                           busybox2
9c10317c7246        busybox             "sh"                About a minute ago   Up About a minute                       busybox1
```

4. 测试容器 `busybox1`和 `busybox2`是否建立互联关系

   方式：ping 对方容器的ip （均能 ping 通，说明 busybox1 容器和 busybox2 容器建立了互联关系）

```
# terminal 1中：
ping <ip2>
# terminal 2中
ping <ip1>
```

多个容器互联，可以采用 `docker compose` ：[`refer here`](https://yeasy.gitbooks.io/docker_practice/content/compose/)

#### 3）配置DNS

暂略

## 5、docker项目

笔记参考目录 <font color=coral>`./docker_couse/Docker 系列基础教程(五).html`</font>

### 1. [compose](https://yeasy.gitbooks.io/docker_practice/content/compose/introduction.html) 

#### 1）安装  二进制包

```
# sudo无 /etc/local/bin/的权限
$ sudo su root
$ curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
$ chmod +x /usr/local/bin/docker-compose

$ `ctrl+D`退出root账户
$ docker-compose -v
docker-compose version 1.24.1, build 4667896b
```

#### 3）卸载

二进制安装的只需要删除二进制文件即可

```
$ sudo rm /usr/local/bin/docker-compose
```

### 2. Django

#### 1）Dockerfile 文件创建

```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```

​		其中， `pip install -r requirements.txt`中的`-r`表示 `Install from the given requirements file.`

#### 2）requirements.txt文件指定python选择的依赖包、

```
Django>=2.0,<3.0
psycopg2>=2.7,<3.0
```

#### 3）docker-compose.yml 文件创建 

 [`docker-compose.yml`](https://yeasy.gitbooks.io/docker_practice/content/compose/compose_file.html#links)文件将把所有的东西关联起来。它描述了应用的构成（一个 web 服务和一个数据库）、使用的 Docker 镜像、镜像之间的连接、挂载到容器的卷，以及服务开放的端口。

```
version: "3"
services:

  db:
    image: postgres

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    links:
      - db
```

### 3. mysql

#### 1）docker创建数据库，并本地挂载

```
# 创建docker容器，挂载到本地 source宿主机中数据存储path, target容器中的数据储存path
docker run -d -e MYSQL_ROOT_PASSWORD=spindle123456 -p 3306:3306 --mount type=bind,source=/opt/mysql/data/db,target=/var/lib/mysql/ --name mysql_v1 mysql

# 容器内启动mysql
docker exec -it mysql_v1 bash
root@f04cf8aad026:/# mysql -uroot -pspindle123456		# 容器内进入mysql
mysql> SHOW VARIABLES LIKE 'datadir'				   # 查看容器内 mysql 的数据存放位置
        +---------------+-----------------+
        | Variable_name | Value           |
        +---------------+-----------------+
        | datadir       | /var/lib/mysql/ |
        +---------------+-----------------+
        1 row in set (0.01 sec)
```

#### 2）数据库操作：

```
1、以管理员身份登录mysql
mysql -u root -p

2、选择mysql数据库
use mysql

3、创建用户并设定密码
create user 'testuser'@'localhost' identified by 'testpassword'

4、使操作生效
flush privileges

5、为用户创建数据库
create database testdb

6、为用户赋予操作数据库testdb的所有权限
--> GRANT privileges ON databasename.tablename TO 'username'@'host'
    说明:
    privileges：用户的操作权限，如SELECT，INSERT，UPDATE等，如果要授予所的权限则使用ALL
    databasename：数据库名
    tablename：表名，如果要授予该用户对所有数据库和表的相应操作权限则可用*表示，如*.*
grant all privileges on testdb.* to test@localhost identified  by '1234'

7、使操作生效
flush privileges

8、用新用户登录
mysql -u test -p


mysql> grant ALL ON *.* TO klaus;
mysql> show grants for klaus;
mysql> select host,user from mysql.user;
+-----------+------------------+
| host      | user             |
+-----------+------------------+
| %         | klaus            |
| %         | root             |
| localhost | mysql.infoschema |
| localhost | mysql.session    |
| localhost | mysql.sys        |
| localhost | root             |
+-----------+------------------+
6 rows in set (0.00 sec)
```

### 4 MongoDb

#### 1）数据库操作

- 启动服务和停止服务

```
# 启动服务  本地服務
mongod --dbpath  /home/u1/mongodb/data  [--logpath  /home/u1/mongodb/log/logs  --fork --auth]
# 停止服务 ： 必须进入admin数据库后停止
user admin
db.shutdownServer()

# 连接远程mongodb
> mongo 192.168.1.215:27017/admin -u <account> -p <password> # 授权登录并进入admin数据库

use admin
db.auth("spindle","spindle123456")

> use runoob
switched to db runoob
> db.createCollection("runoob")     # 先创建集合，类似数据库中的表
> show tables
runoob
>show collections
mycol
system.indexes
runoob
>db.runoob.find().pretty()
...
> db.runoob.drop()
true
> db.dropDatabase()

```

 	mongo服务启动必须要指定文件存放的目录dbpath,--fork以守护进程运行，如果带—fork参数则必须要指定—logpath即日志存放的位置（指定文件不是文件夹）

- MongoDB 连接

```
# 标准 URI 连接语法：
mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
    mongodb:// 这是固定的格式，必须要指定。
    username:password@ 可选项，如果设置，在连接数据库服务器之后，驱动都会尝试登陆这个数据库
    host1 必须的指定至少一个host, host1 是这个URI唯一要填写的。它指定了要连接服务器的地址。如果要连接复制集，请指定多个主机地址。
    portX 可选的指定端口，如果不填，默认为27017
    /database 如果指定username:password@，连接并验证登陆指定数据库。若不指定，默认打开 test 数据库。
    ?options 是连接选项。如果不使用/database，则前面需要加上/。所有连接选项都是键值对name=value，键值对之间通过&或;（分号）隔开	
    
# 使用用户名fred，密码foobar登录localhost的baz数据库。
mongodb://fred:foobar@localhost:27017/baz
```



#### 2）远程身份认证

- shell中：本地连接远程mongodb，一定要先切换到admin数据库，再使用身份认证

```
C:\Users\Wang> mongo 192.168.1.215:27017/
...
> use admin
switched to db admin
> db.auth("klaus","111111")
1
> show dbs
...

# 或者
 C:\Users\Wang> mongo 192.168.1.215:27017/admin -u <account> -p <password>
 				     <ip>        <port> <admin数据库> <账号和密码,密码可隐式输入即enter后再输入>
```

- .net core webapi中"ConnectionString": "mongodb://localhost:27017", 参数设置格式

```
# 标准URL连接语法：
mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
# 如下

```



#### 3）设置宿主机ip访问(windows下没成功，linux下没试，docker中-p就行)

- 安装mongodb后若只能使用`localhost`或者`127.0.0.1`登录，本地和远程均无法使用`宿主机ip`登录，则需设置`mongod.cfg`文件,如下：

```
# network interfaces
net:
  port: 27017
  # =====================改这里===========================
  bindIp: 0.0.0.0
#processManagement:
# =====================改这里===========================
#security:
security:
	authorization: enabled
```

​	`windows`下试了没成功，docker中不需要这样设置，在创建容器时指定-p就可以.

#### 4）docker创建mongodb的镜像和容器：pull方法

```
[centos@localhost ~]$ docker pull mongo

[centos@localhost ~]$ docker run -d --name mongodb -p 27017:27017 -v /opt/mongodatastore/mongodb:/data/db mongo --auth
27de52998cd6d776b68d663ae69ea1a3eec000b1b44ea8b188105294710a9c45

[centos@localhost ~]$ docker exec -it mongodb mongo admin
MongoDB shell version v4.2.1
connecting to: mongodb://127.0.0.1:27017/admin?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("b0a7bc35-b54c-4f20-9d33-5fd94b46d417") }
MongoDB server version: 4.2.1

> db.createUser({user:"spindle", pwd:"spindle123456", roles:["userAdminAnyDatabase", "dbAdminAnyDatabase", "readWriteAnyDatabase"]});
Successfully added user: {
	"user" : "admin",
	"roles" : [
		"userAdminAnyDatabase",
		"dbAdminAnyDatabase",
		"readWriteAnyDatabase"
	]
}

```



## 6 docker-compose.yml创建

```
sudo curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose

$ sudo chmod +x /usr/local/bin/docker-compose
```

`Docker Compose` 是 Docker 官方编排（Orchestration）项目之一，负责快速的**部署分布式应用**

```
docker-compose up  启动服务
docker-compose up -d  后台启动服务
docker-compose down   卸载服务（容器也会被删除）
docker-compose logs  当后台启动服务的时候，可以使用这种方式查看日志
```



## 7 Dockerfile 与 docker-compose.yml

​	<font color=coral>Dockerfile 记录单个镜像的构建过程， docker-compse.yml 记录一个项目(project, 一般是多个镜像)的构建过程。</font>

​	dockerfile的作用是从无到有的构建镜像。它包含安装运行所需的环境、程序代码等。这个创建过程就是使用 dockerfile 来完成的。Dockerfile - 为 docker build 命令准备的，用于建立一个独立的 image ，在 docker-compose 里也可以用来实时 build。
​	docker-compose.yml 是为 docker-compose 准备的脚本，可以同时管理多个 container ，包括他们之间的关系、用官方 image 还是自己 build 、各种网络端口定义、储存空间定义等。
​	docker-compose是编排容器的。例如，你有一个php镜像，一个mysql镜像，一个nginx镜像。如果没有docker-compose，那么每次启动的时候，你需要敲各个容器的启动参数，环境变量，容器命名，指定不同容器的链接参数等等一系列的操作，相当繁琐。而用了docker-composer之后，你就可以把这些命令一次性写在docker-composer.yml文件中，以后每次启动这一整个环境（含3个容器）的时候，你只要敲一个docker-composer up命令就ok了。
















# 二、windows环境下 webapi部署到 虚拟机的ubuntu系统的docker中

[`refer here`](https://www.cnblogs.com/daxnet/p/5782019.html)

1) 将ASP.NET Core Web API应用程序编译成Docker Image
	首先，进入项目根目录（也就是包含有project.json文件的这个目录），使用dotnet publish命令发布应用程序。这就会把编译后的DLL连同依赖项一起，全部复制到bin/Debug/netcoreapp1.0/publish目录下。此时，使用WinSCP类似的软件，将该目录下的所有内容全部复制到Ubuntu的机器上（当然，如果是在Windows 10下使用Docker，也就不需要这个复制的步骤）。复制完成后，在Ubuntu系统中可以看到所有的这些文件.

2) 在这个包含有DockerWebAPI.dll文件的目录下，新建一个Dockerfile文件，使用vim或者nano等文本编辑器，输入以下内容（#开头的行为注释行，可以不输入）：

```
# 基于microsoft/dotnet:latest构建Docker Image
FROM microsoft/dotnet:latest
 
# 进入docker中的/usr/local/src目录
RUN cd /usr/local/src
 
# 创建DockerWebAPI目录
RUN mkdir DockerWebAPI
 
# 设置工作路径
WORKDIR /usr/local/src/DockerWebAPI
 
# 将当前文件夹下的所有文件全部复制到工作目录
COPY *.* ./
 
# 向外界暴露5000端口
EXPOSE 5000
 
# 执行dotnet xxxx.dll命令
CMD ["dotnet", "tgproApi.dll"]
```

3) 在当前目录下，创建dotnet的Doker镜像：

```
docker build -t klaus/docker-webapi .
```

4) 在3中创建的镜像下 docker run 生成容器

```
docker run -it -p 8080:5000 klaus/docker-webapi
```

- -it参数表示需要提供一个模拟的shell环境，并要求有用户交互功能，这样当我们按下Ctrl+C的时候，就可以停止我们的应用程序
- -p 8080:5000参数表示需要将Docker Container的5000端口映射到主机环境的8080端口，也就是客户端可以直接通过8080端口访问我们的应用程序
   - daxnet/docker-webapi参数指定了需要运行的Docker Image。此处采用默认的latest标签

# 三、ASP.NET Core开发-Docker部署运行

## 演示案例：demo

### demo创建和ubuntu测试

- `windows`系统下用`vs`或`dotnet`命令创建`webapi`的`demo`，创建好后，在`Program.cs`中添加`UseUrls("http://*:5000")`（ubuntu中能够使用ip访问的关键）, 代码如下：

  ```
  using System;
  using System.Collections.Generic;
  using Microsoft.AspNetCore;
  using Microsoft.AspNetCore.Hosting;
  
  namespace demoApi
  {
      public class Program
      {
          public static void Main(string[] args)
          {
              CreateWebHostBuilder(args).Build().Run();
          }
  
          public static IWebHostBuilder CreateWebHostBuilder(string[] args) =>
              WebHost.CreateDefaultBuilder(args)
                  .UseUrls("http://*:5000")
                  .UseStartup<Startup>();
      }
  }
  ```

- `cmd`到项目根目录，`dotnet restore`（可忽略），再发布`dotnet publish`, 发布的文件夹路径默认为`~\bin\Debug\netcoreapp2.2\publish`

  `dotnet restore` 是一个隐式的命令，需要还原的时候会自动执行 `dotnet restore` 命令。下面的命令执行时都会隐式调用还原。

  - `new`
  - `run`
  - `build`
  - `publish`
  - `pack`
  - `test`

- `xshell`连接虚拟机的`ubuntu`系统，使用`rz`命令将`publish` 文件夹内容复制到`Ubuntu`系统中

- 测试`ubuntu`中发布的`.dll`是否可以运行(前提：配置了 dotnet 环境)

  ```
  cd webapi/publish/		# publish的文件所在路径
  dotnet demoApi.dll 		# 启动demo
  >>> Hosting environment: Production
      Content root path: /home/klaus/webapi/publish
      Now listening on: http://[::]:5000
      Application started. Press Ctrl+C to shut down.
  curl http://192.168.1.85:5000/api/values		# 192.168.1.85为虚拟机的ip,不是windows的ip
  >>> ["value1","value2"]	# 说明接口调用正常
  ```

### ubuntu中docker镜像创建

[`refer1: `ASP.NET Core开发-Docker部署运行`](https://www.cnblogs.com/linezero/p/docker.html)
[`refer2: docker 部署 webapi 示例`](<https://blog.csdn.net/u014690615/article/details/83590412>)

- 终端进入`publish`文件夹，创建Dockerfile文件，内容如下：

  ```
  # 基于microsoft/dotnet:latest构建Docker Image
  FROM microsoft/dotnet:latest
   
  # 进入docker中的/usr/local/src目录
  RUN cd /usr/local/src
   
  # 创建DockerWebAPI目录
  RUN mkdir DockerWebAPI
   
  # 设置工作路径
  WORKDIR /usr/local/src/DockerWebAPI
   
  # 将当前文件夹下的所有文件全部复制到工作目录
  COPY *.* ./
   
  # 向外界暴露5000端口
  EXPOSE 5000
   
  # 执行dotnet xxxx.dll命令
  CMD ["dotnet", "demoApi.dll"]
  ```

- 通过`Dockerfile`文件创建镜像：在`Dockerfile`所在当前目录, 终端命令如下：

  ```
  docker build -t dockerapi/demo .    # 最后的 " . "不能忽略,且repository name must be lowercase
  ```

- 在镜像下创建容器，命名为`apidemo`, 端口映射为: `51113:5000`

  ```
  docker run -it -p 51113:5000 --name apidemo dockerapi/demo
  >>> 
  warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[35]
        No XML encryptor configured. Key {86157ad5-e0ee-488a-89a5-320bf4edb7f3} may be persisted to storage in unencrypted form.
  Hosting environment: Production
  Content root path: /usr/local/src/DockerWebAPI
  Now listening on: http://[::]:5000
  Application started. Press Ctrl+C to shut down.
  ```

- 测试api 结果如下，api调用成功， 然后`ctrl+C`退出

  ```
  curl http://192.168.1.85:51113/api/values
  >>> ["value1","value2"]
  ```

- 重新开启api容器： `docker container start <container_name or tag>`

  ```
  docker container start apidome		# 开启已经停止的api容器
  >>> apidemo
  curl http://192.168.1.85:51113/api/values	# 连接接口
  >>> ["value1","value2"]
  ```

- 关闭运行状态中的api容器

  ```
  docker container stop apidemo 
  ```

  

