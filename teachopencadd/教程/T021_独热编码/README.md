# T021 · 独热编码

在CADD研讨会2020中开发，Volkamer实验室，夏里特医学院/柏林自由大学 

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Sakshi Misra, CADD研讨会, 夏里特医学院/柏林自由大学
- Talia B. Kimber, 2020, [Volkamer实验室](https://volkamerlab.org), 夏里特医学院
- Yonghui Chen, 2020, [Volkamer实验室](https://volkamerlab.org), 夏里特医学院
- Andrea Volkamer, 2020, [Volkamer实验室](https://volkamerlab.org), 夏里特医学院


## 本教程的目标

本教程的目标是对ChEMBL数据集的子集进行SMILES结构的独热编码，以深入了解独热编码概念及其作为各种机器学习算法中预处理步骤的实用性。

### _理论_ 部分内容

- 分子数据和表示
    - ChEMBL数据库
    - SMILES结构和规则
- 什么是分类数据？
     - 分类数据有什么问题？
     - 如何将分类数据转换为数值数据？
- 独热编码（OHE）概念
     - 为什么要使用独热编码？
     - 独热编码示例
     - 独热编码的优缺点
- 类似：整数或标签编码
- 什么是*padding*（填充）？
- 进一步阅读

### _实践_ 部分内容

- 导入必要包
- 读取输入数据
- 处理数据
     - 双位替换
     - 计算最长（和最短）SMILES
- Python独热编码实现
     - 独热编码（padding=True）
     - 可视化
          - 最短SMILES
          - 最长SMILES
- 补充材料
   - Scikit learn实现
   - Keras实现

### References
- Theoretical background:
     - ChEMBL database: "The ChEMBL bioactivity database: an update." ([<i>Nucleic acids research<i> (2014), <b>42.D1</b>, D1083-D1090](https://doi.org/10.1093/nar/gkt1031))
     - Allen Chieng Hoon Choong, Nung Kion Lee, "*Evaluation of Convolutionary Neural Networks Modeling of DNA Sequences using Ordinal versus one-hot Encoding Method*", [bioRxiv, October 25, 2017](https://doi.org/10.1101/186965).
     - Patricio Cerda, Gael Varoquaux, "*Encoding high-cardinality string categorical variables*", [arXiv:1907, 18 May 2020](https://arxiv.org/pdf/1907.01860v5.pdf).
     - Blogpost: Jason Brownlee, *How to One Hot Encode Sequence Data in Python*, [Machine Learning Mastery, accessed November 9th, 2020](https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/).
     - Blogpost: Krishna Kumar Mahto, *One-Hot-Encoding, Multicollinearity and the Dummy Variable Trap*, medium, Available at [one-hot-encoding-multicollinearity](https://medium.com/data-science/one-hot-encoding-multicollinearity-and-the-dummy-variable-trap-b5840be3c41a), accessed March 25th, 2026.
     - Blogpost: Chris, *What is padding in a neural network?*, archieved from MachineCurve, [Padding](https://github.com/christianversloot/machine-learning-articles/blob/main/what-is-padding-in-a-neural-network.md)
     

- Packages and functions:
     - [**RDKit**](https://www.rdkit.org/docs/GettingStartedInPython.html): Greg Landrum,  *RDKit Documentation*, [PDF](https://buildmedia.readthedocs.org/media/pdf/rdkit/latest/rdkit.pdf), Release on 2019.09.1.
     - [**Scikit-learn**](https://scikit-learn.org/stable/): 
        - [Scikit-learn: Machine Learning in Python](https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html), Pedregosa *et al.*, JMLR 12, pp. 2825-2830, 2011.
        - Jiangang Hao, et al. "A Review of Scikit-learn Package in Python Programming Language." [*Journal of Education and Behavioral Statistics* **Volume: 44 issue: 3** (2019), page(s): 348-361](https://doi.org/10.3102/1076998619832248)
     - [**Keras**](https://keras.io/): Book chapter: "An Introduction to Deep Learning and Keras" in [*Learn Keras for Deep Neural Networks* (2019), **page(s):1-16**](https://doi.org/10.1007/978-1-4842-4240-7).
     - [**Matplotlib**](https://matplotlib.org/)
     - `smiles encoder` function: Blogpost by iwatobipen, *encode and decode SMILES strings* , [Wordpress, accessed November 9th, 2020](https://iwatobipen.wordpress.com/2017/01/22/encode-and-decode-smiles-strings/)
