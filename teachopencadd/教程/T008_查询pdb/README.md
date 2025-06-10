# T008 ·蛋白质数据采集：蛋白质数据库 （PDB）



## 本次讲座的目的


在这个讲座中，我们为下一个讲座奠定了基础，我们将为 EGFR 生成基于配体的集合药效团。因此，我们：
（i） 从 PDB 数据库中获取满足特定条件的所有 EGFR PDB ID（例如，高分辨率的配体结合结构），
（ii） 回收具有最佳结构质量的蛋白质-配体结构，
（iii） 调整所有结构，以及
（iv） 提取并保存配体以用于下一次课程。


### 理论内容


- 蛋白质数据库 （） 
- 使用 Python 包查询 PDB`biotite`和`pypdb` 


### 实用内容


* 选择查询蛋白
* 获取查询 protein 的 PDB 条目数
* 查找满足特定条件的 PDB 条目
* 选择具有最高分辨率的 PDB 条目
* 从顶部结构中获取配体的元数据
* 绘制顶部配体分子
* 创建蛋白质-配体 ID 对
* 对齐 PDB 结构并提取配体



**注意：** 此讲座是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

Authors:

- Anja Georgi, CADD seminar, 2017, Charité/FU Berlin
- Majid Vafadar, CADD seminar, 2018, Charité/FU Berlin
- Jaime Rodríguez-Guerra, [Volkamer lab, Charité](https://volkamerlab.org/)
- Dominique Sydow, [Volkamer lab, Charité](https://volkamerlab.org/)


__Talktorial T008__：此演讲是第一篇 TeachOpenCADD 出版物 （[_J. Cheminform._ （2019）， **11**， 1-7]（https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x）） 中描述的 TeachOpenCADD 管道的一部分，由演讲 T001-T010 组成。


### 引用


* Protein Data Bank 
([PDB website](http://www.rcsb.org/))
* `pypdb` Python package 
([_Bioinformatics_ (2016), **1**, 159-60](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv543); [documentation](http://www.wgilpin.com/pypdb_docs/html/))
* `biotite` Python package ([_BMC Bioinformatics_ (2018), **19**](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2367-z); [documentation](https://www.biotite-python.org/))
* Molecular superposition with the Python package `opencadd` ([repository](https://github.com/volkamerlab/opencadd))
