# T021 ·一热编码

在Charité/FU Berlin Charité Alamamer Lab 2020年CADD研讨会上开发 

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Sakshi Misra，2020年CADD研讨会，Charité/FU柏林 - 塔利亚·B Kimber，2020，[Amplamer Lab] (https：volkamerlab.org），Charité - 陈永辉，2020，[Amsteramer Lab]（https：volkamerlab.org），Charité - Andrea Thomamer，2020，[Thomamer实验室]（https：volkamerlab.org)，Charité

 ## 本期脱口秀的目标

Talktorial的目的是对ChMBE数据集的子集执行SMILES结构的一次热编码，以更深入地理解一次热编码概念以及为什么它作为各种机器学习算法中的预处理步骤有用。

 # * 理论 * 内容

- 分子数据和表示 - ChMBE数据库 - 微笑结构和规则 - 什么是分类数据？ - 分类数据有什么问题？ - 如何将分类数据转换为数字数据？ - 一热编码（OHE）概念 - 为什么使用一次性编码？ - 一热编码示例 - 一热编码的优点和缺点 - 类似：收件箱或标签编码 - 什么是 * 填充 *？ - 补充阅读

 # * 实用 * 中的内容

- 进口必要的包裹 - 读取输入数据 - 处理数据 - 两位数替换 - 计算最长（和最短）微笑 - Python一次性编码实现 - 一热编码（填充=True） - 可视化 - 最短的微笑 - 最长的微笑 - 补充材料 - Scikit学习实现 - Keras实现

 ## 参考文献

- -理论背景： - Chembl数据库：“Chembl生物活性数据库：最新情况”(《核酸研究》(2014年)，42.D1.，D1083-D1090](https://doi.org/10.1093/nar/gkt1031)) - Allen Chieng Hoon Choong，Nung Kion Lee，“*有序与一热编码方法的卷积神经网络DNA序列建模的评估*”，[BioRxiv，2017年10月25日](https://doi.org/10.1101/186965). - -Patricio Cerda，Gael Varoquaux，《*编码高基数字符串分类变量*》，[arxiv：1907，5月18日2020](https://arxiv.org/pdf/1907.01860v5.pdf). - 博客帖子：Jason Brownlee，*How to One HotEncode Sequence Data in Python.[机器学习掌握，11月9日访问，2020](https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/). - 博文：Krishna Kumar Mahto，*One-热编码，多重共线性和虚拟变量陷阱*，数据科学，可从2019年7月8日访问的[one-hot-encoding-multicollinearity](https://towardsdatascience.com/one-hot-encoding-multicollinearity-and-the-dummy-variable-trap-b5840be3c41a/)，获得。 - 博客帖子：克里斯，*什么是神经网络中的填充？*，来自MachineCurve，[Padding](https://github.com/christianversloot/machine-learning-articles/blob/main/what-is-padding-in-a-neural-network.md) 

- 包和函数： - [**RDKit**](https://www.rdkit.org/docs/GettingStartedInPython.html)：格雷格·兰德勒姆，*RDKIT文档*，[PDF](https://buildmedia.readthedocs.org/media/pdf/rdkit/latest/rdkit.pdf)，于2019.09.1发布。 - -[**Scikit-learn**](https://scikit-learn.org/stable/)： - [本刊-学习：Python](https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html)，Pedregosa中的机器学习*等人*，JMLR12，第2825-2830页，2011年。 - -郝建刚等人[*教育与行为统计杂志*卷：44卷：3**(2019)页(S)：348-361](https://doi.org/10.3102/1076998619832248)] - [**凯拉斯**](https://keras.io/)：书章节：《深度学习和凯拉斯导论》，见[*学习深度神经网络的凯拉斯*》(2019年)，**page(s)：1-16**](https://doi.org/10.1007/978-1-4842-4240-7). - [**Matplotlib**](https://matplotlib.org/) - `微笑编码者‘功能：iwatobipen的博客文章，*对微笑字符串进行编码和解码*，[wordpress，11月9日访问，2020](https://iwatobipen.wordpress.com/2017/01/22/encode-and-decode-smiles-strings/) 