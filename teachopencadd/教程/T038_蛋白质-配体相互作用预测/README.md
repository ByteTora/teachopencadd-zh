# T038 · 蛋白质-配体相互作用预测

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Roman Joeres, 2022, [药物生物信息学教席, 萨尔大学/亥姆霍兹药物研究所](https://www.helmholtz-hips.de/de/forschung/teams/team/wirkstoffbioinformatik/), [NextAID项目](https://nextaid.cs.uni-saarland.de/), 萨尔大学


## 本教程的目标

本教程的目标是向读者介绍使用图神经网络（GNN）进行蛋白质-配体相互作用预测的领域。GNN对于将蛋白质和化学分子（配体）等结构数据表示给深度学习模型特别有用。在本教程中，我们将展示如何训练深度学习模型来预测蛋白质和配体之间的相互作用。

### _理论_ 部分内容

* 蛋白质-配体相互作用预测的相关性
* 工作流程
* 生物学背景 - 蛋白质作为图
* 技术背景
  * 图同构网络
  * 二元交叉熵损失

### _实践_ 部分内容

* 计算图表示
  * 配体到图
  * 蛋白质到图
* 数据存储
  * 数据点
  * 数据集
  * 数据模块
* 网络
  * GNN编码器
  * 完整模型
* 训练流程

### References

* Theoretical background
    * Graph Neural Networks:
      Kipf, Welling: "Semi-Supervised Classification with Graph Convolutional Networks", [<i>arXiv</i> (2017)](https://arxiv.org/abs/1609.02907)
      Bronstein, et al.: "Geometric deep learning: going beyond Euclidean data", [<i>IEEE Signal Processing Magazine</i> (2017), <b>4</b>, 18-42](https://doi.org/10.1109/MSP.2017.2693418)
    * GNN-based Protein-Ligand Interaction Prediction:
      Öztürk, et al.: "DeepDTA: Deep drug-target binding affinity prediction", [<i>Bioinformatics</i> (2018), <b>34</b>, i821-i829](https://doi.org/10.1093/bioinformatics/bty593)
      Nguyen, et. al.: "GraphDTA: Predicting drug-target binding affinity with graph neural networks", [<i>Bioinformatics</i> (2021), <b>37</b>, 1140-1147](https://doi.org/10.1093/bioinformatics/btaa921)
    * Graph Isomorphism Network:
      Xu, et al.: "How powerful are graph neural networks?", [<i>arXiv</i> (2018)](https://arxiv.org/abs/1810.00826)

* Practical background
    * [PyTorch](https://pytorch.org/)
    * [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/)
    * [RDKit](http://rdkit.org/): Greg Landrum, *RDKit Documentation*, [PDF](https://www.rdkit.org/UGM/2012/Landrum_RDKit_UGM.Fingerprints.Final.pptx.pdf), Release on 2019.09.1.
