# T038 · Protein Ligand Interaction Prediction

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。

作者：

- Roman Joeres, 2022, [Chair for Drug Bioinformatics, UdS and HIPS](https://www.helmholtz-hips.de/de/forschung/teams/team/wirkstoffbioinformatik/), [NextAID](https://nextaid.cs.uni-saarland.de/) project, Saarland University


## 本教程目标

The goal of this talktorial is to introduce the reader to the field of protein-ligand interaction prediction using graph neural networks (GNNs). GNNs are especially useful for representing structural data such as proteins and chemical molecules (ligands) to a deep learning model. In this talktorial, we will show how to train a deep learning model to predict interactions between proteins and ligands.


### 理论内容

* Relevance of protein-ligand interaction prediction
* Workflow
* Biological background - proteins as graphs
* Technical background
  * Graph Isomorphism Networks
  * Binary Cross Entropy Loss


### 实践内容

* Compute graph representations
  * Ligands to graphs
  * Proteins to graphs
* Data Storages
  * Data points
  * Data set
  * Data module
* Network
  * GNN encoder
  * Full model
* Training routine


### References

* Theoretical background
    * Graph Neural Networks:
      Kipf, Welling: "Semi-Supervised Classification with Graph Convolutional Networks", [<i>arXiv</i> (2017)](https://arxiv.org/abs/1609.02907)
      Bronstein, et al.: "Geometric deep learning: going beyond Euclidean data", [<i>IEEE Signal Processing Magazine</i> (2017), <b>4</b>, 18-42](https://doi.org/10.1109/MSP.2017.2693418)
    * GNN-based Protein-Ligand Interaction Prediction:
      Öztürk, et al.: "DeepDTA: Deep drug-target binding affinity prediction", [<i>Bioinformatics</i> (2018), <b>34</b>, i821-i829](https://doi.org/10.1093/bioinformatics/bty593)
      Nguyen, et. al.: "GraphDTA: Predicting drug-target binding affinity with graph neural networks", [<i>Bioinformatics</i> (2021), <b>37</b>, 1140-1147](https://doi.org/10.1093/bioinformatics/btaa921)
    * Graph Isomorphism Network:
      Xu, et al.: "How powerful are graph neural networks?", [<i>arXiv</i> (2018)](https://arxiv.org/abs/1810.00826)

* Practical background
    * [PyTorch](https://pytorch.org/)
    * [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/)
    * [RDKit](http://rdkit.org/): Greg Landrum, *RDKit Documentation*, [PDF](https://www.rdkit.org/UGM/2012/Landrum_RDKit_UGM.Fingerprints.Final.pptx.pdf), Release on 2019.09.1.
