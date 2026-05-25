# T016 · Protein-ligand interactions

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。

作者：

- Jaime Rodríguez-Guerra 2019-2020, [Volkamer 实验室](https://volkamerlab.org)
- Michele Wichmann, 2019-2020, Charité/FU Berlin
- Yonghui Chen, 2020, [Volkamer 实验室](https://volkamerlab.org)
- Talia B. Kimber, 2020, [Volkamer 实验室](https://volkamerlab.org)
- Andrea Volkamer, 2020, [Volkamer 实验室](https://volkamerlab.org)


## 本教程目标

In this talktorial, we focus on protein-ligand interactions. Understanding such interactions, which are driving molecular recognition, are fundamental in drug design.

To this end, we use two Python tools: the first one, called the Protein–Ligand Interaction Profiler, or [PLIP](https://doi.org/10.1093/nar/gkv315), to get insight into protein-ligand interactions for any sample complex and the second, [NGLView](https://doi.org/10.1093/bioinformatics/btx789), to visualize the interactions in 3D.


### 理论内容

- Protein-ligand interactions
- PLIP: Protein–Ligand Interaction Profiler
    - Web service
    - Algorithm
- Visualization: complex and interactions


### 实践内容

- PDB complex: example with EGFR
- Profiling protein-ligand interactions using PLIP
- Table of interaction types
- Visualization with NGLView
    - Analysis of interactions


### References

- Review on protein-ligand interactions ([_Int. J. Mol. Sci._ (2016), __17__, 144](https://www.mdpi.com/1422-0067/17/2/144))
- A systematic analysis of non-covalent interactions in the PDB database ([_M. Med. Chem. Commun._ (2017), __8__, 1970-1981](https://pubs.rsc.org/en/content/articlelanding/2017/md/c7md00381a#!divAbstract))
- A chapter about how protein–ligand interactions are key for drug action (in [Klebe G. (eds) Drug Design. Springer, Berlin, Heidelberg.](https://link.springer.com/referenceworkentry/10.1007%2F978-3-642-17907-5_4))
* Tools
    * NGLView, the interactive molecule visualizer for Jupyter notebooks ([_Bioinformatics_ (2018), __34__, 1241–124](https://doi.org/10.1093/bioinformatics/btx789))
    * PLIP, the Protein–Ligand Interaction Profiler ([_Nucl. Acids Res._ (2015), __43__, W1, W443-W447](https://academic.oup.com/nar/article/43/W1/W443/2467865))
