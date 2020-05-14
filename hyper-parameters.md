# Models' hyper-parameters configuration

## Decision Tree (CART)

| Parameter | Possible values|
|-----------|----------------|
|criterion | 'gini', 'entropy'|
|splitter| 'best', 'random' |
|max_features| 'auto', 'sqrt', 'log2', None |
|class_weight| 'balanced', None |



## Logist Bayes

| Parameter | Possible values|
|-----------|----------------|
|penalty | 'l2', 'none'|
|tol| numpy.logspace(start=-5, stop=-3, num=10) |
|C| numpy.linspace(start=0, stop=2, num=10) |
|class_weight| 'balanced', None |
|solver| 'lbfgs', 'sag', 'saga'|
|fit_intercept| False, True |


## Naive Bayes

| Parameter | Possible values|
|-----------|----------------|
|var_smoothing| numpy.logspace(start=-10, stop=-8, num=10)|



## Random Forest

| Parameter | Possible values|
|-----------|----------------|
|n_estimators | [int(x) for x in np.linspace(start = 100, stop = 2000, num = 10)]|
|max_features| 'auto', 'sqrt' |
|max_depth| [int(x) for x in np.linspace(10, 110, num = 11)], None |
|bootstrap| False, True |


## Support Vector Machine

| Parameter | Possible values|
|-----------|----------------|
|C | [int(x) for x in np.linspace(start = 1, stop = 1000, num = 100)]|
|gamma| 'scale', 'auto' |
|kernel| 'rbf', 'sigmoid', 'poly' |
|degree| 1, 2, 3, 4, 5 |
|shrinking| False, True |
|tol| [x for x in np.logspace(start = -5, stop = -1, num = 10)] |
|class_weight| 'balanced', None  |
