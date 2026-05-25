# T026 · Kinase similarity: Interaction fingerprints

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。

作者：

- Dominique Sydow, 2021, [Volkamer 实验室, Charité](https://volkamerlab.org/)
- Talia B. Kimber, 2021, [Volkamer 实验室, Charité](https://volkamerlab.org/)
- Andrea Volkamer, 2021, [Volkamer 实验室, Charité](https://volkamerlab.org/)


## 本教程目标

We will assess the similarity between a set of kinases based on detected protein-ligand interactions in available complex structures. The [KLIFS](https://klifs.net/) interaction fingerprint (IFP), which describes the interactions seen in a structurally resolved kinase-ligand complex, will be used in this exercise.  

_Note_: We focus on similarities between orthosteric kinase binding sites; similarities to allosteric binding sites are not covered.


### 理论内容

* Kinase dataset
* Kinase similarity descriptor: KLIFS interaction fingerprint
* Fetching KLIFS data with `opencadd.databases.klifs`


### 实践内容

* Define the kinases of interest
* Retrieve and preprocess data
    * Set up a remote KLIFS session
    * Fetch all structures describing these kinases
    * Filter structures
    * Fetch the structures' IFPs (if available)
    * Merge structural and IFP data
* Show kinase coverage
* Compare structures
    * Prepare IFPs as `numpy` array
    * Calculate pairwise Jaccard distances
* Map structure to kinase distance matrix
* Save kinase distance matrix


### References

* Kinase dataset: [<i>Molecules</i> (2021), <b>26(3)</b>, 629](https://www.mdpi.com/1420-3049/26/3/629) 
* Protein Data Bank
  * PDB URL: http://www.rcsb.org/
  * PDB database: [<i>Acta Cryst.</i> (2002), <b>D58</b>, 899-907](https://doi.org/10.1107/S0907444902003451) and [<i>Structure</i> (2012), <b>20(3)</b>, 391-396](https://doi.org/10.1016/j.str.2012.01.010)
* KLIFS
  * KLIFS URL: https://klifs.net/
  * KLIFS database: [<i>Nucleic Acid Res.</i> (2020), <b>49(D1)</b>, D562-D569](https://doi.org/10.1093/nar/gkaa895)
  * KLIFS binding site definition and interaction fingerprint calculation: [<i>J. Med. Chem.</i> (2014), <b>57(2)</b>, 249-277](https://doi.org/10.1021/jm400378w)
* Interaction fingerprint (IFP): [<i>J. Chem. Inf. Model.</i> (2007), <b>71(1)</b>, 195-207](https://doi.org/10.1021/ci600342e)
* `opencadd`, a Python library for structural cheminformatics
  * GitHub repository: https://github.com/volkamerlab/opencadd
  * Documentation: https://opencadd.readthedocs.io
