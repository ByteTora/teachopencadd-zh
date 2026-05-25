# T026 · Kinase相似性：相互作用指纹

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Dominique Sydow，2021年，[Amplamer Lab，Charité] (https：//volkamerab.org/） - 塔利亚·B Kimber，2021年，[Amsteramer实验室，Charité]（https：//volkamerab.org/） - Andrea Thomamer，2021年，[Thomamer实验室，Charité]（https：//volkamerab.org/)

 ## 本期脱口秀的目标

我们将根据现有复杂结构中检测到的蛋白质-配体相互作用来评估一组kinase之间的相似性。[KLIFS] (https：//klifs.net/）相互作用指纹（IFP)描述了结构分辨的kinase-配体复合物中观察到的相互作用，将用于本练习。 

_注_：我们重点关注正类固醇蛋白结合位点之间的相似性;与变构结合位点的相似性并未涵盖。

 # * 理论 * 内容

* Kinase数据集 * Kinase相似性描述符：KlIFS相互作用指纹 * 使用' opencadd.databases.klifs '获取KlIFS数据

 # * 实用 * 中的内容

* 定义感兴趣的类型 * 卸载和预处理数据 * 设置远程KlIFS会话 * 获取描述这些kinase的所有结构 * 滤波器结构 * 获取结构的IFP（如果可用） * 合并结构和IFP数据 * 显示Kinase覆盖范围 * 比较结构 * 将IFP准备为“numpy”数组 * 计算成对贾卡德距离 * 将结构映射到酶距离矩阵 * 保存Kinase距离矩阵

 # 参考文献

* Kinase数据集：[<i>分子</i>（2021），<b>26（3）</b>，629] (https：//www.mdpi.com/1420-3049/26/3/629） * 蛋白质数据库 * DBC URL：http://www.rcsb.org/ * DBC数据库：[<i>Acta Cryst. </i>（2002），<b>D58</b>，899-907]（https：//doi.org/10.1107/S0907444902003451）和[<i>结构</i>（2012），<b>20（3）</b>，391-396]（https：//doi.org/10.1016/j.str.2012.01.010） * 克利夫斯 * KlIFS URL：https://klifs.net/ * KlIFS数据库：[<i>核酸研究。</i>（2020），<b>49（D1）</b>，D562-D569]（https：//doi.org/10.1093/nar/gkaa895） * KlIFS结合位点定义和相互作用指纹计算：[<i>J. Med. Chem. </i>（2014），<b>57（2）</b>，249-277]（https：//doi.org/10.1021/jm400378w） * 相互作用指纹（IFP）：[<i>J. Chem. Inf.模型。</i>（2007），<b>71（1）</b>，195-207]（https：//doi.org/10.1021/ci600342e) * “opencadd”，一个用于结构化学信息学的Python库 * GitHub存储库：https://github.com/volkamerlab/opencadd * 文档：https://opencadd.readthedocs.io 