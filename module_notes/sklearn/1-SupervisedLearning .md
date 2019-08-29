目录

[TOC]

## 1. Generalized Linear Models

​	`from sklearn import linear_model`

### **线性回归**

​	``  reg = linear_model.LinearRegression()``  

​	模型：`` LinearRegressio(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)``

​	系数：`reg.coef_`

### **Ridge回归**

​	`reg = linear_model.Ridge()`

​	`reg = linear_model.RidgeCV()`

​	`clf = linear_model.RidgeClassifier()`

​	`clf = linear_model.RidgeClassifierCV()`

​	正则化：L2

### **Lasso回归**

​	`reg = linear_model.Lasso()`

​	`reg = linear_model.LassoCV()`

​	 正则化：L1

### **Elastic-Net回归**

​	`reg = linear_model.ElasticNet()`

​	`reg = linear_model.ElasticNetCV()`

​	正则化：l1 and l2 with l1_ratio in [0, 1]

### **逻辑回归**

​	`reg = linear_model.LogisticRegression()`

​	`reg = linear_model.LogisticRegressionCV`

### **多项式回归**：

​	`from sklearn.preprocessing import PolynomialFeatures`

​	`from sklearn.pipeline import Pipeline`

​	将特征拓展为多项式特征，数据扩展，再利用管道连接模型

​	`poly = PolynomialFeatures(degree=2)`

​	`reg = Pipeline[('poly', PolynomialFeatures(degree=2)),('linear', inearRegression(fit_intercept=False))]`

### **梯度下降**

​	`from sklearn import linear_model`

​	`reg = linear_model.SGDRegressor(...)`

> `SGDRegressor(loss='squared_loss', penalty='l2', alpha=0.0001, l1_ratio=0.15,	fit_intercept=True,max_iter=None, tol=None, shuffle=True, verbose=0, epsilon=0.1, random_state=None, learning_rate='invscaling', eta0=0.01,power_t=0.25,warm_start=False, average=False, n_iter=None)`

​	`clf = linear_model.SGDClassifier`

## 2. KernelRidge（KRR）

​	`from sklearn import kernel_ridge`

### **核岭回归** KRR

​	`reg = kernel_ridge.KernelRidge(...)`

>`KernelRidge(alpha=1.0, coef0=1, degree=3, gamma=None, kernel='linear', kernel_params=None)`

## 3. Linear and Quadratic Discriminant Analysis（线性判别分析LDA和二次判别分析QDA）

​	`from sklearn import discriminant_analysis`

### **线性判别分析 LDA**

​	``  model= dicriminant.LinearDiscriminantAnalysis()``  

> `LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage=None,solver='svd', store_covariance=False, tol=0.0001)`



### **二次判别分析 QDA**

​	`model = dicriminant.QuadraticDiscriminantAnalysis()`

> `QuadraticDiscriminantAnalysis(priors=None, reg_param=0.0, store_covariance=False, tol=0.0001)`

## 4. SVM

​	`from sklearn import svm`

### **支持向量机**

​	`reg = svm.SVR(...)`

​	`reg = svm.LinearSVR`

​	`reg = svm.NuSVR`

​	`clf = svm.LinearSVC`

​	`clf = svm.NuSVC`

​	`clf = svm.SVC(...)`

​	参数 `Main pramas:`

```
`Pramas`:
    C : float, optional (default=1.0). Penalty parameter C of the error term.
    kernel : opt, default=’rbf’. {‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or callable.
    degree : opt, default=3.Degree of polynomial kernel(‘poly’). Ignored by all other kernels.
    gamma : float, optional (default=’auto’).Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’.
    probability : boolean, optional (default=False). Whether to enable probability estimates. 
    tol : float, optional (default=1e-3). Tolerance for stopping criterion.
    max_iter : int, opt (default=-1). Hard limit on iterations within solver, or -1 for no limit.
    decision_function_shape : ‘ovo’, ‘ovr’, default=’ovr’.
    		`ovr`/`ova` -- (n_samples, n_classes)
    		`ovo` -- (n_samples, n_classes * (n_classes - 1) / 2)
```

​	属性`Attributes`：

```
Attributes:	
    support_ : array-like, shape = [n_SV]. Indices of support vectors.
    support_vectors_ : array-like, shape = [n_SV, n_features]. Support vectors.
    n_support_ : array-like, dtype=int32, shape = [n_class].
    		Number of support vectors for each class.
    dual_coef_ : array, shape = [n_class-1, n_SV]	
    Coefficients of the support vector in the decision function. 
    coef_ : array, shape = [n_class * (n_class-1) / 2, n_features].
        	Weights assigned to the features (coefficients in the primal problem). This is only 			available in the case of a linear kernel.
    intercept_ : array, shape = [n_class * (n_class-1) / 2]. Constants in decision function.
    fit_status_ : int. 0 if correctly fitted, 1 otherwise (will raise warning)
    probA_ : array, shape = [n_class * (n_class-1) / 2]
    probB_ : array, shape = [n_class * (n_class-1) / 2]
        	If probability=True, the parameters learned in Platt scaling to produce probability 			estimates from decision values. If probability=False, an empty array. Platt scaling 			uses the logistic function 1 / (1 + exp(decision_value * probA_ + probB_)) where 				probA_ and probB_ are learned from the dataset [R20c70293ef72-2]. For more 						information on the multiclass case and training procedure see section 8 of 						[R20c70293ef72-1].
```

​	方法`Methods(svc)`：

```
decision_function(self, X): 
	Evaluates the decision function for the samples in X.
fit(self, X, y[, sample_weight]):
	Fit the SVM model according to the given training data.
get_params(self[, deep]):
	Get parameters for this estimator.
predict(self, X):
	Perform classification on samples in X.
score(self, X, y[, sample_weight]):
	Returns the mean accuracy on the given test data and labels.
set_params(self, \*\*params):
	Set the parameters of this estimator.
```

## 5. Nearest Neighbors

​	`from sklearn import neighbors`

### **寻找最近邻 的点**Find the Nearest Neighbors（unsupervised）

​	`nbrs = neighbors.NearestNeighbors(...)`

​	模型：`NearestNeighbors(n_neighbors=5, radius=1.0, algorithm=’auto’, leaf_size=30, metric=’minkowski’, p=2, metric_params=None, n_jobs=None, **kwargs)`

​	方法`Methods`：

​		`kneighbors(self[, X, n_neighbors, …])	---- Finds the K-neighbors of a point.`

>> `Examples`:
>>
>> ​	`nbrs = neighbors.NearestNeighbors(n_neighbors=5, algorithm='auto')`
>>
>> ​	`nbrs.fit(x)`
>>
>> ​	`nbrs_find = nbrs.keighbors(x_target, return_distance=False)`

### **Nearest Neighbor Algorithms**

​	`from sklearn.neighbors import KDTree, BallTree,  `

### **KNN**

​	`clf = neighbors.KNeighborsClassifier(...)`

​	`reg = neighbors.KNeighborsRegressor(...)`

​	模型：`KNeighborsClassifier(n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30, p=2, metric=’minkowski’, metric_params=None, n_jobs=None, **kwargs)`

​	方法`Methods(clf & reg)`：

	fit(self, X, y): 
		Fit the model using X as training data and y as target values 
	get_params(self[, deep]):
		Get parameters for this estimator.
	kneighbors(self[, X, n_neighbors, …]):
		Finds the K-neighbors of a point.
	kneighbors_graph(self[, X, n_neighbors, mode]):
		Computes the (weighted) graph` of k-Neighbors for points in X
	predict(self, X):
		Predict the class labels for the provided data
	predict_proba(self, X):
		Return probability estimates for the test data X.
	score(self, X, y[, sample_weight]):
		Returns the mean accuracy on the given test data and labels.
	set_params(self, \*\*params):
		Set the parameters of this estimator.
## 6. Naive Bayes

​	`from sklearn import naive_bayes`

​	`clf = naive_bayes.GaussianNB()`

​	模型： `GaussianNB(priors=None, var_smoothing=1e-09)`

​	方法`Methods`：

```
fit(self, X, y[, sample_weight]):
	Fit Gaussian Naive Bayes according to X, y
get_params(self[, deep]):
	Get parameters for this estimator.
partial_fit(self, X, y[, classes, sample_weight]):
	Incremental fit on a batch of samples.
predict(self, X):
	Perform classification on an array of test vectors X.
predict_log_proba(self, X):
	Return log-probability estimates for the test vector X.
predict_proba(self, X):
	Return probability estimates for the test vector X.
score(self, X, y[, sample_weight]):
	Returns the mean accuracy on the given test data and labels.
set_params(self, \*\*params):
	Set the parameters of this estimator.
```

## 7. Decision Trees

​	`from sklearn import tree`

​	`reg = tree.DecisionTreeRegressor()`

​	`clf = tree.DecisionTreeClassifier()`

> `DecisionTreeClassifier(criterion=’gini’, splitter=’best’, max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, class_weight=None, presort=False)`

​	属性`Attributes(clf)`：

	classes_ : array of shape = [n_classes] or a list of such arraysThe classes labels (single output 		problem), or a list of arrays of class labels (multi-output problem).
	feature_importances_ : array of shape = [n_features].Return the feature importances.
	max_features_ : int,The inferred value of max_features.
	n_classes_ : int or list.The number of classes (for single output problems), or a list containing 		the number of classes for each output (for multi-output problems).
	n_features_ : int.The number of features when fit is performed.
	n_outputs_ : int.The number of outputs when fit is performed.
	tree_ : Tree object.The underlying Tree object. Please refer to help(sklearn.tree._tree.Tree) for 		attributes of Tree object and Understanding the decision tree structure for basic usage of 		  these attributes.
​	方法`Methods(clf)`：

	apply(self, X[, check_input]):
		Returns the index of the leaf that each sample is predicted as.
	decision_path(self, X[, check_input]):
		Return the decision path in the tree
	fit(self, X, y[, sample_weight, …]):
		Build a decision tree classifier from the training set (X, y).
	get_depth(self):
		Returns the depth of the decision tree.
	get_n_leaves(self):
		Returns the number of leaves of the decision tree.
	get_params(self[, deep]):
		Get parameters for this estimator.
	predict(self, X[, check_input]):
		Predict class or regression value for X.
	predict_log_proba(self, X):
		Predict class log-probabilities of the input samples X.
	predict_proba(self, X[, check_input]):
		Predict class probabilities of the input samples X.
	score(self, X, y[, sample_weight]):
		Returns the mean accuracy on the given test data and labels.
	set_params(self, \*\*params):
		Set the parameters of this estimator.

## 8. Ensemble methods

​	`from sklearn import ensemble`

### 1. **`Averaging methods`**

#### `1) Bagging meta-estimator `

`clf= ensemble.BaggingClassifier(...)`

> ``BaggingClassifier(base_estimator=None, n_estimators=10, max_samples=1.0, max_features=1.0, bootstrap=True, bootstrap_features=False, oob_score=False, warm_start=False, n_jobs=None, random_state=None, verbose=0)`
>
> > `BaggingClassifier(KNeighborsClassifier(), max_samples=0.5, max_features=0.5)`
>
> `Main Parameters`：
>
> > `base_estimator : just one object or None, optional (default=None). `
> >
> > ​	`specified or NOne. If None, a decision tree is adopted.`
> >
> > `n_estimators : int, optional (default=10).The number of base estimators in the ensemble.`
> > `max_samples : int or float, optional (default=1.0).`
> >
> > ​	`Number of samples to draw from X to train each base estimator.`
> >
> > ​	`If int, then draw max_samples samples.`
> > ​	`If float, then draw "max_samples * X.shape[0]" samples.`
> >
> > `max_features : int or float, optional (default=1.0)`
> >
> > ​	`Similar with that of max_samples, for features extraction`
> >
> > `random_state: int, RandomState instance or None, optional (default=None)`
> >
> > `n_jobs: int or None ,optional(default=None)`
>
> `Attributes`：
>
> > `base_estimator_ : estimator.The base estimator from which the ensemble is grown.`
> >
> > `estimators_ : list of estimators.The collection of fitted base estimators.`
> >
> > `estimators_samples_ : list of arrays.Subset of drawn samples for each base estimator.`
> >
> > `estimators_features_ : list of arrays.Subset of drawn features for each base estimator.`
> >
> > `classes_ : array of shape = [n_classes].The classes labels.`
> >
> > `n_classes_ : int or list.The number of classes.`
> >
> > `oob_score_ : float. Score of the training dataset obtained using an out-of-bag estimate.`
> >
> > `oob_decision_function_ : array of shape = [n_samples, n_classes]`
> >
> > > `Decision function computed with out-of-bag estimate on the training set. If 	n_estimators is small it might be possible that a data point was never left out during the bootstrap. In this case, oob_decision_function_ might contain NaN.`从训练样本中取数据的决策函数。如果`estimator`取的少，则可能有样本会从没被取出来过，导致`oob_decision_function`中存在NaN值
>
> `Methods`：
>
> > `decision_function(self, X): Average of the decision functions of the base classifiers.`
> > `fit(self,X,y[, samp_weight]): Build Bagging ensemble estimator from training set (X, y).`
> > `get_params(self[, deep]): Get parameters for this estimator.`
> > `predict(self, X): Predict class for X.`
> > `predict_log_proba(self, X): Predict class log-probabilities for X.`
> > `predict_proba(self, X): Predict class probabilities for X.`
> > `score(self, X, y[, sample_weight]):Returns mean accuracy on given test data and labels.`
> > `set_params(self, \*\*params): Set the parameters of this estimator.`

`reg = ensemble.BaggingRegressor(...)`

>`BaggingRegressor(base_estimator=None, n_estimators=10, max_samples=1.0, max_features=1.0, bootstrap=True, bootstrap_features=False, oob_score=False, warm_start=False, n_jobs=None, random_state=None, verbose=0)`
>
>`Main Parameters:`
>
>> `Similar with that of clf`
>
>`Attributes:`
>
>> `estimators_ : list of estimators.The collection of fitted sub-estimators.`
>>
>> `estimators_samples_ : list of arrays.Subset of drawn samples for each base estimator.`
>>
>> `estimators_features_ : list of arrays.Subset of drawn features for each base estimator.`
>>
>> `oob_score_: float. Score of the training dataset obtained using an out-of-bag estimate.`
>>
>> `oob_prediction_: array of shape = [n_samples]. Refer to that of clf's attributes`
>
>`Methods:`
>
>>`fit(self,X,y[, sam_weight]): Build Bagging ensemble estimators from training set (X, y).`
>>`get_params(self[, deep]): Get parameters for this estimator.`
>>`predict(self, X): Predict regression target for X.`
>>`score(self, X, y[, samp_weight]): Returns coeffs of determination R^2 of the prediction.`
>>`set_params(self, \*\*params): Set the parameters of this estimator.`

#### `2) Forests of randomized trees `

`reg = ensemble.RandomForestRegressor(...)`

> ...

`clf = ensemble.RandomForestClassifier(...)`

>`RandomForestClassifier(n_estimators=’warn’, criterion=’gini’, max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=’auto’, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, class_weight=None)` <font color=mediumpurple>`(可以直接处理multi-label problem)`</font>
>
>>`RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)`
>
>`Parames:`
>
>> `Reger to :` [`params are here`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier)
>
>`Attributes:`
>
>>`estimators_ : list of DecisionTreeClassifier`
>>
>>``classes_ : array of shape = [n_classes] or a list of such arrays`
>>
>>​	`classes labels (single output problem), list of lass labels arr (multi-output problem).`
>>
>>`n_classes_ : int or list, classes number(single output) or list of numbers(muilti-label)` 
>>
>>`n_features_ : int`
>>
>>`n_outputs_ : int`
>>
>>[`feature_importances_`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.feature_importances_)`: array of shape = [n_features]. `
>>
>>​	`Return the feature importances (the higher, the more important the feature).`
>>
>>`oob_score_ : float.Score of the training dataset obtained using an out-of-bag estimate.`
>>
>>`oob_decision_function_ : array of shape = [n_samples, n_classes]`

> `Methods:`
>
> > `apply(self, X): Apply trees in the forest to X, return leaf indices.`
> > `decision_path(self, X): Return the decision path in the forest`
> > `fit(self, X, y[, sample_weight]): Build a forest of trees from the training set (X, y).`
> > `get_params(self[, deep]): Get parameters for this estimator.`
> > `predict(self, X): Predict class for X.`
> > `predict_log_proba(self, X): Predict class log-probabilities for X.`
> > <font color=orange>`predict_proba`</font>`(self, X): Predict class probabilities for X. `
> > `score(self, X, y[, sample_weight]): Returns mean accuracy on the given test data and labels.`
> > `set_params(self, \*\*params)	Set the parameters of this estimator.`

#### `3) Voting Regressor and Classifier`

`reg = ensemble.VotingRegressor(...)`

- <font color=MediumSlateBlue>`scikit-learn estimators in the VotingClassifier must support predict_proba method`</font>

> `VotingRegressor(estimators, weights=None, n_jobs=None)`
>
> > `VotingRegressor([('lr', r1), ('rf', r2)])`
>
> `Attributes`：
>
> > `estimators_ : list of regressors. `
> >
> > ​	`The collection of fitted sub-estimators as defined in estimators that are not None.`
> >
> > `named_estimators_ : Bunch object, a dictionary with attribute access`
> > 	`Attribute to access any fitted sub-estimators by name.`
>
> `Methods`：
>
> > `fit(self, X, y[, sample_weight]): Fit the estimators.`
> > `fit_transform(self, X[, y]):  Fit to data, then transform it.`
> > `get_params(self[, deep]): Get the parameters of the ensemble estimator`
> > `predict(self, X): Predict regression target for X.`
> > `score(self, X, y[, sample_weight]): Returns coeffs of determination R^2 of prediction.`
> > `set_params(self, \*\*params): Setting the parameters for the ensemble estimator`
> > `transform(self, X): Return predictions for X for each estimator.`

`clf = ensemble.VotingClassifier(...)`

>`VotingClassifier(estimators, voting='hard', weights=None, n_jobs=None, flatten_transform=True)`
>
>> `VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)], voting='soft', weights=[2,1,1])`
>
>`Attributes`：
>
>> `estimators_ : list of classifiers`
>> 	`The collection of fitted sub-estimators as defined in estimators that are not None.`
>>
>> `named_estimators_ : Bunch object, a dictionary with attribute access`
>> 	`Attribute to access any fitted sub-estimators by name.`
>>
>> `classes_ : array-like, shape (n_predictions,) The classes labels.`
>
>`Methods:`
>
>>`Entirely same with that of VotingRegressor`

### 2.  **`Boosting methods`**

1. `AdaBoost`

   `reg = ensemble.AdaBoostRegressor(...)`

   `clf = ensumble.AdaBoostClassifier(...)`

   > ``AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm=’SAMME.R’, random_state=None)`
   >
   > >`AdaBoostClassifier(n_estimators=100, random_state=0)`
   >
   > `Main params:`
   >
   > > `base_estimator : object, optional (default=None)`
   > >
   > > > `The base estimator from which the boosted ensemble is built. Support for sample weighting is required, as well as proper classes_ and n_classes_ attributes. If None, then the base estimator is DecisionTreeClassifier(max_depth=1)`
   > >
   > > `n_estimators*: integer, optional (default=50)`
   > >
   > > > `The maximum number of estimators at which boosting is terminated. In case of perfect fit, the learning procedure is stopped early.`
   > >
   > > `learning_rate : float, optional (default=1.)`
   > >
   > > `algorithm : {‘SAMME’, ‘SAMME.R’}, optional (default=’SAMME.R’)`
   > >
   > > > `If ‘SAMME.R’ then use the SAMME.R real boosting algorithm. `base_estimator` must support calculation of class probabilities. If ‘SAMME’ then use the SAMME discrete boosting algorithm. The SAMME.R algorithm typically converges faster than SAMME, achieving a lower test error with fewer boosting iterations.`
   > >
   > > `random_state** : int, RandomState instance or None, optional (default=None)`
   >
   > `Attributes:`
   >
   > > `estimators_ : list of classifiers. The collection of fitted sub-estimators.`
   > >
   > > `classes_ : array of shape = [n_classes]. The classes labels.`
   > >
   > > `n_classes_ : int. The number of classes.`
   > >
   > > `estimator_weights_ : array of floats.Weights for each estimator in the boosted ensemble.`
   > >
   > > `estimator_errors_ : array. Classification error for each estimator in boosted ensemble.`
   > >
   > > [`feature_importances_`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.feature_importances_) `: array of shape = [n_features]. `
   >
   > `Methods:`
   >
   > > `decision_function(self, X): Compute the decision function of X.`
   > > `fit(self,X,y[, sample_weight]): Build a boosted classifier from the training set (X, y).`
   > > `get_params(self[, deep]): Get parameters for this estimator.`
   > > `predict(self, X): Predict classes for X.`
   > > `predict_log_proba(self, X): Predict class log-probabilities for X.`
   > > `predict_proba(self, X): Predict class probabilities for X.`
   > > `score(self, X, y[, samp_weight]): Returns mean accuracy on given test data and labels.`
   > > `set_params(self, \*\*params): Set the parameters of this estimator.`
   > > `staged_decision_function(self,X): Compute decision function of X for boosting iteration.`
   > > `staged_predict(self, X): Return staged predictions for X.`
   > > `staged_predict_proba(self, X): Predict class probabilities for X.`
   > > `staged_score(self, X, y[, sample_weight]): Return staged scores for X, y.`

2. `Gradient Tree Boosting`

   `reg = ensemble.GradientBoostingRegressor(...)`

   > `...`

   `clf = ensemble.GradientBoostingClassifier(...)`

   > `GradientBoostingClassifier(*loss=’deviance’*, *learning_rate=0.1*, *n_estimators=100*, *subsample=1.0*, *criterion=’friedman_mse’*, *min_samples_split=2*, *min_samples_leaf=1*, *min_weight_fraction_leaf=0.0*, *max_depth=3*, *min_impurity_decrease=0.0*, *min_impurity_split=None*, *init=None*, *random_state=None*, *max_features=None*, *verbose=0*, *max_leaf_nodes=None*, *warm_start=False*, *presort=’auto’*, *validation_fraction=0.1*, *n_iter_no_change=None*, *tol=0.0001*)`
   >
   > > ` GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)`
   >
   > `Main params:`
   >
   > > `Reger to :` [`params are here`](`https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier`)
   >
   > `Attributes:`
   >
   > > `n_estimators_ : int.The number of estimators as selected by early stopping `
   > >
   > > [`feature_importances_`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.feature_importances_) `: array, shape (n_features,)`
   > >
   > > `oob_improvement_ : array, shape (n_estimators,)`
   > >
   > > > `The improvement in loss (= deviance) on the out-of-bag samples relative to the previous iteration. oob_improvement_[0] is the improvement in loss of the first stage over the `init` estimator.`
   > >
   > > `train_score_ : array, shape (n_estimators,)`
   > >
   > > > `The i-th score train_score_[i] is the deviance (= loss) of the model at iteration `i`on the in-bag sample. If subsample == 1 this is the deviance on the training data.`
   > >
   > > `loss_ : LossFunction. The concrete LossFunction object.`
   > >
   > > `init_ : estimator. The estimator that provides the initial predictions.`
   > >
   > > `estimators_ : ndarray of DecisionTreeRegressor,shape (n_estimators, loss_.K)`
   > >
   > > > `The collection of fitted sub-estimators. loss_.K is 1 for binary classification, otherwise n_classes.`
   >
   > `Methods:`
   >
   > > `apply(self, X): Apply trees in the ensemble to X, return leaf indices.
   > > decision_function(self, X): Compute the decision function of X.
   > > fit(self, X, y[, sample_weight, monitor]): Fit the gradient boosting model.
   > > get_params(self[, deep]): Get parameters for this estimator.
   > > predict(self, X): Predict class for X.
   > > predict_log_proba(self, X): Predict class log-probabilities for X.
   > > predict_proba(self, X): Predict class probabilities for X.
   > > score(self, X, y[, sample_weight]): Returns mean accuracy on given test data and labels.
   > > set_params(self, \*\*params): Set the parameters of this estimator.
   > > staged_decision_function(self, X): Compute decision function of X for each iteration.
   > > staged_predict(self, X): Predict class at each stage for X.
   > > staged_predict_proba(self, X): Predict class probabilities at each stage for X.`


## 9. Multiclass and multilabel algorithms  (单标签)多类别分类和多标签分类

<font color=orange>`from sklearn import multiclass`</font>

如果能用<font color=tomato> 9.3中的算法</font>实现`multiclass classification`,则直接用，都是开箱即用的(`out-of-box`)。如果是想尝试不同的`multiclass`策略，可以考虑 `sklearn.multiclass`模块的算法

[<font color=MediumPurple>`Refer here:intro of multiclass and multilabel classification`</font>](https://blog.csdn.net/qq_16555103/article/details/89104413)

[<font color=MediumPurple>[`Refer here: estimators for Inherentyly multiclass, Multiclass as OvO, multiclass as OvR, Support multilabel, and Support multiclass-multioutput`]</font>

### 1. Multiclass classification 多类别分类

- 概念：**一个样本属于且只属于多个类中的一个，一个样本只能属于一个类，不同类之间是互斥的**

- 典型方法：

  1. `One-vs-One`     (**<font color=tomato>`N(N-1)/2`</font>**)     

     ​	将`N`个类别中的**两两类别数据进行组合**，然后使用组合后的数据训练出来一个模型，从而产生**<font color=tomato>`N(N-1)/2`</font>**个分类器，将这些分类器的结果进行融合，并将分类器的预测结果使用**多数投票**的方式 输出最终的预测结果值。

     

     <div align=center><img src=".\img\OvO.png" width="70%"/></div>

      <font color=orange>`multiclass.OneVsOneClassifier(estimator, n_jobs=None)`</font>

     > `clf = multiclass.OneVsOneClassifier(LinearSVC(random_state=0)).fit(X, y).predict(X_test) `
     >
     > `Attributes:`
     >
     > > `estimators_ : list of n_classes estimators. Estimators used for predictions.`
     > >
     > > `classes_ : array, shape = [n_classes]. Class labels.`
     > >
     > > `pairwise_indices_: list, length = len(estimators_), or None. `
     > >
     > > ​	  `Indices of samples used when training the estimators. None when estimator does` 	  `not have _pairwise attribute.`
     >
     > `Methods:`
     >
     > > `decision_function(self, X): Decision function for the OneVsOneClassifier.
     > > fit(self, X, y): Fit underlying estimators.
     > > get_params(self[, deep]): Get parameters for this estimator.
     > > partial_fit(self, X, y[, classes]): Partially fit underlying estimators
     > > predict(self, X): Predict multi-class targets using underlying estimators.
     > > score(self, X, y[, sample_weight]): Returns mean accuracy on test data and labels.
     > > set_params(self, \*\*params): Set the parameters of this estimator.`

  2. **<font color=orange>`One-vs-All or One-vs-Rest`</font>**    (**<font color=tomato>`N`</font>**)    <font color=mediumpurple>`The most commonly used strategy and is a fair default choice`</font>

     ​	将多类问题分成`N`个二类分类问题，训练**<font color=tomato>`N`</font>**个二类分类器，**对第`i`个类来说，所有属于第`i`类的样本为正(`positive`)样本，其他样本为负(`negative`)样本**，每个二类分类器将属于`i`类的样本从其他类中分离出来。

     ​	<font color=mediumpurple>`OvR`既可用于`multiclass`问题，也可用于`multilabel`问题</font>。

     <div align=center><img src=".\img\OvR.png" width="70%"/></div>

      <font color=orange>`multiclass.OneVsRestClassifier(estimator, n_jobs=None)`</font>

     > `clf = multiclass.OneVsRestClassifier(LinearSVC(random_state=0)).fit(X, y).predict(X_test) `
     >
     > `Attributes:`
     >
     > > `estimators_ : list of n_classes estimators. Estimators used for predictions.`
     > >
     > > `classes_ : array, shape = [n_classes]. Class labels.`
     > >
     > > `label_binarizer_ : LabelBinarizer object. `
     > >
     > > ​	  `Object used to transform multiclass labels to binary labels and vice-versa.`
     > >
     > > `multilabel_ : boolean. Whether this is a multilabel classifier`
     >
     > `Methods:`
     >
     > > `decision_function(self, X): `（距离决策边界的距离？）
     > >
     > > ​	`Returns distance of each sample from decision boundary for each class.`
     > > `fit(self, X, y): Fit underlying estimators.`
     > > `get_params(self[, deep]): Get parameters for this estimator.`
     > > `partial_fit(self, X, y[, classes]): Partially fit underlying estimators`
     > > `predict(self, X): Predict multi-class targets using underlying estimators.`
     > > `predict_proba(self, X): Probability estimates.`
     > > `score(self, X, y[, sample_weight]): Returns mean accuracy on test data and labels.`
     > > `set_params(self, \*\*params): Set the parameters of this estimator.`

     区别：

     <div align=center><img src=".\img\OvO & OvR.png" width="70%"/></div>

  3. `Error Correcting Output codes` 误差校正输出 （多对多） --- 不熟悉，不推荐

     ​	将模型构建应用分为两个阶段：编码阶段和解码阶段。

     ​	编码阶段中对`K`个类别进行`M`次划分，每次划分将一部分数据分为正类，一部分数据分为反类。每次划分都构建出来一个模型， 模型的结果是在空间中对于每个类别都定义了一个点；

     ​	解码阶段中使用训练出来的模型对测试样例进行预测，将预测样本对应的点和类别之间的点求距离，选择距离最近的类别作为最终的预测类别。

     <div align=center><img src=".\img\errorcollect.png" width="70%"/></div>

     `clf = multiclass.OutputCodeClassifier(...)`

     > `multiclass.OutputCodeClassifier(estimator, code_size=1.5, random_state=None, n_jobs=None)`

     > > `OutputCodeClassifier(clf,code_size=2, random_state=0)`
     >
     > `Pramas:`
     >
     > > `code_size: Percentage of the number of classes to be used to create the code book`
     >
     > `Attributes:`
     >
     > > `estimators_ : list of int(n_classes * code_size) estimators used for predictions.`
     > >
     > > `classes_ : numpy array of shape [n_classes]. Array containing labels.`
     > >
     > > `code_book_ : array [n_classes, code_size].Binary array containing code of each class.`
     >
     > `Methods:`
     >
     > > `fit(self, X, y): Fit underlying estimators.`
     > > `get_params(self[, deep]): Get parameters for this estimator.`
     > > `predict(self, X): Predict multi-class targets using underlying estimators.`
     > > `score(self, X, y[, sample_weight]): Returns mean accuracy on test data and labels.`
     > > `set_params(self, \*\*params): Set the parameters of this estimator.`

### 2. Multilabel classification 多标签分类   `scikit-multilearn module`  &radic;

<font color=tomato>`scikit-multilearn`</font>`: `  （安装库：<font color=mediumpurple>`pip install scikit-multilearn`</font>）

​	`Multi-label classification module for Python built on top of the well-known scikit-learn ecosystem`

[<font color=MediumPurple>`Refer here:solution and module in python of multilabel classification`</font>](http://www.atyun.com/5376.html)

- 概念：一个样本可以属于多个类别（或标签），不同类之间是有关联的
- 典型方法：
  1. 问题转换 -- 问题转化为一个或多个单目标分类或回归问题
     1. 二元关联（`Binary Relevance`）
     2. 分类器链（`Classifier Chains`）
     3. 标签Powerset（`Label Powerset`）
  2. 改进算法
  3. 集成方法

#### 1) 转换策略(`Problem Transformation Methods`) 

<font color=tomato>`from skmultilearn import problem_transform`</font>   内置算法：`[BinaryRelevance, ClassifierChain, LabelPowerset]`

​        • **`Binary Relevance `**  二元关联   --------- y标签之间相互独立

​	最简单的技术，基本上是把每一个标签当做单独的一个分类问题，例如下图左数据集有4个目标变量（标签），在二元关联中，这个问题被分解成4个不同标签的分类问题（如下图右），不考虑标签之间相关性，单独处理每个目标变量。

> `clf = problem_transform.BinaryRelevance(classifier=None, require_dense=None)`
>
> > `clf = problem_transform.BinaryRelevance(GaussianNB())`
>
> `Attributes:`
>
> > `model_count_ : int. Number of trained models, in this classifier equal to n_labels`
> > `partition_ :  List[List[int]], shape=(model_count_,).`
> > 	`list of lists of label indexes, used to index the output space matrix.`
> > `classifiers_: List[:class: ~sklearn.base.BaseEstimator] of shape model_count.`
> > 	`list of classifiers trained per partition.`
>
> `Methods:`
>
> > `fit(self, X, y): Fits classifier to training data.`
> > `get_params(self[, deep]): Get parameters to sub-objects.`
> > `predict(self, X): Predict labels for X.`
> > `score(self, X, y[, sample_weight]): Returns mean accuracy on test data and labels.`
> > `set_params(self, \*\*params): Set the parameters of this estimator.`

<div align=center><img src=".\img\binaryrelevance.png" width="28%"/>&nbsp&nbsp ==>&nbsp&nbsp<img src=".\img\binaryrelevance1.png" width="50%"/></div>

​	 • **`Classifier Chains`**     分类器链      --------- y标签之间相互依赖（链式）

​	第一个分类器只在输入数据上进行训练，然后每个分类器都在输入空间和链上的所有之前的分类器上进行训练，如下图所示(白色部分代表目标变量，黄色部分代表输入空间)。

> `clf = problem_transform.ClassifierChain(classifier=None, require_dense=None, order=None)`
>
> > `clf = problem_transform.ClassifierChain(GaussianNB())`
>
> `Attributes:`
>
> > `classifiers_:  List of shape model_count.list of classifiers trained per partition.`

<div align=center><img src=".\img\classifierchain.png" width="70%"/></div>

​        • **`Label Powerset `**

​	将`multi-label`问题转化为一个`multi-class`问题，一个多类分类器在训练数据中发现的所有唯一的标签组合上被训练。让我们通过一个例子来理解它，如下图。发现x1和x4有相同的标签，x3和x6有相同的标签。因此，标签powerset将这个问题转换为一个单一的多类问题

> `clf = problem_transform.LabelPowerset(classifier=None, require_dense=None)`
>
> > `clf = problem_transform.LabelPowerset(GaussianNB())`
>
> `Attributes:`
>
> > `unique_combinations_:Dict[str,int],mapping from label combination as string to label combination id` 
> >
> > `reverse_combinations_: List[List[int]],label combination id ordered list to list of label indexes for a given combination`
>
> `Methods:`
>
> > `[fit, get_params, inverse_transform, predict, predict_proba, score, set_params, transform]`

<div align=center><img src=".\img\labelpowerset.png" width="30%"/>&nbsp ===> &nbsp<img src=".\img\labelpowerset1.png" width="14.5%"/></div>

```
• Binary Relevance方式的优点如下： 
	• 实现方式简单，容易理解； 
	• 当y值之间不存在相关的依赖关系的时候，模型的效果不错。 
• 缺点如下： 
	• 如果y直接存在相互的依赖关系，那么最终构建的模型的泛化能力比较 弱；
	• 需要构建q个二分类器，q为待预测的y值数量，当q比较大的时候，需要构建的模型会比较多。
	
• Classifier Chains方式的优点如下： 
	• 实现方式相对比较简单，容易理解； 
	• 考虑标签之间的依赖关系，最终模型的泛化能力相对于Binary Relevance方 式构建的模型效果要好。 
• 缺点： 很难找到一个比较适合的标签依赖关系。

• LabelPowerset 方式的优点如下： 
	• 标签powerset给训练集中的每一个可能的标签组合提供了一个独特的类。 
• 缺点如下： 
	• 随着训练数据的增加，类的数量也会增加。因此，增加了模型的复杂性，并降低了精确度。
```

<font color=orange>`multioutput.MultiOutputClassifier(estimator, n_jobs=1)`</font>   `（y标签之间没有依赖关系）`

#### 2) 算法适应(`Algorithm Adaptation`)  `skmultilearn`  

​	在一些算法中，例如随机森林（Random Forest）和岭回归（Ridge regression），Sci-kit learn提供了**多标签分类的内置支持**。因此，你可以直接调用它们并预测输出。

<font color=tomato>`from skmultilearn import adapt`</font> 

在`adapt`中包含的改进`ml-algorithm`有5个：<font color=orange>`BRkNNaClassifier`,`BRkNNbClassifier`,`MLARAM`, `MLTSVM`, `MLkNN`</font>

    +-------------------------+----------------------------------------------------------------------+
    | Classifier              | Description                                     
    +===============================================+=================================================
    | adapt.BRkNNaClassifier | a Binary Relevance kNN classifier that assigns a label    			|
    					   | if at least half of the neighbors are also classified with the label  |
    +------------------------+-----------------------------------------------------------------------+
    | adapt.BRkNNbClassifier | a Binary Relevance kNN classifier that assigns top m labels 			|
    					   | of neighbors with m - average number of labels assigned to neighbors  |
    +------------------------+-----------------------------------------------------------------------+
    | adapt.MLkNN            | a multi-label adapted kNN classifier with bayesian prior corrections  |
    +------------------------+-----------------------------------------------------------------------+
    | adapt.MLARAM           | a multi-Label Hierarchical ARAM Neural Network      			        |
    +------------------------+-----------------------------------------------------------------------+
    | adapt.MLTSVM           | twin multi-Label Support Vector Machines
​	多标签分类采用的算法 (`adapt`中不包含的算法如何python获得？？)

​		1.<font color=mediumpurple> *boosting*: *AdaBoost.MH*</font>和<font color=mediumpurple>*AdaBoost.MR*</font>是`AdaBoost`的多标签数据扩展版本

​		2. k*近邻: <font color=mediumpurple>ML-kNN</font>是将`k-NN`分类器扩展到多标签数据

​		3. 决策树: <font color=mediumpurple> ML-DT </font>

​		4. 向量输出的核方法

​		5. 神经网络:<font color=mediumpurple>P-MLL</font>是反向传播算法的多标签学习问题的扩展 

#### 3) 集成算法

`...`

- 多标签类二值格式化 `Multilabel classification format`

  `sklearn.preprocessing.MultiLabelBinarizer()`

  > `Methods:`
  >
  > > `fit(self, y): Fit the label sets binarizer, storing classes_.`
  > >
  > > `transform(self, y): Transform the given label sets`
  > >
  > > `fit_transform(self, y): Fit the label sets binarizer and transform the given label sets.`
  > > `inverse_transform(self, yt): Transform the given indicator matrix into label sets.`
  > > `set_params(self, \*\*params): Set the parameters for this estimator.`
  > > `get_params(self[, deep]): Get the parameters for this estimator.`

  ```
  >>> from sklearn.preprocessing import MultiLabelBinarizer
  >>> y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]
  >>> MultiLabelBinarizer().fit_transform(y)    # .fit( y) ; .transform(y)
  array([[0, 0, 1, 1, 1],
         [0, 0, 1, 0, 0],
         [1, 1, 0, 1, 0],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 0, 0]])
  ```

### 3.  汇总 summary list of algorithm for multiclass and multilabel in sklearn

#### 1) `Inherently multiclass`

- [`sklearn.naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB)
- [`sklearn.tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)
- [`sklearn.tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier)
- [`sklearn.ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier)
- [`sklearn.naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB)
- [`sklearn.neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)
- [`sklearn.semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation)
- [`sklearn.semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading)
- [`sklearn.discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis)
- [`sklearn.svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC) (setting multi_class=”crammer_singer”)
- [`sklearn.linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression) (setting multi_class=”multinomial”)
- [`sklearn.linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV) (setting multi_class=”multinomial”)
- [`sklearn.neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier)
- [`sklearn.neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid)
- [`sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis)
- [`sklearn.neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier)
- [`sklearn.ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier)
- [`sklearn.linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier)
- [`sklearn.linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV)

#### 2) `Multiclass as One-Vs-One`

- [`sklearn.svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC)
- [`sklearn.svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC).
- [`sklearn.gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier) (setting multi_class = “one_vs_one”)

#### 3) <font color=tomato>`Multiclass as One-Vs-All`</font>

- [`sklearn.ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier)
- [`sklearn.gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier) (setting multi_class = “one_vs_rest”)
- [`sklearn.svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC) (setting multi_class=”ovr”)
- [`sklearn.linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression) (setting multi_class=”ovr”)
- [`sklearn.linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV) (setting multi_class=”ovr”)
- [`sklearn.linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier)
- [`sklearn.linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron)
- [`sklearn.linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier)

#### 4) <font color=tomato>`Support multilabel`</font>

- [`sklearn.tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)
- [`sklearn.tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier)
- [`sklearn.ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier)
- [`sklearn.neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)
- [`sklearn.neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier)
- [`sklearn.neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier)
- [`sklearn.ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier)
- [`sklearn.linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV)

- Support multiclass-multioutput:
  - [`sklearn.tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)
  - [`sklearn.tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier)
  - [`sklearn.ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier)
  - [`sklearn.neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)
  - [`sklearn.neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier)
  - [`sklearn.ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier)

## 100 sklearn.dataset.make_classification 

`make_classification(n_samples=10, n_features=100, n_informative=30, n_classes=3, random_state=1)`



