本文内容如下

[TOC]



## 1. spark安装及环境配置

注：本文目前仅单机使用spark, 不适用于集群
[`refer:Spark快速入门`](https://www.w3cschool.cn/spark/spark-quickstart.html)
[`refer:Spark入门(python)`](https://www.cnblogs.com/Vito2008/p/5216324.html)

安装所需：
- linux系统环境(这里使用的是ubuntu系统)
- Java开发环境JDK

### Java开发环境安装

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

### 安装Spark

- 下载Spark: http://spark.apache.org/downloads.html

- 在目标安装目录下解压缩该下载的`.tgz`压缩文件

  ```
  tar -zxvf spark-2.4.4-bin-hadoop2.7.tgz
  sudo mv spark-2.4.4-bin-hadoop2.7 /usr/lib/			# 移动安装后的spark目录
  ```

- 添加spark的环境变量

  ```
  # 这里编辑的是 ~/.bashrc文件，也可以编辑~/.bash_profile或~/.profile文
  $ sudo vim ~/.bashrc      #　添加路径（在系统更目录下即可执行 spark-shell） 
          # adding bin path of spark to system path
  		 export SPARK_HOME=/usr/lib/spark-2.4.4-bin-hadoop2.7
  		 export PATH=$PATH:${SPARK_HOME}/bin	
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

  

