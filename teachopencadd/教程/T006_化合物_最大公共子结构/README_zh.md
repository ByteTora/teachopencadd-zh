# T006 ·最大公共子结构

* * 注：** 本talkorial是 TeachOpenCADD 的一部分，该平台在教学特定领域的技能，并提供管道模板作为研究项目的起点。

作者：

- Oliver Nagel，CADD研讨会，2017年，Charité/FU柏林 - Jaime Rodríguez-Guerra，2019-2020，[Amsteramer Lab] (https：volkamerlab.org），Charité - Andrea Thomamer，2019-2020，[Thomamer实验室]（https：volkamerlab.org)，Charité

* * Talkorial T006**：此Talkorial是 TeachOpenCADD 管道的一部分，如[第一篇 TeachOpenCADD论坛] (https：//jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)，包括Talkript T001-T010。

 ## 这次谈话的目的

 大规模化学数据的聚类和分类对于药物发现中各种化学应用领域的导航、分析和知识发现至关重要。

在上一篇文章中，我们学习了如何对分子进行分组（聚类），发现一个簇中的分子看起来彼此相似，并且共享一个共同的支架。除了目视检查，我们还将在这里学习如何计算一组分子共有的最大子结构。

 # 内容*理论*

- 一组分子中最大公共子结构的鉴定简介 - FMC算法详解 

 # 内容* 现实 *

* 加载和绘制分子 * 使用不同的输入参数运行FMC算法 * 更多元化的集成：从ChMBE下载的 EGFR化学物质 * 使用交互式世界自适应识别MC

 # 参考文献

* Dalke A、Hastings J.、FMC：一种针对多个MC问题的新颖算法。[*J. Cheminf.* 2013; **5**（增刊1）：O6] (https：//www.ncbi.nlm.nih.gov/pmc/articles/PMC3606201/） * 雷蒙德·JW.，Willet P.，化学结构匹配的最大公共子图同形算法。[*J Comput Aided Mol Des。* 2002年7月; **16**（7）：521-33]（https：//link.springer.com/article/10.1023/A：1021271615909） * [Dalke的网站，包含算法信息]（http：//dalkescientific.com/writings/diary/archive/2012/05/12/mcs_background.html） * [有关MCs的RDKit Cookbook文档]（http：//www.rdkit.org/docs/Cookbook.html#using-custom-mcs-atom-types) 