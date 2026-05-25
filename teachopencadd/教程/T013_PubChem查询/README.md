# T013 · 从 PubChem 获取数据

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Jaime Rodríguez-Guerra, 2019-2020, [Volkamer lab, Charité](https://volkamerlab.org/)
- Dominique Sydow, 2019-2020, [Volkamer lab, Charité](https://volkamerlab.org/)
- Yonghui Chen, 2019-2020, [Volkamer lab, Charité](https://volkamerlab.org/)


## 本教程的目标

在本教程中，您将学习如何使用 API 网络服务在 [PubChem](https://pubchem.ncbi.nlm.nih.gov/) 中搜索与输入 SMILES 相似的化合物。

### _理论_ 部分内容

* PubChem
* PubChem 的程序化访问

### _实践_ 部分内容

* PubChem API 的简单示例
  * 如何获取化合物的 PubChem CID
  * 基于 PubChem CID 检索分子性质
  * 使用 PubChem 描绘化合物
* 查询 PubChem 中的相似化合物
  * 确定查询化合物
  * 创建任务并获取作业密钥
  * 作业完成后下载结果
  * 获取结果分子的规范 SMILES
  * 显示结果

### References
* Literature:
    * PubChem 2019 update: [_Nucleic Acids Res._ (2019), __47__, D1102-1109](https://academic.oup.com/nar/article/47/D1/D1102/5146201)
    * PubChem in 2021: [_Nucleic Acids Res._(2021), __49__, D1388–D1395](https://academic.oup.com/nar/article/49/D1/D1388/5957164)
* Documentation: 
    * [PubChem Source Information](https://pubchem.ncbi.nlm.nih.gov/sources)
    * [PUG REST](https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest)
    * [Programmatic Access](https://pubchemdocs.ncbi.nlm.nih.gov/programmatic-access)
    * [PubChem - Wikipedia](https://en.wikipedia.org/wiki/PubChem)
