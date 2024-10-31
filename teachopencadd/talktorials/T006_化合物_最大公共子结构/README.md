# T006 ·最大公共子结构


 **注意：** 本talktorial是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供管道模板作为研究项目的起点。

Authors:

- Oliver Nagel, CADD Seminars, 2017, Charité/FU Berlin
- Jaime Rodríguez-Guerra, 2019-2020, [Volkamer lab](https://volkamerlab.org), Charité
- Andrea Volkamer, 2019-2020, [Volkamer lab](https://volkamerlab.org), Charité


 **Talktorial T006** ：此Talktorial是 TeachOpenCADD 管道的一部分，如[第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)，包括 talktorials T001-T010。


## 本次talktorial的目的


大规模化学数据的聚类和分类对于药物发现中各种化学应用领域的导航、分析和知识发现至关重要。

在上一篇文章中，我们学习了如何对分子进行分组（聚类），发现一个簇中的分子看起来彼此相似，并且共享一个共同的支架。除了目视检查，我们还将在这里学习如何计算一组分子共有的最大子结构。


### 内容*理论*


- 一组分子中最大公共子结构的鉴定简介 
- FMCS 算法详解 


### 内容*实际*


* 加载和绘制分子
* 使用不同的输入参数运行 FMCS 算法
* 更多样化的集合：从 ChEMBL 下载的 EGFR 化合物
* 使用交互式临界自适应识别 MCS


### 参考文献


* Dalke A, Hastings J., FMCS: a novel algorithm for the multiple MCS problem. [*J. Cheminf.* 2013; **5** (Suppl 1): O6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3606201/)
* Raymond JW., Willet P., Maximum common subgraph isomorphism algorithms for the matching of chemical structures. [*J Comput Aided Mol Des.* 2002 Jul; **16**(7):521-33](https://link.springer.com/article/10.1023/A:1021271615909)
* [Dalke's website with info on algorithm](http://dalkescientific.com/writings/diary/archive/2012/05/12/mcs_background.html)
* [RDKit Cookbook documentation on MCS](http://www.rdkit.org/docs/Cookbook.html#using-custom-mcs-atom-types)
