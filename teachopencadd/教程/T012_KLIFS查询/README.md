# T012 · 从 KLIFS 获取数据

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Dominique Sydow, 2019-2020, [Volkamer lab, Charité](https://volkamerlab.org/)
- Jaime Rodríguez-Guerra, 2019-2020, [Volkamer lab, Charité](https://volkamerlab.org/)
- David Schaller, 2020, [Volkamer lab, Charité](https://volkamerlab.org/)


## 本教程的目标

[KLIFS](https://klifs.net/) 是一个激酶-配体相互作用指纹和结构数据库。

首先，我们将使用一个查询激酶（[EGFR](https://www.uniprot.org/uniprot/P00533)）来获取所有可用的蛋白质结构，并探索其结合的配体以及相互作用指纹。然后，我们将探索 EGFR 抑制剂 [吉非替尼](https://pubchem.ncbi.nlm.nih.gov/compound/Gefitinib) 的生物活性数据，以寻找脱靶靶标。最后，我们提供了一个便捷函数，允许轻松探索不同的激酶。

### _理论_ 部分内容

* 激酶
* EGFR 与吉非替尼
* KLIFS 数据库
* KLIFS OpenAPI
* `opencadd`

### _实践_ 部分内容

* 定义感兴趣的激酶和配体：EGFR 和吉非替尼
* 生成 KLIFS Python 客户端
* 探索 KLIFS OpenAPI
  * 激酶组
  * 激酶家族
  * 激酶
  * 结构
  * 相互作用指纹
  * 结构坐标
  * 配体
* 案例研究：EGFR（使用 `opencadd`）
  * 获取 EGFR 的所有结构
  * 平均相互作用指纹
  * 选择一个 EGFR-吉非替尼结构示例
  * 使用 `nglview` 显示结构
  * 使用 `rdkit` 显示所有激酶结合配体
  * 探索吉非替尼的筛选数据
* 探索 KLIFS 中的随机激酶

### References

* Introduction to protein kinases and inhibition ([Chapter 9 in _Med. Chem. Anticancer Drugs_ (2008), 251-305](https://www.sciencedirect.com/science/article/pii/B9780444528247000093))
* Kinase classification by Manning _et al._ ([_Science_ (2002), __298__, 1912-1934](https://pubmed.ncbi.nlm.nih.gov/12471243/))
* Kinase-centric computational drug development ([_Annu. Rep. Med. Chem._ (2017), __50__, 197-236](https://www.sciencedirect.com/science/article/pii/S0065774317300040?via%3Dihub))
* EGFR and Gefitinib 
  * Review on the EGFR family ([_Pharmacol. Res._ (2019), __139__, 395-411](https://www.sciencedirect.com/science/article/abs/pii/S104366181831747X?via%3Dihub) and [_Front. Cell Dev. Biol._ (2016), __8__](https://www.frontiersin.org/articles/10.3389/fcell.2016.00088/full))
  * EGFR kinase details on [UniProt](https://www.uniprot.org/uniprot/P00533)
  * Gefitinib details on [PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/Gefitinib)
* KLIFS - a kinase-inhibitor interactions database
   * Main database/website reference ([_Nucleic Acids Res._ (2020)](https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkaa895/5934416))
   * Introduction of the KLIFS website & database ([_Nucleic Acids Res._ (2016), __44__, 6, D365–D371](https://doi.org/10.1093/nar/gkv1082))
   * Initial KLIFS dataset, binding mode classification, residue numbering ([_J. Med. Chem._ (2014), __57__, 2, 249-277](https://pubs.acs.org/doi/abs/10.1021/jm400378w))
* NGLView, the interactive molecule visualizer ([_Bioinformatics_ (2018), __34__, 1241–124](https://doi.org/10.1093/bioinformatics/btx789))
