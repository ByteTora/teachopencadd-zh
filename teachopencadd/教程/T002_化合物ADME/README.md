# T002 · 分子过滤：ADME 和先导化合物相似性标准

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供作为研究项目起点的流程模板。

作者：

- Michele Wichmann, CADD seminars 2017, Charité/FU Berlin
- Mathias Wajnberg, CADD seminars 2018, Charité/FU Berlin
- Dominique Sydow, 2018-2020, [Volkamer 实验室](https://volkamerlab.org), Charité
- Andrea Volkamer, 2018-2020, [Volkamer 实验室](https://volkamerlab.org), Charité


__教程 T002__：本教程是 [第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x) 中描述的 TeachOpenCADD 流程的一部分，包含教程 T001-T010。


## 本教程目标

在药物设计的背景下，根据候选分子的物理化学性质等进行过滤非常重要。在本教程中，从 ChEMBL（__教程 T001__）获取的化合物将通过 Lipinski 的五规则进行过滤，以仅保留口服生物可利用的化合物。


### _理论_ 内容

* ADME - 吸收、分布、代谢和排泄
* 先导化合物相似性和 Lipinski 五规则 (Ro5)
* 先导化合物相似性背景下的雷达图


### _实践_ 内容

* 定义并可视化示例分子
* 计算并绘制 Ro5 的分子属性
* 检查 Ro5 的符合性
* 将 Ro5 应用于 EGFR 数据集
* 可视化 Ro5 属性（雷达图）


### References

* ADME criteria ([Wikipedia](https://en.wikipedia.org/wiki/ADME) and [<i>Mol Pharm.</i> (2010), <b>7(5)</b>, 1388-1405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3025274/))
* [SwissADME](https://www.nature.com/articles/srep42717) webserver
* What are lead compounds? ([Wikipedia](https://en.wikipedia.org/wiki/Lead_compound))
* What is the LogP value? ([Wikipedia](https://en.wikipedia.org/wiki/Partition_coefficient))
* Lipinski et al. "Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings." ([<i>Adv. Drug Deliv. Rev.</i> (1997), <b>23</b>, 3-25](https://www.sciencedirect.com/science/article/pii/S0169409X96004231))
* Ritchie et al. "Graphical representation of ADME-related molecule properties for medicinal chemists" ([<i>Drug. Discov. Today</i> (2011), <b>16</b>, 65-72](https://www.ncbi.nlm.nih.gov/pubmed/21074634))
