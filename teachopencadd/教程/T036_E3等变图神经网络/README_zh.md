# T036 ·E（3）-不变图神经网络简介

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Joschka Grozen，2022年，[建模和模拟主席] (https：//mosi.uni-saarland.de/），[NextAID]（https：//nextaid.cs.uni-saarland.de/)项目，萨尔大学

 ## 本期脱口秀的目标

这篇谈话文章应该作为对具有3D形态信息的分子点云表示的机器学习的入门，即嵌入欧几里得空间的分子图（请参阅 ** Talkorial 033**）。您将了解为什么欧几里得等方差和不变性是以点云作为输入的神经网络（NN）的重要属性，并了解如何实现和训练此类NN。除了从理论上讨论它们之外，本笔记本还旨在演示普通图神经网络（GNN）在实际处理点云时的缺点。

 # * 理论 * 内容

* 为什么是3D坐标？ * 将分子表示为点云 * 欧几里得空间中的等变性和不变性以及我们关心的原因 * 如何构建$\text{E}（n）$-不变和等变模型 * QM 9数据集

 # * 实用 * 中的内容

* 点云可视化 * 设置并检查QM 9数据集 * 预处理 * 原子数分布和点云大小 * 数据拆分、回归目标电子空间范围分布 * 模型实现 * 简单的“天真的欧几里得”GNN * 演示：纯GNN不是E（3）不变的 * EGNN模型 * 演示：我们的EGNN是E（3）不变的 * 训练和评价 * 设置 * 培训EGNN * 训练平原GNN * 比较评价

 # 参考文献

# 理论 * 134K分子的量子化学结构和性质(QM9)**：[科学数据</i>(2014)](https://www.nature.com/articles/sdata201422/?ref=https://githubhelp.com) * MoleculeNet：分子机器学习的基准**：[<i>化学。科学</i>，2018年，<b>9</b>，513-530](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc02664a) * E(N)-等变图神经网络**：[<i>机器学习国际会议</i>(2021)，<b>139</b>，99323-9332](https://proceedings.mlr.press/v139/satorras21a.html) * SE(3)-转换器：3D旋转-平移等变注意网络**：[神经信息处理系统进展</i>(2021)，<b>33</b>，1970-1981](https://proceedings.neurips.cc/paper/2020/file/15231a7ce4ba789d13b722cc5c955834-Paper.pdf) * TorchMD-Net：基于神经网络的分子势等变转换器**：[Arxiv Preprint(2022年)</i>](https://arxiv.org/abs/2202.02541) * DiffDock**：[<i>arxiv预印</i>(2022年)](https://arxiv.org/abs/2210.01776)

# 实用 * [Pytorch Geographic QM 9版本] (https：//pytorch-geographic.readthedocs.io/en/latest/modules/guardiets. html #torch_geographic. guardiets. QM 9) 