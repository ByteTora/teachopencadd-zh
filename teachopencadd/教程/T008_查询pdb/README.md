# T008 · 蛋白质数据获取：蛋白质数据库 (PDB)

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供作为研究项目起点的流程模板。

作者：

- Anja Georgi, CADD seminar, 2017, Charité/FU Berlin
- Majid Vafadar, CADD seminar, 2018, Charité/FU Berlin
- Jaime Rodríguez-Guerra, [Volkamer 实验室, Charité](https://volkamerlab.org/)
- Dominique Sydow, [Volkamer 实验室, Charité](https://volkamerlab.org/)


__教程 T008__：本教程是第一篇 TeachOpenCADD 出版物 ([_J. Cheminform._ (2019), **11**, 1-7](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)) 中描述的 TeachOpenCADD 流程的一部分，包含教程 T001-T010。


## 本教程目标

在本教程中，我们将为下一个教程（为 EGFR 生成基于配体的集合药效团）奠定基础。具体来说，我们 
(i) 从 PDB 数据库中获取满足特定条件（如高分辨率、配体结合结构）的所有 EGFR 的 PDB ID，
(ii) 检索具有最佳结构质量的蛋白质-配体结构，
(iii) 对齐所有结构，以及 
(iv) 提取并保存将在下一个教程中使用的配体。


### 理论内容

* 蛋白质数据库 (PDB)
* 使用 Python 包 `biotite` 和 `pypdb` 查询 PDB


### 实践内容

* 选择查询蛋白质
* 获取查询蛋白质的 PDB 条目数量
* 查找满足特定条件的 PDB 条目
* 选择分辨率最高的 PDB 条目
* 获取最优结构中配体的元数据
* 绘制最优配体分子
* 创建蛋白质-配体 ID 配对
* 对齐 PDB 结构并提取配体


### References

* Protein Data Bank 
([PDB website](http://www.rcsb.org/))
* `pypdb` Python package 
([_Bioinformatics_ (2016), **1**, 159-60](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv543); [documentation](http://www.wgilpin.com/pypdb_docs/html/))
* `biotite` Python package ([_BMC Bioinformatics_ (2018), **19**](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2367-z); [documentation](https://www.biotite-python.org/))
* Molecular superposition with the Python package `opencadd` ([repository](https://github.com/volkamerlab/opencadd))
