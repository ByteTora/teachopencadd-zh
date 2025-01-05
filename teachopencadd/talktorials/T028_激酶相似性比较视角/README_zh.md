# T028 · Kinase相似性：比较不同的角度

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- 塔利亚·B Kimber，2021年，[Amsteramer实验室，Charité] (https：//volkamerab.org/） - Dominique Sydow，2021年，[Amplamer Lab，Charité]（https：//volkamerab.org/） - Andrea Thomamer，2021年，[Thomamer实验室，Charité]（https：//volkamerab.org/)

 ## 本期脱口秀的目标

我们将比较关于同工酶相似性的不同观点，这些观点在之前的笔记本中已详细讨论：

* ** Talkorial T024**：Kinase口袋序列（KlIFS口袋序列） * ** Talkorial T025**：Kinase口袋结构（基于KlIFS口袋残基的KiSSim指纹） * ** Talkorial T026**：Kinase-配体相互作用曲线（基于KlIFS口袋残基的KlIFS IFP） * ** Talkorial T027**：配体分析数据（使用ChMBE 29生物活性数据）

_注意_：我们仅关注正类固醇蛋白结合位点之间的相似性;与变构结合位点的相似性并未涵盖（T027是一个例外，因为分析数据没有区分结合位点）。

 # * 理论 * 内容

* Kinase数据集 * Kinase相似性描述符（考虑4种不同的方法） * 距离矩阵条件

 # * 实用 * 中的内容

* 加载酶相似性和距离矩阵 * 距离矩阵条件 * 可视化示例视角的相似性 * 将酶相似性矩阵可视化为热图 * 将相似性可视化为树图 * 从四个不同的角度想象相似之处 * 预处理距离矩阵 * 规范化矩阵 * 定义Kinase顺序 * 想象一下酶的相似性 * 结果分析

 # 参考文献

* Kinase数据集：[<i>分子</i>（2021），<b>26（3）</b>，629] (https：//www.mdpi.com/1420-3049/26/3/629） * 使用“scipy”进行集群和树图：https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html * 距离矩阵： * https://en.wikipedia.org/wiki/Distance_matrix * 吉尔伯特，A。C.和Jain，L.“如果它没有损坏，就不要修复它：稀疏指标修复。“_2017第55届艾尔顿通信、控制和计算年度会议（艾尔顿)_。IEEE，2017年。https://arxiv.org/pdf/1710.10655.pdf 