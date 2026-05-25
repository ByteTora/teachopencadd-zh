# T027 · 激酶相似性：配体谱

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Talia B. Kimber, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Dominique Sydow, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Andrea Volkamer, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)


## 本教程的目标

本教程的目标是通过配体分析数据（ChEMBL29）研究激酶相似性。在药物设计的背景下，常做如下假设：如果一个化合物在两个不同的激酶上都被测试为活性，那么这两个激酶可能具有一定程度的相似性。在本教程中，我们将使用这个假设。同时还涉及激酶混杂性的概念。

### _理论_ 部分内容

* 激酶数据集
* 生物活性数据
* 激酶相似性描述符：配体谱
    * 激酶相似性
    * 激酶混杂性
* 从相似性矩阵到距离矩阵

### _实践_ 部分内容

* 定义感兴趣的激酶
* 检索数据
* 预处理数据
    * 命中或非命中
* 激酶混杂性
* 激酶相似性
    * 将相似性可视化为激酶矩阵
    * 保存激酶相似性矩阵
* 激酶距离矩阵
    * 保存激酶距离矩阵

### References

* Kinase dataset: [<i>Molecules</i> (2021), <b>26(3)</b>, 629](https://www.mdpi.com/1420-3049/26/3/629) 
* ChEMBL database
  * Website: https://www.ebi.ac.uk/chembl/
  * Paper: [<i>Nucleic Acid Research</i> (2017), <b>45(D1)</b>, D945-D954](https://doi.org/10.1093/nar/gkw1074) 
* KinMap
  * Website: http://www.kinhub.org/kinmap/
  * Paper: [<i>BMC Bioinformatics</i> (2017), <b>18(1)</b>, 16](https://doi.org/10.1186/s12859-016-1433-7) 
