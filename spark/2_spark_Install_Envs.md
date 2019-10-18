本文内容如下

[TOC]





注：本文目前仅单机使用spark, 不适用于集群
[`refer:Spark快速入门`](https://www.w3cschool.cn/spark/spark-quickstart.html)
[`refer:Spark入门(python)`](https://www.cnblogs.com/Vito2008/p/5216324.html)

安装所需：
- linux系统环境(这里使用的是ubuntu系统)
- Java开发环境JDK

## Java开发环境安装

[`Windows下的java环境搭建`](http://www.runoob.com/java/java-environment-setup.html#win-install)

 - 确认ubuntu系统是否安装过java, 出现如下所示输出，则表明并未安装过java

   ```
   $ java -version
   >>>
   The program 'java' can be found in the following packages:
   * default-jre
   * gcj-5-jre-headless
   * openjdk-8-jre-headless
   * gcj-4.8-jre-headless
   * gcj-4.9-jre-headless
   * openjdk-9-jre-headless
   Try: sudo apt install <selected package>
   ```

- ubuntu上安装java  

  **以后可以下载 `.tar.gz`的bin包安装  （解压后重命名改短一些再解压安装）**

  [`refer: Ubuntu安装JDK详解`](https://blog.csdn.net/gatieme/article/details/52723931)

  ```
  # 如下链接下载 jdk 的 tar.gz 包
  https://login.oracle.com/mysso/signon.jsp
  # 新建java安装目录
  sudo mkdir -p /usr/java/
  # (JDK包所在目录下)将改名后的 jdk 包 移动到 /usr/java/ 目录下
  sudo mv jdk1.8.xxx.tar.gz /usr/java/
  # 解压 jdk 包
  sudo tar zxvf jdk1.8.xxx.tar.gz
  # 重新命名，短一点儿
  sudo mv jdk1.8.xxx/ jdk18/
  # 配置环境变量
  sudo vim .bashrc
  # 在末尾添加如下内容：
  # added by jdk installer 20191012
  JAVA_HOME=/usr/java/jdk18
  JRE_HOME=$JAVA_HOME/jre
  JAVA_BIN=$JAVA_HOME/bin
  CLASSPATH=.;$JAVA_HOME/lib/dt.jar;$JAVA_HOME/lib/tools.jar;$JRE_HOME/lib
  PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
  export JAVA_HOME JRE_HOME PATH CLASSPATH
  
  # 更新环境变量设置，使其立即生效
  source ~/.bashrc
  # 验证java安装是否成功
  terminal >> java -version
      klaus@Messi:~$ java -version
      java version "1.8.0_221"
      Java(TM) SE Runtime Environment (build 1.8.0_221-b11)
    Java HotSpot(TM) 64-Bit Server VM (build 25.221-b11, mixed mode)
  ```

  
  
  1) 安装jre:  

  ```
$ sudo apt-get install default-jre
  ```
  
  2) 安装OpenJDK

  ```
$ sudo apt-get install default-jdk
  ```
  
  3) 设置java环境变量
  
  ```
  # 1. 查看java版本
  $ java -version				# java version "1.8.0-222"
  # 2. 查看java真实路径
  ls -l /etc/alternatives/java
  >>> lrwxrwxrwx 1 root root 46 Sep 11 19:39 /etc/alternatives/java -> /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
  其中 java的真实安装路径为： /usr/lib/jvm/java-8-openjdk-amd64
  # 2. 设置java环境变量  对当前用户有效（全局用户在 /etc/profile中）
  $ sudo vim .bashrc
          export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
          export JRE_HOME=$JAVA_HOME/jre
          export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
          export PATH=$PATH:$JAVA_HOME/bin
  # 3. 执行source命令使更改立即生效
  $ source ~/.bashrc
  ```



## 安装 scala

- 下载地址：https://www.scala-lang.org/download/2.11.12.html，下载 `scala-2.11.12.tgz`

- 解压，重命名，移动到　`/usr/lib/scala/`

- 添加系统变量

  ```
  sudo vim .bashrc
  # 添加以下内容
      export　SCALA_HOME=/usr/lib/scala
      export PATH=$PATH:${SCALA_HOME}/bin
  
  klaus@Messi:~$ scala -version
  Scala code runner version 2.11.12 -- Copyright 2002-2017, LAMP/EPFL
  # 由于版本问题，scala　进入后会报错
  [ERROR] Failed to construct terminal; falling back to unsupported
  java.lang.NumberFormatException: For input string: "0x100"
  ....
  # 解决方法：更换scala版本为2.11.8, ok.
  ```

- 卸载：直接删除解压后的scala文件夹，注销掉　.bashrc　中的环境配置

  

## 安装 Intellij IDEA

- [官网下载](https://www.jetbrains.com/idea/download/#section=linux) IDEA 安装包  `.tar.gz` 

- 终端进入解压目录(这里设置在 `/opt/Intellij/`)下的 `bin 子目录` 下，然后在终端下运行启动命令：<font color=coral>`./idea.sh`</font>

- 官方激活码：`idea.medeming.com`

- 安装 scala 插件

  本地下载好后从本地导入插件，下载插件地址：https://plugins.jetbrains.com/plugin/1347-scala/versions

  下载与 Intellij IDEA 自带的插件版本一致的插件 .zip

  IDEA 中选择从本地安装插件，选择下载的插件`scala-intellij-bin-2019.2.36.zip`，然后`restart IDEA`即可

- 新建scala的`IDEA`项目的时候，`scala SDK`为空，需要 `Create --> Browse选择上一步安装scala中的最终安装目录`即可继续创建项目。



## 安装Spark (注意版本问题，spark  scala   hadoop  java)

- 下载Spark: http://spark.apache.org/downloads.html

  `spark:2.4.4、scala: 2.11.12` <font color=coral>(建议换成 spark2.3.x-with-hadoop2.7, scala2.11.8)</font>

- 在目标安装目录下解压缩该下载的`.tgz`压缩文件

  ```
  tar -zxvf spark-2.4.4-bin-hadoop2.7.tgz
  sudo mv spark-2.4.4-bin-hadoop2.7 spark
  sudo mv spark/ /usr/lib/spark/			# 移动安装后的spark目录
  ```

- 添加spark的环境变量

  ```
  # 这里编辑的是 ~/.bashrc文件，也可以编辑~/.bash_profile或~/.profile文
  $ sudo vim ~/.bashrc      #　添加路径（在系统更目录下即可执行 spark-shell） 
          # adding bin path of spark to system path
  		 export SPARK_HOME=/usr/lib/spark-2.4.4-bin-hadoop2.7
  		 export PATH=${SPARK_HOME}/bin:$PATH
  # 执行source命令使配置更改立即生效
  $ source ~/.bashrc
  ```

- 测试安装情况

  ```
  $ spark-shell
  >>>
  19/09/11 22:32:58 WARN Utils: Your hostname, ubuntu resolves to a loopback address: 127.0.1.1; using 192.168.1.85 instead (on interface ens33)
  19/09/11 22:32:58 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
  19/09/11 22:32:59 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
  Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
  Setting default log level to "WARN".
  To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
  Spark context Web UI available at http://192.168.1.85:4040
  Spark context available as 'sc' (master = local[*], app id = local-1568266386781).
  Spark session available as 'spark'.
  Welcome to
        ____              __
       / __/__  ___ _____/ /__
      _\ \/ _ \/ _ `/ __/  '_/
     /___/ .__/\_,_/_/ /_/\_\   version 2.4.4
        /_/
           
  Using Scala version 2.11.12 (OpenJDK 64-Bit Server VM, Java 1.8.0_222)
  Type in expressions to have them evaluated.
  Type :help for more information.
  
  scala> 
  
  # scala命令查询
  scala> :help
  All commands can be abbreviated, e.g., :he instead of :help.
  :edit <id>|<line>        edit history
  :help [command]          print this summary or command-specific help
  :history [num]           show the history (optional num is commands to show)
  :h? <string>             search the history
  :imports [name name ...] show import history, identifying sources of names
  :implicits [-v]          show the implicits in scope
  :javap <path|class>      disassemble a file or class name
  :line <id>|<line>        place line(s) at the end of history
  :load <path>             interpret lines in a file
  :paste [-raw] [path]     enter paste mode or paste a file
  :power                   enable power user mode
  :quit                    exit the interpreter
  :replay [options]        reset the repl and replay all previous commands
  :require <path>          add a jar to the classpath
  :reset [options]         reset the repl to its initial state, forgetting all session entries
  :save <path>             save replayable session to a file
  :sh <command line>       run a shell command (result is implicitly => List[String])
  :settings <options>      update compiler options, if possible; see reset
  :silent                  disable/enable automatic printing of results
  :type [-v] <expr>        display the type of an expression without evaluating it
  :kind [-v] <expr>        display the kind of expression's type
  :warnings                show the suppressed warnings from the most recent line which had any
  ```

  其中：

  <font color=coral>`Spark context Web UI available at http://192.168.1.85:4040`</font>
  `Spark context available as 'sc' (master = local[*], app id = local-1568266386781).`
  `Spark session available as 'spark'.`

  访问网址：`http://192.168.1.85:4040`, 结果如下

  <div align=center><img src='./img/1.png' width=80%></div>

- 测试python情况：<font color=coral>`pyspark`</font>

  ```
  klaus@ubuntu:~$ pyspark 
  Python 2.7.12 (default, Aug 22 2019, 16:36:40) 
  [GCC 5.4.0 20160609] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  19/09/11 22:59:28 WARN Utils: Your hostname, ubuntu resolves to a loopback address: 127.0.1.1; using 192.168.1.85 instead (on interface ens33)
  19/09/11 22:59:28 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
  19/09/11 22:59:28 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
  Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
  Setting default log level to "WARN".
  To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
  Welcome to
        ____              __
       / __/__  ___ _____/ /__
      _\ \/ _ \/ _ `/ __/  '_/
     /__ / .__/\_,_/_/ /_/\_\   version 2.4.4
        /_/
  
  Using Python version 2.7.12 (default, Aug 22 2019 16:36:40)
  SparkSession available as 'spark'.
  >>> 
  
  ```

- anaconda 安装 pyspark 

  单独建立一个 spark 的虚拟环境会不会更合适？

  ```
  conda search pyspark  # 会显示所有版本pyspark及对应的python版本
          klaus@ubuntu:~$ conda search pyspark
          Loading channels: done
          # Name                  Version           Build  Channel             
          pyspark                   2.2.0          py27_0  pkgs/free           
          pyspark                   2.2.0          py35_0  pkgs/free           
          pyspark                   2.2.0          py36_0  pkgs/free           
          pyspark                   2.3.0          py27_0  pkgs/main           
          pyspark                   2.3.0          py35_0  pkgs/main           
          pyspark                   2.3.0          py36_0  pkgs/main           
          pyspark                   2.3.1          py27_1  pkgs/main           
          pyspark                   2.3.1          py35_1  pkgs/main           
          pyspark                   2.3.1          py36_1  pkgs/main           
          pyspark                   2.3.1          py37_1  pkgs/main           
          pyspark                   2.3.2          py27_0  pkgs/main           
          pyspark                   2.3.2          py36_0  pkgs/main           
          pyspark                   2.3.2          py37_0  pkgs/main           
          pyspark                   2.4.0          py27_0  pkgs/main           
          pyspark                   2.4.0          py36_0  pkgs/main           
          pyspark                   2.4.0          py37_0  pkgs/main           
          pyspark                   2.4.1            py_0  pkgs/main           
          pyspark                   2.4.3            py_0  pkgs/main           
          pyspark                   2.4.4            py_0  pkgs/main
  conda install pyspark=2.3.2   # 对应默认安装的是 python-3.6.6
  ```

  

