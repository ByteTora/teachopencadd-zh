# T028 · 激酶相似性：比较不同视角

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Talia B. Kimber, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Dominique Sydow, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Andrea Volkamer, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)


## 本教程的目标

我们将比较先前笔记本中详细讨论的激酶相似性的不同视角：

* **教程 T024**：激酶口袋序列（KLiFS口袋序列）
* **教程 T025**：激酶口袋结构（基于KLiFS口袋残基的KiSSim指纹）
* **教程 T026**：激酶-配体相互作用谱（基于KLiFS口袋残基的KLiFS IFP）
* **教程 T027**：配体分析数据（使用ChEMBL29生物活性数据）

_注_：我们仅关注正构激酶结合位点之间的相似性；不涉及变构结合位点的相似性（T027例外，因为分析数据不区分结合位点）。

### _理论_ 部分内容

* 激酶数据集
* 激酶相似性描述符（考虑4种不同方法）
* 距离矩阵条件

### _实践_ 部分内容

* 加载激酶相似性和距离矩阵
* 距离矩阵条件
* 可视化示例视角的相似性
  * 将激酶相似性矩阵可视化为热图
  * 将相似性可视化为树状图
* 可视化四个不同视角的相似性
  * 预处理距离矩阵
    * 归一化矩阵
    * 定义激酶顺序
  * 可视化激酶相似性
  * 结果分析

### References

* Kinase dataset: [<i>Molecules</i> (2021), <b>26(3)</b>, 629](https://www.mdpi.com/1420-3049/26/3/629) 
* Clustering and dendrograms with `scipy`: https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
* Distance matrix:
    * https://en.wikipedia.org/wiki/Distance_matrix
    * Gilbert, A. C. and Jain, L. "If it ain't broke, don't fix it: Sparse metric repair." _2017 55th Annual Allerton Conference on Communication, Control, and Computing (Allerton)_. IEEE, 2017. https://arxiv.org/pdf/1710.10655.pdf
