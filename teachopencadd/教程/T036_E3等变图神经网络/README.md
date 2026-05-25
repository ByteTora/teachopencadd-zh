# T036 · E(3)等变图神经网络导论

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Joschka Groß, 2022, [建模与仿真教席](https://mosi.uni-saarland.de/), [NextAID项目](https://nextaid.cs.uni-saarland.de/), 萨尔大学


## 本教程的目标

本教程旨在介绍对具有3D构象信息的分子点云表示进行机器学习（即嵌入到欧几里得空间中的分子图，见**教程 033**）。您将学习为什么欧几里得等变性和不变性是接受点云作为输入的神经网络（NN）的重要性质，并学习如何实现和训练此类NN。除了理论讨论外，本笔记本还旨在实际展示普通图神经网络（GNN）在处理点云时的不足。

### _理论_ 部分内容

* 为什么使用3D坐标？
* 将分子表示为点云
* 欧几里得空间中的等变性和不变性及其重要性
* 如何构建$\text{E}(n)$-不变和等变模型
* QM9数据集

### _实践_ 部分内容

* 点云可视化
* 设置并检查QM9数据集
  * 预处理
  * 原子数分布和点云大小
  * 数据划分、回归目标电子空间范围分布
* 模型实现
  * 普通"朴素欧几里得"GNN
  * 演示：普通GNN不是E(3)-不变的
  * EGNN模型
  * 演示：我们的EGNN是E(3)-不变的
* 训练和评估
  * 设置
  * 训练EGNN
  * 训练普通GNN
  * 比较评估

### References

#### Theoretical
* **Quantum chemistry structures and properties of 134k molecules (QM9)**: [<i>Scientific data</i> (2014)](https://www.nature.com/articles/sdata201422/?ref=https://githubhelp.com)
* **MoleculeNet: a benchmark for molecular machine learning**: [<i>Chem. Sci.</i>, 2018, <b>9</b>, 513-530](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc02664a)
* **E(n)-Equivariant Graph Neural Networks**: [<i>International conference on machine learning</i> (2021), <b>139</b>, 99323-9332](https://proceedings.mlr.press/v139/satorras21a.html)
* **SE(3)-transformers: 3D roto-translation equivariant attention networks**: [<i>Advances in Neural Information Processing Systems</i> (2021), <b>33</b>, 1970-1981](https://proceedings.neurips.cc/paper/2020/file/15231a7ce4ba789d13b722cc5c955834-Paper.pdf)
* **TorchMD-NET: Equivariant Transformers for Neural Network based Molecular Potentials**: [<i>arXiv preprint (2022)</i>](https://arxiv.org/abs/2202.02541)
* **DiffDock**: [<i>arXiv preprint</i> (2022)](https://arxiv.org/abs/2210.01776)

#### Practical
* [Pytorch Geometric QM9 version](https://pytorch-geometric.readthedocs.io/en/latest/modules/datasets.html#torch_geometric.datasets.QM9)
