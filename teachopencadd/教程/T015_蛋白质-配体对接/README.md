# T015 · Protein ligand docking

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。

作者：

- Jaime Rodríguez-Guerra, 2019-20, [Volkamer 实验室, Charité](https://volkamerlab.org/)  
- Dominique Sydow, 2019-20, [Volkamer 实验室, Charité](https://volkamerlab.org/)  
- Michele Wichmann, 2019-20, student work at [Volkamer 实验室, Charité](https://volkamerlab.org/)  
- Maria Trofimova, CADD seminar, 2020, Charité/FU Berlin  
- David Schaller, 2020-21, [Volkamer 实验室, Charité](https://volkamerlab.org/)  
- Andrea Volkamer, 2021, [Volkamer 实验室, Charité](https://volkamerlab.org/)  


## 本教程目标

In this talktorial, we will use molecular docking to predict the binding mode of a small molecule in a protein binding site. The epidermal growth factor receptor ([EGFR](https://www.uniprot.org/uniprot/P00533)) will serve as a model system to explain important steps of a molecular docking workflow with the docking software [Smina](https://sourceforge.net/projects/smina/), a fork of Autodock Vina.


### 理论内容

- Molecular docking
- Sampling algorithms
- Scoring functions
- Limitations
- Visual inspection
- Docking software
  - Commercial
  - Free (for academics)


### 实践内容

- Preparation of protein and ligand 
- Binding site definition
- Docking calculation
- Docking results visualization


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
