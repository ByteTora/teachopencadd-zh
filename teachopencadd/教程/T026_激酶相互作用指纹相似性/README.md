# T026 · 激酶相似性：相互作用指纹

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Dominique Sydow, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Talia B. Kimber, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Andrea Volkamer, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)


## 本教程的目标

我们将基于现有复合物结构中检测到的蛋白质-配体相互作用，评估一组激酶之间的相似性。本练习将使用[KLiFS](https://klifs.net/)相互作用指纹（IFP），该指纹描述了结构解析的激酶-配体复合物中的相互作用。

_注_：我们关注正构激酶结合位点之间的相似性；不涉及变构结合位点的相似性。

### _理论_ 部分内容

* 激酶数据集
* 激酶相似性描述符：KLiFS相互作用指纹
* 使用`opencadd.databases.klifs`获取KLiFS数据

### _实践_ 部分内容

* 定义感兴趣的激酶
* 检索和预处理数据
    * 设置远程KLiFS会话
    * 获取描述这些激酶的所有结构
    * 过滤结构
    * 获取结构的IFP（如有）
    * 合并结构和IFP数据
* 显示激酶覆盖范围
* 比较结构
    * 将IFP准备为`numpy`数组
    * 计算成对Jaccard距离
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
  * KLIFS binding site definition and interaction fingerprint calculation: [<i>J. Med. Chem.</i> (2014), <b>57(2)</b>, 249-277](https://doi.org/10.1021/jm400378w)
* Interaction fingerprint (IFP): [<i>J. Chem. Inf. Model.</i> (2007), <b>71(1)</b>, 195-207](https://doi.org/10.1021/ci600342e)
* `opencadd`, a Python library for structural cheminformatics
  * GitHub repository: https://github.com/volkamerlab/opencadd
  * Documentation: https://opencadd.readthedocs.io
