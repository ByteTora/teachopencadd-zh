# T003 · 分子过滤：不想要的子结构

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供作为研究项目起点的流程模板。

作者：

- Maximilian Driller, CADD seminar, 2017, Charité/FU Berlin
- Sandra Krüger, CADD seminar, 2018, Charité/FU Berlin


__教程 T003__：本教程是第一篇 TeachOpenCADD 出版物 ([_J. Cheminform._ (2019), **11**, 1-7](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x)) 中描述的 TeachOpenCADD 流程的一部分，包含教程 T001-T010。


## 本教程目标

有些子结构我们更倾向于不包含在我们的筛选库中。在本教程中，我们将了解不同类型的不想要的子结构，以及如何使用 RDKit 查找、高亮和移除它们。


### 理论内容

* 不想要的子结构
* Pan Assay Interference Compounds (PAINS)  


### 实践内容

* 加载并可视化数据
* 过滤 PAINS
* 过滤不想要的子结构
* 高亮子结构
* 子结构统计


### References

* Pan Assay Interference compounds ([wikipedia](https://en.wikipedia.org/wiki/Pan-assay_interference_compounds), [_J. Med. Chem._ (2010), **53**, 2719-2740](https://pubs.acs.org/doi/abs/10.1021/jm901137j)) 
* Unwanted substructures according to Brenk *et al.* ([_Chem. Med. Chem._ (2008), **3**, 435-44](https://onlinelibrary.wiley.com/doi/full/10.1002/cmdc.200700139))
* Inspired by a Teach-Discover-Treat tutorial ([repository](https://github.com/sriniker/TDT-tutorial-2014/blob/master/TDT_challenge_tutorial.ipynb))
* RDKit ([repository](https://github.com/rdkit/rdkit), [documentation](https://www.rdkit.org/docs/index.html))
