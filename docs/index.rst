.. teachopencadd 文档主文件，由
   sphinx-quickstart 于 Thu Mar 15 13:55:56 2018 创建。
   你可以完全按自己的喜好调整本文件，但它至少应
   包含根 `toctree` 指令。

TeachOpenCADD
=============

   本网站免费并向所有用户开放，无需登录！

化学信息学和结构生物信息学的开源编程包是构建计算机辅助药物设计（CADD）模块化、可复现、可复用流程的强大工具。虽然这些工具的文档是可用的，但只有少数免费可访问的示例教授以 CADD 应用为重点的底层概念，尤其面向该领域的新用户。

TeachOpenCADD 是一个由学生为学生开发的教学平台，提供 CADD 核心主题的教学材料。由于我们同时涵盖这些主题的理论方面和实践方面，该平台面向具有生物学/化学背景以及计算背景的学生和研究人员。

每个主题都提供一个交互式 Jupyter Notebook，使用开源包，如 Python 包 ``rdkit``、``pypdb``、``biopandas``、``nglview`` 以及 ``mdanalysis``。主题在不断扩展，并欢迎社区贡献。除教学目的外，TeachOpenCADD 材料还可作为用户项目导向修改和扩展的起点。

*新版*：我们使用 6 个 notebook 扩展了 TeachOpenCADD 平台，介绍深度学习及其在 CADD 相关主题中的应用。

.. raw:: html

   <p align="center">
   <img src="_static/images/TeachOpenCADD_topics.png" alt="TeachOpenCADD topics" width="800"/>
   <br>
   <font size="1">
   图改编自 TeachOpenCADD 出版物中的 Figure 1
   <a href="https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x">
   (D. Sydow <i>et al.</i>, J. Cheminformatics, 2019)</a>.
   </font>
   </p>

目录
-----------------

.. toctree::
   :maxdepth: 1
   :caption: 我们的 talktorials

   all_talktorials
   talktorials

.. toctree::
   :maxdepth: 1
   :caption: 本地运行

   installing

.. toctree::
   :maxdepth: 1
   :caption: 开发

   contribute
   api

.. toctree::
   :maxdepth: 1
   :caption: 关于 TeachOpenCADD

   contact
   acknowledgments
   citation
   license
   funding

.. toctree::
   :maxdepth: 1
   :caption: 外部资源

   external_dependencies
   external_tutorials_collections
