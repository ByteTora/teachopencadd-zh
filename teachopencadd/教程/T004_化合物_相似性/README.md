# T004 · 基于配体的筛选：化合物相似性

**注：** 本教程是 TeachOpenCADD 的一部分，TeachOpenCADD 是一个旨在教授领域专用技能，并提供可作为研究项目起点的流程模板的平台。

作者：

- Andrea Morger, 2017-2020, [Volkamer 实验室](https://volkamerlab.org/), Charité
- Franziska Fritz, CADD 研讨课, 2018, Charité/FU Berlin
- Yonghui Chen, 2019-2020, [Volkamer 实验室](https://volkamerlab.org/), Charité
- Dominique Sydow, 2018-2020, [Volkamer 实验室](https://volkamerlab.org/), Charité

__教程 T004__：本教程是 [第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)中描述的 TeachOpenCADD 流程的一部分，该流程包含**教程 T001-T010**。

## 本教程的目标

在本教程中，我们将熟悉不同的分子编码方法（描述符、指纹）和比较方法（相似性度量）。此外，我们以 EGFR 抑制剂吉非替尼（Gefitinib）为查询分子，对 ChEMBL 数据库中经 Lipinski 五规则过滤的 EGFR 测试分子数据集（参见**教程 T002**）进行虚拟筛选（相似性搜索）。

### _理论_ 部分内容

* 分子相似性
* 分子描述符
* 分子指纹
  * 基于子结构的指纹
  * MACCS 指纹
  * Morgan 指纹与圆形指纹
* 分子相似性度量
  * Tanimoto 系数
  * Dice 系数
* 虚拟筛选
  * 使用相似性搜索进行虚拟筛选
  * 富集图

### _实践_ 部分内容

* 导入并绘制分子
* 计算分子描述符
  * 1D 分子描述符：分子量
  * 2D 分子描述符：MACCS 指纹
  * 2D 分子描述符：Morgan 指纹
* 计算分子相似性
  * MACCS 指纹：Tanimoto 和 Dice 相似性
  * Morgan 指纹：Tanimoto 和 Dice 相似性
* 使用相似性搜索进行虚拟筛选
  * 将查询分子与数据集中的所有分子进行比较
  * 相似性值分布
  * 可视化最相似分子
  * 生成富集图
  * 计算富集因子

### 参考文献

* "药物化学中的分子相似性"综述（[<i>J. Med. Chem.</i> (2014), <b>57</b>, 3186-3204](https://pubmed.ncbi.nlm.nih.gov/24151987)）
* [Morgan 指纹](http://www.rdkit.org/docs/GettingStartedInPython.html#morgan-fingerprints-circular-fingerprints)，使用 `rdkit`
* 扩展连通性指纹 ECFP 的描述（[<i>J. Chem. Inf. Model.</i> (2010), <b>50</b>, 742-754](https://pubs.acs.org/doi/abs/10.1021/ci100050t)）
* 什么是化学空间？（[<i>ACS Chem. Neurosci.</i> (2012), <b>19</b>, 649-57](https://www.ncbi.nlm.nih.gov/pubmed/23019491)）
* `rdkit` 中的[分子描述符列表](https://www.rdkit.org/docs/GettingStartedInPython.html#list-of-available-descriptors)
* `rdkit` 中的[指纹列表](https://www.rdkit.org/docs/GettingStartedInPython.html#list-of-available-fingerprints)
* 富集图简介（[Applied Chemoinformatics, Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim, (2018), **1**, 313-31](https://onlinelibrary.wiley.com/doi/10.1002/9783527806539.ch6h)）
