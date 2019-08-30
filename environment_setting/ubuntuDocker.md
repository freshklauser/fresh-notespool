[TOC]

## 1. Ubuntu Docker安装

- 验证` Ubuntu `版本是否支持`Docker`：`uname -r`

  ```
  klaus@ubuntu:~$ uname -r
  4.15.0-55-generic
  ```

- 获取最新版本的 `Docker` 安装包

  ```
  wget -qO- https://get.docker.com/ | sh
  reboot
  ```

- 启动 `Docker`后台服务

  ```
  sudo service docker start
  ps -af|grep docker  # 查看docker进程
  ```

- 测试运行hello-world

  ```
  docker run hello-world
  ```

  

