# T001 · 化合物数据获取 (ChEMBL)

## 课程目标

在此notebook中，我们将会学到更多有关CHEMBL数据库的知识，以及如何从CHEMBL数据库中提取数据,例如:特定靶点的(化合物，活性)数据对。这些数据集合可以用在很多化学信息学的下游任务中，如相似性搜索、聚类或机器学习中。

我们的工作将包括寻找针对特定靶点进行测试的化合物，并筛选可用的生物活性数据。

### *原理部分*

* ChEMBL 数据库
    * ChEMBL web services
    * ChEMBL web resource client
* 化合物活性衡量指标
    * IC50 衡量
    * pIC50 值

### *实战部分*
    
**目标: 针对特定靶点获取小分子的活性数据列表**

* 连接ChEMBL数据库
* 获取靶点数据(示例: EGFR激酶)
    * 拉取并下载靶点数据
    * 选择靶点ChEMBL ID
* 获取活性数据
    * 拉取并下载特定靶点的生物活性数据
    * 预处理和筛选生物活性数据、
* 获取化合物数据
    * 拉取并下载化合物数据
    * 预处理和过滤化合物数据
* 输出 生物活性-化合物 数据
    * 合并活性和化合物数据, 并添加pIC50值
    * 画出pIC50值分布图
    * 保持在ChEMBL 27 版本
    * 保存结果到文件

### 参考文献

* ChEMBL bioactivity database: [Gaulton *et al.*, <i>Nucleic Acids Res.</i> (2017), 45(Database issue), D945–D954](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5210557/)
* ChEMBL web services: [Davies *et al.*, <i>Nucleic Acids Res.</i> (2015), <b>43</b>, 612-620](https://academic.oup.com/nar/article/43/W1/W612/2467881) 
* [ChEMBL web-interface](https://www.ebi.ac.uk/chembl/)
*  GitHub [ChEMBL web rescource client](https://github.com/chembl/chembl_webresource_client)
* The EBI RDF platform: [Jupp *et al.*, <i>Bioinformatics </i> (2014), 30(9), 1338-9](https://www.ncbi.nlm.nih.gov/pubmed/24413672)
* Info on half maximal inhibitory concentration: [(p)IC50](https://en.wikipedia.org/wiki/IC50)
* [UniProt website](https://www.uniprot.org/)