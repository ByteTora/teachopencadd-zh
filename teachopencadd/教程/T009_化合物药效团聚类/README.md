# T009 ·基础配体的疗效团

* * 注 **：请引导个单元格运行此笔记本。也可以在一个中运行所有单元格，但是，可能会失去很少部分 nglview 3D显示。

 ## 这次演讲的目的 在本次演讲中，我们使用已知的 EGFR 配体（在之前的演讲中选择和对手）来识别每个配体的供应商、受体和杀虫剂功效团的特征。然后将这些聚合物类定义为一个综合疗效团，该疗效团代表一组已了解EGFR配体的特殊性，可用于通过模拟筛选新的EGFR配体。

## 学习目标

# 理论中的内容

* 药效团建模 * 基于结构和配体的药效团建模 * 使用药效团进行虚拟筛选 * 类别：k-means

 # 内容 *实战*

* 从以前的谈话中获取预对齐的配体 * 使用 NGLView 显示配体 * 提取物药效团特性 * 显示所有配体的药效团特征 * 氢键供体 * 氢键受体 * 疏水触点 * 按特征类型收集特征坐标 * 生成集合药效团 * 作为k-means大众装置静态参数 * 设置集群选择的静态参数 * 定义 k-means大众和大众选择函数数 * 集群功能 * 选择相关集群 * 获取选定的集群坐标 * 显示集群 * 氢键供体 * 氢键受体 * 疏水触点 * 显示集合药效团



* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Pratik Dhakal，CADD研讨会，2017年，Charité/FU柏林 - Florian Gusewski，CADD研讨会，2018年，Charité/FU柏林 - Jaime Rodríguez-Guerra，[Amsteramer Lab] (https：//volkamerab.org/），Charité - Dominique Sydow，[Amsteramer Lab]（https：//volkamerab.org/)，Charité

 __Talktext T009__：该Talktext是[第一篇TeachOpenCADD论文] (https：//jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)中描述的TeachOpenCADD管道的一部分，由talkSYS T001-T010组成。

 # 参考文献

* IUPAC药效团定义 ([纯&应用程序化学</i>(1998年)，<b>70</b>，1129-43](https://www.degruyter.com/view/journals/pac/70/5/article-p1129.xml)) * LigandScout中的3D药效团 ([J·化学。信息模型。</i>(2005年)，<b>45</b>，160-9](https://pubs.acs.org/doi/10.1021/ci049885e)) * 图书章节：药效团感知和应用 ([应用化学信息学，Wiley-VCH Verlag GmbH&Co.KGaA，Weinheim，(2018)，**1**，259-82](https://onlinelibrary.wiley.com/doi/10.1002/9783527806539.ch6f)) * 图书章节：基于结构的虚拟筛选([应用化学信息学，Wiley-VCH Verlag GmbH&Co.KGaA，Weinheim，(2018)，**1**，313-31](https://onlinelibrary.wiley.com/doi/10.1002/9783527806539.ch6h)). * Monty Kier和药效团概念的起源 ([<i>互联网电子。J.Mol.DES</i>(2007年)，<b>6</b>，271-9](http://biochempress.com/Files/iejmd_2007_6_0271.pdf)) * Nik Stiefl使用RDKit演示药效团建模 ([GitHub](https://github.com/rdkit/UGM_2016/blob/master/Notebooks/Stiefl_RDKitPh4FullPublication.ipynb))上的RDKit UGM 2016 