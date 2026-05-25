# T022 · 基于配体的筛选：神经网络

在CADD研讨会2020中开发，Volkamer实验室，夏里特医学院/柏林自由大学 

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Ahmed Atta, CADD研讨会, 夏里特医学院/柏林自由大学
- Sakshi Misra, 实习 (2020/21), [Volkamer实验室](https://volkamerlab.org), 夏里特医学院
- Talia B. Kimber, 2020/21, [Volkamer实验室](https://volkamerlab.org), 夏里特医学院
- Andrea Volkamer, 2021, [Volkamer实验室](https://volkamerlab.org), 夏里特医学院


## 本教程的目标

近年来，机器学习和深度学习在药物研究中的应用在解决药物发现中的多样化问题上展现了有前景的结果。在本教程中，我们将熟悉神经网络的基础知识。我们将学习如何构建一个简单的两层神经网络，并在ChEMBL数据的子集上训练它，以预测化合物对目标EGFR的pIC50值。此外，我们从一个外部未标记数据集中选出三个预测对该激酶活性最高的化合物。

### _理论_ 部分内容

- 生物学背景
    - EGFR激酶
    - 化合物活性度量
    - 分子编码
- 神经网络
    - 什么是神经网络？
    - 激活函数
    - 损失函数
- 训练神经网络
- Keras工作流程
- 神经网络的优点和应用

### _实践_ 部分内容

- 数据准备
- 定义神经网络
- 训练模型
- 测试集评估与预测
    - 散点图
- 外部/未标记数据预测
    - 选择前3个化合物

### References

 - Theoretical background:
     - Articles    
         - Siddharth Sharma, "Activation functions in neural networks". [_International Journal of Engineering Applied Sciences and Technology, 2020_ **Vol. 4, Issue 12,** 310-316 (2020).](https://www.ijeast.com/papers/310-316,Tesma412,IJEAST.pdf)
         - Shun-ichi Amari, "Backpropagation and stochastic gradient descent method", [*ScienceDirect  **Volume 5, Issue 4-5**, 185-196*](https://doi.org/10.1016/0925-2312(93)90006-O)
         - Gisbert Schneider et al., "Artificial neural networks for computer-based molecular design", [*ScienceDirect **Volume 70, Issue 3**, 175-222*](https://doi.org/10.1016/S0079-6107(98)00026-1)
         - Filippo Amato et al., "Artificial neural networks in medical diagnosis", [*ScienceDirect  **Volume 11, Issue 2**, 47-58*](https://doi.org/10.2478/v10136-012-0031-x)         
         
     - Blogposts
          - Imad Dabbura, *Coding Neural Network — Forward Propagation and Backpropagtion*, [medium, accessed March 25th, 2026](https://medium.com/data-science/coding-neural-network-forward-propagation-and-backpropagtion-ccf8cf369f76).
          - Lavanya Shukla, *Designing Your Neural Networks*, [towardsdatascience, accessed Sep 23rd, 2019](https://towardsdatascience.com/designing-your-neural-networks-a5e4617027ed)
          - Arthur Arnx, *First neural network for beginners explained (with code)*, [towardsdatascience, accessed Jan 13th, 2019](https://towardsdatascience.com/first-neural-network-for-beginners-explained-with-code-4cfd37e06eaf) 
          - Varun Divakar, *Understanding Backpropagation*, [QuantInst, accessed Nov 19th, 2018](https://blog.quantinsti.com/backpropagation/) 
               
- Packages:
     - [rdkit](http://rdkit.org/): Greg Landrum, *RDKit Documentation*, [PDF](https://www.rdkit.org/UGM/2012/Landrum_RDKit_UGM.Fingerprints.Final.pptx.pdf), Release on 2019.09.1.
     - [Keras](https://keras.io/): Book chapter: "An Introduction to Deep Learning and Keras" in [*Learn Keras for Deep Neural Networks* (2019), **page(s):1-16**](https://doi.org/10.1007/978-1-4842-4240-7).
     - [Sequential model](https://keras.io/api/models/sequential/) in keras
     - [Model training APIs](https://keras.io/api/models/model_training_apis/#model-training-apis)
