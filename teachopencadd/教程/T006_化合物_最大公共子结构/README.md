# T006 · 最大公共子结构

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供作为研究项目起点的流程模板。

作者：

- Oliver Nagel, CADD Seminars, 2017, Charité/FU Berlin
- Jaime Rodríguez-Guerra, 2019-2020, [Volkamer 实验室](https://volkamerlab.org), Charité
- Andrea Volkamer, 2019-2020, [Volkamer 实验室](https://volkamerlab.org), Charité


__教程 T006__：本教程是 [第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x) 中描述的 TeachOpenCADD 流程的一部分，包含教程 T001-T010。


## 本教程目标

大规模化学数据的聚类和分类对于药物发现中各种化学应用领域的导航、分析和知识发现至关重要。

在上一教程中，我们学习了如何对分子进行分组（聚类），并发现同一聚类中的分子彼此相似且共享共同骨架。除了视觉检查外，我们将在此学习如何计算一组分子共有的最大子结构。


### *理论* 内容

* 一组分子中最大公共子结构识别简介
* FMCS 算法详解


### *实践* 内容

* 加载并绘制分子
* 使用不同输入参数运行 FMCS 算法
* 更多样化的集合：从 ChEMBL 下载的 EGFR 化合物
* 使用交互式截止值适应识别 MCS


### References

* Dalke A, Hastings J., FMCS: a novel algorithm for the multiple MCS problem. [*J. Cheminf.* 2013; **5** (Suppl 1): O6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3606201/)
* Raymond JW., Willet P., Maximum common subgraph isomorphism algorithms for the matching of chemical structures. [*J Comput Aided Mol Des.* 2002 Jul; **16**(7):521-33](https://link.springer.com/article/10.1023/A:1021271615909)
* [Dalke's website with info on algorithm](http://dalkescientific.com/writings/diary/archive/2012/05/12/mcs_background.html)
* [RDKit Cookbook documentation on MCS](http://www.rdkit.org/docs/Cookbook.html#using-custom-mcs-atom-types)
