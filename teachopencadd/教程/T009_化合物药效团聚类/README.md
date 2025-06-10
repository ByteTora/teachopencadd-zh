# T009 ·基于配体的药效团


**注意**：请逐个单元格运行此笔记本。也可以在一个中运行所有单元格，但是，可能会缺少部分 nglview 3D 表示。


## 本次演讲的目的
在本演讲中，我们使用已知的 EGFR 配体（在之前的演讲中选择和对齐）来识别每个配体的供体、受体和疏水药效团特征。然后将这些特征聚类以定义一个集合药效团，该药效团代表一组已知 EGFR 配体的特性，可用于通过虚拟筛选搜索新的 EGFR 配体。

## 学习目标

### 理论中的内容

* 药效团建模
  * 基于结构和配体的药效团建模
* 使用药效团进行虚拟筛选
* 聚类：k-means


### 内容 *实战*

* 从以前的谈话中获取预对齐的配体
* 使用 NGLView 显示配体
* 提取物药效团特性
* 显示所有配体的药效团特征
  * 氢键供体
  * 氢键受体
  * 疏水触点
* 按特征类型收集特征坐标
* 生成集合药效团
  * 为 k-means 聚类设置静态参数
  * 设置集群选择的静态参数
  * 定义 k-means 聚类和聚类选择函数
  * 集群功能
  * 选择相关集群
  * 获取选定的集群坐标
* 显示集群
  * 氢键供体
  * 氢键受体
  * 疏水触点
* 显示集合药效团



**Note:** This talktorial is a part of TeachOpenCADD, a platform that aims to teach domain-specific skills and to provide pipeline templates as starting points for research projects.

Authors:

- Pratik Dhakal, CADD seminar, 2017, Charité/FU Berlin
- Florian Gusewski, CADD seminar, 2018, Charité/FU Berlin
- Jaime Rodríguez-Guerra, [Volkamer lab](https://volkamerlab.org/), Charité
- Dominique Sydow, [Volkamer lab](https://volkamerlab.org/), Charité


__Talktorial T009__: This talktorial is part of the TeachOpenCADD pipeline described in the [first TeachOpenCADD paper](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x), comprising of talktorials T001-T010.


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
