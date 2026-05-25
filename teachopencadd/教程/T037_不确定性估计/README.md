# T037 · 不确定性估计

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Michael Backenköhler, 2022, [Volkamer实验室](https://volkamerlab.org), [NextAID项目](https://nextaid.cs.uni-saarland.de/), 萨尔大学


*此教程使用的预测设置（和模型类）改编自__教程 T022__。*


## 本教程的目标

研究人员通常只关注预测质量。然而，在应用预测模型时，研究人员也对特定预测的确定程度感兴趣。估计并提供此类信息是不确定性估计的目标。在本教程中，我们将讨论一些常见方法，并在实践中展示集成方法。

### _理论_ 部分内容

* 为什么模型不能也不应该确定
* 校准
* 方法概述
    * 单确定性方法
    * 集成方法
    * 测试时数据增强

### _实践_ 部分内容

* 数据
* 模型
    * 训练
    * 评估
* 集成 - 多次训练模型
    * 置信区间的覆盖范围
    * 校准
    * 基于排序的评估
* Bagging集成 - 使用不同数据训练模型
    * 基于排序的评估
* 测试时数据增强

### References
* [Gawlikowski, Jakob, et al. "A survey of uncertainty in deep neural networks." _arXiv preprint_ (2021), arXiv:__2107.03342__](https://arxiv.org/abs/2107.03342)
* [Sagi, O. and Rokach, L. "Ensemble learning: A survey". Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 8(4), (2018) p.e1249.](https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/widm.1249?casa_token=1RRjvfS1_k4AAAAA%3AdR5WbRw9n8cp8wuVWx4j1ygfElNKbIJ9wXSmIeBd3C61pD1TEqX0bqswzRhNl8vY1rLDEhl29dseag)
* [Scalia, Gabriele, et al. "Evaluating scalable uncertainty estimation methods for deep learning-based molecular property prediction." _Journal of chemical information and Modeling_ __60.6__ (2020): 2697-2717](https://pubs.acs.org/doi/pdf/10.1021/acs.jcim.9b00975)
* __教程 T022__
