[TOC]

## 1.什么是序列化，反序列化？

1. 序列化：把对象转换为字节序列的过程称为对象的序列化。

  ```
  数据写入 》》》**序列化**——就是把内存里面的这些对象给变成一连串的字节描述的过程。
  ```

2. 反序列化：把字节序列恢复为对象的过程称为对象的反序列化。

  ```
  文件读取》》》**反序列化**——就是把文件中一连串的字节转为一个对象放入内存里存放的过程。
  ```

## 2. 什么情况下需要序列化？

- 当你想把的内存中的对象状态保存到一个文件中或者数据库中时候；

- 当你想用套接字在网络上传送对象的时候；

- 当你想通过`RMI`传输对象的时候；

  (最常用的可能就存数据库的)

## 3. python实现序列化和反序列化

- `pickle.dump(obj, file, [,protocol])`：写入文件并序列化, 将对象obj保存到文件file中去

  ```
  protocol 是序列化模式, 默认是0（ASCII协议，表示以文本的形式进行序列化），protocol的值还可以是1和2（1和2表示以二进制的形式进行序列化。其中，1是老式的二进制协议；2是新二进制协议）
  file表示保存到的类文件对象，file必须有write()接口，file可以是一个以’w’打开的文件或者是一个StringIO对象，也可以是任何可以实现write()接口的对象。
  ```

- `pickle.load(file)`：从文件中读取，并返序列化：

  ```
  将文件中的数据解析为一个python对象。file中有read()接口和readline()接口
  ```




## 4. pickle模块

```
In [5]: help(pickle)
Help on module pickle:
NAME
    pickle - Create portable serialized representations of Python objects.
DESCRIPTION
    See module copyreg for a mechanism for registering custom picklers.
    See module pickletools source for extensive comments.

    Classes:
        Pickler
        Unpickler

    Functions:
        dump(object, file)
        dumps(object) -> string
        load(file) -> object
        loads(string) -> object
```





























