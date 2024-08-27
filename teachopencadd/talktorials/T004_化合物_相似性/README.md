# T004 · 基于配体的筛选：化合物相似性


Authors:

- Andrea Morger, 2017-2020, [Volkamer lab](https://volkamerlab.org/), Charité
- Franziska Fritz, CADD seminar, 2018, Charité/FU Berlin
- Yonghui Chen, 2019-2020, [Volkamer lab](https://volkamerlab.org/), Charité
- Dominique Sydow, 2018-2020, [Volkamer lab](https://volkamerlab.org/), Charité



## 课程目标

在这个教程中，我们将熟悉不同的编码（描述符，指纹）和比较（相似性度量）分子的方法。此外，我们将以相似性搜索的形式进行虚拟筛选，针对EGFR抑制剂Gefitinib对我们从ChEMBL数据库中筛选出的经过Lipinski的五规则过滤的EGFR测试分子数据集进行搜索（见**演讲教程T002**）。

### _理论_ 部分内容

* 分子相似性
* 分子描述符
* 分子指纹
  * 基于子结构的指纹
  * MACCS指纹
  * Morgan指纹和环形指纹
* 分子相似性度量
  * Tanimoto 系数
  * Dice 系数
* 虚拟筛选
  * 使用相似性搜索进行虚拟筛选
  * 富集图



### _实践_ 部分内容

* 导入和绘制分子
* 计算分子描述符
  * 1D分子描述符：分子量
  * 2D分子描述符：MACCS指纹
  * 2D分子描述符：Morgan指纹
* 计算分子相似性
  * MACCS指纹：Tanimoto系数和Dice系数相似性
  * Morgan指纹：Tanimoto系数和Dice系数相似性
* 使用相似性搜索进行虚拟筛选
  * 将查询分子与数据集中的所有分子进行比较
  * 相似性值的分布
  * 可视化最相似的分子
  * 生成富集图
  * 计算富集因子



### 参考文献

* Review on "Molecular similarity in medicinal chemistry" ([<i>J. Med. Chem.</i> (2014), <b>57</b>, 3186-3204](https://pubmed.ncbi.nlm.nih.gov/24151987))
* [Morgan fingerprints](http://www.rdkit.org/docs/GettingStartedInPython.html#morgan-fingerprints-circular-fingerprints) with `rdkit`
* Description of the extended-connectivity fingerprint ECFP ([<i>J. Chem. Inf. Model.</i> (2010), <b>50</b>,742-754](https://pubs.acs.org/doi/abs/10.1021/ci100050t))
* What is the chemical space?
([<i>ACS Chem. Neurosci.</i> (2012), <b>19</b>, 649-57](https://www.ncbi.nlm.nih.gov/pubmed/23019491))
* List of [molecular descriptors](https://www.rdkit.org/docs/GettingStartedInPython.html#list-of-available-descriptors) in `rdkit`
* List of [fingerprints](https://www.rdkit.org/docs/GettingStartedInPython.html#list-of-available-fingerprints) in `rdkit`
* Introduction to enrichment plots ([Applied Chemoinformatics, Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim, (2018), **1**, 313-31](https://onlinelibrary.wiley.com/doi/10.1002/9783527806539.ch6h))
