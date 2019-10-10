本文内容

[TOC]



## 1. Spark 基础

### 1.1 Spark概述

 - 定义：
   Spark： 基于<font color=coral>内存</font>的快速、通用、可扩展的大数据<font color=coral>分析引擎</font>
   语言：Scala

### 1.2 Spark 内置模块

- Spark SQL 结构化数据、Spark Streaming实时计算、Spark Mlib机器学习

- **Spark Core**   --- 离线计算核心模块, 比MapReduce更快

- 独立调度器、**YARN**(hadoop内的)、Mesos(单独的框架)    ---  资源调度

  <div align=center><img src='./img/1-1 spark_builtIn_modules.png' width=80%></div>

### 1.3 Spark特点

<div align=center><img src='./img/1-2.png' width=90%></div>

## 2. Spark的运行模式

### 2.1 集群角色

#### 2.1.1 Master 和 Workers

- Master
  Spark 特有资源调度系统的Leader，掌握整个资源信息

  1）监听 workers 是否工作

  2）对Worker、Application等的管理

- Workers

  Spark 特有资源调度系统的 Slave, 有多个，每个 Slave 掌管着所在节点的资源信息

  功能：

  ​	1）通过 RegisterWorker 注册到 Master;

  ​	2）定时发送心跳到 Master

  ​	3）根据 Master 发送的 application 配置进程环境，并启动 StandaloneExecutorBackend （执行 Task 所需的临时进程）

#### 2.1.2 Driver 和 Executor

- Driver (驱动器）

  执行开发程序中的 main 方法的进程 ，即 client : sc 、spark

  工作内容：

  ​	1）把用户程序转为任务

  ​	2）为执行器节点调度任务

  ​	3）跟踪 Executor 的运行状况

  ​	4）UI 展示应用运行状况

- Executor （执行器）
  负责在 Spark 作业中运行任务

  ​	1）负责运行组成 Spark 应用的任务，并将结果返回给 驱动器进程

  ​	2）通过自身的块管理器（Block Manager）为用户程序中要求换成的 RDD 提供内存式存储。 RDD 是直接缓存在 Executor 进程内的，因此任务在运行时充分利用缓存数据急速运算

**总结**：
    <font color=coral>1）Master 和 Worker 是 Spark 的守护进程，即 Spark 在特定模式下正常运行所需要的进程；</font>
    <font color=coral>2）Driver 和 Executor 是临时进程，当有具体任务提交到 Spark 集群时才会开启的进程。</font>

### 2.2 Local 模式

​	单机运行模式

#### 2.2.1 概述

通过以下几种方式集中设置 Master:

- local: 单核，所有计算都运行在一个线程当中，没有任何并行计算
- local[K]：指定线程数来运行计算， local[4]--运行3个Worker线程。通常 cpu 有几个Core, 就指定几个线程，最大化利用 cpu 的计算能力；
- local[*]: 默认安装 cpu 最多Cores 来设置线程数

#### 2.2.2 安装： 详见 [`spark_Install_Envs.md`](./spark_Install_Envs.md) 文件 

#### 2.2.3 提交流程 

- [<font color=coral>官方SparkPI 案例</font>](http://spark.apache.org/docs/2.1.1/submitting-applications.html)

  ```bash
  # Run application locally on 8 cores
  ./bin/spark-submit \
    --class org.apache.spark.examples.SparkPi \    # 主类 Application's main class 
    --master local[8] \
    ./examples/jars/spark-examples_2.11-2.4.4.jar \ # <application-jar>   主类 main 所在的jar包
    100						   # [application-arguments]  主类 main的参数
  ```

- spark-submit  目录位置： /usr/lib/spark-2.4.4-bin-hadoop2.7/bin
  bin目录下 重要的三个文件： `spark-shell`、`spark-sql`、`spark-submit`

- 1）基本语法 

  ```
  ./bin/spark-submit \
    --class <main-class> \			# 主类 Application's main class 
    --master <master-url> \
    --deploy-mode <deploy-mode> \
    --conf <key>=<value> \
    ... # other options
    <application-jar> \				# 主类 main 所在的jar包
    [application-arguments]			 # 主类 main的参数
  ```

- 2）参数说明
  详细参数及说明参考[spark_commands.md](./spark_commands.md)
  `--master` ：制定 Master 的地址；
  `--class `：你的应用的启动类；
  `--deploy-mode`：是否发布你的驱动到 worker 节点（cluster）或者作为一个本地客户端（client）, default: client；
  `--conf `：任意的 Spark 配置属性，格式 key=value, 如果值包含空格，可以加引号"key=value"；
  `--executor-memory 1G`：指定每个 executor 可用内存为1G；
  `--total-executor-cores 2`：指定每个 executor 使用的 cup 核数为2个；

- 3）任务提交

  ```
  $ spark-shell
  >>> ...
      Spark context Web UI available at http://192.168.1.36:4040
      Spark context available as 'sc' (master = local[*], app id = local-1570673879020).
      Spark session available as 'spark'.
      ...
  
  ```

  - spark context web UI

  - spark context （sc）：上下文，提交任务必须从 spark context 开始， 使用 sc 命令提交任务

    (1）local 运行模式执行 wordcount

    ```
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  word count <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # 在 /home/klaus/ 下创建txt文件，内容如下：
    	piaodehui piaodehui
        zhangjian laonanren
        laonanren laonanren
        tianshui
        
    # terminal 中 开启 spark-shell 命令， 在 scala> 输入如下命令
    scala> sc.textFile("./word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).collect
    # 结果如下
    res2: Array[(String, Int)] = Array((laonanren,3), (zhangjian,1), (piaodehui,2), (tianshui,1))
    
    # 读取初的数据存储到 sc_output 下
    scala> sc.textFile("./word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).saveAsTextFile("./sc_output"）
    # 查看 sc_output 下的文件，如下
    klaus@ubuntu:~/sc_output$ ls -l
    total 8
    -rw-r--r-- 1 klaus klaus 42 Oct  9 19:45 part-00000
    -rw-r--r-- 1 klaus klaus 13 Oct  9 19:45 part-00001
    -rw-r--r-- 1 klaus klaus  0 Oct  9 19:45 _SUCCESS
    ```

    (2）local模式下的进程和WebUI 如下

    <div align=center><img src='./img/1-3.png' width=80%></div>

  - spark session：spark-sql 的入口， 使用 spark 命令提交任务

- 3）Spark 通用运行简易流程

<div align=center><img src='./img/1-4.png' width=80%></div>

在 Local 模式下， Driver 和 executor 合并为一体，同时包含 Driver和 Executor的功能

### 2.2.4 数据流程

<div align=center><img src='./img/1-5.png' width=80%></div>

WordCount 案例分析数据流：

<div align=center><img src='./img/1-6.png' width=80%></div>



### 2.3 Standalone 模式

#### 2.3.1 概述

构建一个由 Master + Slave 构成的 Spark 集群， Spark 运行在集群中。

- Standalone 运行模式

<div align=center><img src='./img/1-7.png' width=80%></div>

#### 2.3.2 安装使用

- 1）进入spark目录下的conf文件夹：

  ```
  klaus@ubuntu:/usr/lib/spark-2.4.4-bin-hadoop2.7/conf$ ls -l   # 全是 .template
  total 36
  -rw-r--r-- 1 klaus klaus  996 Aug 27 14:30 docker.properties.template
  -rw-r--r-- 1 klaus klaus 1105 Aug 27 14:30 fairscheduler.xml.template
  -rw-r--r-- 1 klaus klaus 2025 Aug 27 14:30 log4j.properties.template
  -rw-r--r-- 1 klaus klaus 7801 Aug 27 14:30 metrics.properties.template
  -rw-r--r-- 1 klaus klaus  865 Aug 27 14:30 slaves.template
  -rw-r--r-- 1 klaus klaus 1292 Aug 27 14:30 spark-defaults.conf.template
  -rwxr-xr-x 1 klaus klaus 4221 Aug 27 14:30 spark-env.sh.template
  ```

- 2）修改配置文件名称（去掉 `.template`）

  ```
  sudo mv slaves.template slaves
  sudo mv spark-defaults.conf.template spark-defaults.conf
  sudo mv spark-env.sh.template spark-env.sh
  ```

- 3）修改 slave 文件，添加如下 work 节点

  ```
  # 注释掉原模板中的 localhost 节点
  hadoop102
  hadoop103
  hadoop104
  ```

- 4）修改 spark-env.sh 文件，添加如下配置

  ```
  SPARK_MASTER_HOST=hadoop102
  SPARK_MASTER_PORT=7077
  ```

- 5）分发 spark 包

  ```
  cd ../..
  xsync spark-2.4.4-bin-hadoop2.7/		# xsync 集群同步脚本
  # xsync filename ： 将filename分发到集群中的各个节点中
  ```

#### 2.3.3 JobHistoryServer 配置

- 1）修改 spark-default.conf.template 名称

  ```
  sudo mv spark-defaults.conf.template spark-defaults.conf
  ```

- 2）修改 spark-default.conf 文件（添加如下内容），开启 Log（写日志）

  ```
  spark.eventLog.enabled           true
  spark.eventLog.dir               hdfs://namenode:8021/directory
  ```

  <font color=coral>注意： HDFS上的目录需要提前存在</font>

- 3）修改 spark-env.sh 文件，添加如下配置 （读日志）

  ```
  export SPARK_HISTORY_OPTS="-Dspark.history.ui.port=18080
  -Dspark.history.retainedApplications=30
  -Dspark.history.fs.logDirectory=hdfs://hadoop102:9000/directory"
  ```

- 参数描述：

  - spark.eventLog.dir ：Application 在运行过程中所有信息均记录在该属性指定的路径下；
  - spark.history.ui.port=18080：webui 访问的端口号；
  - spark.history.fs.logDirectory=hdfs://hadoop102:9000/directory：配置了该属性后，在spark.history-server.sh时就无需显式的指定路径， Spark  History Server 页面只展示该指定路径下的信息

  - spark.history.retainedApplications=30 指定保存 Application 历史记录的个数，如果超过这个值，内存中旧的应用程序信息将被删除，而不是页面上显式的应用数

- 4）分发配置文件

  ```
  xsync spark-defaults.conf
  xsync spark-env.sh
  # 分发后查看集群是否启动，如下图
  util.sh		# spark目录下，但是没看到这个文件存在，不知道啥情况
  ```

<div align=center><img src='./img/1-9.png' width=50%></div>

- 5）启动历史服务

  ```
  # spark 目录下
  sbin/start-history-server.sh
  ```

- 6）再次执行任务

  ```
  bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \  
  --master spark://hadoop102:7077 \
  --executor-memory 1G \
  --total-executor-cores 2 \
  ./examples/jars/spark-examples_2.11-2.4.4.jar \ 
  100				
  ```

- 7）查看历史服务

  浏览器输入：<font color=coral>`hadoop102:18080`</font>

	#### 2.3.4 HA配置















### 2.4 Yarn 模式













































## 2. Spark Core

## 3. Spark SQL

## 4. Spark Streaming