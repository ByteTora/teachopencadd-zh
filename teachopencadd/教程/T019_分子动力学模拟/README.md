# T019 · 分子动力学模拟

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Pietro Gerletti, CADD研讨会, 夏里特医学院/柏林自由大学
- Mareike Leja, 2020/21, 实习于 [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Jeffrey R Wagner, 2020, [Open Force Field联盟](https://openforcefield.org/)
- David Schaller, 2020/21, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Andrea Volkamer, 2020/21, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)


**注：**

This 教程 was designed to be used with [Google Colab](https://colab.research.google.com/github/volkamerlab/teachopencadd/blob/1bd7cb0c9f6379aebc0c1a0b1c7413685910cffa/teachopencadd/talktorials/019_md_simulation/talktorial.ipynb). It is also possible to use it on a local computer. However, performing the molecular dynamics simulation may take a considerably long time if no GPU is available.

Also, note that this 教程 **will not run on Windows** for the time being (check progress in [this issue](https://github.com/volkamerlab/teachopencadd/issues/136)).


## 本教程的目标

在本教程中，我们将学习为什么分子动力学（MD）模拟对药物设计很重要，以及执行蛋白质-配体复合物MD模拟所需的步骤。激酶EGFR将作为模拟示例系统。

### _理论_ 部分内容

- 分子动力学
- 力场
- 边界条件
- MD模拟与药物设计
- EGFR激酶

### _实践_ 部分内容

- 在Google Colab上安装
- 针对Linux或MacOS本地安装的环境调整
- 导入依赖项
- 下载PDB文件
- 准备蛋白质-配体复合物
  - 蛋白质准备
  - 配体准备
  - 合并蛋白质和配体
- MD模拟设置
  - 力场
  - 系统
- 执行MD模拟
- 下载结果

### References

- Review on the impact of MD simulations in drug discovery ([_J Med Chem_ (2016), **59**(9), 4035‐4061](https://doi.org/10.1021/acs.jmedchem.5b01684))
- Review on the physics behind MD simulations and best practices ([_Living J Comp Mol Sci_ (2019), **1**(1), 5957](https://doi.org/10.33011/livecoms.1.1.5957))
- Review on force fields ([_J Chem Inf Model_ (2018), **58**(3), 565-578](https://doi.org/10.1021/acs.jcim.8b00042))
- Review on EGFR in cancer ([_Cancers (Basel)_ (2017), **9**(5), 52](https://dx.doi.org/10.3390%2Fcancers9050052))
- Summarized statistical knowledge from Pierre-Simon Laplace ([Théorie Analytique des Probabilités _Gauthier-Villars_ (1820), **3**)](https://archive.org/details/uvrescompltesde31fragoog/page/n15/mode/2up)
- Inspired by a notebook form Jaime Rodríguez-Guerra ([github](https://github.com/jaimergp/uab-msc-bioinf/blob/master/MD%20Simulation%20and%20Analysis%20in%20a%20Notebook.ipynb))
- Repositories of [OpenMM](https://github.com/openmm/openmm) and [OpenMM Forcefields](https://github.com/openmm/openmmforcefields), [RDKit](https://github.com/rdkit/rdkit), [PyPDB](https://github.com/williamgilpin/pypdb), [MDTraj](https://github.com/mdtraj/mdtraj), [PDBFixer](https://github.com/openmm/pdbfixer)
- Wikipedia articles about [MD simulations](https://en.wikipedia.org/wiki/Molecular_dynamics), [AMBER](https://en.wikipedia.org/wiki/AMBER) and [force fields](https://en.wikipedia.org/wiki/Force_field_(chemistry)) in general
