# T020 ·分析分子动力学模拟

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Mareike Leja，2020/21，在[Amsteramer Lab，Charité]实习（https：//volkamerab.org/） - David Scholer，2020/21，[Amplamer Lab，Charité] (https：//volkamerab.org/） - Andrea Thomamer，2021年，[Thomamer Lab，Charité]（https：//volkamerab.org/) 

 ## 本期脱口秀的目标

在本期谈话中，我们将介绍分子动力学（MD）模拟的分析方法。介绍的方法包括动画可视化、结构对齐、RMSD计算以及选定的原子距离和键分析。 请注意，我们将使用 ** Talkorial T019** 生成的模拟结果（1 ns，100帧），该结果针对与抑制剂结合的EGFR同工酶（[TSB：3POZ] (https：//www.rcsb.org/structure/3poz））[03P]（https：//www.rcsb.org/rigand/03P)。 

 # * 理论 * 内容

- MD模拟 - 在药物发现过程中的应用 - 灵活结构与静态结构 - 分析MD模拟 - 可视化 - RMSD - 氢键分析

 # * 实用 * 中的内容

- 加载并可视化系统 - 对准 - 蛋白质和配体的RMSD - 随着时间的推移，RMSD - 帧之间的RMSD - 相互作用分析 - 原子距离 - 氢键分析

 # 参考文献

理论背景：

- MD模拟对药物发现的影响回顾（[_J Med Chem_（2016），**59**（9），4035 - 4061] (https：//doi.org/10.1021/acs.jmedchem.5b01684）） - 关于力场的评论（[_J Chem Inf Model_（2018），**58**（3），565-578]（https：//doi.org/10.1021/acs.jcim.8b00042）） - 关于氢键合的评论（[_PLoS One._（2010），**5（8）**，e12029]（https：//doi.org/10.1371%2Fjournal.pone.0012029）） - 分子相互作用指南（[_J. Med. Chem._ 2010，**53（14）**，5061-84]（https：//doi.org/10.1021/jm100112j）） - 维基百科关于[根均方偏差]的文章（https：//en.wikipedia.org/wiki/Root-mean-square_division） - [MDAnalysism]（https：//www.mdAnalysis.org/）和[NGL View]（https：//github.com/arose/nglview)的存储库 