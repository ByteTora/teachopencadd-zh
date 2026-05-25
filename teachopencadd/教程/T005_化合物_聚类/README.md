# T005 · 化合物聚类

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供作为研究项目起点的流程模板。

作者：

- Gizem Spriewald, CADD Seminar, 2017, Charité/FU Berlin
- Calvinna Caswara, CADD Seminar, 2018, Charité/FU Berlin
- Jaime Rodríguez-Guerra, 2019-2020, [Volkamer 实验室](https://volkamerlab.org), Charité


__教程 T005__：本教程是 [第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x) 中描述的 TeachOpenCADD 流程的一部分，包含教程 T001-T010。


## 本教程目标

<!-- TODO：这段文字的表述令人困惑 -->

相似化合物可能结合相同靶点并表现出相似效果。
基于这一相似性质原理，化合物相似性可用于通过聚类构建化学分组。
通过这样的聚类，还可以从更大的筛选化合物集合中选择多样化的化合物子集，用于进一步的实验测试。


### _理论_ 内容

* 聚类和 Jarvis-Patrick 算法简介
* Butina 聚类详解
* 选择多样化化合物


### _实践_ 内容

* 使用 Butina 算法进行聚类
* 可视化聚类结果
* 选择最终化合物列表
* 额外内容：运行时间分析


### References

* Butina, D. Unsupervised Data Base Clustering Based on Daylight’s Fingerprint and Tanimoto Similarity: A Fast and Automated Way To Cluster Small and Large Data Set. _J. Chem. Inf. Comput. Sci._ (1999)
* Leach, Andrew R., Gillet, Valerie J. An Introduction to Chemoinformatics (2003)
* [Jarvis-Patrick Clustering](http://www.improvedoutcomes.com/docs/WebSiteDocs/Clustering/Jarvis-Patrick_Clustering_Overview.htm)
* [TDT Tutorial](https://github.com/sriniker/TDT-tutorial-2014/blob/master/TDT_challenge_tutorial.ipynb)
* [RDKit clustering documentation](http://rdkit.org/docs/Cookbook.html#clustering-molecules)
