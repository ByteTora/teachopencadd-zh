# T007 ·基础配体的选择：机器学习

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

* Jan Philipp Albrecht，2018年CADD研讨会，Charité/FU柏林 * Jacob Gora，2018年CADD研讨会，Charité/FU柏林 * 塔利亚·B Kimber，2019-2020，[Amplamer Lab] (https：volkamerlab.org） * Andrea Thomamer，2019-2020，[Thomamer实验室]（https：volkamerlab.org)

 __Talktext T007__：该Talktext是[第一篇TeachOpenCADD论文] (https：//jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)中描述的TeachOpenCADD管道的一部分，由talkDoctors T001-T010组成。

 ## 这次音乐节的目的

 由于可用的数据来源更大，机器学习（ML）在药物发布方面发展势头强劲，其是在基础上匹配实体的虚拟选择方面。在这次颁奖典礼上，我们将学习如何使用不同的监督式 ML 算法来预测新化合物对我们感兴趣的指标（EGFR）的活性。

 # 内容*理论*

- 数据准备：子编码 - 机器学习（ML） * 监督学习 - 模型验证和评估 * 验证策略：K 折交叉验证 * 衡量标准

 # 内容* 现实 *

- 加载化合物和活性数据 - 数据准备 * 数据标注 * 分子编码 - 机器学习 * 辅助函数 * 随机森林分类器 * 支持向量分类器 * 神经网络分类器 * 交叉验证

 # 引用

* 《RDKit中的指纹》[slides](https://www.rdkit.org/UGM/2012/Landrum_RDKit_UGM.Fingerprints.Final.pptx.pdf)，G.Landrum，RDKit UGM，2012年 * 扩展连接指纹(ECFP)：罗杰斯、大卫和马修·哈恩。<扩展连接性指纹>[_化学信息和模型期刊_50.5(2010年)：742-754.](https://doi.org/10.1021/ci100050t) * 机器学习(ML)： * 随机林(RF)：Breiman，L.“随机森林”。[_机器学习_**45**，5-32(2001).](https://link.springer.com/article/10.1023%2FA%3A1010933404324) * 支持向量机：Cortes，C.，Vapnik，V.“支持向量网络”。[_机器学习_**20**，273-297(1995).](https://link.springer.com/article/10.1007%2FBF00994018) * 人工神经网络(ANN)：范·格文、马塞尔和桑德·博特。《人工神经网络作为神经信息处理的模型》[_计算神经科学前沿11(2017)：114.](https://doi.org/10.3389/fncom.2017.00114) * 性能： * 敏感性和特异性([Wikipedia](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)) * ROC曲线和AuC([Wikipedia](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve)) * 另见[B.Merget](https://github.com/Team-SKI/Publications/tree/master/Profiling_prediction_of_kinase_inhibitors)的GitHub笔记本电脑][*J.Med.Chem.*，2017，60,474−485](https://pubs.acs.org/doi/10.1021/acs.jmedchem.6b01611) * 本说明书中使用的活动中断$PIC_{50}=6.3$ * 对激酶抑制剂的分析预测：走向虚拟测试[J.Med.化学</i>(2017)，<b>60</b>，474-485](https://doi.org/10.1021/acs.jmedchem.6b01611) * 前面提到的出版物附带的笔记本：[Notebook](https://github.com/Team-SKI/Publications/blob/master/Profiling_prediction_of_kinase_inhibitors/Build_ABL1_model.ipynb) 