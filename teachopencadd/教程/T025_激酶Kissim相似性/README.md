# T025 · 激酶相似性：激酶口袋（KiSSim指纹）

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Dominique Sydow, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Talia B. Kimber, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Andrea Volkamer, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)


## 本教程的目标

我们将使用[KiSSim](https://kissim.readthedocs.io/en/latest/)指纹从结构角度评估一组激酶之间的相似性。该指纹描述了结构解析的激酶中的物理化学和空间特性。

_注_：我们关注正构激酶结合位点之间的相似性；不涉及变构结合位点的相似性。

### _理论_ 部分内容

* 激酶数据集
* 激酶相似性描述符：激酶口袋（KiSSim指纹）
* 使用`opencadd.databases.klifs`获取KLiFS数据

### _实践_ 部分内容

* 定义感兴趣的激酶
* 检索和预处理数据
    * 设置远程KLiFS会话
    * 获取描述这些激酶的所有结构
    * 过滤结构
* 显示激酶覆盖范围
* 计算KiSSim指纹
* 比较结构
* 将结构映射到激酶距离矩阵
* 保存激酶距离矩阵

### References

* Kinase dataset: [<i>Molecules</i> (2021), <b>26(3)</b>, 629](https://www.mdpi.com/1420-3049/26/3/629) 
* Protein Data Bank
  * PDB URL: http://www.rcsb.org/
  * PDB database: [<i>Acta Cryst.</i> (2002), <b>D58</b>, 899-907](https://doi.org/10.1107/S0907444902003451) and [<i>Structure</i> (2012), <b>20(3)</b>, 391-396](https://doi.org/10.1016/j.str.2012.01.010)
* KLIFS
  * KLIFS URL: https://klifs.net/
  * KLIFS database: [<i>Nucleic Acid Res.</i> (2020), <b>49(D1)</b>, D562-D569](https://doi.org/10.1093/nar/gkaa895)
  * KLIFS binding site definition: [<i>J. Med. Chem.</i> (2014), <b>57(2)</b>, 249-277](https://doi.org/10.1021/jm400378w)
 * Binding site comparison reviews: 
   * [<i>Curr. Comput. Aided Drug Des. </i> (2008), <b>4</b>, 209-20](https://www.eurekaselect.com/67606/article/how-measure-similarity-between-protein-ligand-binding-sites)
    * [<i>J. Med. Chem. </i> (2016), <b>9</b>, 4121-51](https://pubs.acs.org/doi/10.1021/acs.jmedchem.6b00078)
* KiSSim: Kinase Structural Similarity
  * GitHub repository: https://github.com/volkamerlab/kissim
  * Documentation: https://kissim.readthedocs.io
* `opencadd`, a Python library for structural cheminformatics
  * GitHub repository: https://github.com/volkamerlab/opencadd
  * Documentation: https://opencadd.readthedocs.io
