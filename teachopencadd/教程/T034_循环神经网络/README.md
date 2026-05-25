# T034 · 基于RNN的分子性质预测

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Azat Tagirdzhanov, 2022, [临床生物信息学教席](https://www.ccb.uni-saarland.de/), [NextAID项目](https://nextaid.cs.uni-saarland.de/), 萨尔大学


## 本教程的目标

通过SMILES字符串表示分子，为将自然语言处理技术应用于广泛的分子相关任务铺平了道路。在本教程中，我们将深入探讨其中一种技术：循环神经网络（RNN）。首先，我们将描述不同的RNN架构，然后将其应用于使用QM9数据集的回归任务。

### _理论_ 部分内容

* 作为文本的分子
    * 分词与独热编码
* 循环神经网络（RNN）
    * 原始RNN
    * 训练RNN
    * 梯度消失
    * 门控循环单元

### _实践_ 部分内容

* 数据集
* 模型定义
* 训练
* 评估

### References

#### 教程
* __教程 T021__： One-Hot Encoding
* __教程 T022__： Ligand-based screening: neural networks
* __教程 T033__： Molecular Representations
* __教程 T034__： GNN based property prediction


#### Theoretical background
* Michael Phi, <i>Illustrated Guide to Recurrent Neural Networks</i>, [towardsdatascience](https://towardsdatascience.com/illustrated-guide-to-recurrent-neural-networks-79e5eb8049c9)
* Michael Phi, <i>Illustrated Guide to LSTM’s and GRU’s: A step by-step explanation</i>, [towardsdatascience](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)
* [Modern Recurrent Neural Networks](https://d2l.ai/chapter_recurrent-modern/index.html), <i>D2L.ai: Interactive Deep Learning Book with Multi-Framework Code, Math, and Discussions</i>
* Denny Britz, <i>Recurrent Neural Networks Tutorial</i>, [dennybritz.com](https://dennybritz.com/posts/wildml/recurrent-neural-networks-tutorial-part-1/)
* Andrej Karpathy, <i>The Unreasonable Effectiveness of Recurrent Neural Networks</i>, [Andrej Karpathy blog](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
