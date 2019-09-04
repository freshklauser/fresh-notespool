



### Docker的基本组成

- Docker Client 客户端
- Docker Daemon 守护进程
- Docker Image 镜像
- Docker Container 容器
- Docker Registry 仓库

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





















