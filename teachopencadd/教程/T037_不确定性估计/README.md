# T037 ·不确定性估计

**注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Michael Backenköhler，2022年，[Amplamer实验室] (https：volkamerlab.org），[NextAID]（https：//nextaid.cs.uni-saarland.de/)项目，萨尔大学

* 此Talkorial中使用的预测设置（和模型类）改编自__Talkorial T022__。*

## 本期脱口秀的目标

研究人员通常只关注预测质量。然而，在应用预测模型时，研究人员还对他们对特定预测的确定性感兴趣。估计和提供此类信息是不确定性估计的目标。在这篇谈话中，我们讨论了一些常见的方法并展示了实践中的集成方法。

# *理论* 内容

* 为什么模特不能也不应该确定
* 校准 
* 方法概述 
* 单一确定性方法 
* 集成方法 
* 测试时间数据增强

 # *实用* 中的内容 
 * 数据 
 * 模型 
 * 培训 
 * 评价 
 * 合奏-多次训练模特 
 * 置信区间的覆盖范围 
 * 校准 
 * 基于排名的评估 
 * 装袋集成-用不同数据训练模型 
 * 基于排名的评估 
 * 测试时间数据增强

 # 参考文献 * [Gawlikowski、Jakob等人。“深度神经网络中不确定性的调查。“_arXiv预印本_（2021），arXiv：__2107.03342__] (https：//arxiv.org/ab/2107.03342） * [俄勒冈州萨吉和罗卡奇，L.“享受学习：一项调查”。Wiley跨学科评论：数据挖掘和知识发现，8（4），（2018）p.e1249。]（https：wires.onlinelibrary.wiley.com/doi/abs/10.1002/widm.1249? casa_token= 1RR jvfS1_k4AAAAA%3AdR5WbRw9n8cp8wuVWx 4j1ygfElNKbIJ9wXSmIeBd3C61pD1TEqX 0bqswzRhNl8vY1rLDEhl29dseag） * [Scalia、Gabriele等人。“评估基于深度学习的分子性质预测的可扩展不确定性估计方法。“_化学信息与建模杂志_60.6__（2020）：2697-2717]（https：//pubs.acs.org/doi/pdf/10.1021/acs.jcim.9b00975) * __谈话T022__ 