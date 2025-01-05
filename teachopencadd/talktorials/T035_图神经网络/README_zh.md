# T035 ·基于GNN的分子性质预测

* * 注意 **：这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

* Paula Linh Kramer，2022年，[Amplamer Lab] (https：//volkamerab.org/），[NextAID]（https：//nextaid.cs.uni-saarland.de/)项目，萨尔大学

 ## 本期脱口秀的目标 在本教程中，我们将首先解释图神经网络（GNN）的基本概念，并介绍两种不同的GNN架构。我们将我们的神经网络应用于“QM 9”数据集，该数据集包含小分子。通过这个数据集，我们想要预测分子性质。我们演示了如何使用PyTorch Geographic逐步训练和评估GNN。

 # * 理论 * 内容

* GNN任务 * 消息传递 * 图卷积网络（GCN） * 图同质网络（GIN） * 培训GNN * GNN的应用

 # * 实用 * 中的内容

* 数据集 * 定义GCN和GIN * 培训GNN * 评估模型

 # 参考文献

* 文章： * Atz、Kenneth、Francesca Grisoni和Gisbert Schneider。* 分子表示上的几何深度学习 *，[自然机器智能3.12（2021）：1023-1032] (https：//arxiv.org/pdf/2107.12375.pdf） * Xu、Keyulu、Weihua Hu、Jure Leskovec和Stefanie Jegelka。* 图形神经网络有多强大？*，[国际学习代表会议（ICLR 2019）]（https：//arxiv.org/ins/1810.00826v3） * Welling、Max和Thomas N。基普夫。* 使用图卷积网络的半监督分类 *，[国际学习表示会议（ICLR 2017）]（https：//arxiv.org/pdf/1609.02907.pdf） * 吉尔默、贾斯汀、塞缪尔·S.舍恩霍尔茨，帕特里克·F.莱利、奥里奥尔·维纳尔斯和乔治·E。达尔* 量子化学的神经消息传递 *，[国际机器学习会议。PMLR，2017]（https：//arxiv.org/pdf/1704.01212.pdf)

* 博客帖子： * Maxime Labonne，* 图卷积网络：GNN简介 *，[Maxime Labonne] (https：//mlabonne.github.io/blog/introtn/） * Maxime Labonne，*GIN：如何设计最强大的图形神经网络 *，[Maxime Labonne]（https：//mlabonne.github.io/blog/gin/） * Vortana Say，* 如何在PyTorch中保存和加载模型，具有完整的示例 *，[towardseccience]（https：//towardseccience.com/how-to-save-and-load-a-model-in-pytorch-with-a-full-example-c2920 e617 dee） * Michael Bronstein，* 图神经网络的表现能力和Weisfeiler-Lehman测试 *，[towardsspicience]（https：//towardsspicience.com/expressive-power-of-graph-neural-networks-and-the-weisfeiler-lehman-test-b883 db 3c 7 c49） * Benjamin Sanchez-Lengeling，Emily Reif，* 图形神经网络的温和入门 *，[Distill]（https：//guardian.pub/2021/gnn-intro/)

* 学费： * *Pytorch几何文档 *，[Colab笔记本和视频教程] (https：//pytorch-geographic.readthedocs.io/en/latest/notes/colabs.html） * *Pytorch几何文档 *，[示例介绍]（https：//pytorch-geographic.readthedocs.io/en/latest/notes/introduction.html#learning-meters-on-graph) 