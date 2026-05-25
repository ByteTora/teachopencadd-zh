# T035 · 基于GNN的分子性质预测


**Note**: This 教程 is a part of TeachOpenCADD, a platform that aims to teach domain-specific skills and to provide pipeline templates as starting points for research projects.

作者：

* Paula Linh Kramer, 2022, [Volkamer实验室](https://volkamerlab.org/), [NextAID项目](https://nextaid.cs.uni-saarland.de/), 萨尔大学


## 本教程的目标

在本教程中，我们将首先解释图神经网络（GNN）的基本概念，并介绍两种不同的GNN架构。我们将神经网络应用于`QM9`数据集，这是一个包含小分子的数据集。利用该数据集，我们希望预测分子性质。我们将演示如何使用PyTorch Geometric逐步训练和评估GNN。

### _理论_ 部分内容

* GNN任务
* 消息传递
* 图卷积网络（GCN）
* 图同构网络（GIN）
* 训练GNN
* GNN的应用

### _实践_ 部分内容

* 数据集
* 定义GCN和GIN
* 训练GNN
* 评估模型

### References

* Articles:
    * Atz, Kenneth, Francesca Grisoni, and Gisbert Schneider. *Geometric Deep Learning on Molecular Representations*, [Nature Machine Intelligence 3.12 (2021): 1023-1032](https://arxiv.org/pdf/2107.12375.pdf)
    * Xu, Keyulu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. *How Powerful are Graph Neural Networks?*, [International Conference on Learning Representations (ICLR 2019)](https://arxiv.org/abs/1810.00826v3)
    * Welling, Max, and Thomas N. Kipf. *Semi-supervised classification with graph convolutional networks*, [International Conference on Learning Representations (ICLR 2017)](https://arxiv.org/pdf/1609.02907.pdf)
    * Gilmer, Justin, Samuel S. Schoenholz, Patrick F. Riley, Oriol Vinyals, and George E. Dahl. *Neural Message Passing for Quantum Chemistry*, [International conference on machine learning. PMLR, 2017](https://arxiv.org/pdf/1704.01212.pdf)


* Blog posts:
    * Maxime Labonne, *Graph Convolutional Networks: Introduction to GNNs*, [Maxime Labonne](https://mlabonne.github.io/blog/intrognn/)
    * Maxime Labonne, *GIN: How to Design the Most Powerful Graph Neural Network*, [Maxime Labonne](https://mlabonne.github.io/blog/gin/)
    * Michael Bronstein, *Expressive power of graph neural networks and the Weisfeiler-Lehman test*, [towardsdatascience](https://towardsdatascience.com/expressive-power-of-graph-neural-networks-and-the-weisefeiler-lehman-test-b883db3c7c49)
    * Benjamin Sanchez-Lengeling,  Emily Reif, *A Gentle Introduction to Graph Neural Networks*, [Distill](https://distill.pub/2021/gnn-intro/)


* Tutorials:
    * Pytorch Documentation, *Saving and Loading Models*, [Documentation](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)
    * *Pytorch Geometric Documentation*, [Colab Notebooks and Video Tutorials](https://pytorch-geometric.readthedocs.io/en/latest/notes/colabs.html)
    * *Pytorch Geometric Documentation*, [Introduction by Example](https://pytorch-geometric.readthedocs.io/en/latest/notes/introduction.html#learning-methods-on-graphs)
