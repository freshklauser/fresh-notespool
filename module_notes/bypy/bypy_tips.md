[TOC]

### 一 、基本指令

1. 自动上传文件夹到百度云盘

   `bypy upload 文件路径+文件名`

   ```
   bypy -v upload D:\2_Klaus_AI\3-Tools\xshell6 /clound/xshell
   # 若出现需要授权，按照给的链接复制授权码即可
   ```

2. 显示在云盘根目录下文件列表
   `bypy list`

3. 查看列表和删除

   `bypy list/ls [remotepath] [format] [sort] [order] - list the 'remotepath' directory at Baidu PCS`

   `bypy delete/remove/rm <remotepath> - delete a file / dir remotely at Baidu Yun`

   ```
   bpy list /cloud/installer/
   bypy delete /cloud/kkkkk/           # 删除文件夹
   bypy delete /cloud/installer/dockerddd.exe  # 删除文件，好像无法自动补全文件名
   ```

   

4. 同步
   `bypy syncup`	      `把当前目录同步到云盘`

   `bypy syncdown`	   `把云盘内容同步到本地来`

4. 调试

   运行时添加`-v`参数，会显示进度详情。
   运行时添加`-d`，会显示一些调试信息。
   运行时添加`-ddd`，还会会显示HTTP通讯信息（警告：非常多）

6. Screen远程会话管理功能

   `yum install screen`

   安装完毕后，输入 `screen -S sessionname` 即可创建一个名为 `sessionname` 的`screen`会话窗口。在此窗口中执行想要做的任务，然后同时按下 `ctrl + a`，松开后按下 `d`，即可将此`session`放到后台去运行，并回到之前的对话窗口。在非`screen`对话窗口中，输入 `screen -ls` 可以列举已有的`screen`进程。输入 “`screen -r` 进程代码” 就可以再次调出正在运行的`screen`进程。

   

   主要`bypy`指令：

   ```
   refreshtoken - refresh the access token
   cdl_add <source_url> [save_path] [timeout] - add an offline (cloud) download task
   cdl_addmon <source_url> [save_path] [timeout] - add an offline (cloud) download task and monitor the download progress
   cdl_cancel <task_id>  - cancel an offline (cloud) download task
   cdl_list - list offline (cloud) download tasks
   cdl_query <task_ids>  - query existing offline (cloud) download tasks
   cleancache - remove invalid entries from hash cache file
   combine <remotefile> [localfile] [md5s] - try to create a file at PCS by combining slices, having MD5s specified
   compare [remotedir] [localdir] - compare the remote directory with the local directory
   copy/cp <from> <to> - copy a file / dir remotely at Baidu Yun
   delete/remove/rm <remotepath> - delete a file / dir remotely at Baidu Yun
   downdir [remotedir] [localdir] - download a remote directory (recursively)
   downfile <remotefile> [localpath] - download a remote file.
   download [remotepath] [localpath] - download a remote directory (recursively) / file
   dumpcache - display file hash cache
   list/ls [remotepath] [format] [sort] [order] - list the 'remotepath' directory at Baidu PCS
   listrecycle [start] [limit] - list the recycle contents
   meta <remotepath> [format] - get information of the given path (dir / file) at Baidu Yun.
   mkdir <remotedir> - create a directory at Baidu Yun
   move/mv/rename/ren <from> <to> - move a file / dir remotely at Baidu Yun
   quota/info - displays the quota information
   restore <remotepath> - restore a file from the recycle bin
   search <keyword> [remotepath] [recursive] - search for a file using keyword at Baidu Yun
   stream <remotefile> <localpipe> [format] [chunk] - stream a video / audio file converted to M3U format at cloud side, to a pipe.
   syncdown [remotedir] [localdir] [deletelocal] - sync down from the remote directory to the local directory
   syncup [localdir] [remotedir] [deleteremote] - sync up from the local directory to the remote directory
   upload [localpath] [remotepath] [ondup] - upload a file or directory (recursively)
   download ...
   ```