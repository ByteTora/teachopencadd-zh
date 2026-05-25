# T034 ·基于RNN的分子性质预测

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Azat Tagirdzhanov，2022年，[临床生物信息学主席] (https：//www.ccb.uni-saarland.de/），[NextAID]（https：//nextaid.cs.uni-saarland.de/)项目，萨尔大学

 ## 本期脱口秀的目标

SMILES字符串的分子表示为将自然语言处理技术应用于广泛的分子相关任务铺平了道路。在这篇谈话文章中，我们将更深入地探讨其中一种技术：循环神经网络（RNN）。首先，我们将描述不同的RNN架构，然后使用QM 9数据集将它们应用于回归任务。

 # * 理论 * 内容

* 分子作为文本 * 代币化和一热编码 * 循环神经网络（RNN） * 香草RNN * 培训RNN * 梯度消失 * Gated Recurrent Unit

 # * 实用 * 中的内容

* 数据集 * 模型定义 * 培训 * 评价

 # 参考文献

# 谈话 * __Talkorial T021__：一热编码 * __Talkorial T022__：基于配体的筛选：神经网络 * __Talkorial T033__：分子表示 * __Talkorial T034__：基于GNN的属性预测

 # 理论背景 * Michael Phi，<i>回归神经网络插图指南</i>，[towardsociociancience] (https：//towardsocience.com/illusterad-guide-to-recurrent-neural-networks-79e5eb8049c9） * Michael Phi，<i>LSTM和GRU插图指南：分步解释</i>，[towardsscience]（https：//towardsscience.com/illusterad-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44 e9 eb 85 bf 21） * [现代回归神经网络]（https：//d2l.ai/chapter_recurrent-modern/index.html），<i>D2L.ai：具有多框架代码、数学和讨论的交互式深度学习书籍</i> * Denny Britz，<i>循环神经网络收件箱</i>，[dennybritz.com]（https：//dennybritz.com/posts/wildml/recurrent-neural-networks-tutorial-Part-1/） * Andrej Karpathy，<i>回归神经网络的不合理有效性</i>，[Andrej Karpathy博客]（https：//karpathy.github.io/2015/05/21/rnn-effectiveness/) 