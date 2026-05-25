# T013 ·从PubChem获取数据

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Jaime Rodríguez-Guerra，2019-2020，[Amsteramer Lab，Charité] (https：//volkamerab.org/） - Dominique Sydow，2019-2020，[Amsteramer Lab，Charité]（https：//volkamerab.org/） - 陈永辉，2019-2020，[Amplamer Lab，Charité]（https：//volkamerab.org/)

 ## 本期脱口秀的目标

在本笔记本中，您将了解如何使用API网络服务在[PubChem] (https：//pubchem.ncbi.nlm.nih.gov/)中搜索与输入SMILES类似的化合物。

 # * 理论 * 内容

- PubChem - 通过程序访问PubChem

 # * 实用 * 中的内容

* PubChem API的简单示例 * 如何获取化合物的PubChem CID * 基于PubChem CID验证分子性质 * 用PubChem描绘化合物 * 查询PubChem以获取类似化合物 * 确定查询复合 * 创建任务并获取作业密钥 * 作业完成后下载结果 * 获取所得分子的典型微笑 * 显示结果 

 ## 参考文献

* 文学： * PubChem 2019更新：[_核酸研究._（2019），__47__，D1102-1109] (https：//academic.oup.com/nar/article/47/D1/D1102/5146201） * PubChem 2021年：[_核酸研究._（2021），__49__，D1388-D1395]（https：//academic.oup.com/nar/article/49/D1/D1388/5957164） * 文件： * [PubChem来源信息]（https：//pubchem.ncbi.nlm.nih.gov/sources） * [PUG REST]（https：//pubchemdocs.ncbi.nlm.nih.gov/pug-rest） * [编程访问]（https：//pubchemdocs.ncbi.nlm.nih.gov/programmatic-Access） * [PubChem -维基百科]（https：//en.wikipedia.org/wiki/PubChem) 