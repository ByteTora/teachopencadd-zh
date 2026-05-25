# T019 ·分子动力学模拟

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Pietro Gerletti，2020年CADD研讨会，Charité/FU柏林 - Mareike Leja，2020/21，在[Amsteramer Lab，Charité]实习（https：//volkamerab.org/） - Jeffrey R Wagner，2020年，[Open Force Field Consortium] (https：//openforcefield.org/） - David Scholer，2020/21，[Amplamer Lab，Charité]（https：//volkamerab.org/） - Andrea Thomamer，2020/21，[Thomamer Lab，Charité]（https：//volkamerab.org/)

 __注意__

此谈话文摘旨在与[Google Colab]一起使用（https：//colab.research.google.com/github/volkamerlab/teachopencadd/blo/1bd 7 cb 0 c9 f6379 aebc 0 c1 a0 b1 c7413685910 cffa/teachopencadd/talkopencadd/talkupiter/019_md_simulation/talkorial.ipynb）。也可以在本地计算机上使用它。然而，如果没有可用的图形处理器，执行分子动力学模拟可能需要相当长的时间。

另外，请注意，此谈话脚本 ** 暂时不会在Windows** 上运行（请在[本期] (https：//github.com/volkamerlab/teachopencadd/issues/136）中查看进度)。

 ## 本期脱口秀的目标

 在本期谈话中，我们将了解为什么分子动力学（MD）模拟对于药物设计很重要，以及对与配体复合的蛋白质进行MD模拟所需的步骤。受体受体将作为模拟的样本系统。

 # * 理论 * 内容

- 分子动力学 - 力场 - 边界条件 - MD模拟和药物设计 - EGFR激酶

 # * 实用 * 中的内容

- 在Google Colab上安装 - 为在Linux或MacOS上运行的本地安装调整环境 - Import dependencies - 下载DBC文件 - 准备蛋白质配体复合物 - 蛋白制剂 - 配体制备 - 合并蛋白质和配体 - MD模拟设置 - 力场 - 系统 - 执行MD模拟 - 下载结果

 # 参考文献

- 回顾MD模拟在药物发现中的影响([_J Med Chem_(2016)，**59**(9)，4035‐4061](https://doi.org/10.1021/acs.jmedchem.5b01684)) - 回顾MD模拟和最佳实践背后的物理原理([_Living J Comp Mol Sci_(2019)，**1**(1)，5957](https://doi.org/10.33011/livecoms.1.1.5957)) - 力场回顾([_J化学信息模型_(2018)，**58**(3)，565-578](https://doi.org/10.1021/acs.jcim.8b00042)) - 癌症中的表皮生长因子受体综述([_癌症(巴塞尔)_(2017)，**9**(5)，52](https://dx.doi.org/10.3390%2Fcancers9050052)) - 皮埃尔-西蒙·拉普拉斯总结的统计知识(概率分析S戈蒂尔-维拉尔斯)，**3**)](https://archive.org/details/uvrescompltesde31fragoog/page/n15/mode/2up) - 灵感来自Jaime Rodriguez-Guera([github](https://github.com/jaimergp/uab-msc-bioinf/blob/master/MD%20Simulation%20and%20Analysis%20in%20a%20Notebook.ipynb))的笔记本电脑形式 - [OpenMM](https://github.com/openmm/openmm)和[OpenMM Forcefields](https://github.com/openmm/openmmforcefields)，[RDKit](https://github.com/rdkit/rdkit)，[PyPDB](https://github.com/williamgilpin/pypdb)，[MDTraj](https://github.com/mdtraj/mdtraj)，[PDBFixer](https://github.com/openmm/pdbfixer))的存储库 - 维基百科关于[MD simulations](https://en.wikipedia.org/wiki/Molecular_dynamics)，[琥珀](https://en.wikipedia.org/wiki/AMBER)和[Force fields](https://en.wikipedia.org/wiki/Force_field_(chemistry))])的文章 