# T024 · 激酶相似性：序列

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Talia B. Kimber, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Dominique Sydow, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Andrea Volkamer, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)


## 本教程的目标

在本教程中，我们研究感兴趣激酶的序列相似性。使用KLiFS API检索每个激酶的口袋序列的$85$个残基。

实现了两种相似性度量：

   1. 序列一致性，即基于字符差异的相似性。
   2. 序列相似性，即基于替换矩阵的相似性，反映氨基酸之间的相似性。

_注_：我们关注正构激酶结合位点之间的相似性；不涉及变构结合位点的相似性。

### _理论_ 部分内容

* 激酶数据集
* 激酶相似性描述符：序列
    * 一致性得分
    * 替换得分
* 从相似性矩阵到距离矩阵

### _实践_ 部分内容

* 定义感兴趣的激酶
* 从KLiFS检索序列
* 序列相似性
    * 一致性得分
    * 替换得分
* 激酶相似性
  * 将相似性可视化为激酶矩阵
  * 保存激酶相似性矩阵
* 激酶距离矩阵
  * 保存激酶距离矩阵

### References

* Kinase dataset: [<i>Molecules</i> (2021), <b>26(3)</b>, 629](https://www.mdpi.com/1420-3049/26/3/629) 
* KLIFS
  * KLIFS URL: https://klifs.net/
  * KLIFS database: [<i>Nucleic Acid Res.</i> (2020), <b>49(D1)</b>, D562-D569](https://doi.org/10.1093/nar/gkaa895)
* Sequence-based kinase clustering: Manning _et al._ [<i>Science</i> (2002), <b>298(5600)</b>, 1912-1934](https://doi.org/10.1126/science.1075762)
* Substitution matrix: [<i>PNAS</i> (1992), <b>89(22)<b>, 10915-10919](https://doi.org/10.1073/pnas.89.22.10915)
* Biotite
    * Documentation: https://www.biotite-python.org/index.html
    * [Substitution matrix](https://www.biotite-python.org/latest/apidoc/biotite.sequence.align.SubstitutionMatrix.html)
* Sequence logo: http://www.cbs.dtu.dk/biotools/Seq2Logo/    
