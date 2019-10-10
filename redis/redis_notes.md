





### 1. 启动  [redis](<http://www.runoob.com/redis/redis-install.html>)

- 启动redis服务(前提)： `redis-server`

  若未将redis加入到环境变量，则需要先cd到redis-cle.exe所在目录，再执行上述命令；
  执行上述命令后，要保持一致开启状态，另开cmd窗口来访问redis服务器

```
# cmd1中，保持服务一致运行状态
redis-server

# cmd2中
C:\Users\Wang>redis-cli
redis 127.0.0.1:6379> set testkey 'hello world'
OK
redis 127.0.0.1:6379> get testkey
"hello world"
redis 127.0.0.1:6379>
```

- 查看redis-server 版本： redis-server --version
- 升級redis：

