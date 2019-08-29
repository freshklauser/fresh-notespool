[TOC]



## 1. `Function of pd.DataFrame or pd`

`import pandas as pd`

1. `pd.DataFrame.drop_duplicates(...)`

   <font color=tomato>`drop_duplicates(self, subset=None, keep='first', inplace=False)`</font>
   	`Return DataFrame with duplicate rows removed, optionally only considering certain columns`

```
Parameters
----------
subset : column label or sequence of labels, optional
	Only consider certain columns for identifying duplicates, by default use all of the columns
keep : {'first', 'last', False}, default 'first'
    - ``first`` : Drop duplicates except for the first occurrence.
    - ``last`` : Drop duplicates except for the last occurrence.
    - False : Drop all duplicates.
inplace : boolean, default False. Whether to drop duplicates in place or to return a copy

Returns
-------
deduplicated : DataFrame
```

2. `pd.DataFrame.iterrows`

   ​	`Iterate over DataFrame rows as (index, Series) pairs.`

   `pd.DataFrame.iteritems`

   ​	`Iterate over <column name, Series> pairs.`

   `pd.DataFrame.itertuples(self, index=True, name="Pandas")`

   ​	`Iterate over DataFrame rows as namedtuples, with index value as first element of the tuple`

   ```
   df = pd.DataFrame({'col1':[1,2,3], 'col2':[.01,0.2,0.5], 'col3':[100, 300, 400]}, index=['a', 'b', 'c'])
   print(df)
           col1  col2  col3
       a     1  0.01   100
       b     2  0.20   300
       c     3  0.50   400
   # ---------------------------
   for row in df.iterrows():
   ... 	print(row[0])
   ... 	print('---')
   ... 	print(row[1])
   	a
       ---
       col1      1.00
       col2      0.01
       col3    100.00
       Name: a, dtype: float64
   ```




## 2. 设置选项 pd.set_option

省略号显示问题：通过print输出Dataframe中的数据，当Dataframe行数很多时，中间部分显示省略号.

通过查看pandas的官方文档可知，pandas.set_option() 可以设置pandas相关的参数，从而改变默认参数。 打印pandas数据时，默认是输出100行，多的话中间数据会输出省略号。

在代码中添加以下两行代码，可以改变显示宽度和行数，这样就能完整地查看数据了

```
pd.set_option('display.width', 1000) # 设置字符显示宽度

pd.set_option('display.max_rows', None) # 设置显示最大行

pd.set_option('display.max_columns', None) # 设置显示最大列
```

