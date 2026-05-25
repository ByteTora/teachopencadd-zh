# T016 · 蛋白质-配体相互作用

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Jaime Rodríguez-Guerra 2019-2020, [Volkamer lab](https://volkamerlab.org)
- Michele Wichmann, 2019-2020, Charité/FU Berlin
- Yonghui Chen, 2020, [Volkamer lab](https://volkamerlab.org)
- Talia B. Kimber, 2020, [Volkamer lab](https://volkamerlab.org)
- Andrea Volkamer, 2020, [Volkamer lab](https://volkamerlab.org)


## 本教程的目标

在本教程中，我们专注于蛋白质-配体相互作用。理解这些驱动分子识别的相互作用是药物设计的基础。
为此，我们使用两个 Python 工具：第一个是蛋白质-配体相互作用分析器（[PLIP](https://doi.org/10.1093/nar/gkv315)），用于深入了解任意样本复合物中的蛋白质-配体相互作用；第二个是 [NGLView](https://doi.org/10.1093/bioinformatics/btx789)，用于在 3D 空间中可视化这些相互作用。

### _理论_ 部分内容

* 蛋白质-配体相互作用
* PLIP：蛋白质-配体相互作用分析器
    * 网络服务
    * 算法
* 可视化：复合物与相互作用

### _实践_ 部分内容

* PDB 复合物：以 EGFR 为例
* 使用 PLIP 分析蛋白质-配体相互作用
* 相互作用类型表格
* 使用 NGLView 进行可视化
    * 相互作用分析

### References

- Review on protein-ligand interactions ([_Int. J. Mol. Sci._ (2016), __17__, 144](https://www.mdpi.com/1422-0067/17/2/144))
- A systematic analysis of non-covalent interactions in the PDB database ([_M. Med. Chem. Commun._ (2017), __8__, 1970-1981](https://pubs.rsc.org/en/content/articlelanding/2017/md/c7md00381a#!divAbstract))
- A chapter about how protein–ligand interactions are key for drug action (in [Klebe G. (eds) Drug Design. Springer, Berlin, Heidelberg.](https://link.springer.com/referenceworkentry/10.1007%2F978-3-642-17907-5_4))
* Tools
    * NGLView, the interactive molecule visualizer for Jupyter notebooks ([_Bioinformatics_ (2018), __34__, 1241–124](https://doi.org/10.1093/bioinformatics/btx789))
    * PLIP, the Protein–Ligand Interaction Profiler ([_Nucl. Acids Res._ (2015), __43__, W1, W443-W447](https://academic.oup.com/nar/article/43/W1/W443/2467865))
