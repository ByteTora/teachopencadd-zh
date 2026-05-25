# T014 · 结合位点检测

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

* Adapted from Abishek Laxmanan Ravi Shankar, 2019, internship at Volkamer lab
* Andrea Volkamer, 2020/21, [Volkamer lab, Charité](https://volkamerlab.org/)
* Dominique Sydow, 2020/21, [Volkamer lab, Charité](https://volkamerlab.org/)


## 本教程的目标

蛋白质的结合位点是其功能的关键。在本教程中，我们介绍使用 [protein.plus](https://proteins.plus/) 网络服务器的 DoGSiteScorer 进行计算结合位点检测的概念，并以 EGFR 结构为例进行说明。
此外，我们通过计算两组之间一致残基的百分比，将结果与预定义的 KLIFS 结合位点进行比较。

### _理论_ 部分内容

* 蛋白质结合位点
* 结合位点检测
    * 方法概述
    * DoGSiteScorer
* 与 KLIFS 口袋的比较

### _实践_ 部分内容

* 使用 DoGSiteScorer 进行结合位点检测
    * 提交感兴趣结构的任务
    * 获取 DoGSiteScorer 口袋元数据
    * 选择最合适的口袋
    * 获取最佳结合位点文件内容
    * 研究检测到的口袋
* DoGSiteScorer 与 KLIFS 口袋的比较
    * 获取 DoGSiteScorer 口袋残基
    * 获取 KLIFS 口袋残基
    * 口袋残基重叠

### References
* Prediction, Analysis, and Comparison of Active Sites [Volkamer <i>et al.</i>, (<b>2018</b>)](https://doi.org/10.1002/9783527806539.ch6g), book chapter in Applied Chemoinformatics: Achievements and Future Opportunities, Wiley
* DoGSiteScorer, [Volkamer <i>et al.</i>, <i>J.Chem.Inf.Model</i>, (<b>2012</b>), 52(2):360-372](https://pubmed.ncbi.nlm.nih.gov/22148551/)
* [ProteinsPlus](https://proteins.plus/): a web portal for structure analysis of macromolecules. [Fährrolfes <i>et al.</i>, <i>NAR</i>, (<b>2017</b>), 3;45(W1)](https://pubmed.ncbi.nlm.nih.gov/28472372/)
* [KLIFS](https://klifs.net/): a structural kinase-ligand interaction database, [Kanev <i>et al.</i>, <i>NAR</i>, (<b>2021</b>), 49(D1):D562-D569](https://academic.oup.com/nar/article/49/D1/D562/5934416) 
