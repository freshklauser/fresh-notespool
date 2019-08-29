<div align=center style="font-size:24px";><b>Basic Terms in tensorflow</b></div>

[`Go to here`](https://developers.google.cn/machine-learning/crash-course/glossary#Estimators)

目录：

[TOC]

## 1.  不均衡数据集  <font color=LightCoral>Imbalanced Data</font>

### 1. 概念

​	一种二元分类问题，在此类问题中，两种类别的标签在出现频率方面具有很大的差距。例如，在某个疾病数据集中，0.0001 的样本具有正类别标签，0.9999 的样本具有负类别标签，这就属于分类不平衡问题；但在某个足球比赛预测器中，0.51 的样本的标签为其中一个球队赢，0.49 的样本的标签为另一个球队赢，这就不属于分类不平衡问题。

`imbalance-learn module in sklearn:`

> [`install and contribution`](http://imbalanced-learn.org/en/stable/install.html)`: pip install -U imbalanced-learn`
>
> 

### 2. 处理方式

参考：[机器学习中样本不平衡的处理方法](<https://zhuanlan.zhihu.com/p/28850865>)，[机器学习中如何处理不平衡数据？](<https://www.jiqizhixin.com/articles/021704>)，[`8-ReferPaper`](C:\Users\Wang\OneDrive\1-Python2Depth\8-ReferPaper)

[<font color=cyan>以下内容出处</font>](https://www.zhihu.com/question/30492527/answer/222719942)

#### 1. `sampling`技术: **通过过抽样和欠抽样解决样本不均衡** 

​	抽样是解决样本分布不均衡相对简单且常用的方法，包括过抽样和欠抽样两种。

过抽样

​	过抽样（也叫上采样、over-sampling）方法通过增加分类中少数类样本的数量来实现样本均衡，最直接的方法是简单复制少数类样本形成多条记录，这种方法的缺点是如果样本特征少而可能导致过拟合的问题；经过改进的过抽样方法通过在少数类中加入随机噪声、干扰数据或通过一定规则产生新的合成样本，例如经典过采样算法：<font color=orange>SMOTE</font>算法。

​	`SMOTE`算法是通过对少数样本进行插值来获取新样本的。新的少数类样本产生的策略：**对每个少数类样本a，在a的最近邻中随机选一个样本b，然后在a、b之间的连线上随机选一点作为新合成的少数类样本**。

欠抽样

​	欠抽样（也叫下采样、under-sampling）方法通过减少分类中多数类样本的样本数量来实现样本均衡，最直接的方法是随机地去掉一些多数类样本来减小多数类的规模，缺点是会**丢失多数类样本中的一些重要信息**。

​	总体上，过抽样和欠抽样更适合大数据分布不均衡的情况，尤其是第一种（过抽样）方法应用更加广泛。

#### 2. `Cost-sensitive`学习器： **通过正负样本的惩罚权重解决样本不均衡**

​	通过正负样本的惩罚权重解决样本不均衡的问题的思想是在算法实现过程中，对于分类中不同样本数量的类别分别赋予不同的权重（一般思路分类中的小样本量类别权重高，大样本量类别权重低），然后进行计算和建模。

​	使用这种方法时需要对样本本身做额外处理，只需在算法模型的参数中进行相应设置即可。很多模型和算法中都有基于类别参数的调整设置，<font color=orange>允许算法改变权重weight变得cost-sensitive</font>。以`scikit-learn`中的<font color=orange>`SVM`</font>为例，通过在<font color=orange>`class_weight : {dict, 'balanced'}`</font>中针对不同类别针对不同的权重，来<font color=orange>手动指定不同类别的权重</font>。如果使用其默认的方法balanced，那么`SVM`会将权重设置为与不同类别样本数量呈反比的权重来做自动均衡处理，<font color=orange>计算公式</font>为：<font color=orange>`n_samples / (n_classes * np.bincount(y))`</font>。

​	如果算法本身支持安装class的比例来调整权重（weight）， 而形成`cost-senistive`的学习（如<font color=orange>`SVM`、`RandomForest`</font>），这种思路是更加简单且高效的方法。

#### 3. 组合集成方法：**通过组合/集成方法解决样本不均衡**

​	组合/集成方法指的是在每次生成训练集时使用所有分类中的小样本量，同时从分类中的大样本量中随机抽取数据来与小样本量合并构成训练集，这样反复多次会得到很多训练集和训练模型。最后在应用时，使用组合方法（例如投票、加权投票等）产生分类预测结果。<font color=orange>典型算法：`EasyEnsemble， BalanceCascade`</font>

​	例如，在数据集中的正、负例的样本分别为100和10000条，比例为1:100。此时可以将负例样本（类别中的大量样本集）随机分为100份（当然也可以分更多），每份100条数据；然后每次形成训练集时使用所有的正样本（100条）和随机抽取的负样本（100条）形成新的数据集。如此反复可以得到100个训练集和对应的训练模型。

​	这种解决问题的思路类似于随机森林。在随机森林中，虽然每个小决策树的分类能力很弱，但是通过大量的“小树”组合形成的“森林”具有良好的模型预测能力。

​	如果计算资源充足，并且对于模型的时效性要求不高的话，这种方法比较合适。

#### 4. **通过特征选择解决样本不均衡**

​	上述几种方法都是基于数据行的操作，通过多种途径来使得不同类别的样本数据行记录均衡。除此以外，还可以考虑使用或辅助于基于列的特征选择方法。

​	一般情况下，样本不均衡也会导致特征分布不均衡，但如果小类别样本量具有一定的规模，那么意味着其特征值的分布较为均匀，可通过选择具有显著型的特征配合参与解决样本不均衡问题，也能在一定程度上提高模型效果。

​	提示 上述几种方法的思路都是基于分类问题解决的。实际上，这种从大规模数据中寻找罕见数据的情况，也可以使用非监督式的学习方法，例如使用One-class SVM进行异常检测。分类是监督式方法，前期是基于带有标签（Label）的数据进行分类预测；而采用非监督式方法，则是使用除了标签以外的其他特征进行模型拟合，这样也能得到异常数据记录。所以，要解决异常检测类的问题，先是考虑整体思路，然后再考虑方法模型。

#### 5. 转化角度 --> 异常点检测问题

​	例如在分类问题时，把小类的样本作为异常点，将问题转化为异常点检测或变化趋势检测问题。 异常点检测即是对那些罕见事件进行识别。变化趋势检测区别于异常点检测在于其通过检测不寻常的变化趋势来识别。

>**Sampling技术：**
>
>优点：独立于学习器， 容易实现
>
>缺点：对噪音敏感， 容易欠拟合或者过拟合。
>
>**Cost-sensitive学习器：**
>
>优点：通过cost自动调节weight来修正bias。
>
>缺点：cost具有不确定性， 算法实现成本高
>
>**集成学习：**
>
>优点：效果比较好， 对噪音不敏感
>
>缺点：计算量大， 容易过拟合
>
>[`refer here`](<https://zhuanlan.zhihu.com/p/34782497>)

### 3. 评价指标

​	把`ACC`受到非均衡影响的叫`imbalance sensitive`的标准， 而把`AUC`这类的叫`imbalance non-sensitive`标准。 所以要<font color=orange>选择`non-sensitive`的标准来衡量非均衡数据</font>。 和`ACC`相关的`F-Measure`， 或者相关系数`Correlation Coefficient（CC）`， 以及决策树用的`tual Information（MI）`这些都是`sensitive`的，不推荐使用。 <font color=orange>`G-Mean`</font>，<font color=orange>` AUC`</font>， 以及基于`ROC`衍生的<font color=orange>`PCF-EC图`</font>`Probility Cost Function - Expected Cost）`等是`non-sensitive`的比较推荐。[`Refer link`](<https://zhuanlan.zhihu.com/p/34782322>)

![`class-imbalance`](.\img\imbalance-metrics-choices.jpg)



## 2. 形心`centroid`

聚类的中心，由 [**k-means**](https://developers.google.cn/machine-learning/crash-course/glossary#k-means) 或 [**k-median**](https://developers.google.cn/machine-learning/crash-course/glossary#k-median) 算法决定。例如，如果 k 为 3，则 k-means 或 k-median 算法会找出 3 个形心。

## 3. 检查点`checkpoint`

一种数据，用于捕获模型变量在特定时间的状态。借助检查点，可以导出模型[**权重**]，跨多个会话执行训练，以及使训练在发生错误之后得以继续（例如作业抢占）。请注意，[**图**]本身不包含在检查点中。

## 4. 凸集`convex set`

欧几里得空间的一个子集，其中任意两点之间的连线仍完全落在该子集内。例如，下面的四个图形第一行两个都是凸集，第二行两个都不是凸集：<font color=SlateBlue>`Another img import method`</font>

<div align=center><img src=".\img\convex_set.png" width="60%"/></div>
<div align=center><img src=".\img\nonconvex_set.png" width="60%"/></div>

## 5. 交叉熵

**对数损失函数**向**多类别分类问题**的一种泛化。交叉熵可以量化两种概率分布之间的差异

## 6. 困惑度

​	一种衡量指标，用于衡量模型能够多好地完成任务。例如，假设任务是读取用户使用智能手机键盘输入字词时输入的前几个字母，然后列出一组可能的完整字词。此任务的困惑度 (P) 是：为了使列出的字词中包含用户尝试输入的实际字词，您需要提供的猜测项的个数。

​	困惑度与交叉熵的关系如下： `P = 2^(- cross_entropy)`

## 7. 嵌套（embeddings）

​	一种分类特征，以连续值特征表示。通常，嵌套是指将高维度向量映射到低维度的空间。

## 8. 中心极限定理和大树定律

**中心极限定理**

​	样本的平均值约等于总体的平均值。不管总体是什么分布，任意一个总体的样本平均值都会围绕在总体的整体平均值周围，并且呈正态分布。 （**样本估计总体，正态分布**）

**大数定律**

​	随机试验中，每次出现的结果不同，但是大量重复试验出现的结果的平均值却几乎总是接近某个确定的值。

[`links here： go on learning tensorflow`](https://developers.google.cn/machine-learning/crash-course/glossary#Estimators)



