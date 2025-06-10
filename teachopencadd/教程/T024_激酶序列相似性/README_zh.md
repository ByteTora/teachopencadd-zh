# T024 · Kinase相似性：序列

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- 塔利亚·B Kimber，2021年，[Amsteramer实验室，Charité] (https：//volkamerab.org/） - Dominique Sydow，2021年，[Amplamer Lab，Charité]（https：//volkamerab.org/） - Andrea Thomamer，2021年，[Thomamer实验室，Charité]（https：//volkamerab.org/)

 ## 本期脱口秀的目标

在这篇谈话文章中，我们研究了感兴趣的酶的序列相似性。KlIFS API用于检索每种酶口袋序列的85美元残基。 

实施两种相似性测量：

 1.序列同一性，即基于字符差异的相似性。 2.序列相似性，即基于取代矩阵的相似性，因此反映了氨基酸之间的相似性。 _注_：我们重点关注正类固醇蛋白结合位点之间的相似性;与变构结合位点的相似性并未涵盖。

 # * 理论 * 内容

* Kinase数据集 * Kinase相似性描述符：序列 * 身份评分 * 替代分数 * 从相似度矩阵到距离矩阵

 # * 实用 * 中的内容

* 定义感兴趣的类型 * 来自KlIFS的收件箱序列 * 序列相似性 * 身份评分 * 替代分数 * Kinase相似性 * 将相似性可视化为酶矩阵 * 保存酶相似性矩阵 * Kinase距离矩阵 * 保存Kinase距离矩阵

 # 参考文献

* Kinase数据集：[<i>分子</i>（2021），<b>26（3）</b>，629] (https：//www.mdpi.com/1420-3049/26/3/629） * 克利夫斯 * KlIFS URL：https://klifs.net/ * KlIFS数据库：[<i>核酸研究。</i>（2020），<b>49（D1）</b>，D562-D569]（https：//doi.org/10.1093/nar/gkaa895） * 基于序列的酶聚集：Manning _et al._ [<i>科学</i>（2002），<b>298（5600）</b>，1912-1934]（https：//doi.org/10.1126/science.1075762） * 替代矩阵：[<i>PNAS</i>（1992），<b>89（22）<b>，10915-10919]（https：//doi.org/10.1073/pnas.89.22.10915） * 黑云母 * 文档：https://www.biotite-python.org/index.html * [Blosum矩阵]（https：www.biotite-python.org/examples/gallery/sequence/blosum_dendrogram.html?亮点=blosum) * 序列标志：http://www.cbs.dtu.dk/biotools/Seq2Logo/ 