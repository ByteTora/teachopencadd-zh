# T001 · 化合物数据获取 (ChEMBL)

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供作为研究项目起点的流程模板。

作者：

- Svetlana Leng, CADD seminar 2017, Volkamer 实验室, Charité/FU Berlin 
- Paula Junge, CADD seminar 2018, Volkamer 实验室, Charité/FU Berlin
- Dominique Sydow, 2019-2020, [Volkamer 实验室, Charité](https://volkamerlab.org/)
- Andrea Volkamer, 2020, [Volkamer 实验室, Charité](https://volkamerlab.org/)
- Yonghui Chen, 2020, [Volkamer 实验室, Charité](https://volkamerlab.org/)


__教程 T001__：本教程是 [第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x) 中描述的 TeachOpenCADD 流程的一部分，包含教程 T001-T010。


## 本教程目标

在本笔记本中，我们将了解更多关于 ChEMBL 数据库的知识，以及如何从 ChEMBL 提取数据，即目标靶点的（化合物，活性数据）配对。这些数据集可用于许多化学信息学任务，如相似性搜索、聚类或机器学习。

我们的工作将包括查找针对特定靶点测试过的化合物，并过滤可用的生物活性数据。


### *理论* 内容

* ChEMBL 数据库
    * ChEMBL 网络服务
    * ChEMBL 网络资源客户端
* 化合物活性度量
    * IC50 度量
    * pIC50 值


### *实践* 内容
    
**目标：获取给定靶点的化合物生物活性数据列表**

* 连接 ChEMBL 数据库
* 获取靶点数据（示例：EGFR 激酶）
    * 获取并下载靶点数据
    * 选择靶点 ChEMBL ID
* 获取生物活性数据
    * 获取并下载靶点的生物活性数据
    * 预处理并过滤生物活性数据
* 获取化合物数据
    * 获取并下载化合物数据
    * 预处理并过滤化合物数据
* 输出生物活性-化合物数据
    * 合并生物活性和化合物数据，并添加 pIC50 值
    * 绘制 pIC50 最高的分子
    * 冻结生物活性数据到 ChEMBL 27
    * 写入输出文件


### References

* ChEMBL bioactivity database: [Gaulton *et al.*, <i>Nucleic Acids Res.</i> (2017), 45(Database issue), D945–D954](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5210557/)
* ChEMBL web services: [Davies *et al.*, <i>Nucleic Acids Res.</i> (2015), <b>43</b>, 612-620](https://academic.oup.com/nar/article/43/W1/W612/2467881) 
* [ChEMBL web-interface](https://www.ebi.ac.uk/chembl/)
*  GitHub [ChEMBL web rescource client](https://github.com/chembl/chembl_webresource_client)
* The EBI RDF platform: [Jupp *et al.*, <i>Bioinformatics </i> (2014), 30(9), 1338-9](https://www.ncbi.nlm.nih.gov/pubmed/24413672)
* Info on half maximal inhibitory concentration: [(p)IC50](https://en.wikipedia.org/wiki/IC50)
* [UniProt website](https://www.uniprot.org/)
