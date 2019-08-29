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

2. 字典排序（按`key`和按`value`排序）

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

     

## 二. 集合

### 1. `set.add` 集合添加元素



## 三、数组、列表

1. 数组转化为列表需要使用 `arr.tolist()`

   ```
   
   ```

2. `a.append(..)`和`a.extend(..)`的区别

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



## 常见错误或警告及解决方法

### 1.  版本过低

- `pip install --upgrade scipy`

