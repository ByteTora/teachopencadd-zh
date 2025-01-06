# T010 ·结合位置相似性和另类预测

* * 注：** 此基座是 TeachOpenCADD 的一部分，该平台在教学特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Angelika Szengel，CADD 2017年研讨会，Charité/FU柏林 - Marvis Sydow，2018年CADD研讨会，Charité/FU柏林 - Richard Gowers，RDKit UGM黑客马拉松2019 - Jaime Rodríguez-Guerra，2020，[Amsteramer Lab] (https：volkamerlab.org），Charité - Dominique Sydow，2018-2020，[Amsteramer Lab]（https：volkamerlab.org），Charité - Mareike Leja，2020，[Amsteramer Lab]（https：volkamerlab.org)，Charité

 __Talkorial T010__：本次演讲是 [第一篇 TeachOpenCADD论坛] (https：//jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)中描述的 TeachOpenCADD 管道的一部分，由演讲 T001-T010 组成。

* * 注 **：请引导个单元格运行此笔记本。也可以在一个中运行所有单元格，但是，可能会缺少很少部分的“nglview”3D显示。

 ## 这次演讲的目的

在本讲座中，我们使用完整蛋白质和结合位点的结构相似性来预测脱靶，即不是药物预期靶标的蛋白质。这可能会导致不必要的副作用或实现所需的药物替代应用（药物重新定位）。 我们讨论了结合位点比较的主要步骤并实施了一种基本方法，即结构之间的几何变化（两个结构之间的均方根偏差）。

# *理论*中的内容

* 脱靶蛋白 * 计算失业预测：结合位置比较 * 成为RMSD 作为类似的简单指标 * 伊玛帕尼，一种前列腺癌

 # * 实用 * 中的内容

* 添加和观看感兴趣的配体（Imatini/STI） * 从DBC获得所有蛋白质-STI 复合物 * 可视为DBC结构 * 对话ZB结构（全蛋白） * 获得成功RMSD（全蛋白） * SEARCH ZB结构（对合位置） * 获取成功RMSD（结合位置） * 过滤掉异常值

 # 参考文献

* 结合部位叠加+对比 * 结合站点比较审查： * [货币。电脑。辅助药物DES。</i>(2008)，<b>4</b>，209-20](https://www.eurekaselect.com/67606/article/how-measure-similarity-between-protein-ligand-binding-sites) * [J.Med.化学。</i>(2016)，<b>9</b>，4121-51](https://pubs.acs.org/doi/10.1021/acs.jmedchem.6b00078) * 与PYTHON的分子叠加：`opencadd`包(`structure.Superpostion`模块)([giHub repository](https://github.com/volkamerlab/opencadd)) * 维基百科关于均方根偏差([RMSD](https://en.wikipedia.org/wiki/Root-mean-square_deviation_of_atomic_positions))和[Structure superposition](https://en.wikipedia.org/wiki/Structural_alignment)]的文章 * 结构叠加：[书中的章节：蛋白质结构比对的算法、应用和挑战*蛋白质化学和结构生物学的进展*(2014年)，**94**，121-75](https://www.sciencedirect.com/science/article/pii/B9780128001684000056?via%3Dihub) * 伊马替尼 * 对伊马替尼的评论：[<i>NAT。克莱恩牧师。Oncol.</i>(2016)，<b>13</b>，431-46](https://www.nature.com/articles/nrclinonc.2016.41) * 伊马替尼乱交： [J.Biol.(2009年)，<b>8</b>，30](https://jbiol.biomedcentral.com/articles/10.1186/jbiol134) * [Imatinib](https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL941)上的Chembl信息 * [伊马替尼相关信息](https://www3.rcsb.org/ligand/STI) * 伊马替尼的副作用 * [MedFact消费品药物Information](https://www.drugs.com/cdi/imatinib.html) * [DrugBank](https://go.drugbank.com/drugs/DB00619) * [BMC Struct.生物</i>(2009年)，<b>9</b>](https://bmcstructbiol.biomedcentral.com/articles/10.1186/1472-6807-9-7) * PDB查询 * `pypdb`Python包 [_生物信息学_(2016)，**1**，159-60](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv543)；[documentation](http://www.wgilpin.com/pypdb_docs/html/) * ‘生物活性物质’ Python包[_BMC Bioinformatics_（2018），**19**] (https：//bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2367-z）; [documination]（https：//www.biotite-python.org/) * 查看 ** Talkorial T008** 了解有关TSB查询的更多详细信息 