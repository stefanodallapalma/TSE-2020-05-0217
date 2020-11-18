# Defect Prediction of Infrastructure-as-Code Using Product and Process Metrics
Replication package for the paper *"Defect Prediction of Infrastructure-as-Code Using Product and Process Metrics"* submitted at Transantions on Software Engineering (TSE 2020).

## Structure
* **rq1** contains data and scripts for RQ1 with respective README;
* **rq2** contains data and scripts for RQ2 with respective README;
* **rq3** contains data and scripts for RQ3 with respective README;
* **data-collection** contains the scripts used to collect the data used for the analysis. **Note:** data may change given the dynamic nature of GitHub (e.g., more commits and files sadded/removed from a repository). 


## Data

In order:

1. `collected_repositories.csv` contains data of the 1114 collected repositories.

2. `selected_repositories.csv` contains data of the 200 repositories that satisfied the inclusion criteria. 



## Tool
s used

* [iac-miner](https://github.com/stefanodallapalma/iac-miner) ([PyPI v0.0.2](https://pypi.org/project/iacminer/)) - to crawl GitHub and collect relevant Ansible-based repositories, as well as labelling defect-prone scripts. It uses *PyDriller* and *RepositoryScorer*.
  
* [PyDriller](https://github.com/ishepard/pydriller) ([PyPI v1.13](https://pypi.org/project/PyDriller/)) - to analyze the history of a repository and to extract process metrics;
  
* [RepositoryScorer](https://github.com/stefanodallapalma/repository-scorer) ([PyPI v1.0.3](https://pypi.org/project/repository-scorer/)) - to compute the scores of the criteria listed in the paper; 


* [AnsibleMetrics](https://github.com/radon-h2020/radon-ansible-metrics) ([PyPI v0.3.2](https://pypi.org/project/ansiblemetrics/)) - to extract product and delta metrics.


## Script for Training and Validation
The data and the scripts are available on Kaggle. Click [here](https://www.kaggle.com/stefadp/ansibledefectsprediction).
The [kernels](https://www.kaggle.com/stefadp/ansibledefectsprediction/kernels?sortBy=hotness&group=everyone&pageSize=20&datasetId=591542) are divided in three groups:

* the kernels with title *\<owner>/\<repository>* were used to answer RQ1.
* the kernels with title ***metrics**/\<owner>/\<repository>* were used to answer RQ2.
* the kernels with title ***rfe**/\<owner>/\<repository>* were used to answer RQ3.
