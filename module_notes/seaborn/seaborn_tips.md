<



目录

[TOC]

## 1. Reference

[`API Reference is here!`](http://seaborn.pydata.org/api.html)

[`Case Reference by myself is here(Inculding some setting details of the plot)!`](https://www.kaggle.com/kernels/scriptcontent/6309253/notebook)

## 2. 基本设置

### 1. 主题`set_style`

`import seaborn as sns`

`sns.set_style(...)`

> `set_style("ticks", {"xtick.major.size": 8, "ytick.major.size": 8})`
>
> >     set_style(style=None, rc=None)
> >         Set the aesthetic style of the plots.	  
> >         This affects things like the color of the axes, whether a grid is
> >         enabled by default, and other aesthetic elements.
>
> `Parameters:`
>
> >     `style : dict, None, or one of {darkgrid, whitegrid, dark, white, ticks}`
> >     	 `A dictionary of parameters or the name of a preconfigured set.`
> >     `rc : dict, optional`
> >     	`Parameter mappings to override the values in the preset seaborn
> >          style dictionaries. This only updates parameters that are
> >          considered part of the style definition.`
> >
> >     `return a dict of parameters or use in a ``with`` statement to temporarily set the style.`

`senborn`是对`matplotlib`的封装，有5中样式的`image theme`

主题样式：

- `darkgrid` `:` 
- `whitegrid`：只有水平方向网格，
- `dark`
- `white`
- `ticks`

`sns.set():` 默认主题

​	![image](.\theme\default theme style.png)

`sns.set_style('whitegrid'):`设置主题样式为`whitestyle`

​	![`whitegrid`](.\theme\whitegrid.png)

`sns.set_style('white')`

​	![`white`](.\theme\white.png)

`sns.set_style('dark')`

​	![`dark`](.\theme\dark.png)

`sns.set_style('darkgrid')` `(default theme style is darkgrid)`

​	![`darkgrid`](.\theme\darkgrid.png)

`sns.set_style('ticks')`

​	![`ticks`](.\theme\ticks.png)

### 2. 坐标轴spine

`sns.despine()`：去掉坐标轴的 `right`和`top`轴

​	![`sns.despine`](.\theme\despine.png)

> `despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
>     Remove the top and right spines from plot(s).`
>
> `params:`
>
> > `    fig : matplotlib figure, optional
> >         Figure to despine all axes of, default uses current figure.
> >  ax : matplotlib axes, optional. Specific axes object to despine.
> >  top, right, left, bottom : boolean, optional. If True, remove that spine.
> >  offset : int or dict, optional.
> >         Absolute distance, in points, spines should be moved away
> >         from the axes (negative values move spines inward). A single value
> >         applies to all spines; a dict can be used to set offset values per
> >         side.图距离坐标轴的偏移距离.
> >  trim : bool, optional.
> >         If True, limit spines to the smallest and largest major tick
> >         on each non-despined axis.`

`sns.despine(top=False, right=False, offset=50):`

​	![`set offset of despine`](.\theme\despine_offset.png) 

### 3. 子图差异化风格

采用 `with`语句实现单个子图的风格设置。如下图，子图1与2的`theme style`是不同的

`code`:

>`with sns.axes_style("ticks"):
>    plt.subplot(211)
>    #sns.despine(top=True, left=True, offset=10)
>    sinplot()
>plt.subplot(212)
>sinplot(-1)`

​	![`theme style for subplot`](.\theme\theme style for subplot.png)![`theme subplot2`](.\theme\theme style for subplot2.png)

### 4. 背景/环境变量 `set_context`

`sns.set_context`(...)

> `set_context("talk", font_scale=1.5, rc={"lines.linewidth": 2})`
>
> ```
> set_context(context=None, font_scale=1, rc=None)
>         Set the plotting context parameters.
>    
>         This affects things like the size of the labels, lines, and other
>         elements of the plot, but not the overall style. The base context
>         is "notebook", and the other contexts are "paper", "talk", and "poster",
>         which are version of the notebook parameters scaled by .8, 1.3, and 1.6,
>         respectively.
>    
>         Parameters
>         ----------
>         context : dict, None, or one of {paper, notebook, talk, poster}
>             A dictionary of parameters or the name of a preconfigured set.
>         font_scale : float, optional
>             Separate scaling factor to independently scale the size of the
>             font elements.
>         rc : dict, optional
>             Parameter mappings to override the values in the preset seaborn
>             context dictionaries. This only updates parameters that are
>             considered part of the context definition.
> ```

### 5. 调色板`set_palette`

`sns.set_palette(...)`

> `set_palette("Set1", 8, .75)`
>
> > ```
> > set_palette(palette, n_colors=None, desat=None, color_codes=False)
> >      Set the matplotlib color cycle using a seaborn palette.
> >      
> >      Parameters
> >      ----------
> >      palette : seaborn color paltte | matplotlib colormap | hls | husl
> >          Palette definition. Should be something that :func:`color_palette`
> >          can process.
> >      n_colors : int
> >          Number of colors in the cycle. The default number of colors will depend
> >          on the format of ``palette``, see the :func:`color_palette`
> >          documentation for more information.
> >      desat : float
> >          Proportion to desaturate each color by.
> >      color_codes : bool
> >          If ``True`` and ``palette`` is a seaborn palette, remap the shorthand
> >          color codes (e.g. "b", "g", "r", etc.) to the colors from this palette.
> > ```

调色板`palette:`

- `color_palette()`返回调色板，能传入任何`matplotlib`所支持的颜色，不写参数则默认颜色
- `set_palette()`**<!--设置所有图的颜色-->**，也可以用`with`语句设置临时颜色

1. 分类色板

   6个默认的颜色循环主题：`deep, muted, pastel, dark, bright, colorblind`。新版如下图所示默认有10个默认离散颜色块：

   `current_palette = sns.color_palette()`

   `sns.palplot(current_palette) `

   > `sns.color_palette(palette=None, n_colors=None, desat=None):`
   >
   > ​	`Return a list of colors defining a color palette.`
   >
   > ​	` n_colors : int, optional. Number of colors in the palette`        
   >
   > `sns.palplot(pal, size=1):`
   >
   > ​	`Plot the values in a color palette as a horizontal array.`

   ![`color palette`](.\color\color_palette default.png)

   

2. 圆形画板

   ​	在一个圆形的颜色空间中画出均匀间隔的颜色(这样的色调会保持亮度和饱和度不变)。这是大多数的当他们需要使用比当前默认颜色循环中设置的颜色更多时的默认方案。

   ​	最常用的方法是使用`hls`的颜色空间，这是`RGB`值的一个简单转换。

   - `sns.palplot(sns.color_palette(palette='hls', 10))`

     > `pal:ette:`
     >
     > ​	`deep, muted, bright, pastel, dark, colorblind(seaborn palette names)`
     >
     > ​	`matplotlib cmap:hls, husl or lots of others(refering to website)`

   ![`color_palette`](.\color\color_palette define2.png)

   - `sns.palplot(sns.hls_palette(n_colors=6, h=0.01, l=0.6, s=0.65)):`

     > `sns.hls_palette: Get a set of evenly spaced colors in HLS hue space`
     >
     > ​	`n_colors: numer of colors in the palette`
     >
     > ​	`h: float, first hue(色调)`
     >
     > ​	`l: float, lightness(亮度)`
     >
     > ​	`s: float, saturation(饱和度)`

3. 连续色板

   色彩随数据变换，比如数据越来越重要则颜色越来越深，如果想要翻转渐变，可以在面板名称中添加一个`_r`后缀

   - `sns.palplot(sns.color_palette('Purples'))	# cmap refers to website`![`cmap_purples`](.\color\purples_cmap.png)

   - 色调线性变换`cmap: cubehelix` `or sns.cubehelix_palette()`

     `sns.palplot(sns.color_palette("cubehelix", 10))`

     `sns.palplot(sns.cubehelix_palette(8, start=0.5, rot=-0.75))`![`cmap_cubehelix`](.\color\cmap_cubehelix.png)

   - 定制连续调色板 `light_palette or dark_palette`

     `sns.palplot(sns.light_palette('green'))`![`light_palette`](.\color\light_palette.png)

     `sns.palplt(sns.dark_palette('purple'))` ![`dark_palette`](.\color\dark_palette.png)

## 3. 分类图 Categorical plots  ( catplot &radic; )

- <font color=limegreen,>`seaborn.catplot(...)`</font> 通过设置<font color=limegreen>`kind`参数</font>可以实现各种分类属性的图（<font color=#1E90FF>能实现很多类型的图，推荐多看看</font>）[`Link is here`](http://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot)

  `catplot`**(**<font color=Orange>x</font>=None**,** <font color=Orange>y</font>=None**,**<font color=Orange> hue</font>=None**,** <font color=orange>data</font>=None**,** *row=None***,** *col=None***,** *col_wrap=None***,** *estimator=<function mean>***,** *ci=95***,** *n_boot=1000***,** *units=None***,** *order=None***,** *hue_order=None***,** *row_order=None***,** *col_order=None***,** <font color=orange>kind='strip'</font>**,** *height=5***,** *aspect=1***,** *orient=None***,** *color=None***,** <font color=orange>palette</font>=None**,** *legend=True***,** *legend_out=True***,** *sharex=True***,** *sharey=True***,** *margin_titles=False***,** *facet_kws=None***,** ***kwargs***)

  > ```
  > g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise, kind="violin")
  > g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)
  > ```

  > `Main params:`
  >
  > > `kind: strip散点， swarm分散点，violin提琴`
  > >
  > > `aspect: 纵横比； orient方向v/h； palette调色板...`
  >
  > `Return:`
  >
  > > <font color=skyblue>`g: FacetGrid`</font>.`Returns the FacetGrid object with the plot on it for further tweaking.`

  ![`catplot_facetgrid`](.\figure\seaborn-catplot-7.png)

- `Categorical scatterplots:`

  - [`stripplot()`](http://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot) (with `kind="strip"`; the default) 

    `stripplot`**(**<font color=Orange>x</font>=None**,** <font color=Orange>y</font>=None**,** <font color=Orange>hue</font>=None**,** <font color=Orange>data</font>=None**,** *order=None***,** *hue_order=None***,** <font color=Orange>jitter=True</font>**,** <font color=Orange>dodge</font>=False**,** *orient=None***,** *color=None***,** <font color=Orange>palette</font>=None**,** *size=5***,** *edgecolor='gray'***,** *linewidth=0***,** *ax=None***,** ***kwargs***)

    >```
    >ax = sns.stripplot(x="day", y="total_bill", hue="smoker", data=tips, jitter=True, palette="Set2", dodge=True)
    >```

    > `params:`
    >
    > > `jitter:`  `jitter=True`则`hue`指定的字段数据会散布开来，而不是所有数据在同一条线上
    > >
    > > `dodge:` `hue`定义时，`dodge=True`则hue对应的数据会根据类别分开显示(如下图Yes和No对应 的数据点分开显示， 而不是橙色和青色混在一起)	
    >
    > `return:` <font color=orange>`ax: matplotlib Axes`</font>. `Returns the Axes object with the plot drawn onto it.`

    ![`stripplot`](.\figure\seaborn-stripplot-8.png)

  - [`swarmplot()`](http://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot) (with `kind="swarm"`)

    `swarmplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** <font color=orange>data</font>=None**,** *order=None***,** *hue_order=None***,** *<font color=orange>dodge=False</font>***,** *orient=None***,** *color=None***,** <font color=orange>*palette=None*</font>**,** *size=5***,** *edgecolor='gray'***,** *linewidth=0***,** *ax=None***,** ***kwargs***)**

    >```
    >ax = sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)
    >```

    > `return:`: <font color=orange>`ax: matplotlib Axes`</font>. `Returns the Axes object with the plot drawn onto it.`

    ![`swarmplot`](.\figure\seaborn-swarmplot-2.png)

- `Categorical distribution plots:`

  - [`boxplot()`](http://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot) (with `kind="box"`)

    `boxplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** <font color=orange>data</font>=None***,** *order=None***,** *hue_order=None***,** *orient=None***,** *color=None***,** *palette=None***,** *saturation=0.75***,** *width=0.8***,** *dodge=True***,** <font color=orange>*fliersize=5*</font>**,** *linewidth=None***,** <font color=skyblue>*whis=1.5*</font>**,** *notch=False***,** *ax=None***,** ***kwargs***)

    >```
    >ax = sns.boxplot(x="day", y="total_bill", hue="time", data=tips, linewidth=2.5)
    >```

    >`params:`
    >
    >> `fliersize: float, optional. Size of markers used to indicate outlier observations.`
    >>
    >> `whis: Proportion of IQR past the low and high quartiles to extend the plot whiskers.` 	  `Points outside this range will be identified as` <font color=skyblue>`outliers(1.5IQR)`</font>.
    >
    >`return:`: <font color=orange>`ax: matplotlib Axes`</font>. `Returns the Axes object with the plot drawn onto it.`

    ![`boxplot`](.\figure\seaborn-boxplot-4.png)

  - [`violinplot()`](http://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot) (with `kind="violin"`)

    `violinplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** *data=None***,** *order=None***,** *hue_order=None***,** *bw='scott'***,** *cut=2***,** <font color=orange>*scale='area'*</font>**,** *scale_hue=True***,** *gridsize=100***,** *width=0.8***,** *inner='box'***,** <font color=orange>*split=False*</font>**,** *dodge=True***,** *orient=None***,** *linewidth=None***,** *color=None***,** *palette=None***,** *saturation=0.75***,** *ax=None***,** ***kwargs***)

    >```
    >ax = sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted", split=True, scale='count')
    >```

    >`params:`
    >
    >> `scale: {area(default), count, width},`
    >>
    >> ​	`If area, each violin will have the same area.`
    >>
    >> ​	`If count, violin's width will be scaled by number of observations in that bin.` 
    >>
    >> ​	`If width, each violin will have the same width.`
    >>
    >> `split: bool, optional.`
    >>
    >>  	`split=True 则violin左右两侧表示的是两个不同属性的数据`
    >>
    >> ​	 `如下图sex中的Male和Female, violin左侧为Male, 右侧为Female） `
    >
    >`return:`: <font color=orange>`ax: matplotlib Axes`</font>. `Returns the Axes object with the plot drawn onto it.`

    ![`violinplot`](.\figure\seaborn-violinplot-6.png)

    

  - [`boxenplot()`](http://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn.boxenplot) (with `kind="boxen"`)

    ![`boxenplot`](.\figure\seaborn-boxenplot-2.png)

- `Categorical estimate plots:`

  - [`pointplot()`](http://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot) (with `kind="point"`)

    `pointplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** <font color=orange>data</font>=None**,** *order=None***,** *hue_order=None***,** *estimator=<function mean>***,** <font color=orange>*ci=95*</font>**,** *n_boot=1000***,** *units=None***,** <font color=orange>*markers='o'*</font>**,** <font color=orange>*linestyles='-'*</font>**,** *dodge=False***,** *join=True***,** *scale=1***,** *orient=None***,** *color=None***,** *palette=None***,** *errwidth=None***,** *capsize=None***,** *ax=None***,** ***kwargs***)

    >```
    >ax = sns.pointplot(x="time", y="total_bill", hue="smoker", data=tips, markers=["o", "x"], linestyles=["-", "--"])
    >```

    >`params:`
    >
    >> `ci: 置信区间，float or “sd” or None. if sd,tandard deviation. if None,no draw`
    >
    >`return:`: <font color=orange>`ax: matplotlib Axes`</font>. `Returns the Axes object with the plot drawn onto it.`

    ![`pointplot`](.\figure\seaborn-pointplot-4.png)

  - [`barplot()`](http://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot) (with `kind="bar"`)

    `barplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** <font color=orange>data</font>=None**,** order=None***,** *hue_order=None***,** *estimator=<function mean>***,** <font color=orange>*ci=95*</font>**,** *n_boot=1000***,** *units=None***,** *orient=None***,** *color=None***,** *palette=None***,** *saturation=0.75***,** *errcolor='.26'***,** *errwidth=None***,** *capsize=None***,** *dodge=True***,** *ax=None***,** ***kwargs***)

    >```
    >ax = sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
    >```

    >`params:`
    >
    >> `ci: 置信区间，float or “sd” or None. if sd,tandard deviation. if None,no draw`
    >>
    >> `order: Order to plot the categorical levels in(x轴顺序)`
    >
    >`return:`: <font color=orange>`ax: matplotlib Axes`</font>. `Returns the Axes object with the plot drawn onto it.`

    ![`boxplot`](.\figure\seaborn-barplot-2.png)

  - [`countplot()`](http://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot) (with `kind="count"`)

    `countplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** <font color=orange>data</font>=None**,** *order=None***,** *hue_order=None***,** *orient=None***,** *color=None***,** *palette=None***,** *saturation=0.75***,** *dodge=True***,** *ax=None***,** ***kwargs***)

    >```
    >ax = sns.countplot(x="class", hue="who", data=titanic)
    >```

    >`return:`: <font color=orange>`ax: matplotlib Axes`</font>. `Returns the Axes object with the plot drawn onto it.`

    ![`countplot`](.\figure\seaborn-countplot-2.png)

## 4. 分布图 Distribution plots  ????????????

- [`jointplot`](http://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot)`(x, y[, data, kind, stat_func, …])` 双标图

  > `Draw a plot of two variables with bivariate and univariate graphs.A convenient interface to the JointGrid class, with several canned plot kinds.if you need more flexibility, you should use JointGrid directly.` <font color=orange>`JointGrid`的轻量级封装</font>

  `jointplot`**(**<font color=orange>x</font>**,** <font color=orange>y</font>**,** <font color=orange>data</font>=None**,** <font color=orange>kind</font>='scatter'**,** *stat_func=None***,** *color=None***,** *height=6***,** *ratio=5***,** *space=0.2***,** *dropna=True***,** *xlim=None***,** *ylim=None***,** *joint_kws=None***,** *marginal_kws=None***,** *annot_kws=None***,** ***kwargs***)

  > ```
  > g = (sns.jointplot("bill", "tip", data=tips, kind="hex").set_axis_labels("x", "y"))
  > ```

  > `params:`
  >
  > > `kind : { “scatter” | “reg” | “resid” | “kde” | “hex” }, optional`
  >
  > `return:`: <font color=skyblue>`grid: JointGrid`</font>. `Returns the JointGrid object with the plot on it..`

<div align=center><img src=".\figure\seaborn-jointplot-6.png" width="45%"/><img src=".\figure\seaborn-jointplot-4.png" width="45%"/></div>

- [`pairplot`](http://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot)`(data[, hue, hue_order, palette, …])`

  ​        `Plot pairwise relationships in a dataset.`

- [`distplot`](http://seaborn.pydata.org/generated/seaborn.distplot.html#seaborn.distplot)`(a[, bins, hist, kde, rug, fit, …])`

  ​	`Flexibly plot a univariate distribution of observations.`

- [`kdeplot`](http://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot)`(data[, data2, shade, vertical, …])`

  ​	`Fit and plot a univariate or bivariate kernel density estimate.`

- [`rugplot`](http://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot)`(a[, height, axis, ax])`

  ​	`Plot datapoints in an array as sticks on an axis.`

## 5. 相关图 Relational plots

- [`relplot`](http://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot)`([x, y, hue, size, style, data, row, …])`

  > `Figure-level interface for drawing relational plots onto a FacetGrid.`

  `relplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** <font color=orange>style</font>=None**,** <font color=orange>*size=None*</font>**,** <font color=orange>data</font>=None**,** *row=None***,** *col=None***,** *col_wrap=None***,** *row_order=None***,** *col_order=None***,** *palette=None***,** *hue_order=None***,** *hue_norm=None***,** *sizes=None***,** *size_order=None***,** *size_norm=None***,** *markers=None***,** *dashes=None***,** *style_order=None***,** *legend='brief'***,** <font color=orange>*kind='scatter'*</font>**,** *height=5***,** *aspect=1***,** *facet_kws=None***,** ***kwargs***)

  >```
  >g = sns.relplot(x="total_bill", y="tip", hue="day", col="time", row="sex", data=tips)
  >```

  > `Main params:`
  >
  > > `size : name of variables in `data` or vector data, optional`.散点大小
  > >
  > > `style: name of variables in data or vector data, optional` 散点形状`marker`
  > >
  > > `row, col: vars name, opt.Categorical variables that will determine faceting of the grid.`
  > >
  > > `kind: {scatter and line}.Kind of plot to draw`
  >
  > <font color=skyblue>`g: FacetGrid`</font>.`Returns the FacetGrid object with the plot on it for further tweaking.`

  <div align=center><img src=".\figure\seaborn-relplot-3.png" width="80%"/></div>

- [`scatterplot`](http://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot)`([x, y, hue, style, size, data, …])`

  > `Draw a scatter plot with possibility of several semantic groupings.`

  `scatterplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** <font color=orange>style</font>=None**,** <font color=orange>*size=None*</font>**,** <font color=orange>data</font>=None**,** *palette=None***,** *hue_order=None***,** *hue_norm=None***,** *sizes=None***,** *size_order=None***,** *size_norm=None***,** *markers=True***,** *style_order=None***,** *x_bins=None***,** *y_bins=None***,** *units=None***,** *estimator=None***,** *ci=95***,** *n_boot=1000***,** *alpha='auto'***,** *x_jitter=None***,** *y_jitter=None***,** *legend='brief'***,** *ax=None***,** ***kwargs***)

  >```
  >cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
  >ax = sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", palette=cmap, data=tips)
  >```

  > `Main pramas:`
  >
  > > `size : name of variables in `data` or vector data, optional`.散点大小
  > >
  > > `style: name of variables in data or vector data, optional` 散点形状`marker`
  >
  > `return:`: <font color=orange>`ax: matplotlib Axes`</font>.` Returns the Axes object with the plot drawn onto it`

  <div align=center><img src=".\figure\seaborn-scatterplot-8.png" width="45%"/><img src=".\figure\seaborn-scatterplot-4.png" width="45%"/></div>

- [`lineplot`](http://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot)`([x, y, hue, size, style, data, …])`

  > `Draw a line plot with possibility of several semantic groupings.`

  `lineplot`**(**<font color=orange>x</font>=None**,** <font color=orange>y</font>=None**,** <font color=orange>hue</font>=None**,** <font color=orange>style</font>=None**,** <font color=orange>*size=None*</font>**,** <font color=orange>data</font>=None**,** *palette=None***,** *hue_order=None***,** *hue_norm=None***,** *sizes=None***,** *size_order=None***,** *size_norm=None***,** <font color=orange>*dashes=True*</font>**,** *markers=None***,** *style_order=None***,** *units=None***,** *estimator='mean'***,** *ci=95***,** *n_boot=1000***,** <font color=orange>*sort=True*</font>**,** *err_style='band'***,** *err_kws=None***,** *legend='brief'***,** *ax=None***,** ***kwargs***)

  > ```
  > ax = sns.lineplot(x="timepoint", y="signal", hue="event", style="event", data=fmri)
  > ```

  > `Main params:`
  >
  > > `sort: boolean, optional. If True, data will be sorted by the x and y variables,`
  > >
  > > `err_style : “band” or “bars”, optional. Default is "band"`
  >
  > `return:`: <font color=orange>`ax: matplotlib Axes`</font>.` Returns the Axes object with the plot drawn onto it`

  <div align=center><img src=".\figure\seaborn-lineplot-6.png" width="45%"/><img src=".\figure\seaborn-lineplot-14.png" width="45%"/></div>

## 6. 矩阵图 Matrix plots

- [`heatmap`](http://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap)`(data[, vmin, vmax, cmap, center, …])`

  ​	`Plot rectangular data as a color-encoded matrix.`

  `heatmap`**(**<font color=orange>data</font>**,** <font color=orange>vmin</font>=None**,** <font color=orange>vmax</font>=None**,** <font color=orange>cmap</font>=None**,** *center=None***,** *robust=False***,** <font color=orange>annot=None</font>**,** *fmt='.2g'***,** *annot_kws=None***,** <font color=orange>linewidths=0</font>**,** *linecolor='white'***,** *cbar=True***,** *cbar_kws=None***,** *cbar_ax=None***,** *square=False***,** *xticklabels='auto'***,** *yticklabels='auto'***,** *mask=None***,** *ax=None***,** ***kwargs***)

  ```
  ax = sns.heatmap(flights, vmax=3, vmin=-2, center=1, annot=True, linewidths=.5)
  ```

> `Main params:`
>
> > `vmin, vmax, center: min, max val and val of the colorbar's center. 颜色bar的最大最小和中心值 `
> >
> > `cbar: boolean, whether to draw a colorbar.`
> >
> > `annot: if True, write the data value in each cell. `
> >
> > `linewidths=0.5: 效果如下图左`
>
> `return:`: <font color=orange>`ax: matplotlib Axes`</font>.` Returns the Axes object with the plot drawn onto it`

<div align=center><img src=".\figure\seaborn-heatmap-6.png" width="45%"/>&nbsp<img src=".\figure\seaborn-heatmap-5.png" width="45%"/></div>

- [`clustermap`](http://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn.clustermap)`(data[, pivot_kws, method, …])`

  ​	`Plot a matrix dataset as a hierarchically-clustered heatmap.`

  [`Pls go to here for details`](http://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn.clustermap)

  <div align=center><img src=".\figure\seaborn-clustermap-4.png" width="35%"/>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<img src=".\figure\seaborn-clustermap-7.png" width="35%"/></div>

## 7. 回归图 Regression plots

- [`lmplot`](http://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot)`(x, y, data[, hue, col, row, palette, …])`

  ​	`Plot data and regression model fits across a FacetGrid.` -- <font color=tomato>`Combination of regplot and FacetGrid`</font>

  `lmplot`**(**<font color=orange>x</font>**,** <font color=orange>y</font>**,** <font color=orange>data</font>**,** <font color=orange>hue</font>=None**,** <font color=orange>col</font>=None**,** <font color=orange>row</font>=None**,** *palette=None***,** *col_wrap=None***,** *height=5***,** *aspect=1***,** *markers='o'***,** *sharex=True***,** *sharey=True***,** *hue_order=None***,** *col_order=None***,** *row_order=None***,** *legend=True***,** *legend_out=True***,** *x_estimator=None***,** *x_bins=None***,** *x_ci='ci'***,** *scatter=True***,** *fit_reg=True***,** *ci=95***,** *n_boot=1000***,** *units=None***,** *order=1***,** *logistic=False***,** *lowess=False***,** *robust=False***,** *logx=False***,** *x_partial=None***,** *y_partial=None***,** *truncate=False***,** *x_jitter=None***,** *y_jitter=None***,** *scatter_kws=None***,** *line_kws=None***,** *size=None***)**

  ```
  g = sns.lmplot(x="total_bill", y="tip", row="sex", col="time", data=tips, height=3)
  ```

> `Main params:`
>
> > `col, row : strings, Variables that define subsets of the data 更多分类变量进行平铺显示 `
> >
> > `col_wrap : int, optional.“Wrap” column variable at this width.每行最高平铺列数 `

<div align=center><img src=".\figure\seaborn-lmplot-3.png" width="45%"/>&nbsp<img src=".\figure\seaborn-lmplot-9.png" width="38.5%"/></div>

- [`regplot`](http://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot)`(x, y[, data, x_estimator, x_bins, …])`

  ​	`Plot data and a linear regression model fit.`

  ​	<font color=tomato>`Regplot is an axes-level function while lmplot is a figure-level function that combines regplot and FacetGrid.`</font>

  `regplot`**(**x**,** *y***,** *data=None***,** *x_estimator=None***,** *x_bins=None***,** *x_ci='ci'***,** *scatter=True***,** *fit_reg=True***,** *ci=95***,** *n_boot=1000***,** *units=None***,** *order=1***,** *logistic=False***,** *lowess=False***,** *robust=False***,** *logx=False***,** *x_partial=None***,** *y_partial=None***,** *truncate=False***,** *dropna=True***,** *x_jitter=None***,** *y_jitter=None***,** *label=None***,** *color=None***,** *marker='o'***,** *scatter_kws=None***,** *line_kws=None***,** *ax=None*)

> [`params go to here(main params are x, y and data)`](http://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot)
>
> `return:`: <font color=orange>`ax: matplotlib Axes`</font>.` Returns the Axes object containing the plot`

<div align=center><img src=".\figure\seaborn-lmplot-3.png" width="450" height="280"/></div>

- [`residplot`](http://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot)`(x, y[, data, lowess, x_partial, …])`

  ​	`Plot the residuals of a linear regression.`

  ​	[`Pls go to here for details(Actually not many details to refer to )`](http://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot)

## 8.  Multi-plot grids

### 1. Pair grids 对图   ( PairGrid )  &radic;

- [`PairGrid`](http://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid)(data[, hue, hue_order, palette, …])

  ​	`Subplot grid for plotting pairwise relationships in a dataset.`

  `PairGrid`**(**<font color=orange>data</font>**,** <font color=orange>hue</font>=None**,** *hue_order=None***,** *palette=None***,** *hue_kws=None***,** <font color=orange>vars</font>=None**,** *x_vars=None***,** *y_vars=None***,** *diag_sharey=True***,** *height=2.5***,** *aspect=1***,** *despine=True***,** *dropna=True***,** *size=None***)**

>`Main pramas:`
>
>> `vars: 可以是特征的子集`
>
>**`Methods of PairGrid:`**
>
>- [`PairGrid.map`](http://seaborn.pydata.org/generated/seaborn.PairGrid.map.html#seaborn.PairGrid.map)(func, **kwargs)
>
>​	`Plot with the same function in every subplot.`
>
>​	<font color=mediumpurple>`在对图PairGrid的每一个子图(包括对角线子图和非对角线子图)plot相同的func图，如g.map(plt.scatter, ...) `</font>
>
>```
>g = sns.PairGrid(iris)
>g = g.map(plt.scatter)	# 每一个subplot都相同，均为散点图，如下图左
>```
>
>- [`PairGrid.map_diag`](http://seaborn.pydata.org/generated/seaborn.PairGrid.map_diag.html#seaborn.PairGrid.map_diag)(func, **kwargs)
>
>​	`Plot with a univariate(单变量) function on each diagonal subplot.`
>
>​	<font color=mediumpurple>`每一个对角线子图都plot单变量图如plt.hist`</font>
>
>- [`PairGrid.map_offdiag`](http://seaborn.pydata.org/generated/seaborn.PairGrid.map_offdiag.html#seaborn.PairGrid.map_offdiag)(func, **kwargs)
>
>​	`Plot with a bivariate function on the off-diagonal subplots.`
>
><font color=mediumpurple>	`每一个非对角线子图都plot双变量子图如plt.scatter`</font>
>
>```
>g = sns.PairGrid(iris, hue="species") # 实例化PairGrid, 如下图中
>g = g.map_diag(plt.hist)	   		 # 对角线子图绘制hist图
>g = g.map_offdiag(plt.scatter) 		 # 非对角线子图绘制scatter图
>```
>
>- [`PairGrid.map_lower`](http://seaborn.pydata.org/generated/seaborn.PairGrid.map_lower.html#seaborn.PairGrid.map_lower)(func, **kwargs)
>
>​	`Plot with a bivariate function on the lower diagonal subplots.`
>
>​	<font color=mediumpurple>`每一个下对角线子图都plot双变量图如sns.kdeplot`</font>
>
>- [`PairGrid.map_upper`](http://seaborn.pydata.org/generated/seaborn.PairGrid.map_upper.html#seaborn.PairGrid.map_upper)(func, **kwargs)
>
>​	`Plot with a bivariate function on the upper diagonal subplots`
>
>​	<font color=mediumpurple>`每一个上对角线子图都plot双变量图如plt.scatter`</font>
>
>- **`PairGrid.add_legend([legend_data, title, label_order])`**
>
>​	`Draw a legend, maybe placing it outside axes and resizing the figure.`
>
>```
>g = sns.PairGrid(iris)				# 实例化PairGrid, 如下图右
>g = g.map_upper(plt.scatter)			# 对角线以上子图:scatter
>g = g.map_lower(sns.kdeplot, cmap="Blues") # 对角线以下子图:kdeplot
>g = g.map_diag(sns.kdeplot, lw=3, legend=False) # 对角线子图:kdeplot
>```
>
>- `PairGrid.savefig (*args, **kwargs): Save the figure.`
>
>- `PairGrid.set(**kwargs): Set attributes on each subplot Axes.`

<div align=center><img src=".\figure\seaborn-PairGrid-1.png" width="30%"/><img src=".\figure\seaborn-PairGrid-3.png" width="34%"/><img src=".\figure\seaborn-PairGrid-8.png" width="30%"/></div>

### 2. Joint grids 联合图  ( JointGrid )  &radic;

- [`JointGrid`](http://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid)(x, y[, data, height, ratio, …])

  ​	`Grid for drawing a bivariate(双变量) plot with marginal univariate（边缘单变量） plots.`

  `JointGrid`**(**<font color=orange>x</font>**,** <font color=orange>y</font>**,** <font color=orange>data</font>=None***,** *height=6***,** *ratio=5***,** *space=0.2***,** *dropna=True***,** *xlim=None***,** *ylim=None***,** *size=None***)

> **`Methods of JointGrid:`**
>
> - [`JointGrid.plot`](http://seaborn.pydata.org/generated/seaborn.JointGrid.plot.html#seaborn.JointGrid.plot)(<font color=orange>`joint_func`</font>, <font color=orange>`marginal_func`</font>[, …])
>
>   ​	`Shortcut to draw the full plot.`
>
>   ​	 <font color=mediumpurple>用`joint_func`指定的图绘制双变量图，用`marginal_func`指定的图绘制边缘上下的单变量图</font>
>
>   ```
>   g = sns.JointGrid(x="total_bill", y="tip", data=tips)
>   g = g.plot(sns.regplot, sns.distplot)		# 如下图左
>   ```
>
> - [`JointGrid.plot_joint`](http://seaborn.pydata.org/generated/seaborn.JointGrid.plot_joint.html#seaborn.JointGrid.plot_joint)(func, **kwargs)
>
>   ​	`Draw a bivariate plot of x and y.`
>
>   ​	 <font color=mediumpurple>用`func`指定的图绘制双变量图</font>
>
> - [`JointGrid.plot_marginals`](http://seaborn.pydata.org/generated/seaborn.JointGrid.plot_marginals.html#seaborn.JointGrid.plot_marginals)(func, **kwargs)
>
>   ​	`Draw univariate plots for x and y separately.`
>
>   ​	 <font color=mediumpurple>用`func`指定的图绘制边缘上下的单变量图</font>
>
>   ```
>   from scipy import stats
>   g = sns.JointGrid(x="total_bill", y="tip", data=tips)   # 如下图右
>   g = g.plot_joint(plt.scatter,color="g", s=40, edgecolor="white")
>   g = g.plot_marginals(sns.distplot, kde=False, color="g")
>   -------------------------------------------------------
>   ==> 等价于 g = g.plot(plt.scatter, sns.distplot)
>   -------------------------------------------------------
>   g = g.annotate(stats.pearsonr)
>   ```
>
> - **`JointGrid.annotate`**(func[, template, stat, loc]):
>
>   ​	`Annotate the plot with a statistic about the relationship.`
>
> - **`JointGrid.savefig`**(*args, **kwargs): 
>
>   ​	`Wrap figure.savefig defaulting to tight bounding box.`
>
> - **`JointGrid.set_axis_labels`**([xlabel, ylabel]):
>
>   ​	`Set the axis labels on the bivariate axes.`

<div align=center><img src=".\figure\seaborn-JointGrid-2.png" width="48%"/><img src=".\figure\seaborn-JointGrid-5.png" width="48%"/></div>

### 3. Facet grids  ( FacetGrid )  &radic; 

- [`FacetGrid`](http://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid)`(data[, row, col, hue, col_wrap, …])`

  ​	`Multi-plot grid for plotting conditional relationships.` 

  `FacetGrid`**(**<font color=orange>data</font>**,** <font color=orange>row</font>=None**,** <font color=orange>col=None</font>**,** <font color=orange>hue</font>=None**,** <font color=orange>col_wrap=None</font>**,** *sharex=True***,** *sharey=True***,** *height=3***,** *aspect=1***,** *palette=None***,** *row_order=None***,** *col_order=None***,** *hue_order=None***,** *hue_kws=None***,** *dropna=True***,** *legend_out=True***,** *despine=True***,** *margin_titles=False***,** *xlim=None***,** *ylim=None***,** *subplot_kws=None***,** *gridspec_kws=None***,** *size=None***)**

> **`Main methods of FacetGrid:`** [`links here in the bottom of page`](http://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid)
>
> - <font color=orange>[`FacetGrid.map`](http://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn.FacetGrid.map)`(func, *args, **kwargs)`</font>
>
> ​	`Apply a plotting function to each facet’s subset of the data.` 
>
> ​	<font color=mediumpurple>`在Facet的每一个子图上画一样的func图`</font>
>
> ```
> ordered_days = pd.Categorical(["Thur", "Fri", "Sat", "Sun"])
> g = sns.FacetGrid(tips,col="days",hue="smoker",col_order=orderd_days)
> g.map(plt.scatter, "total_bill", "tip", alpha=.7) 
> g.add_legend()
> ----------------------------------------------------------------
> # g.map(plt.scatter, ...) ===> FacetGrid.map(func, *args, **kwargs)
> ```

<div align=center><img src=".\figure\seaborn-FacetGrid-4.png" width="450" height="300"/></div>

**`Methods of FacetGrid:`**

| `init(data[, row, col, hue, col_wrap, …])`        | `Initialize the matplotlib figure and FacetGrid object.`     |
| :------------------------------------------------ | ------------------------------------------------------------ |
| `add_legend``([legend_data, title, label_order])` | `Draw a legend, maybe placing it outside axes and resizing the figure.` |
| `despine(**kwargs)`                               | `Remove axis spines from the facets.`                        |
| `facet_axis(row_i, col_j)`                        | `Make the axis identified by these indices active and return it.` |
| `facet_data`()                                    | `Generator for name indices and data subsets for each facet.` |
| `map(func, *args, **kwargs)`                      | `Apply a plotting function to each facet’s subset of the data.` |
| `map_dataframe(func, *args, **kwargs)`            | `Like .map but passes args as strings and inserts data in kwargs.` |
| `savefig (*args, **kwargs)`                       | `Save the figure.`                                           |
| `set`(**kwargs)                                   | `Set attributes on each subplot Axes.`                       |
| `set_axis_labels`([x_var, y_var])                 | `Set axis labels on the left column and bottom row of the grid.` |
| `set_titles ([template, row_template, …])  `      | `Draw titles either above each facet or on the grid margins.` |
| `set_xlabels ([label])`                           | ``Label the x axis on the bottom row of the grid.`           |
| `set_xticklabels ([labels, step])`                | `Set x axis tick labels on the bottom row of the grid.`      |
| `set_ylabels ([label])`                           | `Label the y axis on the left column of the grid.`           |
| `set_yticklabels ([labels])`                      | `Set y axis tick labels on the left column of the grid.`     |

`Attributes: ax | Easy access to single axes.`





<!--添加示意图，参数看情况 可以写一些主要的和tips,重点在常用的图-->

