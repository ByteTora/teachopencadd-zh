# T005 · 化合物聚类

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Gizem Spriewald, CADD Seminar, 2017, Charité/FU Berlin
- Calvinna Caswara, CADD Seminar, 2018, Charité/FU Berlin
- Jaime Rodríguez-Guerra, 2019-2020, [Volkamer lab](https://volkamerlab.org), Charité


__教程 T005__：此教程是 TeachOpenCADD 流程的一部分，详见[第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)，包含教程 T001-T010。


## 本教程的目标

相似的化合物可能结合相同的靶标并表现出相似的效果。基于这一相似性质原理，化合物相似性可用于通过聚类构建化学分组。通过这样的聚类，还可以从较大的筛选化合物集合中选择多样化的化合物子集，用于进一步的实验测试。

### _理论_ 部分内容

* 聚类简介与 Jarvis-Patrick 算法
* Butina 聚类详解
* 挑选多样化化合物

### _实践_ 部分内容

* 使用 Butina 算法进行聚类
* 可视化聚类结果
* 挑选最终化合物列表
* 扩展：运行时间分析

### References

* Butina, D. Unsupervised Data Base Clustering Based on Daylight’s Fingerprint and Tanimoto Similarity: A Fast and Automated Way To Cluster Small and Large Data Set. _J. Chem. Inf. Comput. Sci._ (1999)
* Leach, Andrew R., Gillet, Valerie J. An Introduction to Chemoinformatics (2003)
* [Jarvis-Patrick Clustering](http://www.improvedoutcomes.com/docs/WebSiteDocs/Clustering/Jarvis-Patrick_Clustering_Overview.htm)
* [TDT Tutorial](https://github.com/sriniker/TDT-tutorial-2014/blob/master/TDT_challenge_tutorial.ipynb)
* [RDKit clustering documentation](http://rdkit.org/docs/Cookbook.html#clustering-molecules)
