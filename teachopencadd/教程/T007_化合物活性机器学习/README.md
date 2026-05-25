# T007 · 基于配体的筛选：机器学习

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

* Jan Philipp Albrecht, CADD seminar 2018, Charité/FU Berlin
* Jacob Gora, CADD seminar 2018, Charité/FU Berlin
* Talia B. Kimber, 2019-2020, [Volkamer lab](https://volkamerlab.org)
* Andrea Volkamer, 2019-2020, [Volkamer lab](https://volkamerlab.org)


__教程 T007__：此教程是 TeachOpenCADD 流程的一部分，详见[第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)，包含教程 T001-T010。


## 本教程的目标

随着数据来源的不断扩大，机器学习（ML）在药物发现中，尤其在基于配体的虚拟筛选中获得了越来越多的关注。在本教程中，我们将学习如何使用不同的监督式 ML 算法来预测新型化合物对感兴趣靶标（EGFR）的活性。

### _理论_ 部分内容

* 数据准备：分子编码
* 机器学习（ML）
    * 监督学习
* 模型验证与评估
    * 验证策略：K 折交叉验证
    * 性能指标

### _实践_ 部分内容

* 加载化合物和活性数据
* 数据准备
    * 数据标注
    * 分子编码
* 机器学习
    * 辅助函数
    * 随机森林分类器
    * 支持向量分类器
    * 神经网络分类器
    * 交叉验证

### References

* "Fingerprints in the RDKit" [slides](https://www.rdkit.org/UGM/2012/Landrum_RDKit_UGM.Fingerprints.Final.pptx.pdf), G. Landrum, RDKit UGM 2012
* Extended-connectivity fingerprints (ECFPs): Rogers, David, and Mathew Hahn. "Extended-connectivity fingerprints." [_Journal of chemical information and modeling_ 50.5 (2010): 742-754.](https://doi.org/10.1021/ci100050t)
* Machine learning (ML):
  * Random forest (RF): Breiman, L. "Random Forests". [_Machine Learning_ **45**, 5–32 (2001).](https://link.springer.com/article/10.1023%2FA%3A1010933404324)
  * Support vector machines (SVM): Cortes, C., Vapnik, V. "Support-vector networks". [_Machine Learning_ **20**, 273–297 (1995).](https://link.springer.com/article/10.1007%2FBF00994018)
  * Artificial neural networks (ANN): Van Gerven, Marcel, and Sander Bohte. "Artificial neural networks as models of neural information processing." [_Frontiers in Computational Neuroscience_ 11 (2017): 114.](https://doi.org/10.3389/fncom.2017.00114)
* Performance: 
  * Sensitivity and specificity ([Wikipedia](https://en.wikipedia.org/wiki/Sensitivity_and_specificity))
  * ROC curve and AUC ([Wikipedia](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve))
* See also [github notebook by B. Merget](https://github.com/Team-SKI/Publications/tree/master/Profiling_prediction_of_kinase_inhibitors) from [*J. Med. Chem.*, 2017, 60, 474−485](https://pubs.acs.org/doi/10.1021/acs.jmedchem.6b01611) 
* Activity cutoff $pIC_{50} = 6.3$ used in this 教程
  * Profiling Prediction of Kinase Inhibitors: Toward the Virtual Assay [<i>J. Med. Chem.</i> (2017), <b>60</b>, 474-485](https://doi.org/10.1021/acs.jmedchem.6b01611)
  * Notebook accompanying the publication mentioned before: [Notebook](https://github.com/Team-SKI/Publications/blob/master/Profiling_prediction_of_kinase_inhibitors/Build_ABL1_model.ipynb)
