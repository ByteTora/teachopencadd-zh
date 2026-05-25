# T020 · 分子动力学模拟分析

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Mareike Leja, 2020/21, 实习于 [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- David Schaller, 2020/21, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Andrea Volkamer, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/) 


## 本教程的目标

在本教程中，我们将介绍分子动力学（MD）模拟的分析方法。介绍的方法包括动画可视化、结构比对、RMSD计算以及选定原子距离和氢键分析。
注意，我们将使用**教程 T019** 在EGFR激酶（[PDB: 3POZ](https://www.rcsb.org/structure/3poz)）与抑制剂[03P](https://www.rcsb.org/ligand/03P)结合上生成的模拟结果（1ns，100帧）。

### _理论_ 部分内容

- MD模拟
    - 在药物发现过程中的应用
    - 柔性vs.静态结构
- 分析MD模拟
  - 可视化
  - RMSD
  - 氢键分析

### _实践_ 部分内容

- 加载和可视化系统
- 比对
- 蛋白质和配体的RMSD
  - RMSD随时间变化
  - 帧间RMSD
- 相互作用分析
  - 原子距离
  - 氢键分析

### References

Theoretical Background:

- Review on the impact of MD simulations in drug discovery ([_J Med Chem_ (2016), **59**(9), 4035‐4061](https://doi.org/10.1021/acs.jmedchem.5b01684))
- Review on force fields ([_J Chem Inf Model_ (2018), **58**(3), 565-578](https://doi.org/10.1021/acs.jcim.8b00042))
- Review on hydrogen bonding ([_PLoS One._ (2010), **5(8)**, e12029](https://doi.org/10.1371%2Fjournal.pone.0012029))
- Guide to molecular interactions ([_J. Med. Chem._ 2010, **53(14)**, 5061-84](https://doi.org/10.1021/jm100112j))
- Wikipedia Article about [root-mean-square deviation](https://en.wikipedia.org/wiki/Root-mean-square_deviation)
- Repositories of [MDAnalysis](https://www.mdanalysis.org/) and [NGL View](https://github.com/arose/nglview)
