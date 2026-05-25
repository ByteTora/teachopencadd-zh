# T008 · 蛋白质数据获取：蛋白质数据库（PDB）

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Anja Georgi, CADD seminar, 2017, Charité/FU Berlin
- Majid Vafadar, CADD seminar, 2018, Charité/FU Berlin
- Jaime Rodríguez-Guerra, [Volkamer lab, Charité](https://volkamerlab.org/)
- Dominique Sydow, [Volkamer lab, Charité](https://volkamerlab.org/)


__教程 T008__：此教程是 TeachOpenCADD 流程的一部分，详见第一篇 TeachOpenCADD 论文（[_J. Cheminform._ (2019), **11**, 1-7](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)），包含教程 T001-T010。


## 本教程的目标

在本教程中，我们将为下一个教程进行基础工作，届时我们将为 EGFR 生成一个基于配体的集成药效团。因此，我们将：
（i）从 PDB 数据库中获取所有满足特定条件（例如，具有高分辨率的配体结合结构）的 EGFR PDB ID，
（ii）检索结构质量最佳的蛋白质-配体结构，
（iii）比对所有结构，以及
（iv）提取并保存配体以供下一个教程使用。

### _理论_ 部分内容

* 蛋白质数据库（PDB）
* 使用 Python 包 `biotite` 和 `pypdb` 查询 PDB

### _实践_ 部分内容

* 选择查询蛋白
* 获取查询蛋白的 PDB 条目数量
* 查找满足特定条件的 PDB 条目
* 选择分辨率最高的 PDB 条目
* 获取最佳结构的配体元数据
* 绘制最佳配体分子
* 创建蛋白质-配体 ID 对
* 比对 PDB 结构并提取配体

### References

* Protein Data Bank 
([PDB website](http://www.rcsb.org/))
* `pypdb` Python package 
([_Bioinformatics_ (2016), **1**, 159-60](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv543); [documentation](http://www.wgilpin.com/pypdb_docs/html/))
* `biotite` Python package ([_BMC Bioinformatics_ (2018), **19**](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2367-z); [documentation](https://www.biotite-python.org/))
* Molecular superposition with the Python package `opencadd` ([repository](https://github.com/volkamerlab/opencadd))
