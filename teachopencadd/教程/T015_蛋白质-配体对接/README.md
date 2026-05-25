# T015 ·蛋白质配体对接

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Jaime Rodríguez-Guerra，2019-20，[Amsteramer Lab，Charité] (https：//volkamerab.org/） - Dominique Sydow，2019-20，[Amplamer Lab，Charité]（https：//volkamerab.org/） - Michele Wichmann，2019-20，学生在[Charité实验室]工作（https：//volkamerab.org/） - Maria Trofimova，CADD研讨会，2020年，Charité/FU柏林 - David Scholer，2020-21，[Amplamer实验室，Charité]（https：//volkamerab.org/） - Andrea Thomamer，2021年，[Thomamer实验室，Charité]（https：//volkamerab.org/) 

 ## 本期脱口秀的目标

在本期谈话中，我们将使用分子对接来预测小分子在蛋白质结合位点的结合模式。表皮生长因子受体（[EGFR] (https：//www.uniprot.org/uniprot/P00533））将充当模型系统，以解释使用对接软件[Smina]（https：//sourceforge.net/projects/smina/）（Autodock Vina的分支)进行分子对接工作流程的重要步骤。

 # * 理论 * 内容

- 分子对接 - 采样算法 - 评分函数 - 限制 - 目视检查 - 对接软件 - 商业 - 免费（针对学术界）

 # * 实用 * 中的内容

- 蛋白质和配体的制备 - 绑定站点定义 - 对接计算 - 对接结果可视化

 # 参考资料 - -分子对接： - Pagadala等人，[_Biophy Rev_(2017)，__9__，91-102](https://doi.org/10.1007/s12551-016-0247-1) - Meng_et al_，[_Curr计算机辅助药物DES_(2011)，__7__，2,146-157](https://doi.org/10.2174/157340911795677602) - 格罗姆斯基等人，[_NAT Rev Chem_(2019年)，__3__，119-128](https://doi.org/10.1038/s41570-018-0066-y) - 对接和评分功能评估： - Warren_et al_，[_J Med Chem_(2006)，__49_，20,5912-31](https://doi.org/10.1021/jm050362n) - Wang_et al_，[_Phys Chem Chem Phys_(2016)，__18__，18,12964-75](https://doi.org/10.1039/c6cp01555g) - KOES等人，[_J化学信息模型_(2013)，__53__，8,1893年-1904年](https://doi.org/10.1021/ci300604z) - 金伯等人，[_Int J Mol Sci_，(2021年)，__22__，9，1-34](https://doi.org/10.3390/ijms22094435) - 麦克纳特等人，[_J化学信息_(2021年)，__13_，43，13-43](https://doi.org/10.1186/s13321-021-00522-2) - 对接结果的目视检查：Fischer等人，[_J Med Chem_(2021年)，____，5,2489–2500](https://doi.org/10.1021/acs.jmedchem.0c02227) - 使用的工具 - -[OpenBabel](http://openbabel.org/wiki/Main_Page) - -[Smina](https://sourceforge.net/projects/smina/) - -[NGLView](http://nglviewer.org/nglview/latest/) 