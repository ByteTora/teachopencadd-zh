# T002 · 分子筛选：ADME和类药性标准

## 教程目标

在药物设计领域，根据例如它们的物理化学性质来筛选候选分子非常重要。在这个教程中，我们将使用 Lipinski 的五规则来筛选从 ChEMBL 获取的化合物（见课程 __T001__），以保留只有口服生物利用度的化合物。

### _理论_ 部分

* ADME - 吸收、分布、代谢和排泄
* 类药性与利平斯基五规则（Ro5）
* 在类药性背景下的雷达图

### _实践_ 部分

* 定义并可视化示例分子
* 计算并绘制Ro5的分子属性
* 检查Ro5的合规性
* 将Ro5应用于EGFR数据集
* 可视化Ro5属性（雷达图）

### 参考文献

* ADME criteria ([Wikipedia](https://en.wikipedia.org/wiki/ADME) and [<i>Mol Pharm.</i> (2010), <b>7(5)</b>, 1388-1405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3025274/))
* [SwissADME](https://www.nature.com/articles/srep42717) webserver
* What are lead compounds? ([Wikipedia](https://en.wikipedia.org/wiki/Lead_compound))
* What is the LogP value? ([Wikipedia](https://en.wikipedia.org/wiki/Partition_coefficient))
* Lipinski et al. "Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings." ([<i>Adv. Drug Deliv. Rev.</i> (1997), <b>23</b>, 3-25](https://www.sciencedirect.com/science/article/pii/S0169409X96004231))
* Ritchie et al. "Graphical representation of ADME-related molecule properties for medicinal chemists" ([<i>Drug. Discov. Today</i> (2011), <b>16</b>, 65-72](https://www.ncbi.nlm.nih.gov/pubmed/21074634))