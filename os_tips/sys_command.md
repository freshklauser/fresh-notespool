- ubuntu安装软件常用位置：

  `/usr/lib/`    `/opt/`
  
- 保存终端内容到本地文件

  ```
  script  <localfilename> 			# 开始记录终端内容
  ......
  exit							  # 结束记录
  # 或者直接在command后面加  >> <filename> 将command执行后的内容保存到本地文件中
  ```

  ```
  保存terminal命令及输出内容到local file:
  1) 保存输入命令： 
  	"history | tee history.txt" 在terminal中输出命令的output的同时，将output保存在history.txt文件中；
  	"history > history.txt"  覆盖
  	"history >> history.txt" 追加整个history命令编译内容
  2）保存命令编译后的输出内容：
  	"whereis python | tee output.txt"  覆盖模式
  	"whereis python | tee -a output.txt" (-a表示追加模式)将命令的输出保存在output.txt中
  	"ps -ef | grep python >> output.txt"不在terminal中显示，直接将结果重定向到output.txt文件中
  ```

- curl

  ```
  在Linux中curl是一个利用URL规则在命令行下工作的文件传输工具，可以说是一款很强大的http命令行工具。它支持文件的上传和下载，是综合传输工具，但按传统，习惯称url为下载工具。
  语法：curl [option] [url]
              -A/--user-agent <string>              设置用户代理发送给服务器
              -b/--cookie <name=string/file>    cookie字符串或文件读取位置
              -c/--cookie-jar <file>                    操作结束后把cookie写入到这个文件中
              -C/--continue-at <offset>            断点续转
              -D/--dump-header <file>              把header信息写入到该文件中
              -e/--referer                                  来源网址
              -f/--fail                                          连接失败时不显示http错误
              -o/--output                                  把输出写到该文件中
              -O/--remote-name                      把输出写到该文件中，保留远程文件的文件名
              -r/--range <range>                      检索来自HTTP/1.1或FTP服务器字节范围
              -s/--silent                                    静音模式。不输出任何东西
              -T/--upload-file <file>                  上传文件
              -u/--user <user[:password]>      设置服务器的用户和密码
              -w/--write-out [format]                什么输出完成后
              -x/--proxy <host[:port]>              在给定的端口上使用HTTP代理
              -#/--progress-bar                        进度条显示当前的传送状态	
  eg.
  	curl -o linux.html http://www.linux.com
  	curl -o dodo1.jpg http:www.linux.com/dodo1.JPG
  ```

- ubuntu清楚terminal的历史记录

  ```#
  $ history -c		# 清楚历史记录(16.04版本再次打开terminal时还有有历史记录)
  
  # 彻底清楚历史记录(删掉 .bash_history文件)
  $ rm -rf ~/.bash_history
  $ history -c
  ```

- ubuntu安装 notepadqq (替换notepad++)

  ```
  # 安装
  snap install --classic notepad11
  sudo apt-get update
  # 卸载
  sudo apt-get remove notepadqq
  sudo add-apt-repository --remove ppa:notepadqq-team/notepadqq
  ```

- ubuntu建立程序的软连接实现terminal终端启动：建立执行文件到/usr/local/bin的软连接

  ```
  # 建立sublimetext的软连接，terminal通过subl 启动
  ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl
  # 调用
  subl <filename>
  ```

- Typora 安装好后不需要建立软连接，可以直接在terminal中使用 `typora <filename>` 打开文件

- ubuntu下 notepadqq 和 sublimetext都无法输入中文

  refer for sublimetext: https://blog.csdn.net/weixin_41762173/article/details/79379131

  ```
  待解决
  ```

- `xshell`与ubuntu传输文件：lrzsz

  https://cloud.tencent.com/developer/article/1182215

  rz　命令无法传输空文件

- `df -h` 命令 

  用法：df [选项]... [文件]...
  	`Show information about the file system on which each FILE resides,
  or all file systems by default.`

  ```
  klaus@ubuntu:~$ df -h
  文件系统        容量  已用  可用 已用% 挂载点
  udev            956M     0  956M    0% /dev
  tmpfs           197M   12M  186M    6% /run
  /dev/sda1        29G   15G   13G   53% /
  tmpfs           985M  153M  833M   16% /dev/shm
  tmpfs           5.0M  4.0K  5.0M    1% /run/lock
  tmpfs           985M     0  985M    0% /sys/fs/cgroup
  vmhgfs-fuse     783G   15G  768G    2% /mnt/hgfs
  tmpfs           197M   84K  197M    1% /run/user/1000
  /dev/loop0       89M   89M     0  100% /snap/core/7396
  /dev/loop1      145M  145M     0  100% /snap/notepadqq/855
  ```

  

- ```
  klaus@ubuntu:~$ df -h
  文件系统        容量  已用  可用 已用% 挂载点
  udev            956M     0  956M    0% /dev
  tmpfs           197M   12M  186M    6% /run
  /dev/sda1        29G   15G   13G   53% /
  tmpfs           985M  153M  833M   16% /dev/shm
  tmpfs           5.0M  4.0K  5.0M    1% /run/lock
  tmpfs           985M     0  985M    0% /sys/fs/cgroup
  vmhgfs-fuse     783G   15G  768G    2% /mnt/hgfs
  tmpfs           197M   84K  197M    1% /run/user/1000
  /dev/loop0       89M   89M     0  100% /snap/core/7396
  /dev/loop1      145M  145M     0  100% /snap/notepadqq/855
  
  ```

  

1、命令：touch [文件]（创建文件）

2、命令：mkdir -p 目标文件递归创建文件夹（如：mkdir -p /usr/local/d1/d2/d3）

- 删除文件夹： `rm -rf 目录名字`

- 创建多级目录： `mkdir -p dir1/dir2/dir3/...`

  ```
  -m, --mode=模式   设定权限<模式> (类似 chmod)，而不是 rwxrwxrwx 减 umask
  -p, --parents     需要时创建上层目录，如目录早已存在则不当作错误
  -v, --verbose     每次创建新目录都显示信息
  -Z, --context=CONTEXT (SELinux) set security context to CONTEXT
  --help     显示此帮助信息并退出
  --version  输出版本信息并退出
  ```

  

3、命令：rm [文件]（删除）；

    rm -r [文件]删除目录；
    rm -f [文件]删除文件；
    rm -rf [文件] 删除所有；

4、命令：cat [文件]（查看文件内容，适合小篇幅文件）

5、命令：more [文件]（查看所有内容，适合大篇幅文件，空格进行翻页，回车进入下一行，ctrl+C退出）

6、命令：head -number [文件]（查看文件前多少行）

7、命令：tail -number [文件]（查看文件后多少行）

8、命令：vim（编辑，进入后点击“i”键，进入insert模式，：wq保存退出，：q!不保存退出）

9、命令： cp [文件]  复制源文件：  `cp -r * ~/klaus/localfile`

    cp -r [文件] 递归复制源目录

10、命令：mv  

- A：修改文件名称的功能（源文件名  新文件名）
- B：移动文件位置（源文件名称  新文件位置+新文件名）

11、命令：ln（link）；ln -s [源文件] [目标文件] （硬链接则不需要-s选项）
	`ln -s /mnt/hgfs/share/ ~/share` 
	将 hgfs中的share文件创建软链接到 用户目录下的share文件夹中 （share文件夹需要提前建好）

- 软连接特点：权限是所有人都可以访问，并且软连接文件指向源文件，软链接就像windows系统中的快捷方式一样
- 硬链接特点：类似copy，和源文件是同步更新数据，硬链接不能跨文件系统分区，软链接可以

12、命令：chmod 改变文件或目录的权限；

- A：chmod【{ugo}{+-=}】【文件或目录】
- B：chmod 【mode=421】【文件目录】（4代表r——读，2代表w——写、创建、删除，1代表x——进入该目录）

13、命令：su -userName （切换用户）

14、命令：chown（改变文件的所有者）；chown userName 文件名

15、命令：chgrp（改变文件的所有组）；chgrp groupName 文件名

16、命令：find 【搜索范围路径】 -name [名称]

    find 【搜索范围路径】 -size 【+-文件大小】
    find 【时间查找】：天：ctime、atime、mtime；分钟：cmin、amin、mmin；

注：c表示：change改变文件属性的意思（比如所有者、所有组、权限变更）

    a表示：access表示被访问过的意思（比如查看过等）
    m表示：modify更改内容的意思
    在时间前面添加：-表示之内，+表示之外

17、find应用的连接符：-a（and的意思，逻辑与） ; -o（or的意思，逻辑或）

18、find -type （根据文件类型查找）：f表示二进制文件，l表示软链接文件，d表示目录

19、命令：man【命令或者配置文件】；（帮助命令，非常有用，可以获得命令的帮助文档）

20、命令：whatis【命令】；查看命令的描述

21、命令：【命令】--help；查看命令的选项用法

22、命令：tar        [`refer`](<https://www.runoob.com/linux/linux-comm-tar.html>)
	语法：tar -zxvf[-zcvf] 【源文件名】 -C 【路径】   解压

> tar 
> 解包：`tar -xvf FileName.tar`
> 打包：`tar -cvf FileName.tar DirName `  （注：tar是打包，不是压缩！）
>
> .tar.gz 和 .tgz
> 解压：<font color=coral>`tar -zxvf FileName.tar.gz`</font>
> 压缩：<font color=coral>`tar -zcvf FileName.tar.gz DirName`</font>

    -c: 建立压缩档案
    -x：解压
    -t：查看内容
    -r：向压缩归档文件末尾追加文件
    -u：更新原压缩包中的文件
    以上五个是独立的命令，压缩解压都要用到其中一个，可以和别的命令连用但只能用其中一个。下面的参数是根据需要在压缩或解压档案时可选的。
    -x：产生的解压缩文件；
    -f：指定压缩后的文件名；
    -z：支持gzip解压文件
    -Z：支持compress解压文件
    -v：显示操作过程；
    -j：支持bzip2解压文件
    -v：显示所有过程
    -O：将文件解开到标准输出
    ...

描述：打包目录 生成的后缀名.tar.gz，或者进行解压，最后配置加-C表示文件解压后存放的路径

解压gz文件：gunzip FileName.gz 

23、命令：zip；

    语法：zip 选项【-r】【压缩后文件名称】【源文件】；
    描述：zip的格式是windows和linux通用的格式，可以压缩文件和目录，压缩目录时需要选项-r；

24、命令：unzip

    语法：unzip【解压缩的文件】；
    描述：进行解压缩，最后配置加-d表示文件解压后存放的路径；

25、命令：ping

    A、首先ping一下回环地址127.0.0.1检查自己本机的网络协议是否正确；
    B、再ping一下本机ip查看自己本机的网络是否正确；
    C、然后检查对方网络设置、防火墙、插件等等；
    D、如果发现丢包率里没有丢失数据包、可能是网络、网线的原因；
    E、ping配置选项ping -c 6 192.168.80.100（表示ping6次后断开）；
    F、ping配置选项ping -s 60000（最大65507）；

26、查看网卡信息：ifconfig；
	关机：shutdown -h now；
	重启：reboot；
	ctrl+l ：清屏；
	ctrl+c：退出应用；
	tab键：信息补全；

27、命令：grep（过滤，可以将指定内容进行过滤然后输出）

28、命令：| （管道，将一个命令的输出传送给另一个命令，作为另外一个命令的输入。管道可以连接N个命令）

29、命令：>（输出重定向到一个文件上）；>>（输出重定向追加结果到一个文件上） 例如：ls > a.txt

30、命令：<（输入的信息重定向） 例如： wall < a.txt

31、命令：wall [内容]（广播、显示）

32、命令：2>（错误重定向，一般把程序执行的错误日志信息存放在log日志中）

33、命令：vi/vim（编辑）
	注：当输入vi/vim时，进入命令模式，输入“i”/“a”/“o”，可进入插入（insert）模式，按ESC进入编辑模式，输入（：q！），不保存退出；输入（：wq），保存并退出；
	a：在光标后附加文本；
	A：在本行行末附加文本；
	i： 在光标前插入文本；
	I：在本行开始插入文本；
	o：在光标下插入新行；
	O：在光标上插入新行；
命令模式下光标移动至文章的最后： G
命令模式下光标移动至文章的开头： 0
命令模式下光标移动至行尾: $
命令模式下光标左右上下移动： h, l, k, j
命令模式下撤销：u	

34、删除命令（编辑模式中）：

        x：删除光标所在处字符；
        nx：删除光标所在处后n个字符；
        dd：删除光标所在行，ndd删除n行；
        dG：删除光标所在行到末尾的内容；
        ：n1，n2d （删除指定范围的行）；

35、复制和粘贴：

        yy、Y：复制当前行；
        nyy、nY：复制当前行以下n行；
        dd：剪切当前行；
        ndd：剪切当前行以下n行；
        p、P：粘贴在当前光标所在行下或行上；

36、命令：r（取代光标所在处字符）；

    R（从光标所在处开始替换字符，按ESC结束；
    u（取消上一步操作）；
    /string（向前搜索指定字符串搜索时忽略大小写：set ic）
    n（搜索指定字符串的下一个出现位置）
    ：%s/old/new/g （全文替换指定old字符串）
    ：n1，n2s/old/new/g （在一定范围内替换指定字符串）

37、用户管理配置文件：

    用户信息文件：/etc/passwd
    密码文件：/etc/shadow
    用户配置文件：/etc/login.defs    /etc/default/useradd
    新用户信息文件：/etc/skel
    用户组文件：/etc/group
    用户组密码文件：/etc/gshadow

38、Linux用户一般分为三种： 
	A、超级用户（root UID=0）
	B、普通用户（UID 500-60000）
	C、伪用户（UID 1-499）

39、用户组管理命令：

    添加用户组：groupadd【配置选项】【组名】
    形如：groupadd -g 1001 webs
    删除用户组：groupdel【组名】
    形如：groupdel webs
    修改用户组：groupmod -n【新组名】【旧组名】
    查看用户属于那些用户组：groups ul

40、用户管理命令：

    添加用户：useradd 
    	形如：useradd -u 1002 -g webapps -G sys，root -d /web -s /bin/bash -c “is a u2” -e 2015-12-12 
    	u：UID；g：缺省所属用户组的名称或GID；G：指定用户所属多个组；d：宿主目录；s：命令解释器Shell；c：描述信息；e：指定用户失效时间
    修改用户：usermod -l 【新用户名】【旧用户名】
    删除用户：userdel -r 【用户名】
    禁用用户：usermod -L 【用户名】；passwd -l 【用户名】
    恢复用户：usermod -U 【用户名】；passwd -u 【用户名】
    命令：gpasswd -a（添加用户到用户组中）
    			-d（从用户组中删除用户）
    			-A（设置用户管理员）

41、命令：w(who，查看用户信息)

    TTY：表示以什么方式登陆这台计算机；
    FROM：表示从什么位置登陆的；
    LOGIN@：表示登陆时间；
    IDLE：表示用户闲置时间；
    JCPU：表示当前这个用户执行的所有进程所消耗时的总和；
    PCPU：表示执行程序耗费的时间；

注：load avegage表示系统的负载值，分别显示过去的1、5、15分钟系统的负载程度，如果想知道系统的平均负载，三者之和除3即可，最终结果如果在0.8以下表示系统正常，如果达到几十或上百，那么系统负载非常高，可能无法响应任何命令；

42、命令：at

    语法：at 【时间】
    绝对计时方法：HH：MM YYYY-MM-DD
    相对计时方法：now + n minutes now + n hours now + n days
    描述：安排一个或多个命令在指定的时间运行一次，ctrl+d保存退出任务

43、命令：at -d or atrm（删除队列中的任务）

    at-l or atq（查看队列中的人物）

44、命令：crontab

    语法：crontab{-l|-r|-e}
        -l 显示当前的crontab；
        -r 删除当前的crontab；
        -e 使用编辑器编辑当前的crontab；

45、命令：ps -el | grep 【进程名】 （查看进程状态）

- ps命令查看进程对于的id : `ps -ef | grep vim`
- kill命令杀死进程： `kill -9 进程id`

46、系统文件构成：

    /usr/bin、/bin：存放所有用户可以执行的命令；
    /usr/sbin、/sbin：存放只有root可以执行的命令；
    /home：用户缺省的宿主目录；
    /proc：虚拟文件系统，存放当前进程信息；
    /dev：存放设备文件；
    /lib：存系统程序运行所需的共享库；
    /lost+found：存放一下系统出错的检查结果；
    /tmp：存放临时文件；
    /etc：存放系统配置文件；
    /var：包含经常发生变动的文件，如日志文件、计划任务等；
    /usr：存放所有命令、库、手册等；
    /boot：内核文件及自举程序文件保存位置；
    /mnt：临时文件系统的安装点；

47、命令：yum（自动解决软件包依赖关系，方便的软件包升级）

    查找软件包：yum search【软件包名】；
    安装：yum install【软件包名】；
    检查升级：yum check-update【软件包名】；
    升级：yum update【软件包名】；
    软件包查询：yum list | grep 【软件包名】；
    软件包信息：yum info 【软件包名称】；
    卸载：yum remove 【软件包名】；
    帮助：yum -help、man yum；
    例如安装gcc：yum install gcc；
