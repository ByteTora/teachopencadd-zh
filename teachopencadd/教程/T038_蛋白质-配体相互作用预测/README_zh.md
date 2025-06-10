# T038 ·蛋白质配体相互作用预测

**注意:** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Roman Joeres，2022年，[UdS和HIPS药物生物信息学主席] (https：//www.helmholtz-hips.de/de/forschung/team/team/spokstoffbioinformatik/）[NextAID]（https：//nextaid.cs.uni-saarland.de/)项目，萨尔大学

 ## 本期脱口秀的目标

这篇谈话文章的目标是向读者介绍使用图神经网络（GNN）预测蛋白质-配体相互作用的领域。GNN对于将蛋白质和化学分子（配体）等结构数据表示为深度学习模型特别有用。在本期谈话中，我们将展示如何训练深度学习模型来预测蛋白质和配体之间的相互作用。

 # *理论* 内容

* 蛋白质-配体相互作用预测的相关性
* 工作流 
* 生物背景-蛋白质作为图表 
* 技术背景 
* 图同质网络 
* 二元交叉熵损失

 # *实用* 中的内容

* 计算图形表示 
* 图形配体 
* 蛋白质到图表 
* 数据存储器 
* 数据点 
* 数据集 
* 数据模块 
* 网络 
* GNN编码器 
* 完整模型 
* 训练例程

 # 参考文献

* 理论背景 * 图形神经网络： Kipf，Welling：“使用图卷积网络的半监督分类”，[<i>arXiv</i>（2017）] (https：//arxiv.org/ab/1609.02907） 布朗斯坦等人：“几何深度学习：超越欧几里得数据”，[<i>IEEE Signal Process Magazine</i>（2017），<b>4</b>，18-42]（https：//doi.org/10.1109/MSP.2017.2693418） * 基于GNN的蛋白质-配体相互作用预测： Öztürk等人：“DeepDART：深度药物-靶点结合亲和力预测”，[<i>生物信息学</i>（2018），<b>34</b>，i821-i829]（https：//doi.org/10.1093/bioinformatics/bty593） 阮等人等人：“GraphDART：利用图神经网络预测药物-靶点结合亲和力”，[<i>生物信息学</i>（2021），<b>37</b>，1140-1147]（https：//doi.org/10.1093/bioinformatics/bta 921） * 图同质网络： 徐等人：“图神经网络有多强大？”，[<i>arXiv</i>（2018）]（https：//arxiv.org/ab/1810.00826)

* 实践背景 * [PyTorch] (https：//pytorch.org/） * [PyTorch Geographic]（https：//pytorch-geographic.readthedocs.io/en/latest/） * [RDKit]（http：//rdkit.org/）：Greg Landrum，*RDKit Document *，[PDF]（https：//www.rdkit.org/UGM/2012/Landrum_RDKit_UGM.Fingerprints.Final.pptx.pdf)，发布日期：2019.09.1。 