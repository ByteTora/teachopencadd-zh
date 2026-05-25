# T034 · RNN-based molecular property prediction

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。

作者：

- Azat Tagirdzhanov, 2022, [Chair for Clinical Bioinformatics](https://www.ccb.uni-saarland.de/), [NextAID](https://nextaid.cs.uni-saarland.de/) project, Saarland University


## 本教程目标

通过 SMILES 字符串的分子表示为将自然语言处理技术应用于广泛的分子相关任务铺平了道路。在本教程中，我们将深入探讨其中一种技术：循环神经网络（RNN）。首先，我们将介绍不同的 RNN 架构，然后将其应用于 QM9 数据集上的回归任务。


### 理论内容

* Molecules as text
    * Tokenization and one-hot encoding
* Recurrent Neural Networks (RNNs)
    * Vanilla RNN
    * Training an RNN
    * Vanishing gradients
    * Gated Recurrent Unit


### 实践内容

* Dataset
* Model definition
* Training
* Evaluation


### References

#### 系列教程
* __教程 T021__：独热编码
* __教程 T022__：基于配体的筛选：神经网络
* __教程 T033__：分子表示
* __教程 T034__：基于 GNN 的性质预测


#### Theoretical background
* Michael Phi, <i>Illustrated Guide to Recurrent Neural Networks</i>, [towardsdatascience](https://towardsdatascience.com/illustrated-guide-to-recurrent-neural-networks-79e5eb8049c9)
* Michael Phi, <i>Illustrated Guide to LSTM’s and GRU’s: A step by-step explanation</i>, [towardsdatascience](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)
* [Modern Recurrent Neural Networks](https://d2l.ai/chapter_recurrent-modern/index.html), <i>D2L.ai: Interactive Deep Learning Book with Multi-Framework Code, Math, and Discussions</i>
* Denny Britz, <i>Recurrent Neural Networks Tutorial</i>, [dennybritz.com](https://dennybritz.com/posts/wildml/recurrent-neural-networks-tutorial-part-1/)
* Andrej Karpathy, <i>The Unreasonable Effectiveness of Recurrent Neural Networks</i>, [Andrej Karpathy blog](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
