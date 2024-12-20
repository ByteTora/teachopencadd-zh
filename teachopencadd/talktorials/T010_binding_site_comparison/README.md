# T010 ·结合位点相似性和脱靶预测

**注意：** 此讲座是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

Authors:

- Angelika Szengel, CADD seminar 2017, Charité/FU Berlin
- Marvis Sydow, CADD seminar 2018, Charité/FU Berlin
- Richard Gowers, RDKit UGM hackathon 2019
- Jaime Rodríguez-Guerra, 2020, [Volkamer lab](https://volkamerlab.org), Charité
- Dominique Sydow, 2018-2020, [Volkamer lab](https://volkamerlab.org), Charité
- Mareike Leja, 2020, [Volkamer lab](https://volkamerlab.org), Charité


__Talktorial T010__：此演讲是 [第一篇 TeachOpenCADD 论文]（https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x） 中描述的 TeachOpenCADD 管道的一部分，由演讲 T001-T010 组成。


**注意**：请逐个单元格运行此笔记本。也可以在一个中运行所有单元格，但是，可能会缺少部分 'nglview' 3D 表示。


## 本次演讲的目的

在本讲座中，我们使用完整蛋白质和结合位点的结构相似性来预测脱靶，即不是药物预期靶标的蛋白质。这可能会导致不必要的副作用或实现所需的药物替代应用（药物重新定位）。
我们讨论了结合位点比较的主要步骤并实施了一种基本方法，即结构之间的几何变化（两个结构之间的均方根偏差）。

### *理论*中的内容

* 脱靶蛋白
* 计算脱靶预测：结合位点比较
* 成对 RMSD 作为相似性的简单度量
* 伊马替尼，一种酪氨酸激酶抑制剂


### Contents in *Practical*

* 加载和可视化感兴趣的配体 （Imatinib/STI）
* 从 PDB 获取所有蛋白质-STI 复合物
* 可视化 PDB 结构
* 对齐 PDB 结构（全蛋白）
* 获取成对 RMSD（全蛋白）
* 对齐 PDB 结构（结合位点）
* 获取成对 RMSD（结合位点）
* 过滤掉异常值


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
  * [PDB information on Imatinib](https://www3.rcsb.org/ligand/STI)
  * Side effects of Imatinib
    * [MedFacts Consumer Drug Information](https://www.drugs.com/cdi/imatinib.html)
    * [DrugBank](https://go.drugbank.com/drugs/DB00619)
    * [<i>BMC Struct. Biol.</i> (2009), <b>9</b>](https://bmcstructbiol.biomedcentral.com/articles/10.1186/1472-6807-9-7)
* PDB queries
  * `pypdb` Python package 
[_Bioinformatics_ (2016), **1**, 159-60](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv543); [documentation](http://www.wgilpin.com/pypdb_docs/html/)
  * `biotite` Python package [_BMC Bioinformatics_ (2018), **19**](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2367-z); [documentation](https://www.biotite-python.org/)
  * Check out **Talktorial T008** for more details on PDB queries
