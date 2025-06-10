# T012 ·从KlIFS获取数据

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Dominique Sydow，2019-2020，[Amsteramer Lab，Charité] (https：//volkamerab.org/） - Jaime Rodríguez-Guerra，2019-2020，[Amsteramer Lab，Charité]（https：//volkamerab.org/） - David Scholer，2020，[Amplamer实验室，Charité]（https：//volkamerab.org/)

 ## 本期脱口秀的目标

[KLIFS] (https：//klifs.net/）是一个用于kinase-配体相互作用指纹和结构的数据库。在这篇谈话文章中，我们将使用对此数据库（KLIFS OpenAPI）的编程访问和' opencadd '（[GitHub]（https：//github.com/volkamerlab/opencadd））包来与其丰富的内容进行交互。 首先，我们将使用查询酶（[EGFR]（https：//www.uniprot.org/uniprot/P00533））来获取所有可用的蛋白质结构并探索其结合的配体以及相互作用指纹。然后，我们将探索EGFR抑制剂[吉非替尼]的生物活性数据（https：//pubchem.ncbi.nlm.nih.gov/compound/吉非替尼)，以寻找脱靶物。最后但并非最不重要的是，我们提供了一个便利功能，可以轻松探索不同的kinase。

 # * 理论 * 内容

- 激酶 - EGFR和吉非替尼 - KlIFS数据库 - KlIFS OpenAPI - “opencadd”

 # * 实用 * 中的内容

- 定义感兴趣的蛋白质和配体：EGFR和吉非替尼 - 生成KlIFS Python客户端 - 探索KlIFS OpenAPI - Kinase组 - 激酶家族 - 激酶 - 结构 - 互动指纹 - 结构坐标 - 配体 - 案例研究：EGFR（使用“opencadd”） - 获取EGFR的所有结构 - 平均交互指纹 - 选择EGFR-吉非替尼结构示例 - 用“nglview”显示结构 - 用“rdKit”显示所有与kinase结合的配体 - 探索吉非替尼的分析数据 - 探索KlIFS中的随机酶

 # 参考文献

* 蛋白激酶和抑制导论([第9章in_Med.化学。《抗癌药物》(2008)，251-305](https://www.sciencedirect.com/science/article/pii/B9780444528247000093)) * 由Manning等人进行的Kinase分类([_Science_(2002)，__298__，1912-1934](https://pubmed.ncbi.nlm.nih.gov/12471243/)) * 以Kinase为中心的计算药物开发([_Annu.众议员梅德。化学_(2017)，__50__，197-236](https://www.sciencedirect.com/science/article/pii/S0065774317300040?via%3Dihub)) * EGFR和吉非替尼 * EGFR家族综述([_Pharmacol.Res._(2019)，__139__，395-411](https://www.sciencedirect.com/science/article/abs/pii/S104366181831747X?via%3Dihub)和[_Front.单元格设备《生物》(2016)，__8__](https://www.frontiersin.org/articles/10.3389/fcell.2016.00088/full)) * [UniProt](https://www.uniprot.org/uniprot/P00533)上的EGFR激酶详细信息 * [PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/Gefitinib)上的吉非替尼详情 * KLIF--一个激酶-抑制物相互作用数据库 * 主要数据库/网站参考([_核酸资源_(2020)](https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkaa895/5934416)) * KLIFS网站和数据库介绍([_核酸研究报告_(2016)，__44__，6，D365–D371](https://doi.org/10.1093/nar/gkv1082)) * 初始KLIFS数据集、结合模式分类、残基编号([_J.Med.化学_(2014)，__57_，2,249-277](https://pubs.acs.org/doi/abs/10.1021/jm400378w)) * NGLView，交互式分子可视化工具([_生物信息学_(2018)，__34__，1241–124](https://doi.org/10.1093/bioinformatics/btx789)) 