[TOC]

## 一.  字典

### 1. `dict.setdefualt(...)`

`setdefault(self, key, default=None, /)`

> `Insert key with a value of default if key is not in the dictionary.`
>
> `Return the value for key if key is in the dictionary, else default.`

```
>>> adict = {}
>>> Users = list('abcdfeg')		# ['a', 'b', 'c', 'd', 'f', 'e', 'g']
>>> for user in Users:
... 	adict.setdefault(user, {})
>>> adict
{'a': {}, 'b': {}, 'c': {}, 'd': {}, 'f': {}, 'e': {}, 'g': {}}
```

### 2. 字典排序（按`key`和按`value`排序） -- sorted 实现多级排序

`sorted(iterable, /, *, key=None, reverse=False)`

> `Return a new list containing all items from the iterable in ascending order.`
>
> ​	`A custom key function can be supplied to customize the sort order, and the
> reverse flag can be set to request the result in descending order.`

- <font color=tomato>`sorted by key of a dict:`</font>  (`key=lambda x: x[`<font color=red>`0`</font>`]`)

  ```
  In [4]: adict = {'a':21, 'c':5, 'f':3, 'b':54, 'e':74, 'd':0}
  
  In [7]: listadict_asc_key = sorted(adict.items(), key=lambda x:x[0], reverse=False)
  In [8]: listadict_asc_key
  Out[8]: [('a', 21), ('b', 54), ('c', 5), ('d', 0), ('e', 74), ('f', 3)]
  
  In [9]: listadict_desc_key = sorted(adict.items(), key=lambda x:x[0], reverse=True)
  In [10]: listadict_desc_key
  Out[10]: [('f', 3), ('e', 74), ('d', 0), ('c', 5), ('b', 54), ('a', 21)]
  ```

- <font color=tomato>`sorted by value of a dict:`</font>  (`key=lambda x: x[`<font color=red>`1`</font>`]`)

  ```
  In [11]: listadict_asc_value = sorted(adict.items(), key=lambda x:x[1], reverse=False)
  In [12]: listadict_desc_value = sorted(adict.items(), key=lambda x:x[1], reverse=True)
  
  In [13]: listadict_asc_value
  Out[13]: [('d', 0), ('f', 3), ('c', 5), ('a', 21), ('b', 54), ('e', 74)]
  In [14]: listadict_desc_value
  Out[14]: [('e', 74), ('b', 54), ('a', 21), ('c', 5), ('f', 3), ('d', 0)]
  ```

- <font color=tomato>`sorted by value of a dict:`</font>  (<font color=tomato>`key=itemgetter(1)`</font>)

  ```
  # 对字典排序
  >>> d = {'data1':3, 'data2':1, 'data3':2, 'data4':4}  
  >>> sorted(d.iteritems(), key=itemgetter(1), reverse=True)   # 按dict的value进行排序
  [('data4', 4), ('data1', 3), ('data3', 2), ('data2', 1)]  
  ```

  `operator`模块提供的`itemgetter`数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号）

  ```
  a = [1,2,3] 
  b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值> b(a) 
  2 
  b=operator.itemgetter(1,0)   //定义函数b，获取对象的第1个域和第0个的值
  b(a) 
  (2, 1) 
  
  # itemgetter实现多级排序
  >>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),]  
  >>> sorted(students, key=itemgetter(1,2))      				# sort by grade then by age  
  [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]  
  ```

### 3. dict基本属性

```
In [20]: u
Out[20]:
{'u1': {'a': [1, 342, 22, 13, 4], 'b': [112, 32, 4, 5]},
 'u2': {'c': [1, 2, 3]}}
 
In [21]: u['u1'].items()
Out[21]: dict_items([('a', [1, 342, 22, 13, 4]), ('b', [112, 32, 4, 5])])

In [22]: u['u1']
Out[22]: {'a': [1, 342, 22, 13, 4], 'b': [112, 32, 4, 5]}

In [23]: u['u1'].keys()
Out[23]: dict_keys(['a', 'b'])

In [24]: u['u1'].values()
Out[24]: dict_values([[1, 342, 22, 13, 4], [112, 32, 4, 5]])

In [25]: max(u['u1'].values())			# value为列表时返回的结果 why ???
Out[25]: [112, 32, 4, 5]

In [28]: su ={'u1':{'a':12, 'b':112, 'c':32}, 'u2':{'c':4}}
In [29]: su['u1'].values()
Out[29]: dict_values([12, 112, 32])
In [30]: max(su['u1'].values())
Out[30]: 112
```



### 4. <font color=coral>赋值、浅拷贝、深拷贝</font>(`interesting!!`)

[`图示 refer`](https://blog.csdn.net/A123333333333/article/details/83046502)

- 赋值：即对同一个对象的引用，一变俱变
- 拷贝：复制对象，相互独立，值的变化不相互影响
  - 浅拷贝：只拷贝父对象，子对象仍是复制
  - 深拷贝：拷贝父对象和子对象（均相互独立）

- 原字典改变，则新字典改变情况：

  ```
  >>> dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42}}
  >>> new1 = dict1
  >>> new2 = dict1.copy()
  >>> new3 = copy.deepcopy(dict1)
  >>> dict1['f'] = 100
  >>> dict1['d']['d5'] = 500
  >>> dict1
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd5': 500}, 'f': 100}
  >>> new1			# 赋值：new1父对象和子对象均为引用，值随着改变
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd5': 500}, 'f': 100}
  >>> new2			# 浅拷贝：new2父对象(拷贝)不变，子对象(引用)值改变
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd5': 500}}
  >>> new3			# 深拷贝：new3父对象和子对象均为拷贝，值不变
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42}}
  ```

- 新字典改变，原字典的改变情况

  ```
  >>> dict1 = {"a": 1, "b": 2, "c": 3, "d": {"d1": 41, "d2": 42}}
  >>> new1, new2, new3 字典内容与dict1相同
  # ------------------------ 等号= 赋值 -------------------------
  >>> new1['d']['d3'] = 100
  >>> new1
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd3': 100}}
  >>> dict1					# dict1随new1改变而改变
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd3': 100}}
  
  # ------------------------ 浅拷贝() -------------------------
  >>> dict1 = {"a": 1, "b": 2, "c": 3, "d": {"d1": 41, "d2": 42}}
  >>> new2 = dict1.copy()
  >>> new2
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42}}
  >>> dict1
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42}}
  >>> new2['d']['d4'] = 4000		
  >>> new2
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd4': 4000}}
  >>> dict1				# 改变浅拷贝后的字典的二级内容，dict1对应二级内容会改变
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd4': 4000}}
  >>> new2['f'] = 5000			
  >>> new2
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd4': 4000}, 'f': 5000}
  >>> dict1				# 改变浅拷贝后的字典的一级内容，dict1对应一级内容不改变
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd4': 4000}}
  
  # ------------------------ 深拷贝 -------------------------
  >>> dict1 = {"a": 1, "b": 2, "c": 3, "d": {"d1": 41, "d2": 42}}
  >>> new3 = copy.deepcopy(dict1)
  >>> new3
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42}}
  >>> dict1
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42}}
  >>> new3['d']['d8'] = 2000
  >>> new3
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd8': 2000}}
  >>> dict1					# 相互独立，不影响dict1的值
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42}}
  >>> new3['x'] = 1000
  >>> new3
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42, 'd8': 2000}, 'x': 1000}
  >>> dict1					# 相互独立，不影响dict1的值
  {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 41, 'd2': 42}}
  ```

  

## 二. 集合

### 1. `set.add` 集合添加元素



## 三、数组、列表

1. 数组转化为列表需要使用 `arr.tolist()`

   ```
   
   ```

2. `a.append(..)`和`a.extend(..)`的区别

   - `append:` object 整体作为一个元素加入到 a 中, **增加的元素个数为 1**
   - `extend:` object中的元素逐一作为单个元素加入到 a 中, **增加的元素个数为 `len(object)`**

   ```
   >>> append(...) method of builtins.list instance 
       L.append(object) -> None -- append object to end
   >>> extend(...) method of builtins.list instance
       L.extend(iterable) -> None -- extend list by appending elements from the ite
   rable
   
   In [27]: a = [1,2,3]
   In [28]: b1 = [11,22,33]
   In [29]: b2 = [111,222,333]
   In [30]: b1.append(a)
   In [31]: b1
   Out[31]: [11, 22, 33, [1, 2, 3]]
   In [32]: b2.extend(a)
   In [33]: b2
   Out[33]: [111, 222, 333, 1, 2, 3]		# difference with b1
   ```

   

## 四、random

1. 随机打乱顺序 `random.shuffle`

   `import random`

   `random.shuffle(x, random=None)`

   > `Shuffle list x in place, and return None. Method of random.Random instance`
   >
   > ​	`Optional argument random is a 0-argument function returning a random float in [0.0, 1.0); if it is the default None, the standard random.random will be used.`

   

   ```
   In [32]: listadict_desc_value = [('e', 74), ('b', 54), ('a', 21), ('c', 5), ('f', 3), ('d', 0)]
   In [33]: random.shuffle(listadict_desc_value)
   In [34]: listadict_desc_value
   Out[34]: [('a', 21), ('d', 0), ('c', 5), ('e', 74), ('b', 54), ('f', 3)]
   ```

## 五、循环

1. `continue` 和 `break`

   `continue:` 跳到<font color=mediumpurple>最近所在循环</font>的开头处

   `break:` 跳出<font color=mediumpurple>最近所在的循环</font>（跳过整个最近的循环语句）

   嵌套循环可以使用 return 跳出最外层循环 或者 使用 `嵌套for ...else...语句`

## 六、装饰器

举例：

```
# 定义装饰器，监控运行时间
def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        stop_time = time.perf_counter()
        print("Func {}, run time: {}".format(func.__name__, stop_time - start_time))
        return res
    return wrapper
```

## 七、文件读写

### 1. codec.open(...)

- **`codecs.open(filename, mode='r', encoding=None, errors='strict', buffering=1)`**
  1) *底层编码文件始终以二进制模式打开。读取和写入时不会自动转换'\n'。mode参数可以是内置open()函数可接受的任何二进制模式；'b'会自动添加*
  2) *encoding指定要用于该文件的编码。任何对字节进行编码和解码的编码都是允许的，并且文件方法支持的数据类型取决于所使用的编解码器*

- `codec.open()`与`open()`的区别
  `codecs`是Python中标准库的内容，而`codecs.open`和内置函数open（）的不同在于，open函数无法打开一份由不同编码组成的同一份文件，而`codecs.open`如文档所说，始终以二进制模式打开，故打开就是Unicode格式，所以，codecs.open能打开由不同编码格式组成的文件

- <font color=coral>BUT</font>, 建议不同编码格式组成的文件读写有问题时，直接采用 rb 模式 open，获得 byte类型，再通过字符串截取

  参考 推荐系统代码中的读取

  ```
  for line in open(self.bookmark_path, 'rb').readlines()[1:]:
  	line = str(line.strip())[2:-1].split(r'\t')    
  ```

  

## 常见错误或警告及解决方法

### 1.  版本过低

- `pip install --upgrade scipy`

