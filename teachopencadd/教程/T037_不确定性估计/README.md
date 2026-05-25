# T037 · Uncertainty estimation

**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。

作者：

- Michael Backenköhler, 2022, [Volkamer 实验室](https://volkamerlab.org), [NextAID](https://nextaid.cs.uni-saarland.de/) project, Saarland University


*The predictive setting (and the model class) used in this talktorial is adapted from __Talktorial T022__.*


## 本教程目标

Researchers often focus on prediction quality alone. However, when applying a predictive model, researchers are also interested in how certain they can be in a specific prediction. Estimating and providing such information is the goal of uncertainty estimation. In this talktorial, we discuss some common methodologies and showcase ensemble methods in practice.


### 理论内容

* Why a model can't and shouldn't be certain
* Calibration
* Methods overview
    * Single deterministic methods
    * Ensemble methods
    * Test-time data augmentation


### 实践内容
* Data
* Model
    * Training
    * Evaluation
* Ensembles - Training a model multiple times
    * Coverage of confidence intervals
    * Calibration
    * Ranking-based evaluation
* Bagging ensemble - Training a model with varying data
    * Ranking-based evaluation
* Test-time data augmentation


### References
* [Gawlikowski, Jakob, et al. "A survey of uncertainty in deep neural networks." _arXiv preprint_ (2021), arXiv:__2107.03342__](https://arxiv.org/abs/2107.03342)
* [Sagi, O. and Rokach, L. "Ensemble learning: A survey". Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 8(4), (2018) p.e1249.](https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/widm.1249?casa_token=1RRjvfS1_k4AAAAA%3AdR5WbRw9n8cp8wuVWx4j1ygfElNKbIJ9wXSmIeBd3C61pD1TEqX0bqswzRhNl8vY1rLDEhl29dseag)
* [Scalia, Gabriele, et al. "Evaluating scalable uncertainty estimation methods for deep learning-based molecular property prediction." _Journal of chemical information and Modeling_ __60.6__ (2020): 2697-2717](https://pubs.acs.org/doi/pdf/10.1021/acs.jcim.9b00975)
* __Talktorial T022__
