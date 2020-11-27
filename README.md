# Within-Project Defect Prediction of Infrastructure-as-Code Using Product and Process Metrics

Replication package for the paper *"Defect Prediction of Infrastructure-as-Code Using Product and Process Metrics"* submitted at Transantions on Software Engineering (TSE 2020).

## Info

* **METRICS.md** - Table of metrics used to train the models (introduced in Section 3.3)
* **HYPER-PARAMETERS.md** - Hyper-parameters used to train the models (introduced in Section 3.4)
* **RQ1.md** - Results of RQ1.
* **RQ2.md** - Results of RQ2.
* **RQ3.md** - Results of RQ3. (**TO ADD**)



## Data

In order:

1. `collected-repositories.csv` - the 1050 collected repositories.

2. `selected-repositories.csv` - the 200 repositories that satisfied the inclusion criteria in Table 1.

3. `analyzed-repositories.csv` - the 104 repositories used to answer the RQs.

4. `rq1.csv` - data collected to answer RQ1 (Techniques performance).

5. `rq2.csv` - data collected to answer RQ2 (Metrics performance).

6. `rq3.json` - data collected to answer RQ3 (Recursive Feature Elimination). (**TO ADD**)



## Kaggle
On kaggle it is possible to find the dataset containing the data to build the models. [Go to Kaggle](https://www.kaggle.com/stefadp/ansibledefectsprediction/) or [download](https://www.kaggle.com/stefadp/ansibledefectsprediction/download) the dataset.


The [kernels](https://www.kaggle.com/stefadp/ansibledefectsprediction/kernels?sortBy=hotness&group=everyone&pageSize=20&datasetId=591542) are divided in three groups:

* `rq1/<owner>/<repository>` were used for RQ1.
* `tse2020/rq2/<owner>/<repository>` were used for RQ2.
* `tse2020/rq3/<owner>/<repository>` were used for RQ3.
* `tse2020/add/<owner>/<repository>` were used for an additional analysis of RQ3.



## Tool Suite

1. `IaC Github Repositories Collector` - To collect active repositories. Available on [Github](https://github.com/radon-h2020/radon-repositories-collector) and [PyPI](https://pypi.org/project/repositories-collector/).

2. `Repository Scorer` - To collect repository metrics based on best engineering practices. 
Available on [Github](https://github.com/radon-h2020/radon-repository-scorer) and [PyPI](https://pypi.org/project/repository-scorer/).

3. `IaC Repository Miner` - To miner repositories and collect product, delta, and process metrics.
Available on [Github](https://github.com/radon-h2020/radon-repository-miner) and [PyPI](https://pypi.org/project/repository-miner/).
 
    3.1. `AnsibleMetrics` - To extract product metrics for Ansible.
    Available on [Github](https://github.com/radon-h2020/radon-ansible-metrics) and [PyPI](https://pypi.org/project/ansiblemetrics/).
 
    3.1. `PyDriller` - To analyze commit history and extract process metrics.
    Available on [Github](https://github.com/ishepard/pydriller) and [PyPI](https://pypi.org/project/PyDriller/).

4. `IaC Defect Predictor` - To build and evaluate models. Available on [Github](https://github.com/radon-h2020/radon-defect-prediction-cli) and [PyPI](https://pypi.org/project/radon-defect-predictor/).




