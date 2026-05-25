# T010 · 结合位点相似性与脱靶预测

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供作为研究项目起点的流程模板。

作者：

- Angelika Szengel, CADD seminar 2017, Charité/FU Berlin
- Marvis Sydow, CADD seminar 2018, Charité/FU Berlin
- Richard Gowers, RDKit UGM hackathon 2019
- Jaime Rodríguez-Guerra, 2020, [Volkamer 实验室](https://volkamerlab.org), Charité
- Dominique Sydow, 2018-2020, [Volkamer 实验室](https://volkamerlab.org), Charité
- Mareike Leja, 2020, [Volkamer 实验室](https://volkamerlab.org), Charité


__教程 T010__：本教程是 [第一篇 TeachOpenCADD 论文](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x) 中描述的 TeachOpenCADD 流程的一部分，包含教程 T001-T010。


**注意**：请逐个单元格运行此笔记本。虽然也可以一次性运行所有单元格，但部分 `nglview` 3D 显示可能会缺失。


## 本教程目标

在本教程中，我们使用完整蛋白质和结合位点的结构相似性来预测脱靶蛋白，即药物非预期靶点的蛋白质。这可能导致不想要的副作用，或实现药物的理想替代应用（药物重定位）。
我们讨论了结合位点比较的主要步骤，并实现了一种基本方法，即结构之间的几何变异（两个结构之间的均方根偏差）。


### *理论* 内容

* 脱靶蛋白
* 计算脱靶预测：结合位点比较
* 成对 RMSD 作为简单的相似性度量
* 伊马替尼，一种酪氨酸激酶抑制剂


### *实践* 内容

* 加载并可视化目标配体（伊马替尼/STI）
* 从 PDB 获取所有蛋白质-STI 复合物
* 可视化 PDB 结构
* 对齐 PDB 结构（完整蛋白质）
* 获取成对 RMSD（完整蛋白质）
* 对齐 PDB 结构（结合位点）
* 获取成对 RMSD（结合位点）
* 过滤离群值


### References

* Binding site superposition + comparison 
  * Binding site comparison reviews: 
    * [<i>Curr. Comput. Aided Drug Des. </i> (2008), <b>4</b>, 209-20](https://www.eurekaselect.com/67606/article/how-measure-similarity-between-protein-ligand-binding-sites)
    * [<i>J. Med. Chem. </i> (2016), <b>9</b>, 4121-51](https://pubs.acs.org/doi/10.1021/acs.jmedchem.6b00078)
  * Molecular superposition with Python: `opencadd` package (`structure.superposition` module) ([GitHub repository](https://github.com/volkamerlab/opencadd))
  * Wikipedia article on root mean square deviation ([RMSD](https://en.wikipedia.org/wiki/Root-mean-square_deviation_of_atomic_positions)) and [structural superposition](https://en.wikipedia.org/wiki/Structural_alignment)
  * Structural superposition: [Book chapter: Algorithms, Applications, and Challenges of Protein Structure Alignment in *Advances in Protein Chemistry and Structural Biology* (2014), **94**, 121-75](https://www.sciencedirect.com/science/article/pii/B9780128001684000056?via%3Dihub)
* Imatinib  
  * Review on Imatinib: [<i>Nat. Rev. Clin. Oncol.</i> (2016), <b>13</b>, 431-46](https://www.nature.com/articles/nrclinonc.2016.41)
  * Promiscuity of imatinib: 
[<i>J. Biol.</i> (2009), <b>8</b>, 30](https://jbiol.biomedcentral.com/articles/10.1186/jbiol134)
  * [ChEMBL information on Imatinib](https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL941)
  * [PDB information on Imatinib](https://www.rcsb.org/ligand/STI)
  * Side effects of Imatinib
    * [MedFacts Consumer Drug Information](https://www.drugs.com/cdi/imatinib.html)
    * [DrugBank](https://go.drugbank.com/drugs/DB00619)
    * [<i>BMC Struct. Biol.</i> (2009), <b>9</b>](https://bmcstructbiol.biomedcentral.com/articles/10.1186/1472-6807-9-7)
* PDB queries
  * `pypdb` Python package 
[_Bioinformatics_ (2016), **1**, 159-60](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv543); [documentation](http://www.wgilpin.com/pypdb_docs/html/)
  * `biotite` Python package [_BMC Bioinformatics_ (2018), **19**](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2367-z); [documentation](https://www.biotite-python.org/)
  * Check out **Talktorial T008** for more details on PDB queries
