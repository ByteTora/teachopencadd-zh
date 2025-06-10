# T004 ·基础配体的选择：化学物质相似性

 作者：

- Andrea Morger，2017-2020，[Amplamer Lab] (https：//volkamerab.org/），Charité - Franziska Fritz，CADD研讨会，2018年，Charité/FU柏林 - 陈永辉，2019-2020，[Amplamer Lab]（https：//volkamerab.org/），Charité - Dominique Sydow，2018-2020，[Amsteramer Lab]（https：//volkamerab.org/)，Charité



## 课程目标

在这个教程中，我们将熟悉不同的编码（描述符，指纹）和比较（相似性度量）分子的方法。此外，我们将以类似的方式进行模拟筛选，针对EGFR形成剂Gefitini对我们从ChEmbL数据库中选出的经过Lipinski的五条规则过滤的EGFR测试子数据集进行数据库（见**演讲课程T002**）。

# _理论_ 部分内容

* 分子相似性 * 分子描述符 * 分子指纹 * 基于子结构的指纹 * MACS皱纹 * Morgan皱纹和环形皱纹 * 分子相似性度量 * 谷本数 * 骰子数 * 虚拟筛选 * 使用相似性搜索进行虚拟筛选 * 富集图



# _实践_ 部分内容

* 导入和绘制分子 * 计算分子描述符 * 1D子描述符：子量 * 2D字符描述符：MACS纹路 * 2D字符描述符：Morgan指数 * 计算分子相似性 * MACS指数：Tanimoto相似数和Dice数相似性 * Morgan指数：Tanimoto指数和Dice指数相似 * 使用相似性搜索进行虚拟筛选 * 将查询分子与数据集中的所有分子进行比较 * 相似性值的分布 * 可视化最相似的分子 * 生成富集图 * 计算富集因子



# 参考文献

* 回顾《药物化学中的分子相似性》([J.Med.化学</i>(2014)，<b>57</b>，3186-3204](https://pubmed.ncbi.nlm.nih.gov/24151987)) * [带`rdkit`的摩根fingerprints](http://www.rdkit.org/docs/GettingStartedInPython.html#morgan-fingerprints-circular-fingerprints) * 扩展连接指纹ECFP的描述([J.信息模型。</i>(2010年)，<b>50</b>，742-754](https://pubs.acs.org/doi/abs/10.1021/ci100050t)) * 化学空间是什么？ ([<ACSChem.</i>(2012年)，<b>19</b>，649-57](https://www.ncbi.nlm.nih.gov/pubmed/23019491)) * `rdkit`中的[分子descriptors](https://www.rdkit.org/docs/GettingStartedInPython.html#list-of-available-descriptors)]列表 * `rdkit`中的[fingerprints](https://www.rdkit.org/docs/GettingStartedInPython.html#list-of-available-fingerprints)列表 * 浓缩地块简介([应用化学信息学，Wiley-VCH Verlag GmbH&Co.KGaA，Weinheim，(2018)，**1**，313-31](https://onlinelibrary.wiley.com/doi/10.1002/9783527806539.ch6h)) 