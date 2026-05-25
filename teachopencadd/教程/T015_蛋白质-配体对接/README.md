# T015 · 蛋白质-配体对接

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Jaime Rodríguez-Guerra, 2019-20, [Volkamer lab, Charité](https://volkamerlab.org/)  
- Dominique Sydow, 2019-20, [Volkamer lab, Charité](https://volkamerlab.org/)  
- Michele Wichmann, 2019-20, student work at [Volkamer lab, Charité](https://volkamerlab.org/)  
- Maria Trofimova, CADD seminar, 2020, Charité/FU Berlin  
- David Schaller, 2020-21, [Volkamer lab, Charité](https://volkamerlab.org/)  
- Andrea Volkamer, 2021, [Volkamer lab, Charité](https://volkamerlab.org/)  


## 本教程的目标

在本教程中，我们将使用分子对接来预测小分子在蛋白质结合位点中的结合模式。表皮生长因子受体（[EGFR](https://www.uniprot.org/uniprot/P00533)）将作为模型系统，通过对接软件 [Smina](https://sourceforge.net/projects/smina/)（Autodock Vina 的一个分支）来解释分子对接工作流程的重要步骤。

### _理论_ 部分内容

* 分子对接
* 采样算法
* 评分函数
* 局限性
* 视觉检查
* 对接软件
  * 商用软件
  * 免费软件（针对学术界）

### _实践_ 部分内容

* 蛋白质和配体的准备
* 结合位点定义
* 对接计算
* 对接结果可视化

### References
- Molecular docking:
    - Pagadala _et al._, [_Biophy Rev_ (2017), __9__, 91-102](https://doi.org/10.1007/s12551-016-0247-1)
    - Meng _et al._, [_Curr Comput Aided Drug Des_ (2011), __7__, 2, 146-157](https://doi.org/10.2174/157340911795677602)
    - Gromski _et al._, [_Nat Rev Chem_ (2019), __3__, 119-128](https://doi.org/10.1038/s41570-018-0066-y)
- Docking and scoring function assessment:
    - Warren _et al._, [_J Med Chem_ (2006), __49__, 20, 5912-31](https://doi.org/10.1021/jm050362n)
    - Wang _et al._, [_Phys Chem Chem Phys_ (2016), __18__, 18, 12964-75](https://doi.org/10.1039/c6cp01555g)
    - Koes _et al._, [_J Chem Inf Model_ (2013), __53__, 8, 1893-1904](https://doi.org/10.1021/ci300604z)
    - Kimber _et al._, [_Int J Mol Sci_, (2021), __22__, 9, 1-34](https://doi.org/10.3390/ijms22094435)
    - McNutt _et al._, [_J Cheminform_ (2021), __13__, 43, 13-43](https://doi.org/10.1186/s13321-021-00522-2)
- Visual inspection of docking results: Fischer et al., [_J Med Chem_ (2021), __64__, 5, 2489–2500](https://doi.org/10.1021/acs.jmedchem.0c02227)
- Tools used
    - [OpenBabel](http://openbabel.org)
    - [Smina](https://sourceforge.net/projects/smina/)
    - [NGLView](http://nglviewer.org/nglview/latest/)
