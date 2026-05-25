# T024 · Kinase similarity: Sequence

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。

作者：

- Talia B. Kimber, 2021, [Volkamer 实验室, Charité](https://volkamerlab.org/)
- Dominique Sydow, 2021, [Volkamer 实验室, Charité](https://volkamerlab.org/)
- Andrea Volkamer, 2021, [Volkamer 实验室, Charité](https://volkamerlab.org/)


## 本教程目标

In this talktorial, we investigate sequence similarity for kinases of interest. KLIFS API is used to retrieve the $85$ residues of the pocket sequence for each kinase. 

Two similarity measures are implemented:

   1. Sequence identity, i.e., the similarity which is based on character-wise discrepancy.
   2. Sequence similarity, i.e., the similarity which is based on a substitution matrix, thus, reflecting similarities between amino acids.
   
_Note_: We focus on similarities between orthosteric kinase binding sites; similarities to allosteric binding sites are not covered.


### 理论内容

* Kinase dataset
* Kinase similarity descriptor: Sequence
    * Identity score
    * Substitution score
* From similarity matrix to distance matrix


### 实践内容

* Define the kinases of interest
* Retrieve sequences from KLIFS
* Sequence similarity
    * Identity score
    * Substitution score
* Kinase similarity
  * Visualize similarity as kinase matrix
  * Save kinase similarity matrix
* Kinase distance matrix
  * Save kinase distance matrix


### References

* Kinase dataset: [<i>Molecules</i> (2021), <b>26(3)</b>, 629](https://www.mdpi.com/1420-3049/26/3/629) 
* KLIFS
  * KLIFS URL: https://klifs.net/
  * KLIFS database: [<i>Nucleic Acid Res.</i> (2020), <b>49(D1)</b>, D562-D569](https://doi.org/10.1093/nar/gkaa895)
* Sequence-based kinase clustering: Manning _et al._ [<i>Science</i> (2002), <b>298(5600)</b>, 1912-1934](https://doi.org/10.1126/science.1075762)
* Substitution matrix: [<i>PNAS</i> (1992), <b>89(22)<b>, 10915-10919](https://doi.org/10.1073/pnas.89.22.10915)
* Biotite
    * Documentation: https://www.biotite-python.org/index.html
    * [Substitution matrix](https://www.biotite-python.org/latest/apidoc/biotite.sequence.align.SubstitutionMatrix.html)
* Sequence logo: http://www.cbs.dtu.dk/biotools/Seq2Logo/    
