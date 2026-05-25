# T009 · 基于配体的药效团

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供作为研究项目起点的流程模板。

作者：

- Pratik Dhakal, CADD seminar, 2017, Charité/FU Berlin
- Florian Gusewski, CADD seminar, 2018, Charité/FU Berlin
- Jaime Rodríguez-Guerra, [Volkamer 实验室](https://volkamerlab.org/), Charité
- Dominique Sydow, [Volkamer 实验室](https://volkamerlab.org/), Charité


__教程 T009__：本教程是 [第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x) 中描述的 TeachOpenCADD 流程的一部分，包含教程 T001-T010。


**注意**：请逐个单元格运行此笔记本。虽然也可以一次性运行所有单元格，但部分 nglview 3D 显示可能会缺失。


## 本教程目标

在本教程中，我们使用上一教程中选择并对齐的已知 EGFR 配体，来识别每个配体的供体、受体和疏水药效团特征。然后将这些特征聚类以定义集合药效团，该药效团代表了已知 EGFR 配体集合的属性，可用于通过虚拟筛选搜索新的 EGFR 配体。


## 学习目标


### *理论* 内容

* 药效团建模
  * 基于结构和配体的药效团建模
* 基于药效团的虚拟筛选
* 聚类：k-means


### *实践* 内容

* 从上一教程获取预对齐的配体
* 使用 NGLView 显示配体
* 提取药效团特征
* 显示所有配体的药效团特征
  * 氢键供体
  * 氢键受体
  * 疏水接触
* 按特征类型收集特征坐标
* 生成集合药效团
  * 设置 k-means 聚类的静态参数
  * 设置聚类选择的静态参数
  * 定义 k-means 聚类和聚类选择函数
  * 聚类特征
  * 选择相关聚类
  * 获取选定聚类的坐标
* 显示聚类
  * 氢键供体
  * 氢键受体
  * 疏水接触
* 显示集合药效团


### References

* IUPAC pharmacophore definition 
([<i>Pure & Appl. Chem</i> (1998), <b>70</b>, 1129-43](https://www.degruyter.com/view/journals/pac/70/5/article-p1129.xml))
* 3D pharmacophores in LigandScout 
([<i>J. Chem. Inf. Model.</i> (2005), <b>45</b>, 160-9](https://pubs.acs.org/doi/10.1021/ci049885e))
* Book chapter: Pharmacophore Perception and Applications 
([Applied Chemoinformatics, Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim, (2018), **1**, 259-82](https://onlinelibrary.wiley.com/doi/10.1002/9783527806539.ch6f))
* Book chapter: Structure-Based Virtual Screening ([Applied Chemoinformatics, Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim, (2018), **1**, 313-31](https://onlinelibrary.wiley.com/doi/10.1002/9783527806539.ch6h)).
* Monty Kier and the origin of the pharmacophore concept 
([<i>Internet Electron. J. Mol. Des.</i> (2007), <b>6</b>, 271-9](http://biochempress.com/Files/iejmd_2007_6_0271.pdf))
* Nik Stiefl's demonstration of pharmacophore modeling with RDKit 
([RDKit UGM 2016 on GitHub](https://github.com/rdkit/UGM_2016/blob/master/Notebooks/Stiefl_RDKitPh4FullPublication.ipynb)) 
