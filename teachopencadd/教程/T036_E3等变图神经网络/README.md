# T036 · An introduction to E(3)-invariant graph neural networks

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。

作者：

- Joschka Groß, 2022, [Chair for Modelling and Simulation](https://mosi.uni-saarland.de/), [NextAID](https://nextaid.cs.uni-saarland.de/) project, Saarland University


## 本教程目标

This talktorial is supposed to serve as an introduction to machine learning on point cloud representations of molecules with 3D conformer information, i.e., molecular graphs that are embedded into Euclidean space (see **Talktorial 033**). You will learn why Euclidean equivariance and invariance are important properties of neural networks (NNs) that take point clouds as input and learn how to implement and train such NNs. In addition to discussing them in theory, this notebook also aims to demonstrate the shortcomings of plain graph neural networks (GNNs) when working with point clouds practically.


### 理论内容

* Why 3D coordinates?
* Representing molecules as point clouds
* Equivariance and Invariance in euclidean space and why we care
* How to construct $\text{E}(n)$-invariant and equivariant models
* The QM9 dataset


### 实践内容

* Visualization of point clouds
* Set up and inspect the QM9 dataset
  * Preprocessing
  * Atomic number distribution and point cloud size
  * Data split, distribution of regression target electronic spatial extent
* Model implementation
  * Plain "naive Euclidean" GNN
  * Demo: Plain GNNs are not E(3)-invariant
  * EGNN model
  * Demo: Our EGNN is E(3)-invariant
* Training and evaluation
  * Setup
  * Training the EGNN
  * Training the plain GNN
  * Comparative evaluation


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
