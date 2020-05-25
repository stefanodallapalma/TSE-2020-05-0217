import json
import os
from statistics import mean, stdev
import collections

optimal = []
all_selected = []
auc = []
selected_sets = []


for file in os.listdir('data'):
    with open(os.path.join('data', file), 'r') as infile:
        df = json.load(infile)
        n = df['optimal_n']
        optimal.append(n)
        all_selected.extend(df['selected'])
        selected_sets.append(df['selected'])
        auc.append(df['scores'][n-1])

print('\n|=== Statistics =====|')
print('| Mean features\t-', round(mean(optimal)), '|')
print('| Std features\t-', round(stdev(optimal)), '|')
print('| Mean PR-AUC\t-', round(mean(auc)*100), '|')
print('| Std PR-AUC\t-', round(stdev(auc)*100), '|')

print('\n#    METRIC')
print('----------------------')
counter = collections.Counter(x for x in all_selected)
counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)}
for key, value in counter.items():
    print(value, '-', key)



# Find most common combination of metrics
from itertools import combinations


name_to_id = dict()

all_selected = list(set(all_selected))
for i in range(0, len(all_selected)):
    name_to_id[all_selected[i]] = i

map = dict()

id_subsets = []
final_map = dict()

for i in range(0, len(selected_sets)):
    s = selected_sets[i]
    for item in s:
        map.setdefault(item, set()).add(i) 

K = 2

for k, v in list(map.items()):
    if len(v) < 2:
        continue
    
    for c in list(combinations(v, K)):
        if c not in id_subsets:
            id_subsets.append(c)

        idx = id_subsets.index(c)
        final_map.setdefault(idx, set()).add(k)

sets = []
for v in final_map.values():
    if v not in sets:
        sets.append(v)

merged_final = dict()
for k, v in final_map.items():
    idx = sets.index(v) 
    merged_final[idx] = merged_final.get(idx, 0) + len(id_subsets[k])

merged_final = {k: v for k, v in sorted(merged_final.items(), key=lambda item:  item[1], reverse=True)} # sort dict by len of key

for k, v in list(merged_final.items()):
    if len(sets[k]) < 2:
        continue

    count = 0
    for s2 in selected_sets:
        if sets[k].intersection(s2) == sets[k]:
            count += 1
    
    merged_final[k] = count

merged_final = {k: v for k, v in sorted(merged_final.items(), key=lambda item:  item[1], reverse=True)} # sort dict by len of key


top = 20
i = 1

print(f'\n#    TOP {top} COMBINATIONS')
print('------------------------')

for k, v in list(merged_final.items()):
    if len(sets[k]) < 2:
        continue

    if i <= top:
        print(v, '-', ', '.join(sets[k]))
    
    i += 1