import re
import os
import numpy as np
import pandas as pd

from collections import deque
from scipy.stats import wilcoxon
from statsmodels.stats.multitest import multipletests

dataset = pd.read_csv('rq2_data.csv')

iac_df = dataset[dataset.metrics == 'ico']
iacprocess_df = dataset[dataset.metrics == 'ico-process']
iacdelta_df = dataset[dataset.metrics == 'ico-delta']
process_df = dataset[dataset.metrics == 'process']
deltaprocess_df = dataset[dataset.metrics == 'delta-process']
delta_df = dataset[dataset.metrics == 'delta']
total_df = dataset[dataset.metrics == 'total']

print('IAC')
print(iac_df.describe())
print()
print('TOTAL')
print(total_df.describe())
print()
print('IAC PROCESS')
print(iacprocess_df.describe())
print()
print('IAC DELTA')
print(iacdelta_df.describe())
print()
print('PROCESS')
print(process_df.describe())
print()
print('DELTA PROCESS')
print(deltaprocess_df.describe())
print()
print('DELTA')
print(delta_df.describe())


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
        iac_df.mean_pr_auc, 
        iacdelta_df.mean_pr_auc, 
        iacprocess_df.mean_pr_auc, 
        total_df.mean_pr_auc, 
        deltaprocess_df.mean_pr_auc, 
        process_df.mean_pr_auc, 
        delta_df.mean_pr_auc
    ],

    mcc = [
        iac_df.mean_mcc, 
        iacdelta_df.mean_mcc, 
        iacprocess_df.mean_mcc, 
        total_df.mean_mcc, 
        deltaprocess_df.mean_mcc, 
        process_df.mean_mcc, 
        delta_df.mean_mcc
    ],

    rocauc = [
        iac_df.mean_roc_auc, 
        iacdelta_df.mean_roc_auc, 
        iacprocess_df.mean_roc_auc, 
        total_df.mean_roc_auc, 
        deltaprocess_df.mean_roc_auc, 
        process_df.mean_roc_auc, 
        delta_df.mean_roc_auc
    ],

    precision = [
        iac_df.mean_precision, 
        iacdelta_df.mean_precision, 
        iacprocess_df.mean_precision, 
        total_df.mean_precision, 
        deltaprocess_df.mean_precision, 
        process_df.mean_precision, 
        delta_df.mean_precision
    ],

    recall = [
        iac_df.mean_recall, 
        iacdelta_df.mean_recall, 
        iacprocess_df.mean_recall, 
        total_df.mean_recall, 
        deltaprocess_df.mean_recall, 
        process_df.mean_recall, 
        delta_df.mean_recall
    ],

    f1 = [
        iac_df.mean_f1, 
        iacdelta_df.mean_f1, 
        iacprocess_df.mean_f1, 
        total_df.mean_f1, 
        deltaprocess_df.mean_f1, 
        process_df.mean_f1, 
        delta_df.mean_f1
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

        metrics = ''
        if i == 0:
            metrics = 'ico'
        elif i == 1:
            metrics = 'ico_delta'
        elif i == 2:
            metrics = 'ico_process'
        elif i == 3:
            metrics = 'total'
        elif i == 4:
            metrics = 'process_delta'
        elif i == 5:
            metrics = 'process'
        elif i == 6:
            metrics = 'delta'

        row[-1] = metrics
        row.rotate(1)
        stattest_values.append(row)

        row_diff[-1] = metrics
        row_diff.rotate(1)
        diff_values.append(row_diff)

    diff_df = pd.DataFrame(diff_values, columns=['metrics', 'ico', 'ico-delta', 'ico-process', 'total', 'process_delta', 'process', 'delta'])
    print('\nDifferences:')
    print(diff_df)

    test_df = pd.DataFrame(stattest_values, columns=['metrics', 'ico', 'ico-delta', 'ico-process', 'total', 'process_delta', 'process', 'delta'])
    print('\nStatistical test:')
    print(test_df)

    # DECOMMENT THIS CODE TO SAVE RESULTS (Differences between means) AS A CSV FILE
    # with open(f'{name}_diff.csv', 'w') as outfile:
    #    diff_df.to_csv(outfile, index=False)

    # DECOMMENT THIS CODE TO SAVE RESULTS (Statistical test) AS A CSV FILE
    # with open(f'{name}_test.csv', 'w') as outfile:
    #    test_df.to_csv(outfile, index=False)