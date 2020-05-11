import re
import os
import numpy as np
import pandas as pd

from collections import deque
from scipy.stats import wilcoxon
from statsmodels.stats.multitest import multipletests

dataset = pd.read_csv('rq1&2_data.csv')

dt_df = dataset[dataset.approach == 'CART']
lr_df = dataset[dataset.approach == 'LR']
nb_df = dataset[dataset.approach == 'NB']
rf_df = dataset[dataset.approach == 'RF']
svc_df = dataset[dataset.approach == 'SVM']

print('Random Forest:')
print(rf_df.describe())
print()
print('Decition Tree (CART):')
print(dt_df.describe())
print()
print('Support Vector Classifier:')
print(svc_df.describe())
print()
print('Logistic Regression:')
print(lr_df.describe())
print()
print('Naive Bayes:')
print(nb_df.describe())


# function to calculate Cohen's d for independent samples
def cohend(d1, d2):
	n1, n2 = len(d1), len(d2) # calculate the size of samples
	s1, s2 = np.var(d1, ddof=1), np.var(d2, ddof=1) # calculate the variance of the samples
	s = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2)) # calculate the pooled standard deviation
	u1, u2 = np.mean(d1), np.mean(d2) # calculate the means of the samples
	return (u1 - u2) / s # calculate the effect size


# function to calculate Wilcoxon's ranked test
def _wilcoxon(d1, d2):
    difference = []
    zip_object = zip(d1, d2)
    for list1_i, list2_i in zip_object:
        difference.append(list1_i-list2_i)

    _, p = wilcoxon(difference)
    return p

eval_measures = dict(
    prauc = [
        rf_df.pr_auc, 
        dt_df.pr_auc, 
        svc_df.pr_auc, 
        lr_df.pr_auc, 
        nb_df.pr_auc
    ],

    mcc = [
        rf_df.mcc, 
        dt_df.mcc, 
        svc_df.mcc, 
        lr_df.mcc, 
        nb_df.mcc
    ],

    rocauc = [
        rf_df.roc_auc, 
        dt_df.roc_auc, 
        svc_df.roc_auc, 
        lr_df.roc_auc, 
        nb_df.roc_auc
    ],

    precision = [
        rf_df.precision, 
        dt_df.precision, 
        svc_df.precision, 
        lr_df.precision, 
        nb_df.precision
    ],

    recall = [
        rf_df.recall, 
        dt_df.recall, 
        svc_df.recall, 
        lr_df.recall, 
        nb_df.recall
    ],

    f1 = [rf_df.f1, 
        dt_df.f1, 
        svc_df.f1, 
        lr_df.f1, 
        nb_df.f1
    ]
)


for name, measures in eval_measures.items():
    print()
    print('##################################################')
    print('#', name.upper())
    print('##################################################')

    stattest_values = []
    diff_values = []

    for i in range(0, len(measures)):
    
        row = deque([None] * (len(measures) + 1))
        row_diff = deque([None] * (len(measures) + 1))
        
        for j in range(0, len(measures)):
            
            if j == i:
                continue
            elif j < i:
                row[j] ='{:0.2e}'.format(_wilcoxon(measures[i], measures[j]))
                row_diff[j] = round(measures[i].mean() - measures[j].mean(), 4)
            else:
                row[j] = round(cohend(measures[i], measures[j]) , 4)

        model = ''
        if i == 0:
            model = 'RF'
        elif i == 1:
            model = 'CART'
        elif i == 2:
            model = 'SVM'
        elif i == 3:
            model = 'LR'
        elif i == 4:
            model = 'NB'

        row[-1] = model
        row.rotate(1)
        stattest_values.append(row)

        row_diff[-1] = model
        row_diff.rotate(1)
        diff_values.append(row_diff)

    diff_df = pd.DataFrame(diff_values, columns=['Model', 'RF', 'CART', 'SVM', 'LR', 'NB'])
    print('\nDifferences:')
    print(diff_df)

    test_df = pd.DataFrame(stattest_values, columns=['Model', 'RF', 'CART', 'SVM', 'LR', 'NB'])
    print('\nStatistical test:')
    print(test_df)

    # DECOMMENT THIS CODE TO SAVE RESULTS (Differences between means) AS A CSV FILE
    # with open(f'{name}_diff.csv', 'w') as outfile:
    #    diff_df.to_csv(outfile, index=False)

    # DECOMMENT THIS CODE TO SAVE RESULTS (Statistical test) AS A CSV FILE
    # with open(f'{name}_test.csv', 'w') as outfile:
    #    test_df.to_csv(outfile, index=False)