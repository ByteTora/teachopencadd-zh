# T025 · Kinase相似性：Kinase口袋（KiSSim指纹）

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Dominique Sydow，2021年，[Amplamer Lab，Charité] (https：//volkamerab.org/） - 塔利亚·B Kimber，2021年，[Amsteramer实验室，Charité]（https：//volkamerab.org/） - Andrea Thomamer，2021年，[Thomamer实验室，Charité]（https：//volkamerab.org/)

 ## 本期脱口秀的目标

我们将使用[KiSSim] (https：//kissim.readthedocs.io/en/latest/)指纹从结构角度评估一组kinase之间的相似性。该指纹描述了结构分辨的kinase的物理化学和空间性质。

_注_：我们重点关注正类固醇蛋白结合位点之间的相似性;与变构结合位点的相似性并未涵盖。

 # * 理论 * 内容

* Kinase数据集 * Kinase相似性描述符：Kinase口袋（KiSSim指纹） * 使用' opencadd.databases.klifs '获取KlIFS数据

 # * 实用 * 中的内容

* 定义感兴趣的类型 * 卸载和预处理数据 * 设置远程KlIFS会话 * 获取描述这些kinase的所有结构 * 滤波器结构 * 显示Kinase覆盖范围 * 计算KiSSim指纹 * 比较结构 * 将结构映射到酶距离矩阵 * 保存Kinase距离矩阵

 # 参考文献

* Kinase数据集：[分子(2021年)、26(3)、629](https://www.mdpi.com/1420-3049/26/3/629) * 蛋白质数据库 * PDB URL：http://www.rcsb.org/ * pdb数据库：[Acta Cryst.</i>(2002年)，<b>D58</b>，899-907](https://doi.org/10.1107/S0907444902003451)和[<i>Structure</i>(2012)，<b>20(3)</b>，391-396](https://doi.org/10.1016/j.str.2012.01.010) * KLIF * KLIFSURL：https://klifs.net/ * KLIF数据库：[<i>核酸研究</i>(2020)，<b>49(D1)</b>，D562-D569](https://doi.org/10.1093/nar/gkaa895) * KLIFS结合位点定义：[J.Med.化学</i>(2014年)，<b>57(2)</b>，249-277(https://doi.org/10.1021/jm400378w) * 结合站点比较审查： * [货币。电脑。辅助药物DES。</i>(2008)，<b>4</b>，209-20](https://www.eurekaselect.com/67606/article/how-measure-similarity-between-protein-ligand-binding-sites) * [J.Med.化学。</i>(2016)，<b>9</b>，4121-51](https://pubs.acs.org/doi/10.1021/acs.jmedchem.6b00078) * KiSSim：Kinase结构相似性 * giHub仓库：https://github.com/volkamerlab/kissim * 文档：https://kissim.readthedocs.io * `opencadd`，一个用于结构化学信息学的Python库 * giHub仓库：https://github.com/volkamerlab/opencadd * 文档：https://opencadd.readthedocs.io 