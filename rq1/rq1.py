import re
import os
import pandas as pd

dataset = pd.read_csv('rq1&2_data.csv')

occurrences = []
projects = {}
for name in dataset.name.unique():
    idxmax =  dataset[dataset.name==name].pr_auc.idxmax()

    max_pr_auc = dataset.pr_auc.iloc[idxmax]
    occurrences.append(dataset.approach.iloc[idxmax])
    projects[name] = idxmax
    
    for idx, row in dataset[dataset.name==name].iterrows():
        if row.pr_auc == max_pr_auc and idx != idxmax:
            occurrences.append(dataset.approach.iloc[idx])

print()
print('|======= Occurrences ========|')
print(occurrences.count('RF'), '- Random Forest')
print(occurrences.count('CART'), '- Decision Tree')
print(occurrences.count('SVM'), '- Support Vector Classifier')
print(occurrences.count('LR'), '- Logistic Regression')
print(occurrences.count('NB'), '- Naive Bayes')

print()

print('| Project | Best model | AUC-PR (Std) | MCC (Std) | AUC-ROC (Std) | Precision (Std) | Recall (Std) | F1 (Std) | ')
print('|---------|------------|--------------|-----------|---------------|-----------------|--------------|----------|')
for name, idx in sorted(projects.items()):
    row = dataset.iloc[idx]
    pr = round(row.pr_auc*100, 2)
    std_pr = round(row.std_pr_auc*100, 2)
    mcc = round(row.mcc*100, 2)
    std_mcc = round(row.std_mcc*100, 2)
    roc = round(row.roc_auc*100, 2)
    std_roc = round(row.std_roc_auc*100, 2)
    pre = round(row.precision*100, 2)
    std_pre = round(row.std_precision*100, 2)
    rec = round(row.recall*100, 2)
    std_rec = round(row.std_recall*100, 2)
    f1 = round(row.f1*100, 2)
    std_f1 = round(row.std_f1*100, 2)

    to_print = '| {} | {} | {:.2f} ({:.2f}) | {:.2f} ({:.2f}) | {:.2f} ({:.2f}) | {:.2f} ({:.2f}) | {:.2f} ({:.2f}) | {:.2f} ({:.2f}) |'.format(name, row.approach, pr, std_pr, mcc, std_mcc, roc, std_roc, pre, std_pre, rec, std_rec, f1, std_f1)
    print(to_print)