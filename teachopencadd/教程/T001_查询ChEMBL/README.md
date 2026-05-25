# T001 ·化学物数据获取（ChMBE）

## 课程目标

在这个笔记本中，我们将来会学到更多有关CHEMBL数据库的知识，以及如何从CHEMBL数据库中提取数据，例如：指定点的（化学物质，活性）数据对。这些数据集合可以用在很多化学信息学的下游任务中，如相似性搜索、聚类或机器学习中。

我们的工作将包括寻找针对特定靶点进行测试的化合物，并筛选可用的生物活性数据。

# *原理部分*

* ChEmbL 数据库 * ChEmbL网络服务 * ChEmbL网络资源客户端 * 化合物活性衡量指标 * IC50数量 * pIC50 值

# *实战部分* * *目标：针对特定地点获取小分子的活动数据列表**

* 连接ChMBE数据库 * 获取点数据（示例：EGFR酶） * 拉取并下载靶点数据 * 选择点ChMBE ID * 获取活性数据 * 拉取并下载特定靶点的生物活性数据 * 预处理和选择生物活性数据， * 获取化合物数据 * 拉取并下载化合物数据 * 预处理和过滤化合物数据 * 输入生物活性-化学物质数据 * 结合活性和化学数据，并添加pIC50 * 画出pIC50值分布图 * 保持在ChMBE 27 版本 * 保存结果到文件

# 参考文献

* ChEmbL生物活性数据库：[Gaulton *et al.*，<i>Nucleic Acids Res. </i>（2017），45（数据库问题），D945-D954] (https：//www.ncbi.nlm.nih.gov/pmc/articles/PMC5210557/） * ChEmbL网络服务：[Davies *et al.*，<i>Nucleic Acids Res. </i>（2015），<b>43</b>，612-620]（https：//academic.oup.com/nar/article/43/W1/W612/2467881） * [ChMBE网络界面]（https：//www.ebi.ac.uk/chembl/） * GitHub [ChMBE网络撤销客户端]（https：//github.com/chembl/chembl_webresourc_client） * EBI RDF平台：[Deliverp *et al.*，<i>生物信息学</i>（2014），30（9），1338-9]（https：//www.ncbi.nlm.nih.gov/pubmed/24413672） * 关于一半最大抑制浓度的信息：[（p）IC 50]（https：//en.wikipedia.org/wiki/IC50） * [UniProt网站]（https：//www.uniprot.org/)