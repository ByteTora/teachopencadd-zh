#!/usr/bin/env python3
"""
Translate T012-T038 README.md files from English to Chinese.

Rules:
1. Translate title, note, aim, contents to Chinese. Keep all URLs, DOIs, code refs unchanged.
2. Keep author names in English; translate "Volkamer lab" → "Volkamer 实验室"
3. "talktorial" → "教程", "Talktorial" → "教程"
4. Keep ALL references section in original English - do NOT translate ANY part of references
5. Keep technical terms in English (KLIFS, SMILES, PDB, etc.)
6. Keep markdown formatting and structure intact
"""

import re
import os


def translate_file(source, target):
    with open(source, "r") as f:
        content = f.read()

    # Split at the References section heading
    # We need to find where the References section starts
    # Patterns: "### References", "## References", "### References" etc.
    ref_patterns = [
        r"\n## References\n",
        r"\n### References\n",
        r"\n# References\n",
        r"\n## References\r?\n",
        r"\n### References\r?\n",
    ]

    ref_start = -1
    for pattern in ref_patterns:
        m = re.search(pattern, content)
        if m:
            ref_start = m.start()
            break

    if ref_start != -1:
        main_part = content[:ref_start]
        ref_part = content[ref_start:]
    else:
        main_part = content
        ref_part = ""

    # Apply translations to main_part only
    main_part = apply_translations(main_part)
    main_part = apply_file_specific_translations(main_part, os.path.basename(source))

    # Ensure ref_part is untouched
    result = main_part + ref_part

    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w") as f:
        f.write(result)
    print(f"✓ {os.path.basename(source)} → {target}")


def apply_translations(text):
    # Common patterns across all files

    # Translate "Note" callout
    text = text.replace(
        "**Note:** This talktorial is a part of TeachOpenCADD, a platform that aims to teach domain-specific skills and to provide pipeline templates as starting points for research projects.",
        "**注意：** 本教程是 TeachOpenCADD 的一部分，该平台旨在教授特定领域的技能，并提供作为研究项目起点的流程模板。",
    )

    # Translate "Aim of this talktorial" headings
    text = text.replace("## Aim of this talktorial", "## 本教程目标")
    text = text.replace("## Aim of the talktorial", "## 本教程目标")

    # Translate "Contents in Theory" headings
    text = text.replace("### Contents in *Theory*", "### 理论内容")
    text = text.replace("### Contents in _Theory_", "### 理论内容")
    text = text.replace("### Contents in Theory", "### 理论内容")

    # Translate "Contents in Practical" headings
    text = text.replace("### Contents in *Practical*", "### 实践内容")
    text = text.replace("### Contents in _Practical_", "### 实践内容")

    # Translate "Volkamer lab" / "Volkamer Lab" to "Volkamer 实验室"
    text = text.replace("Volkamer lab", "Volkamer 实验室")
    text = text.replace("Volkamer Lab", "Volkamer 实验室")

    # Translate "talktorial" references within text (but not in URLs or code)
    # Be careful: "Talktorial" at start of sentences, "talktorial" in middle
    # We'll use careful replacements
    
    return text


def apply_file_specific_translations(text, filename):
    """Apply file-specific translations based on the source filename."""
    
    # T012
    if "T012" in filename:
        text = text.replace("# T012 · Data acquisition from KLIFS", "# T012 · 从 KLIFS 获取数据")
        text = text.replace(
            "[KLIFS](https://klifs.net/) is a database for kinase-ligand interaction fingerprints and structures. In this talktorial, we will use the programmatic access to this database (KLIFS OpenAPI) and the `opencadd` ([GitHub](https://github.com/volkamerlab/opencadd)) package to interact with its rich content.",
            "[KLIFS](https://klifs.net/) 是一个激酶-配体相互作用指纹和结构数据库。在本教程中，我们将使用该数据库的编程访问接口（KLIFS OpenAPI）和 `opencadd`（[GitHub](https://github.com/volkamerlab/opencadd)）包来交互其丰富的内容。",
        )
        text = text.replace(
            "First, we will use a query kinase ([EGFR](https://www.uniprot.org/uniprot/P00533)) to fetch all available protein structures and explore their bound ligands as well as interaction fingerprints. Then, we will explore the bioactivity data for the EGFR inhibitor [Gefitinib](https://pubchem.ncbi.nlm.nih.gov/compound/Gefitinib) in order to find off-targets. Last but not least, we offer a convenience function that allows to easily explore different kinases.",
            "首先，我们将使用一个查询激酶（[EGFR](https://www.uniprot.org/uniprot/P00533)）来获取所有可用的蛋白质结构，并探索其结合的配体以及相互作用指纹。然后，我们将探索 EGFR 抑制剂 [Gefitinib](https://pubchem.ncbi.nlm.nih.gov/compound/Gefitinib) 的生物活性数据，以寻找脱靶靶点。最后，我们提供了一个便捷函数，可以轻松探索不同的激酶。",
        )
        # Theory contents
        text = text.replace("- Kinases\n- EGFR and Gefitinib\n- KLIFS database\n- KLIFS OpenAPI\n- `opencadd`", "- 激酶\n- EGFR 与 Gefitinib\n- KLIFS 数据库\n- KLIFS OpenAPI\n- `opencadd`")
        # Practical contents
        text = text.replace("- Define kinase and ligand of interest: EGFR and Gefitinib\n- Generate a KLIFS Python client\n- Explore the KLIFS OpenAPI\n  - Kinase groups\n  - Kinase families\n  - Kinases\n  - Structures\n  - Interaction fingerprints\n  - Structure coordinates\n  - Ligands\n- Case study: EGFR (using `opencadd`)\n  - Get all structures for EGFR\n  - Average interaction fingerprint\n  - Select an example EGFR-Gefitinib structure\n  - Show the structure with `nglview`\n  - Show all kinase-bound ligands with `rdkit`\n  - Explore profiling data for Gefitinib\n- Explore a random kinase in KLIFS",
            "- 定义目标激酶和配体：EGFR 与 Gefitinib\n- 生成 KLIFS Python 客户端\n- 探索 KLIFS OpenAPI\n  - 激酶分组\n  - 激酶家族\n  - 激酶\n  - 结构\n  - 相互作用指纹\n  - 结构坐标\n  - 配体\n- 案例研究：EGFR（使用 `opencadd`）\n  - 获取 EGFR 的所有结构\n  - 平均相互作用指纹\n  - 选择一个 EGFR-Gefitinib 示例结构\n  - 使用 `nglview` 显示结构\n  - 使用 `rdkit` 显示所有激酶结合配体\n  - 探索 Gefitinib 的 profiling 数据\n- 探索 KLIFS 中的随机激酶")

    # T013
    elif "T013" in filename:
        text = text.replace("# T013 · Data acquisition from PubChem", "# T013 · 从 PubChem 获取数据")
        text = text.replace(
            "In this notebook, you will learn how to search for compounds similar to an input SMILES in [PubChem](https://pubchem.ncbi.nlm.nih.gov/) with the API web service.",
            "在本教程中，您将学习如何使用 API 网络服务在 [PubChem](https://pubchem.ncbi.nlm.nih.gov/) 中搜索与输入 SMILES 相似的化合物。",
        )
        text = text.replace("- PubChem\n- Programmatic access to PubChem", "- PubChem\n- PubChem 编程访问")
        text = text.replace(
            "* Simple examples for the PubChem API\n  * How to get the PubChem CID for a compound\n  * Retrieve molecular properties based on a PubChem CID\n  * Depict a compound with PubChem\n* Query PubChem for similar compounds\n  * Determine a query compound\n  * Create task and get the job key\n  * Download results when job finished\n  * Get canonical SMILES for resulting molecules\n  * Show the results",
            "* PubChem API 简单示例\n  * 如何获取化合物的 PubChem CID\n  * 基于 PubChem CID 检索分子性质\n  * 使用 PubChem 描绘化合物\n* 查询 PubChem 中的相似化合物\n  * 确定查询化合物\n  * 创建任务并获取作业密钥\n  * 作业完成后下载结果\n  * 获取结果分子的规范 SMILES\n  * 显示结果",
        )

    # T014
    elif "T014" in filename:
        text = text.replace("# T014 · Binding site detection", "# T014 · 结合位点检测")
        text = text.replace(
            "The binding site of a protein is the key to its function. In this talktorial, we introduce the concepts of computational binding site detection tools using DoGSiteScorer from the [protein.plus](https://proteins.plus/) web server, exemplified on an EGFR structure.",
            "蛋白质的结合位点是其功能的关键。在本教程中，我们将介绍计算结合位点检测工具的概念，使用 [protein.plus](https://proteins.plus/) 网络服务器上的 DoGSiteScorer，以 EGFR 结构为例进行说明。",
        )
        text = text.replace(
            "Additionally, we compare the results to the pre-defined KLIFS binding site by calculating the percentage of residues in accordance between the two sets.",
            "此外，我们通过计算两组之间一致残基的百分比，将结果与预定义的 KLIFS 结合位点进行比较。",
        )
        text = text.replace("* Protein binding sites\n* Binding site detection\n    * Methods overview\n    * DoGSiteScorer\n* Comparison to KLIFS pocket",
            "* 蛋白质结合位点\n* 结合位点检测\n    * 方法概述\n    * DoGSiteScorer\n* 与 KLIFS 结合口袋的比较")
        text = text.replace(
            "* Binding site detection using DoGSiteScorer\n    * Job submission of structure of interest\n    * Get DoGSiteScorer pocket metadata\n    * Pick the most suitable pocket\n    * Get best binding site file content\n    * Investigate detected pocket\n* Comparison between DoGSiteScorer and KLIFS pocket\n    * Get DoGSiteScorer pocket residues\n    * Get KLIFS pocket residues\n    * Overlap of pocket residues",
            "* 使用 DoGSiteScorer 进行结合位点检测\n    * 提交目标结构的任务\n    * 获取 DoGSiteScorer 结合口袋元数据\n    * 选择最合适的结合口袋\n    * 获取最佳结合位点文件内容\n    * 检查检测到的结合口袋\n* DoGSiteScorer 与 KLIFS 结合口袋的比较\n    * 获取 DoGSiteScorer 结合口袋残基\n    * 获取 KLIFS 结合口袋残基\n    * 结合口袋残基的重叠",
        )
        # Translate author line
        text = text.replace("* Adapted from Abishek Laxmanan Ravi Shankar, 2019, internship at Volkamer lab",
            "* 改编自 Abishek Laxmanan Ravi Shankar, 2019, Volkamer 实验室实习")

    # T015
    elif "T015" in filename:
        text = text.replace("# T015 · Protein ligand docking", "# T015 · 蛋白质-配体对接")
        text = text.replace(
            "In this talktorial, we will use molecular docking to predict the binding mode of a small molecule in a protein binding site. The epidermal growth factor receptor ([EGFR](https://www.uniprot.org/uniprot/P00533)) will serve as a model system to explain important steps of a molecular docking workflow with the docking software [Smina](https://sourceforge.net/projects/smina/), a fork of Autodock Vina.",
            "在本教程中，我们将使用分子对接来预测小分子在蛋白质结合位点中的结合模式。表皮生长因子受体（[EGFR](https://www.uniprot.org/uniprot/P00533)）将作为模型系统，使用对接软件 [Smina](https://sourceforge.net/projects/smina/)（Autodock Vina 的一个分支）解释分子对接工作流程的重要步骤。",
        )
        text = text.replace("- Molecular docking\n- Sampling algorithms\n- Scoring functions\n- Limitations\n- Visual inspection\n- Docking software\n  - Commercial\n  - Free (for academics)",
            "- 分子对接\n- 采样算法\n- 评分函数\n- 局限性\n- 视觉检查\n- 对接软件\n  - 商业软件\n  - 免费（学术用途）")
        text = text.replace("- Preparation of protein and ligand \n- Binding site definition\n- Docking calculation\n- Docking results visualization",
            "- 蛋白质和配体的准备\n- 结合位点定义\n- 对接计算\n- 对接结果可视化")
        text = text.replace("- Michele Wichmann, 2019-20, student work at [Volkamer lab, Charité](https://volkamerlab.org/)",
            "- Michele Wichmann, 2019-20, [Volkamer 实验室, Charité](https://volkamerlab.org/) 学生工作")

    # T016
    elif "T016" in filename:
        text = text.replace("# T016 · Protein-ligand interactions", "# T016 · 蛋白质-配体相互作用")
        text = text.replace(
            "In this talktorial, we focus on protein-ligand interactions. Understanding such interactions, which are driving molecular recognition, are fundamental in drug design.",
            "在本教程中，我们将重点介绍蛋白质-配体相互作用。理解这些驱动分子识别的相互作用是药物设计的基础。",
        )
        text = text.replace(
            "To this end, we use two Python tools: the first one, called the Protein–Ligand Interaction Profiler, or [PLIP](https://doi.org/10.1093/nar/gkv315), to get insight into protein-ligand interactions for any sample complex and the second, [NGLView](https://doi.org/10.1093/bioinformatics/btx789), to visualize the interactions in 3D.",
            "为此，我们使用两个 Python 工具：第一个是蛋白质-配体相互作用分析器（Protein–Ligand Interaction Profiler），简称 [PLIP](https://doi.org/10.1093/nar/gkv315)，用于深入了解任何样本复合物的蛋白质-配体相互作用；第二个是 [NGLView](https://doi.org/10.1093/bioinformatics/btx789)，用于在 3D 中可视化这些相互作用。",
        )
        text = text.replace("- Protein-ligand interactions\n- PLIP: Protein–Ligand Interaction Profiler\n    - Web service\n    - Algorithm\n- Visualization: complex and interactions",
            "- 蛋白质-配体相互作用\n- PLIP：蛋白质-配体相互作用分析器\n    - 网络服务\n    - 算法\n- 可视化：复合物与相互作用")
        text = text.replace("- PDB complex: example with EGFR\n- Profiling protein-ligand interactions using PLIP\n- Table of interaction types\n- Visualization with NGLView\n    - Analysis of interactions",
            "- PDB 复合物：以 EGFR 为例\n- 使用 PLIP 分析蛋白质-配体相互作用\n- 相互作用类型表\n- 使用 NGLView 可视化\n    - 相互作用分析")

    # T017
    elif "T017" in filename:
        text = text.replace("# T017 · Advanced NGLview usage", "# T017 · 高级 NGLView 使用")
        text = text.replace(
            "[NGLView](http://nglviewer.org/nglview/latest/) is a powerful Jupyter widget that allows you to show molecular structures in your notebooks in a 3D interactive view! It supports both single conformations and trajectories, as well as a plethora of representations. In this talktorial we will cover how to use it in different scenarios, from simpler cases to more intricate ones.",
            "[NGLView](http://nglviewer.org/nglview/latest/) 是一个强大的 Jupyter 控件，可以让您在笔记本中以 3D 交互视图显示分子结构！它支持单个构象和轨迹，以及多种表示方式。在本教程中，我们将介绍如何在不同的场景中使用它，从简单的案例到更复杂的案例。",
        )
        text = text.replace("* NGL and NGLView\n* NGL object model and terminology", "* NGL 与 NGLView\n* NGL 对象模型与术语")
        text = text.replace(
            "* First steps: make sure everything works!\n    * Experiment with the interactive controls\n* Basic API usage:\n    * Show a structure using its PDB identifier\n    * Show a structure using a local file\n    * Saving the widget state as a screenshot for offline viewing\n    * Customize the representations\n    * Control representations by selections\n    * NMR and multimodel structures\n    * Load more than one structure\n    * Show and hide components\n* Advanced usage:\n    * Custom coloring schemes and representations\n    * Add geometric objects at selected atoms\n    * Create interactive interfaces\n    * Access the JavaScript layer\n* Troubleshooting tips:\n    * Check which Jupyter platform you are working from\n    * How to install `nglview`, the right way",
            "* 第一步：确保一切正常！\n    * 实验交互控件\n* 基本 API 使用：\n    * 使用 PDB 标识符显示结构\n    * 使用本地文件显示结构\n    * 保存控件状态为屏幕截图以供离线查看\n    * 自定义表示方式\n    * 通过选择控制表示方式\n    * NMR 和多模型结构\n    * 加载多个结构\n    * 显示和隐藏组件\n* 高级用法：\n    * 自定义配色方案和表示方式\n    * 在选定原子处添加几何对象\n    * 创建交互界面\n    * 访问 JavaScript 层\n* 故障排除技巧：\n    * 检查您使用的 Jupyter 平台\n    * 如何正确安装 `nglview`",
        )

    # T018
    elif "T018" in filename:
        text = text.replace("# T018 · Automated pipeline for lead optimization", "# T018 · 先导化合物优化自动化流程")
        text = text.replace(
            "In this talktorial, we will learn how to develop an **automated structure-based virtual screening pipeline**. ",
            "在本教程中，我们将学习如何开发一个**基于结构的自动化虚拟筛选流程**。",
        )
        text = text.replace(
            "The pipeline is **particularly suited for the hit expansion and lead optimization** phases of a drug discovery project, where a promising ligand (i.e. an initial hit or lead compound) needs to be structurally modified in order to improve its binding affinity and selectivity for the target protein. The general architecture of the pipeline can thus be summarized as follows (Figure 1).",
            "该流程**特别适用于药物发现项目中的 hit expansion 和先导化合物优化**阶段，其中一个有前景的配体（即初始 hit 或先导化合物）需要进行结构修饰，以提高其对目标蛋白质的结合亲和力和选择性。该流程的总体架构可总结如下（图 1）。",
        )
        text = text.replace("* **Input**\n    * Target protein structure and a promising ligand (e.g. lead or hit compound), plus specifications of the processes that need to be performed.\n      \n      \n* **Processes**\n    * Detection of the most druggable binding site for the given protein structure.\n    * Finding derivatives and structural analogs for the ligand, and filtering them based on drug-likeness. \n    * Performing docking calculations on the detected protein binding site using the selected analogs.\n    * Analyzing and vizualizing predicted protein–ligand interactions and binding modes for each analog.\n    \n    \n* **Output**\n    * New ligand structure(s) optimized for affinity, selectivity and drug-likeness.",
            "* **输入**\n    * 目标蛋白质结构和一个有前景的配体（例如先导化合物或 hit 化合物），以及需要执行过程的规格说明。\n      \n      \n* **处理过程**\n    * 检测给定蛋白质结构中最具成药性的结合位点。\n    * 寻找配体的衍生物和结构类似物，并基于类药性进行筛选。\n    * 使用选定的类似物对检测到的蛋白质结合位点进行对接计算。\n    * 分析和可视化每个类似物预测的蛋白质-配体相互作用和结合模式。\n    \n    \n* **输出**\n    * 针对亲和力、选择性和类药性优化的新配体结构。",
        )
        text = text.replace("*Figure 1*: General architecture of the automated structure-based virtual screening pipeline.",
            "*图 1*：基于结构的自动化虚拟筛选流程总体架构。")
        text = text.replace("- [Drug design pipeline](#Drug-design-pipeline)\n- [Protein binding site](#Protein-binding-site) \n- [Chemical similarity search](#Chemical-similarity-search)\n- [Molecular docking](#Molecular-docking)\n- [Protein&mdash;ligand interactions](#Protein&mdash;ligand-interactions)\n- [Visual inspection of docking results](#Visual-inspection-of-docking-results)",
            "- [药物设计流程](#Drug-design-pipeline)\n- [蛋白质结合位点](#Protein-binding-site)\n- [化学相似性搜索](#Chemical-similarity-search)\n- [分子对接](#Molecular-docking)\n- [蛋白质-配体相互作用](#Protein&mdash;ligand-interactions)\n- [对接结果视觉检查](#Visual-inspection-of-docking-results)")
        text = text.replace("- [Outline of the virtual screening pipeline](#Outline-of-the-virtual-screening-pipeline)\n- [Creating a new project](#Creating-a-new-project)\n- [The input data](#The-input-data)\n- [Processing the input protein data](#Processing-the-input-protein-data)\n- [Processing the input ligand data](#Processing-the-input-ligand-data)\n- [Binding site detection](#Binding-site-detection)\n- [Ligand similarity search](#Ligand-similarity-search)\n- [Docking calculations](#Docking-calculations)\n- [Analysis of protein&mdash;ligand interactions](#Analysis-of-protein&mdash;ligand-interactions)\n- [Selection of the best analog](#Selection-of-the-best-analog)\n- [Putting the pieces together: A fully automated pipeline](#Putting-the-pieces-together:-A-fully-automated-pipeline)",
            "- [虚拟筛选流程概述](#Outline-of-the-virtual-screening-pipeline)\n- [创建新项目](#Creating-a-new-project)\n- [输入数据](#The-input-data)\n- [处理输入蛋白质数据](#Processing-the-input-protein-data)\n- [处理输入配体数据](#Processing-the-input-ligand-data)\n- [结合位点检测](#Binding-site-detection)\n- [配体相似性搜索](#Ligand-similarity-search)\n- [对接计算](#Docking-calculations)\n- [蛋白质-配体相互作用分析](#Analysis-of-protein&mdash;ligand-interactions)\n- [选择最佳类似物](#Selection-of-the-best-analog)\n- [整合所有环节：完全自动化流程](#Putting-the-pieces-together:-A-fully-automated-pipeline)")

    # T019
    elif "T019" in filename:
        text = text.replace("# T019 · Molecular dynamics simulation", "# T019 · 分子动力学模拟")
        text = text.replace(
            "This talktorial was designed to be used with [Google Colab](https://colab.research.google.com/github/volkamerlab/teachopencadd/blob/1bd7cb0c9f6379aebc0c1a0b1c7413685910cffa/teachopencadd/talktorials/019_md_simulation/talktorial.ipynb). It is also possible to use it on a local computer. However, performing the molecular dynamics simulation may take a considerably long time if no GPU is available.",
            "本教程专为与 [Google Colab](https://colab.research.google.com/github/volkamerlab/teachopencadd/blob/1bd7cb0c9f6379aebc0c1a0b1c7413685910cffa/teachopencadd/talktorials/019_md_simulation/talktorial.ipynb) 一起使用而设计。也可以在本地计算机上使用。然而，如果没有 GPU，执行分子动力学模拟可能需要相当长的时间。",
        )
        text = text.replace(
            "Also, note that this talktorial **will not run on Windows** for the time being (check progress in [this issue](https://github.com/volkamerlab/teachopencadd/issues/136)).",
            "另请注意，本教程**暂时无法在 Windows 上运行**（查看 [此 issue](https://github.com/volkamerlab/teachopencadd/issues/136) 的进展）。",
        )
        text = text.replace(
            "In this talktorial, we will learn why molecular dynamics (MD) simulations are important for drug design and which steps are necessary to perform an MD simulation of a protein in complex with a ligand. The kinase EGFR will serve as sample system for simulation.",
            "在本教程中，我们将学习为什么分子动力学（MD）模拟对药物设计很重要，以及执行蛋白质与配体复合物的 MD 模拟需要哪些步骤。激酶 EGFR 将作为模拟的示例系统。",
        )
        text = text.replace("- Molecular dynamics\n- Force fields\n- Boundary conditions\n- MD simulations and drug design\n- EGFR kinase",
            "- 分子动力学\n- 力场\n- 边界条件\n- MD 模拟与药物设计\n- EGFR 激酶")
        text = text.replace("- Installation on Google Colab\n- Adjust environment for local installations running on Linux or MacOS\n- Import dependencies\n- Download PDB file\n- Prepare the protein ligand complex\n  - Protein preparation\n  - Ligand preparation\n  - Merge protein and ligand\n- MD simulation set up\n  - Force field\n  - System\n- Perform the MD simulation\n- Download results",
            "- 在 Google Colab 上安装\n- 调整在 Linux 或 MacOS 上本地安装的环境\n- 导入依赖项\n- 下载 PDB 文件\n- 准备蛋白质-配体复合物\n  - 蛋白质准备\n  - 配体准备\n  - 合并蛋白质和配体\n- MD 模拟设置\n  - 力场\n  - 系统\n- 执行 MD 模拟\n- 下载结果")

    # T020
    elif "T020" in filename:
        text = text.replace("# T020 · Analyzing molecular dynamics simulations", "# T020 · 分子动力学模拟分析")
        text = text.replace(
            "In this talktorial, we will introduce methods for the analysis of molecular dynamics (MD) simulations. The introduced methods include animated visualization, structural alignment, RMSD calculation as well as selected atom distances and hydrogen bond analysis. ",
            "在本教程中，我们将介绍分子动力学（MD）模拟的分析方法。介绍的方法包括动画可视化、结构比对、RMSD 计算以及选定原子距离和氢键分析。",
        )
        text = text.replace(
            "Note, we will work with the simulation results (1ns, 100 frames) generated with **Talktorial T019** on the EGFR kinase ([PDB: 3POZ](https://www.rcsb.org/structure/3poz)) bound to inhibitor [03P](https://www.rcsb.org/ligand/03P).",
            "注意，我们将使用**教程 T019** 生成的模拟结果（1ns，100 帧），该模拟针对与抑制剂 [03P](https://www.rcsb.org/ligand/03P) 结合的 EGFR 激酶（[PDB: 3POZ](https://www.rcsb.org/structure/3poz)）进行。",
        )
        text = text.replace("- MD simulations\n    - Application in the drug discovery process\n    - Flexible vs. static structures\n- Analyzing MD simulations\n  - Visualization\n  - RMSD\n  - Hydrogen bond analysis",
            "- MD 模拟\n    - 在药物发现过程中的应用\n    - 柔性结构与静态结构\n- 分析 MD 模拟\n  - 可视化\n  - RMSD\n  - 氢键分析")
        text = text.replace("- Load and visualize the system\n- Alignment\n- RMSD of protein and ligand\n  - RMSD over time\n  - RMSD between frames\n- Interaction analysis\n  - Atomic distances\n  - Hydrogen bond analysis",
            "- 加载和可视化系统\n- 比对\n- 蛋白质和配体的 RMSD\n  - RMSD 随时间变化\n  - 帧间 RMSD\n- 相互作用分析\n  - 原子距离\n  - 氢键分析")

    # T021
    elif "T021" in filename:
        text = text.replace("# T021 · One-Hot Encoding", "# T021 · 独热编码")
        text = text.replace("Developed in the CADD seminar 2020, Volkamer Lab, Charité/FU Berlin",
            "开发于 2020 年 CADD 研讨会，Volkamer 实验室，Charité/FU Berlin")
        text = text.replace(
            "The aim of the talktorial is to perform one-hot encoding of SMILES structures on a subset of the ChEMBL data set to gain a deeper understanding on the one-hot encoding concept and why it is useful as a pre-processing step in various machine learning algorithms.",
            "本教程的目标是在 ChEMBL 数据集的子集上对 SMILES 结构进行独热编码，以深入理解独热编码的概念，以及为什么它作为各种机器学习算法中的预处理步骤非常有用。",
        )
        text = text.replace("- Molecular data and representation\n    - ChEMBL database\n    - SMILES structures and rules\n- What is categorical data?\n     - What is the problem with categorical data?\n     - How to convert categorical data to numerical data?\n- The One-Hot Encoding (OHE) concept\n     - Why using one-hot encoding?\n     - Example of one-hot encoding\n     - Advantages and disadvantages of one-hot encoding\n- Similar: Integer or label encoding\n- What is *padding*?\n- Further readings",
            "- 分子数据与表示\n    - ChEMBL 数据库\n    - SMILES 结构与规则\n- 什么是分类数据？\n     - 分类数据有什么问题？\n     - 如何将分类数据转换为数值数据？\n- 独热编码（OHE）概念\n     - 为什么使用独热编码？\n     - 独热编码示例\n     - 独热编码的优缺点\n- 类似方法：整数编码或标签编码\n- 什么是*padding*？\n- 延伸阅读")
        text = text.replace("- Import necessary packages\n- Read the input data\n- Process the data\n     - Double digit replacement\n     - Compute longest (& shortest) SMILES\n- Python one-hot encoding implementation\n     - One-hot encode (padding=True)\n     - Visualization\n          - Shortest SMILES\n          - Longest SMILES \n- Supplementary material\n   - Scikit learn implementation\n   - Keras implementation",
            "- 导入必要包\n- 读取输入数据\n- 处理数据\n     - 双位数替换\n     - 计算最长（和最短）SMILES\n- Python 独热编码实现\n     - 独热编码（padding=True）\n     - 可视化\n          - 最短 SMILES\n          - 最长 SMILES\n- 补充材料\n   - Scikit learn 实现\n   - Keras 实现")

    # T022
    elif "T022" in filename:
        text = text.replace("# T022 · Ligand-based screening: neural networks", "# T022 · 基于配体的筛选：神经网络")
        text = text.replace("Developed in the CADD seminar 2020, Volkamer Lab, Charité/FU Berlin",
            "开发于 2020 年 CADD 研讨会，Volkamer 实验室，Charité/FU Berlin")
        text = text.replace(
            "In recent years, the use of machine learning, and deep learning, in pharmaceutical research has shown promising results in addressing diverse problems in drug discovery. In this talktorial, we get familiar with the basics of neural networks. We will learn how to build a simple two layer neural network and train it on a subset of ChEMBL data in order to predict the pIC50 values of compounds against EGFR, the target of interest. Furthermore, we select three compounds from an external, unlabeled data set that are predicted to be the most active against that kinase.",
            "近年来，机器学习和深度学习在制药研究中的应用在解决药物发现中的各种问题方面展现了有前景的结果。在本教程中，我们将熟悉神经网络的基础知识。我们将学习如何构建一个简单的两层神经网络，并在 ChEMBL 数据的子集上进行训练，以预测化合物对目标 EGFR 的 pIC50 值。此外，我们将从一个外部未标记数据集中选择三个预测对该激酶活性最高的化合物。",
        )
        text = text.replace("- Biological background\n    - EGFR kinase\n    - Compound activity measures\n    - Molecule encoding\n- Neural networks\n    - What is a neural network?\n    - Activation function\n    - Loss function\n- Training a neural network\n- Keras workflow\n- Advantages and applications of neural networks",
            "- 生物学背景\n    - EGFR 激酶\n    - 化合物活性度量\n    - 分子编码\n- 神经网络\n    - 什么是神经网络？\n    - 激活函数\n    - 损失函数\n- 训练神经网络\n- Keras 工作流程\n- 神经网络的优点与应用")
        text = text.replace("- Data preparation\n- Define neural network\n- Train the model\n- Evaluation & prediction on test set\n    - Scatter plot\n- Prediction on external/unlabeled data\n    - Select the top 3 compounds",
            "- 数据准备\n- 定义神经网络\n- 训练模型\n- 评估与测试集预测\n    - 散点图\n- 对外部/未标记数据的预测\n    - 选择前 3 个化合物")

    # T023
    elif "T023" in filename:
        text = text.replace("# T023 · What is a kinase?", "# T023 · 什么是激酶？")
        text = text.replace(
            "In this talktorial, we will talk about kinases: why are they important in life and drug design, what do they look like, and what data resources are available?",
            "在本教程中，我们将讨论激酶：为什么它们在生命和药物设计中如此重要，它们长什么样，以及有哪些数据资源可用？",
        )
        text = text.replace(
            "Finally, we select a set of kinases which will be analyzed in the forthcoming talktorials **T024**-**T028** with respect to their similarity, the goal being to gain insight into potential off-target effects.",
            "最后，我们选择一组激酶，这些激酶将在接下来的教程 **T024**-**T028** 中分析它们的相似性，目的是深入了解潜在的脱靶效应。",
        )
        text = text.replace("- Kinases in a nutshell\n    - The human kinome\n    - Kinase structures and important motifs\n- Kinase resources\n    - Kinase structures and related information\n    - Bioactivity data\n- Kinase similarity: Off-targets and promiscuous binding\n- Kinase dataset compilation",
            "- 激酶概述\n    - 人类激酶组\n    - 激酶结构和重要基序\n- 激酶资源\n    - 激酶结构及相关信息\n    - 生物活性数据\n- 激酶相似性：脱靶与混杂结合\n- 激酶数据集编制")
        text = text.replace("- Define the kinases of interest", "- 定义目标激酶")

    # T024
    elif "T024" in filename:
        text = text.replace("# T024 · Kinase similarity: Sequence", "# T024 · 激酶相似性：序列")
        text = text.replace(
            "In this talktorial, we investigate sequence similarity for kinases of interest. KLIFS API is used to retrieve the $85$ residues of the pocket sequence for each kinase. ",
            "在本教程中，我们研究目标激酶的序列相似性。使用 KLIFS API 检索每个激酶的结合口袋序列的 $85$ 个残基。",
        )
        text = text.replace(
            "Two similarity measures are implemented:",
            "实现了两种相似性度量：",
        )
        text = text.replace(
            "  1. Sequence identity, i.e., the similarity which is based on character-wise discrepancy.\n   2. Sequence similarity, i.e., the similarity which is based on a substitution matrix, thus, reflecting similarities between amino acids.",
            "  1. 序列一致性（Sequence identity），即基于字符差异的相似性。\n   2. 序列相似性（Sequence similarity），即基于替换矩阵的相似性，从而反映氨基酸之间的相似性。",
        )
        text = text.replace("_Note_: We focus on similarities between orthosteric kinase binding sites; similarities to allosteric binding sites are not covered.",
            "_注意_：我们关注的是正构激酶结合位点之间的相似性；不涉及变构结合位点的相似性。")
        text = text.replace("* Kinase dataset\n* Kinase similarity descriptor: Sequence\n    * Identity score\n    * Substitution score\n* From similarity matrix to distance matrix",
            "* 激酶数据集\n* 激酶相似性描述符：序列\n    * 一致性分数\n    * 替换分数\n* 从相似性矩阵到距离矩阵")
        text = text.replace("* Define the kinases of interest\n* Retrieve sequences from KLIFS\n* Sequence similarity\n    * Identity score\n    * Substitution score\n* Kinase similarity\n  * Visualize similarity as kinase matrix\n  * Save kinase similarity matrix\n* Kinase distance matrix\n  * Save kinase distance matrix",
            "* 定义目标激酶\n* 从 KLIFS 检索序列\n* 序列相似性\n    * 一致性分数\n    * 替换分数\n* 激酶相似性\n  * 将相似性可视化为激酶矩阵\n  * 保存激酶相似性矩阵\n* 激酶距离矩阵\n  * 保存激酶距离矩阵")

    # T025
    elif "T025" in filename:
        text = text.replace("# T025 · Kinase similarity: Kinase pocket (KiSSim fingerprint)", "# T025 · 激酶相似性：激酶结合口袋（KiSSim 指纹）")
        text = text.replace(
            "We will assess the similarity between a set of kinases from a structural point of view using the [KiSSim](https://kissim.readthedocs.io/en/latest/) fingerprint. This fingerprint describes the physicochemical and spatial properties in structurally resolved kinases.",
            "我们将使用 [KiSSim](https://kissim.readthedocs.io/en/latest/) 指纹从结构角度评估一组激酶之间的相似性。该指纹描述了结构解析激酶中的物理化学和空间性质。",
        )
        text = text.replace("_Note_: We focus on similarities between orthosteric kinase binding sites; similarities to allosteric binding sites are not covered.",
            "_注意_：我们关注的是正构激酶结合位点之间的相似性；不涉及变构结合位点的相似性。")
        text = text.replace("* Kinase dataset\n* Kinase similarity descriptor: Kinase pockets (KiSSim fingerprint)\n* Fetching KLIFS data with `opencadd.databases.klifs`",
            "* 激酶数据集\n* 激酶相似性描述符：激酶结合口袋（KiSSim 指纹）\n* 使用 `opencadd.databases.klifs` 获取 KLIFS 数据")
        text = text.replace("* Define the kinases of interest\n* Retrieve and preprocess data\n    * Set up a remote KLIFS session\n    * Fetch all structures describing these kinases\n    * Filter structures\n* Show kinase coverage\n* Calculate KiSSim fingerprints\n* Compare structures\n* Map structure to kinase distance matrix\n* Save kinase distance matrix",
            "* 定义目标激酶\n* 检索和预处理数据\n    * 设置远程 KLIFS 会话\n    * 获取描述这些激酶的所有结构\n    * 筛选结构\n* 显示激酶覆盖度\n* 计算 KiSSim 指纹\n* 比较结构\n* 将结构映射到激酶距离矩阵\n* 保存激酶距离矩阵")

    # T026
    elif "T026" in filename:
        text = text.replace("# T026 · Kinase similarity: Interaction fingerprints", "# T026 · 激酶相似性：相互作用指纹")
        text = text.replace(
            "We will assess the similarity between a set of kinases based on detected protein-ligand interactions in available complex structures. The [KLIFS](https://klifs.net/) interaction fingerprint (IFP), which describes the interactions seen in a structurally resolved kinase-ligand complex, will be used in this exercise.",
            "我们将基于可用复合物结构中检测到的蛋白质-配体相互作用来评估一组激酶之间的相似性。本练习将使用 [KLIFS](https://klifs.net/) 相互作用指纹（IFP），它描述了结构解析的激酶-配体复合物中观察到的相互作用。",
        )
        text = text.replace("_Note_: We focus on similarities between orthosteric kinase binding sites; similarities to allosteric binding sites are not covered.",
            "_注意_：我们关注的是正构激酶结合位点之间的相似性；不涉及变构结合位点的相似性。")
        text = text.replace("* Kinase dataset\n* Kinase similarity descriptor: KLIFS interaction fingerprint\n* Fetching KLIFS data with `opencadd.databases.klifs`",
            "* 激酶数据集\n* 激酶相似性描述符：KLIFS 相互作用指纹\n* 使用 `opencadd.databases.klifs` 获取 KLIFS 数据")
        text = text.replace("* Define the kinases of interest\n* Retrieve and preprocess data\n    * Set up a remote KLIFS session\n    * Fetch all structures describing these kinases\n    * Filter structures\n    * Fetch the structures' IFPs (if available)\n    * Merge structural and IFP data\n* Show kinase coverage\n* Compare structures\n    * Prepare IFPs as `numpy` array\n    * Calculate pairwise Jaccard distances\n* Map structure to kinase distance matrix\n* Save kinase distance matrix",
            "* 定义目标激酶\n* 检索和预处理数据\n    * 设置远程 KLIFS 会话\n    * 获取描述这些激酶的所有结构\n    * 筛选结构\n    * 获取结构的 IFP（如可用）\n    * 合并结构和 IFP 数据\n* 显示激酶覆盖度\n* 比较结构\n    * 将 IFP 准备为 `numpy` 数组\n    * 计算成对 Jaccard 距离\n* 将结构映射到激酶距离矩阵\n* 保存激酶距离矩阵")

    # T027
    elif "T027" in filename:
        text = text.replace("# T027 · Kinase similarity: Ligand profile", "# T027 · 激酶相似性：配体谱")
        text = text.replace(
            "The aim of this talktorial is to investigate kinase similarity through ligand profiling data (ChEMBL29). In the context of drug design, the following assumption is often made: if a compound was tested active on two different kinases, it is suspected that these two kinases may have some degree of similarity. We will use this assumption in this talktorial. The concept of kinase promiscuity is also covered.",
            "本教程的目标是通过配体 profiling 数据（ChEMBL29）研究激酶相似性。在药物设计的背景下，通常有以下假设：如果一个化合物在两个不同激酶上被测试为活性，那么这两个激酶可能具有一定程度的相似性。在本教程中，我们将使用这个假设。同时也涵盖激酶混杂性的概念。",
        )
        text = text.replace("* Kinase dataset\n* Bioactivity data\n* Kinase similarity descriptor: Ligand profile\n    * Kinase similarity\n    * Kinase promiscuity\n* From similarity matrix to distance matrix",
            "* 激酶数据集\n* 生物活性数据\n* 激酶相似性描述符：配体谱\n    * 激酶相似性\n    * 激酶混杂性\n* 从相似性矩阵到距离矩阵")
        text = text.replace("* Define the kinases of interest\n* Retrieve the data\n* Preprocess the data\n    * Hit or non-hit\n* Kinase promiscuity\n* Kinase similarity\n    * Visualize similarity as kinase matrix\n    * Save kinase similarity matrix\n* Kinase distance matrix\n    * Save kinase distance matrix",
            "* 定义目标激酶\n* 检索数据\n* 预处理数据\n    * Hit 或非 hit\n* 激酶混杂性\n* 激酶相似性\n    * 将相似性可视化为激酶矩阵\n    * 保存激酶相似性矩阵\n* 激酶距离矩阵\n    * 保存激酶距离矩阵")

    # T028
    elif "T028" in filename:
        text = text.replace("# T028 · Kinase similarity: Compare different perspectives", "# T028 · 激酶相似性：不同视角比较")
        text = text.replace(
            "We will compare different perspectives on kinase similarity, which were discussed in detail in previous notebooks:",
            "我们将比较激酶相似性的不同视角，这些视角在之前的教程中已有详细讨论：",
        )
        text = text.replace("* **Talktorial T024**: Kinase pocket sequences (KLIFS pocket sequences)\n* **Talktorial T025**: Kinase pocket structures (KiSSim fingerprint based on KLIFS pocket residues)\n* **Talktorial T026**: Kinase-ligand interaction profiles (KLIFS IFPs based on KLIFS pocket residues)\n* **Talktorial T027**: Ligand profiling data (using ChEMBL29 bioactivity data)",
            "* **教程 T024**：激酶结合口袋序列（KLIFS 结合口袋序列）\n* **教程 T025**：激酶结合口袋结构（基于 KLIFS 结合口袋残基的 KiSSim 指纹）\n* **教程 T026**：激酶-配体相互作用谱（基于 KLIFS 结合口袋残基的 KLIFS IFP）\n* **教程 T027**：配体 profiling 数据（使用 ChEMBL29 生物活性数据）")
        text = text.replace("_Note_: We focus only on similarities between orthosteric kinase binding sites; similarities to allosteric binding sites are not covered (T027 is an exception since the profiling data does not distinguish between binding sites).",
            "_注意_：我们只关注正构激酶结合位点之间的相似性；不涉及变构结合位点的相似性（T027 是个例外，因为 profiling 数据不区分结合位点）。")
        text = text.replace("* Kinase dataset\n* Kinase similarity descriptor (considering 4 different methods)\n* Distance matrix conditions",
            "* 激酶数据集\n* 激酶相似性描述符（考虑 4 种不同方法）\n* 距离矩阵条件")
        text = text.replace("* Load kinase similarity and distance matrices\n* Distance matrix conditions\n* Visualize similarity for example perspective\n  * Visualize kinase similarity matrix as heatmap\n  * Visualize similarity as dendrogram\n* Visualize similarities from the four different perspectives\n  * Preprocess distance matrices\n    * Normalize matrices\n    * Define kinase order\n  * Visualize kinase similarities\n  * Analysis of results",
            "* 加载激酶相似性和距离矩阵\n* 距离矩阵条件\n* 可视化示例视角的相似性\n  * 将激酶相似性矩阵可视化为热图\n  * 将相似性可视化为树状图\n* 可视化四个不同视角的相似性\n  * 预处理距离矩阵\n    * 归一化矩阵\n    * 定义激酶顺序\n  * 可视化激酶相似性\n  * 结果分析")

    # T033
    elif "T033" in filename:
        text = text.replace("# T033 · Molecular representations", "# T033 · 分子表示")
        text = text.replace("__Talktorial T033__: This talktorial is part of the TeachOpenCADD pipeline described in the TeachOpenCADD publication, consisting of Talktorials T033 to T038.",
            "__教程 T033__：本教程是 TeachOpenCADD 论文中描述的 TeachOpenCADD 流程的一部分，包含教程 T033 至 T038。")
        text = text.replace(
            "In this talktorial, we conduct the groundwork for the deep learning talktorials. Specifically, we learn about molecular representations and find that representing a molecule in a computer is not a trivial task. Different representations come with their specific implications and (dis-)advantages.",
            "在本教程中，我们为深度学习教程奠定基础。具体来说，我们学习分子表示，并发现用计算机表示分子并不是一件简单的任务。不同的表示方式有其特定的含义和（优）缺点。",
        )
        text = text.replace("* What is a molecule?\n* Molecular representations\n* Molecular Representations for Humans\n* Computer-age molecular representations",
            "* 什么是分子？\n* 分子表示\n* 面向人类的分子表示\n* 计算机时代的分子表示")
        text = text.replace("* Conformers\n* Molecular graphs\n* Fingerprints",
            "* 构象\n* 分子图\n* 指纹")
        text = text.replace("[Talktorial T017]", "[教程 T017]")
        text = text.replace("[Talktorial T008]", "[教程 T008]")

    # T034
    elif "T034" in filename:
        text = text.replace("# T034 · RNN-based molecular property prediction", "# T034 · 基于 RNN 的分子性质预测")
        text = text.replace(
            "Molecular representation by a SMILES string paved the way for applying natural language processing techniques to a broad range of molecule-related tasks. In this talktorial we will dive deeper into one of these techniques: recurrent neural networks (RNNs). First, we will describe different RNN architectures and then apply them to a regression task using the QM9 dataset.",
            "用 SMILES 字符串表示分子为将自然语言处理技术应用于广泛的分子相关任务铺平了道路。在本教程中，我们将深入研究其中一种技术：循环神经网络（RNN）。首先，我们将描述不同的 RNN 架构，然后将它们应用于使用 QM9 数据集的回归任务。",
        )
        text = text.replace("* Molecules as text\n    * Tokenization and one-hot encoding\n* Recurrent Neural Networks (RNNs)\n    * Vanilla RNN\n    * Training an RNN\n    * Vanishing gradients\n    * Gated Recurrent Unit",
            "* 作为文本的分子\n    * 分词和独热编码\n* 循环神经网络（RNN）\n    * 基础 RNN\n    * 训练 RNN\n    * 梯度消失\n    * 门控循环单元")
        text = text.replace("* Dataset\n* Model definition\n* Training\n* Evaluation",
            "* 数据集\n* 模型定义\n* 训练\n* 评估")

    # T035
    elif "T035" in filename:
        text = text.replace("# T035 · GNN-based molecular property prediction", "# T035 · 基于 GNN 的分子性质预测")
        text = text.replace(
            "In this tutorial, we will first explain the basic concepts of graph neural networks (GNNs) and present two different GNN architectures. We apply our neural networks to the `QM9` dataset, which is a dataset containing small molecules. With this dataset, we want to predict molecular properties. We demonstrate how to train and evaluate GNNs step by step using PyTorch Geometric.",
            "在本教程中，我们将首先解释图神经网络（GNN）的基本概念，并介绍两种不同的 GNN 架构。我们将神经网络应用于 `QM9` 数据集，该数据集包含小分子。使用这个数据集，我们想要预测分子性质。我们将演示如何使用 PyTorch Geometric 逐步训练和评估 GNN。",
        )
        text = text.replace("* GNN Tasks\n* Message Passing\n* Graph Convolutional Network (GCN)\n* Graph Isomorphism Network (GIN)\n* Training a GNN\n* Applications of GNNs",
            "* GNN 任务\n* 消息传递\n* 图卷积网络（GCN）\n* 图同构网络（GIN）\n* 训练 GNN\n* GNN 的应用")
        text = text.replace("* Dataset\n* Defining a GCN and GIN\n* Training a GNN\n* Evaluating the model",
            "* 数据集\n* 定义 GCN 和 GIN\n* 训练 GNN\n* 评估模型")

    # T036
    elif "T036" in filename:
        text = text.replace("# T036 · An introduction to E(3)-invariant graph neural networks", "# T036 · E(3)等变图神经网络导论")
        text = text.replace(
            "This talktorial is supposed to serve as an introduction to machine learning on point cloud representations of molecules with 3D conformer information, i.e., molecular graphs that are embedded into Euclidean space (see **Talktorial 033**). You will learn why Euclidean equivariance and invariance are important properties of neural networks (NNs) that take point clouds as input and learn how to implement and train such NNs. In addition to discussing them in theory, this notebook also aims to demonstrate the shortcomings of plain graph neural networks (GNNs) when working with point clouds practically.",
            "本教程旨在介绍对具有 3D 构象信息的点云分子表示（即嵌入欧几里得空间的分子图，参见**教程 033**）进行机器学习。您将学习为什么欧几里得等变性和不变性是以点云为输入的神经网络（NN）的重要特性，并学习如何实现和训练这样的 NN。除了理论讨论外，本教程还旨在实际演示普通图神经网络（GNN）在处理点云时的不足。",
        )
        text = text.replace("* Why 3D coordinates?\n* Representing molecules as point clouds\n* Equivariance and Invariance in euclidean space and why we care\n* How to construct $\text{E}(n)$-invariant and equivariant models\n* The QM9 dataset",
            "* 为什么需要 3D 坐标？\n* 将分子表示为点云\n* 欧几里得空间中的等变性和不变性及其重要性\n* 如何构建 $\text{E}(n)$ 不变和等变模型\n* QM9 数据集")
        text = text.replace("* Visualization of point clouds\n* Set up and inspect the QM9 dataset\n  * Preprocessing\n  * Atomic number distribution and point cloud size\n  * Data split, distribution of regression target electronic spatial extent\n* Model implementation\n  * Plain \"naive Euclidean\" GNN\n  * Demo: Plain GNNs are not E(3)-invariant\n  * EGNN model\n  * Demo: Our EGNN is E(3)-invariant\n* Training and evaluation\n  * Setup\n  * Training the EGNN\n  * Training the plain GNN\n  * Comparative evaluation",
            '* 点云可视化\n* 设置和检查 QM9 数据集\n  * 预处理\n  * 原子序数分布和点云大小\n  * 数据划分、回归目标电子空间范围分布\n* 模型实现\n  * 普通"朴素欧几里得"GNN\n  * 演示：普通 GNN 不具有 E(3) 不变性\n  * EGNN 模型\n  * 演示：我们的 EGNN 具有 E(3) 不变性\n* 训练与评估\n  * 设置\n  * 训练 EGNN\n  * 训练普通 GNN\n  * 对比评估')

    # T037
    elif "T037" in filename:
        text = text.replace("# T037 · Uncertainty estimation", "# T037 · 不确定性估计")
        text = text.replace(
            "*The predictive setting (and the model class) used in this talktorial is adapted from __Talktorial T022__.*",
            "*本教程中使用的预测设置（和模型类别）改编自__教程 T022__。*",
        )
        text = text.replace(
            "Researchers often focus on prediction quality alone. However, when applying a predictive model, researchers are also interested in how certain they can be in a specific prediction. Estimating and providing such information is the goal of uncertainty estimation. In this talktorial, we discuss some common methodologies and showcase ensemble methods in practice.",
            "研究人员通常只关注预测质量。然而，在应用预测模型时，研究人员也对特定预测的置信程度感兴趣。估计并提供此类信息是不确定性估计的目标。在本教程中，我们讨论一些常见的方法论，并展示集成方法在实践中的应用。",
        )
        text = text.replace("* Why a model can't and shouldn't be certain\n* Calibration\n* Methods overview\n    * Single deterministic methods\n    * Ensemble methods\n    * Test-time data augmentation",
            "* 为什么模型不能也不应该确定\n* 校准\n* 方法概述\n    * 单一确定性方法\n    * 集成方法\n    * 测试时数据增强")
        text = text.replace("* Data\n* Model\n    * Training\n    * Evaluation\n* Ensembles - Training a model multiple times\n    * Coverage of confidence intervals\n    * Calibration\n    * Ranking-based evaluation\n* Bagging ensemble - Training a model with varying data\n    * Ranking-based evaluation\n* Test-time data augmentation",
            "* 数据\n* 模型\n    * 训练\n    * 评估\n* 集成 - 多次训练模型\n    * 置信区间覆盖\n    * 校准\n    * 基于排名的评估\n* Bagging 集成 - 使用变化数据训练模型\n    * 基于排名的评估\n* 测试时数据增强")

    # T038
    elif "T038" in filename:
        text = text.replace("# T038 · Protein Ligand Interaction Prediction", "# T038 · 蛋白质-配体相互作用预测")
        text = text.replace(
            "The goal of this talktorial is to introduce the reader to the field of protein-ligand interaction prediction using graph neural networks (GNNs). GNNs are especially useful for representing structural data such as proteins and chemical molecules (ligands) to a deep learning model. In this talktorial, we will show how to train a deep learning model to predict interactions between proteins and ligands.",
            "本教程的目标是向读者介绍使用图神经网络（GNN）进行蛋白质-配体相互作用预测的领域。GNN 对于向深度学习模型表示结构数据（如蛋白质和化学分子（配体））特别有用。在本教程中，我们将展示如何训练深度学习模型来预测蛋白质和配体之间的相互作用。",
        )
        text = text.replace("* Relevance of protein-ligand interaction prediction\n* Workflow\n* Biological background - proteins as graphs\n* Technical background\n  * Graph Isomorphism Networks\n  * Binary Cross Entropy Loss",
            "* 蛋白质-配体相互作用预测的相关性\n* 工作流程\n* 生物学背景 - 作为图的蛋白质\n* 技术背景\n  * 图同构网络\n  * 二元交叉熵损失")
        text = text.replace("* Compute graph representations\n  * Ligands to graphs\n  * Proteins to graphs\n* Data Storages\n  * Data points\n  * Data set\n  * Data module\n* Network\n  * GNN encoder\n  * Full model\n* Training routine",
            "* 计算图表示\n  * 配体到图\n  * 蛋白质到图\n* 数据存储\n  * 数据点\n  * 数据集\n  * 数据模块\n* 网络\n  * GNN 编码器\n  * 完整模型\n* 训练流程")

    return text


def main():
    base_src = "/Users/new/PycharmProjects/opencadd/teachopencadd/teachopencadd/talktorials"
    base_dst = "/Users/new/PycharmProjects/opencadd/teachopencadd-zh/teachopencadd/教程"

    mapping = [
        ("T012_query_klifs", "T012_KLIFS查询"),
        ("T013_query_pubchem", "T013_PubChem查询"),
        ("T014_binding_site_detection", "T014_结合位点检测"),
        ("T015_protein_ligand_docking", "T015_蛋白质-配体对接"),
        ("T016_protein_ligand_interactions", "T016_蛋白质-配体相互作用"),
        ("T017_advanced_nglview_usage", "T017_高级NGLView使用"),
        ("T018_automated_cadd_pipeline", "T018_自动化CADD流程"),
        ("T019_md_simulation", "T019_分子动力学模拟"),
        ("T020_md_analysis", "T020_分子动力学分析"),
        ("T021_one_hot_encoding", "T021_独热编码"),
        ("T022_ligand_based_screening_neural_network", "T022_基于配体的神经网络筛选"),
        ("T023_what_is_a_kinase", "T023_什么是激酶"),
        ("T024_kinase_similarity_sequence", "T024_激酶序列相似性"),
        ("T025_kinase_similarity_kissim", "T025_激酶Kissim相似性"),
        ("T026_kinase_similarity_ifp", "T026_激酶相互作用指纹相似性"),
        ("T027_kinase_similarity_ligand_profile", "T027_激酶配体谱相似性"),
        ("T028_kinase_similarity_compare_perspectives", "T028_激酶相似性比较视角"),
        ("T033_molecular_representations", "T033_分子表示"),
        ("T034_recurrent_neural_networks", "T034_循环神经网络"),
        ("T035_graph_neural_networks", "T035_图神经网络"),
        ("T036_e3_equivariant_gnn", "T036_E3等变图神经网络"),
        ("T037_uncertainty_estimation", "T037_不确定性估计"),
        ("T038_protein_ligand_interaction_prediction", "T038_蛋白质-配体相互作用预测"),
    ]

    for src_dir, dst_dir in mapping:
        source = os.path.join(base_src, src_dir, "README.md")
        target = os.path.join(base_dst, dst_dir, "README.md")
        if os.path.exists(source):
            translate_file(source, target)
        else:
            print(f"✗ Source not found: {source}")

    print("\nAll translations complete!")


if __name__ == "__main__":
    main()
