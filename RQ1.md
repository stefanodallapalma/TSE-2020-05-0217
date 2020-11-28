# RQ1a - To what extent do code and process metrics predict the defectiveness of IaC blueprints?


The file **rq1_data.csv** contains the results of the application of the five ML methods for each of the 85 projects; while the file **rq1a.py** is the script used to analyze those results.

Run ```python rq1a.py``` to start the analysis.

<br>

## Results per project

| Project | Best model | AUC-PR |
|---------|------------|--------|
| ANXS/postgresql | RF | 0.97 |
| AlbanAndrieu/ansible-jenkins-slave | RF | 0.81 |
| AlbanAndrieu/ansible-nabla | RF | 0.86 |
| AtlasOfLivingAustralia/ala-install | RF | 0.30 |
| CSCfi/ansible-role-slurm | RF | 1.00 |
| CSCfi/ansible-role-users | LR, SVM, CART, RF | 1.00 |
| CentOS-PaaS-SIG/linchpin | RF | 0.89 |
| CoffeeITWorks/ansible_burp2_server | SVM | 0.96 |
| DataDog/ansible-datadog | RF | 0.92 |
| DavidWittman/ansible-redis | RF | 0.99 |
| Graylog2/graylog-ansible-role | SVM | 0.80 |
| HanXHX/ansible-debian-bootstrap | RF | 0.90 |
| HanXHX/ansible-nginx | RF | 0.93 |
| NVIDIA/deepops | RF | 0.69 |
| Oefenweb/ansible-percona-server | SVM | 1.00 |
| Oefenweb/ansible-postfix | SVM, RF | 1.00 |
| Oefenweb/ansible-supervisor | RF | 0.94 |
| PGBlitz/PGBlitz.com | CART | 0.84 |
| PyratLabs/ansible-role-k3s | RF | 0.97 |
| ReSearchITEng/kubeadm-playbook | RF | 0.88 |
| StackStorm/ansible-st2 | RF | 0.85 |
| UnderGreen/ansible-role-mongodb | RF | 0.96 |
| UtrechtUniversity/yoda | RF | 0.69 |
| aalaesar/install_nextcloud | RF | 0.70 |
| ansible-ThoTeam/nexus3-oss | RF | 0.99 |
| ansible-community/ansible-consul | RF | 0.94 |
| ansible-community/ansible-nomad | RF | 0.99 |
| ansible-community/ansible-vault | LR, SVM, CART, RF | 1.00 |
| ansible-community/molecule | RF | 1.00 |
| ansible-lockdown/RHEL7-STIG | RF | 1.00 |
| ansible/workshops | RF | 0.98 |
| ansistrano/deploy | RF | 0.98 |
| anthcourtney/ansible-role-cis-amazon-linux | RF | 0.77 |
| antoiner77/caddy-ansible | RF | 0.93 |
| arillso/ansible.logrotate | RF | 0.88 |
| automium/service-kubernetes | RF | 0.97 |
| bluebanquise/bluebanquise | RF | 0.81 |
| caktus/tequila-django | LR, SVM, RF | 1.00 |
| ceph/ceph-ansible | RF | 0.89 |
| cloudalchemy/ansible-alertmanager | LR | 0.96 |
| cloudalchemy/ansible-blackbox-exporter | LR, CART, RF | 1.00 |
| cloudalchemy/ansible-grafana | RF | 0.94 |
| cloudalchemy/ansible-node-exporter | RF | 0.98 |
| cloudalchemy/ansible-prometheus | RF | 0.99 |
| cloudalchemy/ansible-pushgateway | LR, SVM, RF | 1.00 |
| elastic/ansible-beats | SVM | 1.00 |
| elastic/ansible-elasticsearch | RF | 0.90 |
| evrardjp/ansible-keepalived | RF | 1.00 |
| fgci-org/ansible-role-cuda | SVM, CART, RF | 1.00 |
| fgci-org/fgci-ansible | LR, SVM, CART, RF | 0.99 |
| florianutz/Ubuntu1604-CIS | LR | 0.98 |
| florianutz/Ubuntu1804-CIS | LR | 0.89 |
| freeipa/ansible-freeipa | RF | 0.72 |
| galaxyproject/ansible-galaxy | LR | 0.89 |
| gluster/gdeploy | RF | 0.96 |
| goodrain/rainbond-ansible | RF | 1.00 |
| idealista/mysql_role | LR, SVM, CART, RF | 1.00 |
| integr8ly/installation | RF | 0.45 |
| jcalazan/ansible-django-stack | RF | 1.00 |
| jmunixusers/cs-vm-build | RF | 0.49 |
| kibatic/ansible-traefik | SVM | 0.96 |
| lae/ansible-role-proxmox | LR | 0.92 |
| liip/drifter | RF | 0.88 |
| mrlesmithjr/ansible-manage-lvm | RF | 0.71 |
| naftulikay/ansible-role-degoss | RF | 0.97 |
| netbootxyz/netboot.xyz | RF | 0.96 |
| newrelic/infrastructure-agent-ansible | SVM | 1.00 |
| nusenu/ansible-relayor | SVM | 0.95 |
| oVirt/ovirt-ansible-disaster-recovery | RF | 0.87 |
| oVirt/ovirt-ansible-hosted-engine-setup | RF | 0.96 |
| openfun/arnold | RF | 0.98 |
| openstack/openstack-ansible | RF | 0.68 |
| openstack/openstack-ansible-os_neutron | RF | 0.89 |
| openstack/openstack-ansible-os_nova | RF | 0.78 |
| openstack/openstack-ansible-rabbitmq_server | RF | 0.89 |
| openstack/tripleo-quickstart | RF | 0.37 |
| openstack/tripleo-quickstart-extras | LR | 0.22 |
| openstack/tripleo-validations | RF | 0.76 |
| openstax/cnx-deploy | RF | 1.00 |
| openwisp/ansible-openwisp2 | RF | 0.97 |
| oravirt/ansible-oracle | RF | 0.83 |
| plone/ansible-playbook | RF | 0.97 |
| pulp/pulp_installer | RF | 0.81 |
| redhat-cop/casl-ansible | RF | 0.69 |
| redhat-cop/infra-ansible | RF | 0.76 |
| redhat-cop/openshift-applier | RF | 0.99 |
| redhat-nfvpe/kube-ansible | RF | 0.95 |
| redhat-openstack/infrared | CART | 0.85 |
| riemers/ansible-gitlab-runner | RF | 0.97 |
| roots/trellis | RF | 0.76 |
| roxcknsm/rock | RF | 0.83 |
| rvm/rvm1-ansible | LR, SVM, RF | 1.00 |
| sensu/sensu-ansible | RF | 0.90 |
| snowdrop/k8s-infra | RF | 0.86 |
| splunk/splunk-ansible | RF | 0.77 |
| stackbuilders/sb-debian-base | RF | 0.94 |
| stackhpc/ansible-role-os-images | NB, LR, SVM, CART, RF | 1.00 |
| tenforwardconsulting/subspace | RF | 0.87 |
| valet-sh/valet-sh | RF | 0.80 |
| viasite-ansible/ansible-role-zsh | RF | 0.99 |
| vitabaks/postgresql_cluster | RF | 0.84 |
| wazuh/wazuh-ansible | RF | 0.82 |
| willshersystems/ansible-sshd | LR | 1.00 |
| wso2/ansible-apim | SVM | 0.78 |



<br>


****

# RQ1b - How is the prediction performance affected by the choice of learning methods?


The file **rq1_data.csv** contains the results of the application of the five ML methods for each of the 85 projects; while the file **rq1b.py** is the script used to analyze those results aggregating data by model.

Run ```python rq1b.py``` to start the analysis.


<br>


## Summary of techniques

### Random Forest

||roc_auc|std_roc_auc|pr_auc|std_pr_auc|precision|std_precision|recall|std_recall|f1|std_f1|mcc|std_mcc|
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|count|102|102|102|102|102|102|102|102|102|102|102|102|
|mean|0.952805|0.070191|0.874779|0.142161|0.771883|0.232233|0.836295|0.205005|0.766808|0.207510|0.741107|0.229799|
|std|0.059548|0.070516|0.156831|0.105553|0.207766|0.113468|0.162590|0.124031|0.199233|0.103259|0.210818|0.120869|
|min|0.650000|0.000000|0.140600|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|-0.012241|0.000000|
|25%|0.943678|0.018547|0.814713|0.050529|0.700823|0.171395|0.778488|0.132397|0.683552|0.155491|0.656272|0.166542|
|50%|0.972358|0.054180|0.929638|0.139621|0.824876|0.229954|0.886411|0.214802|0.821980|0.202652|0.797233|0.230491|
|75%|0.993139|0.096270|0.983523|0.218235|0.916464|0.302955|0.943493|0.275497|0.900736|0.260649|0.885245|0.280589|
|max|1.000000|0.350000|1.000000|0.437500|1.000000|0.471405|1.000000|0.484123|1.000000|0.471405|1.000000|0.671855|

<br>

### Decision Tree (CART)
||roc_auc|std_roc_auc|pr_auc|std_pr_auc|precision|std_precision|recall|std_recall|f1|std_f1|mcc|std_mcc|
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|count|104|104|104|104|104|104|104|104|104|104|104|104|
|mean|0.899357|0.115592|0.748569|0.224070|0.781049|0.227888|0.853670|0.199098|0.784940|0.205769|0.759230|0.228334|
|std|0.079062|0.059036|0.197381|0.096660|0.187953|0.112902|0.129486|0.110270|0.175074|0.096068|0.184621|0.111517|
|min|0.623838|0.000000|0.066018|0.000000|0.082192|0.000000|0.269886|0.000000|0.142857|0.000000|0.112958|0.000000|
|25%|0.865886|0.087254|0.653809|0.186356|0.666667|0.175548|0.811756|0.142377|0.699866|0.154587|0.656607|0.164305|
|50%|0.917696|0.110014|0.801927|0.229493|0.839414|0.235890|0.885008|0.197582|0.825641|0.206178|0.789984|0.224610|
|75%|0.958505|0.157428|0.891967|0.286969|0.912806|0.296913|0.944394|0.277009|0.910326|0.268388|0.893018|0.292306|
|max|1.000000|0.251768|1.000000|0.425835|1.000000|0.500000|1.000000|0.473853|1.000000|0.415515|1.000000|0.546191|

<br>

### Support Vector Classifier

||roc_auc|std_roc_auc|pr_auc|std_pr_auc|precision|std_precision|recall|std_recall|f1|std_f1|mcc|std_mcc|
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|count|102|102|102|102|102|102|102|102|102|102|102|102|
|mean|0.910876|0.108371|0.794522|0.180579|0.680427|0.271587|0.774127|0.242654|0.673281|0.238926|0.642384|0.261302|
|std|0.078843|0.073941|0.199745|0.110759|0.222140|0.115445|0.180363|0.130410|0.211858|0.102467|0.213372|0.110704|
|min|0.656738|0.000000|0.198112|0.000000|0.056701|0.000000|0.248311|0.000000|0.100000|0.000000|0.077774|0.000000|
|25%|0.870315|0.054899|0.685952|0.104588|0.533644|0.219714|0.678508|0.179400|0.529462|0.170796|0.487219|0.188090|
|50%|0.934234|0.113650|0.855054|0.186756|0.714926|0.287000|0.793561|0.257401|0.704039|0.249075|0.672029|0.265238|
|75%|0.970733|0.150306|0.952560|0.273855|0.863816|0.353434|0.921474|0.335404|0.838993|0.303956|0.825418|0.333355|
|max|1.000000|0.320048|1.000000|0.399084|1.000000|0.500000|1.000000|0.500000|1.000000|0.422616|1.000000|0.540062|

<br>

### Logistic Regression
||roc_auc|std_roc_auc|pr_auc|std_pr_auc|precision|std_precision|recall|std_recall|f1|std_f1|mcc|std_mcc|
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|count|104|104|104|104|104|104|104|104|104|104|104|104|
|mean|0.898880|0.111832|0.774081|0.173490|0.616925|0.237031|0.786038|0.198201|0.626141|0.199731|0.593126|0.219922|
|std|0.089670|0.088745|0.216069|0.100438|0.259983|0.108483|0.211755|0.116365|0.249900|0.092921|0.248174|0.111780|
|min|0.503987|0.000000|0.136490|0.000000|0.051935|0.000000|0.027778|0.000000|0.050000|0.000000|-0.007589|0.000000|
|25%|0.845946|0.054502|0.637491|0.111299|0.427134|0.174023|0.710714|0.131339|0.440699|0.147721|0.417811|0.146277|
|50%|0.923472|0.102624|0.861361|0.175728|0.666667|0.253038|0.854472|0.202788|0.689684|0.198765|0.600826|0.215431|
|75%|0.963744|0.148232|0.944562|0.250948|0.827922|0.312337|0.932668|0.282416|0.852494|0.261809|0.812259|0.302998|
|max|1.000000|0.446999|1.000000|0.398587|1.000000|0.448611|1.000000|0.460146|1.000000|0.420892|1.000000|0.535707|

<br>

#### Logistic Regression with multicollinearity reduction (VIF<=10)

| | roc_auc | std_roc_auc | pr_auc | std_pr_auc | precision | std_precision | recall | std_recall | f1 | std_f1 | mcc | std_mcc|
|:---|-----:|------------:|-------:|-----------:|----------:|--------------:|-------:|-----------:|---:|-------:|----:|-------:|
| count | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 |
| mean | 0.866065 | 0.135863 | 0.726330 | 0.197639 | 0.574322 | 0.258028 | 0.738797 | 0.226098 | 0.580353 | 0.215946 | 0.517436 | 0.251943 |
| std | 0.0883351 | 0.087017 | 0.209820 | 0.089792 | 0.228874 | 0.114451 | 0.213002 | 0.133633 | 0.219243 | 0.105729 | 0.225046 | 0.134041 |
| min | 0.572222 | 0.000000 | 0.174830 | 0.000000 | 0.0326005 | 0.000000 | 0.142857 | 0.000000 | 0.062990 | 0.000000 | -0.209165 | 0.000000 |
| 25% | 0.809436 | 0.077240 | 0.608789 | 0.147107 | 0.408007 | 0.182200 | 0.638889 | 0.143570 | 0.424490 | 0.150081 | 0.360644 | 0.154535 |
| 50% | 0.876484 | 0.119183 | 0.791667 | 0.189984 | 0.595238 | 0.268355 | 0.785714 | 0.198053 | 0.611111 | 0.198360 | 0.500938 | 0.228373 |
| 75% | 0.930964 | 0.188588 | 0.881347 | 0.252215 | 0.746377 | 0.343592 | 0.889785 | 0.309505 | 0.727974 | 0.286284 | 0.679940 | 0.351160 |
| max | 1.000000 | 0.380870 | 1.000000 | 0.447239 | 1.000000 | 0.482804 | 1.000000 | 0.500000 | 1.000000 | 0.482694 | 1.000000 | 0.669038 |

#### Logistic Regression on the same 97 projects without multicollinearity reduction

| | roc_auc | std_roc_auc | pr_auc | std_pr_auc | precision | std_precision | recall | std_recall | f1 | std_f1 | mcc | std_mcc |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 |
| mean | 0.898208 | 0.114483 | 0.784431 | 0.171370 | 0.625281 | 0.235728 | 0.797877 | 0.195925 | 0.637097 | 0.199493 | 0.601074 | 0.221874 |
| std | 0.091392 | 0.091138 | 0.212951 | 0.101841 | 0.261265 | 0.108526 | 0.208489 | 0.118776 | 0.251719 | 0.0933984 | 0.251425 | 0.112819 |
| min | 0.503987 | 0.000000| 0.136490 | 0.000000  | 0.051935 | 0.000000 | 0.027778 | 0.000000 | 0.050000 | 0.000000 | -0.007589 | 0.000000|
| 25% | 0.842117 | 0.051358 | 0.654202 | 0.108064 | 0.436749 | 0.177865 | 0.722222 | 0.122838 | 0.442560 | 0.148034 | 0.423167 | 0.147281 |
| 50% | 0.923382 | 0.106051 | 0.875000 | 0.173809 | 0.673329 | 0.254353 | 0.867411 | 0.205823 | 0.705358 | 0.199178 | 0.621007 | 0.218914 |
| 75% | 0.964409 | 0.156201 | 0.944915 | 0.248590 | 0.854762 | 0.312086 | 0.933761 | 0.28435  | 0.856321 | 0.261776 | 0.824564 | 0.304574 |
| max | 1.000000 | 0.446999 | 1.000000 | 0.398587 | 1.000000 | 0.438164 | 1.000000 | 0.460146 | 1.000000 | 0.420892 | 1.000000 | 0.535707 |

<br>


### Naive Bayes:

||roc_auc|std_roc_auc|pr_auc|std_pr_auc|precision|std_precision|recall|std_recall|f1|std_f1|mcc|std_mcc|
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|count|104|104|104|104|104|104|104|104|104|104|104|104|
|mean|0.836236|0.131312|0.561300|0.200247|0.499101|0.230269|0.747854|0.240577|0.516721|0.200838|0.458486|0.225839|
|std|0.097884|0.067278|0.273922|0.085158|0.280307|0.112340|0.171726|0.129209|0.247812|0.099655|0.248177|0.119541|
|min|0.579721|0.000000|0.083450|0.000000|0.025000|0.000000|0.250000|0.000000|0.045455|0.000000|0.005475|0.000000|
|25%|0.769091|0.085508|0.305476|0.144766|0.237183|0.155347|0.622113|0.155894|0.312755|0.130239|0.262247|0.142284|
|50%|0.840147|0.123608|0.596732|0.207595|0.501314|0.232865|0.776095|0.240206|0.526709|0.190912|0.427484|0.218057|
|75%|0.920628|0.169176|0.810225|0.263370|0.734297|0.320698|0.877404|0.332987|0.695881|0.273735|0.616368|0.287866|
|max|1.000000|0.365624|1.000000|0.378886|1.000000|0.471405|1.000000|0.494872|1.000000|0.460642|1.000000|0.687184|


<br>
<br>

## Differences among means and statistical tests

**Difference table info:**
* Values below the diagonal are difference between the mean of the model in the row and the model in the column. A negative value means that the model in the row performed worse than the one in the column.

**Statistical test table info:**
* Values above the diagonal are the Choen's *d* effect size.
* Values below the diagonal are the p-values for the pairwise Wilcoxon's rank test.
* The shown p-values are not corrected for the number of comparisons. To do so, multiply each value by the number of comparisons, that is: *p-value * 10*.

<br>

### AUC-PR

**Differences:**

| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | - | - | - | -|
| CART | -0.1262 | - | - | - | -|
| SVM | -0.0803 | 0.0460 | - | - | -|
| LR | -0.1007 | 0.0255 | -0.0204 | - | -|
| NB | -0.3135 | -0.1873 | -0.2332 | -0.2128 | -|

| Model       |       LR | LR(VIF<=10)   |
|:------------|---------:|:--------------|
| LR          | -        | -             |
| LR(VIF<=10) |  -0.0581 | -             |


**Statistical test:**

| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | 0.7072 | 0.4469 | 0.5326 | 1.4011|
| CART | 2.18e-08 | - | -0.2314 | -0.1233 | 0.7844|
| SVM | 2.60e-12 | 2.55e-02 | - | 0.0982 | 0.9714|
| LR | 6.39e-06 | 4.67e-04 | 2.67e-01 | - | 0.8625|
| NB | 9.50e-15 | 2.27e-16 | 2.71e-11 | 2.66e-18 | -|

| Model       |       LR |   LR(VIF<=10) |
|:------------|---------:|--------------:|
| LR          |    -     |        0.2749 |
| LR(VIF<=10) | 1.15e-05 |     -         |


### MCC

**Differences:**
| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | - | - | - | -|
| CART | 0.0181 | - | - | - | -|
| SVM | -0.0987 | -0.1168 | - | - | -|
| LR | -0.1480 | -0.1661 | -0.0493 | - | -|
| NB | -0.2826 | -0.3007 | -0.1839 | -0.1346 | -|

| Model       |       LR | LR(VIF<=10)   |
|:------------|---------:|:--------------|
| LR          | -        |    -         |
| LR(VIF<=10) |  -0.0836 |    -          |


**Statistical test:**
| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | -0.0915 | 0.4655 | 0.6422 | 1.2264|
| CART | 5.70e-01 | - | 0.5861 | 0.7594 | 1.3750|
| SVM | 5.22e-11 | 1.65e-06 | - | 0.2127 | 0.7940|
| LR | 2.55e-06 | 3.37e-16 | 9.88e-02 | - | 0.5425|
| NB | 1.01e-12 | 8.64e-18 | 3.88e-09 | 6.10e-11 | -|

| Model       |       LR |   LR(VIF<=10) |
|:------------|---------:|--------------:|
| LR          |    -     |        0.3505 |
| LR(VIF<=10) | 0.000577 |      -        |

### ROC-AUC

**Differences:**
| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | - | - | - | -|
| CART | -0.0534 | - | - | - | -|
| SVM | -0.0419 | 0.0115 | - | - | -|
| LR | -0.0539 | -0.0005 | -0.0120 | - | -|
| NB | -0.1166 | -0.0631 | -0.0746 | -0.0626 | -|

| Model       |       LR | LR(VIF<=10)   |
|:------------|---------:|:--------------|
| LR          | -      |      -         |
| LR(VIF<=10) |  -0.0321 |    -           |


**Statistical test:**
| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | 0.7626 | 0.6002 | 0.7071 | 1.4356|
| CART | 2.23e-09 | - | -0.1459 | 0.0056 | 0.7094|
| SVM | 7.96e-12 | 1.92e-01 | - | 0.142 | 0.8390|
| LR | 2.16e-08 | 5.84e-01 | 2.50e-01 | - | 0.6674|
| NB | 3.61e-15 | 1.89e-13 | 9.55e-10 | 3.09e-14 | -|

| Model       |       LR |   LR(VIF<=10) |
|:------------|---------:|--------------:|
| LR          |    -      |        0.3576 |
| LR(VIF<=10) | 2.32e-05 |      -      |

### Precision

**Differences:**
| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | - | - | - | -|
| CART | 0.0092 | - | - | - | -|
| SVM | -0.0915 | -0.1006 | - | - | -|
| LR | -0.1550 | -0.1641 | -0.0635 | - | -|
| NB | -0.2728 | -0.2819 | -0.1813 | -0.1178 | -|

| Model       |      LR | LR(VIF<=10)   |
|:------------|--------:|:--------------|
| LR          | -     |        -       |
| LR(VIF<=10) |  -0.051 |     -          |

**Statistical test:**

| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | -0.0463 | 0.4252 | 0.6578 | 1.1041|
| CART | 7.28e-01 | - | 0.4894 | 0.7235 | 1.1815|
| SVM | 7.54e-10 | 2.82e-05 | - | 0.2624 | 0.7162|
| LR | 9.49e-06 | 1.52e-15 | 7.66e-02 | - | 0.4358|
| NB | 1.55e-11 | 7.33e-18 | 9.71e-08 | 1.81e-09 | -|

| Model       |     LR |   LR(VIF<=10) |
|:------------|-------:|--------------:|
| LR          |        |        0.2075 |
| LR(VIF<=10) | 0.0423 |      -      |

### Recall 

**Differences:**

| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | - | - | - | -|
| CART | 0.0174 | - | - | - | -|
| SVM | -0.0622 | -0.0795 | - | - | -|
| LR | -0.0503 | -0.0676 | 0.0119 | - | -|
| NB | -0.0884 | -0.1058 | -0.0263 | -0.0382 | -|

| Model       |       LR | LR(VIF<=10)   |
|:------------|---------:|:--------------|
| LR          | -      |      -         |
| LR(VIF<=10) |  -0.0591 |      -         |


**Statistical test:**

| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | -0.1183 | 0.3621 | 0.2659 | 0.5287|
| CART | 9.08e-01 | - | 0.5074 | 0.3853 | 0.6958|
| SVM | 6.36e-06 | 2.42e-04 | - | -0.0605 | 0.1492|
| LR | 1.16e-02 | 4.16e-05 | 5.64e-01 | - | 0.1981|
| NB | 2.85e-05 | 1.08e-08 | 1.68e-01 | 6.23e-03 | -|

| Model       |     LR |   LR(VIF<=10) |
|:------------|-------:|--------------:|
| LR          |    -    |        0.2803 |
| LR(VIF<=10) | 0.0035 |      -      |

### F1

**Differences:**
| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | - | - | - | -|
| CART | 0.0181 | - | - | - | -|
| SVM | -0.0935 | -0.1117 | - | - | -|
| LR | -0.1407 | -0.1588 | -0.0471 | - | -|
| NB | -0.2501 | -0.2682 | -0.1566 | -0.1094 | -|

| Model       |       LR | LR(VIF<=10)   |
|:------------|---------:|:--------------|
| LR          | -      |      -         |
| LR(VIF<=10) |  -0.0567 |     -          |

**Statistical test:**
| Model | RF | CART | SVM | LR | NB|
|---|---|---|---|---|---|
| RF | - | -0.0967 | 0.4548 | 0.6218 | 1.1111|
| CART | 4.75e-01 | - | 0.5751 | 0.736 | 1.2502|
| SVM | 2.05e-11 | 1.55e-06 | - | 0.2033 | 0.6786|
| LR | 2.55e-06 | 1.98e-16 | 6.37e-02 | - | 0.4397|
| NB | 3.66e-12 | 7.25e-18 | 4.95e-08 | 2.90e-10 | -|

| Model       |      LR |   LR(VIF<=10) |
|:------------|--------:|--------------:|
| LR          |    -     |        0.2404 |
| LR(VIF<=10) | 0.00761 |      -      |
