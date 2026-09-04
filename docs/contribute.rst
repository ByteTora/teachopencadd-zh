面向贡献者
================

欢迎通过请求新主题、提出想法或参与开发来为本项目做贡献！

- 在我们的 `GitHub 讨论区 <https://github.com/volkamerlab/teachopencadd/discussions>`_ 与管理员和其他 TeachOpenCADD 用户互动！
- 提交新 talktorials（参见 `提交新 talktorials`_）。
- 通过修复 bug 或扩展内容来更新现有 talktorials（参见 `更新 talktorials`_）。
- 帮助我们维护 TeachOpenCADD（参见 `维护 talktorials`_）。


提交新 talktorials
--------------------------

这是一份如何提交新 talktorials 的分步指南。

1. Fork 仓库：https://docs.github.com/en/get-started/quickstart/fork-a-repo

2. 向我们询问你的 talktorial 索引（我们的 notebook 以 T001、T002、… 编号）。

3. Clone 你的 fork::

    git clone git@github.com:your-github-name/teachopencadd.git

4. 进入 clone/下载后的 ``teachopencadd`` 文件夹::

    cd teachopencadd

5. 检出一个新分支，用你的姓名缩写、talktorial 索引和简短标题命名（例如 ``ab-t099-fingerprints``）::

    git checkout -b ab-t099-fingerprints

6. 创建 ``toc-dev`` 环境::

    # Create environment with dependencies
    mamba env create -f devtools/test_env.yml -n toc-dev
    # On MacOS with M1 chip you may need
    CONDA_SUBDIR=osx-64 mamba env create -f devtools/test_env.yml -n toc-dev

    # Activate enviroment
    conda activate toc-dev

    # Pip install teachopencadd in editable mode
    cd ..
    pip install -e teachopencadd
    cd teachopencadd

    # Interact with the talktorials via e.g. Jupyter Lab
    jupyter lab

   如果你向 ``devtools/test_env.yml`` 添加了新依赖，需要重做**第 6 步**。

7. 使用你的 talktorial 索引和短名复制以下模板文件夹（此处示例为 ``T099_fingerprints``::

    cp -r teachopencadd/talktorials/T000_template/ teachopencadd/talktorials/T099_fingerprints

8. 将所有 ``T000_template`` 或 "T000 · Talktorial topic title" 实例替换为你的 talktorial 索引和标题。

   a. ``T099_fingerprints/talktorial.ipynb`` 是 talktorial 模板（`参见此处示例 <https://github.com/volkamerlab/teachopencadd/blob/master/teachopencadd/talktorials/T000_template/talktorial.ipynb>`_），你在其中开发你的新 talktorial。开始前请通读该模板，因为它包含大量关于内容和风格要求的信息。

   b. 你无需担心更新 ``T099_fingerprints/README.md``，因为我们会用 notebook 的前几个部分自动生成这些 README（更多细节见 `维护 talktorials`_）。

   c. 顾名思义，文件夹 ``T099_fingerprints/data/`` 和 ``T099_fingerprints/images/`` 可用于存储输入/输出数据和图片。只要可能，请避免添加文件，改为通过 URL 获取数据/图片。有疑问时请询问我们。

9. 将你的新 talktorial 文件夹骨架推送（push）到你的 GitHub 仓库（将 ``T099_fingerprints`` 和 ``ab-t099-fingerprints`` 替换为你自己的）::

    # Add folder
    git add teachopencadd/talktorials/T099_fingerprints/
    # Commit changes
    git commit -m "T099: Add talktorial folder skeleton"
    # Push changes
    git push origin ab-t099-fingerprints

10. 用我们的 PR 模板创建拉取请求（PR）：

    a. 前往你的 fork ``https://github.com/your-github-name/teachopencadd/pulls`` 并点击 "New pull request"。

    b. 选择以下内容：

       - ``base repository: volkamberlab/teachopencadd`` 且 ``base: master``

       - ``head repository: your-github-name/teachopencadd`` 且 ``compare: ab-t099-fingerprints``

    c. 点击 "Create pull request"。

    d. 当 PR 描述窗口打开时，请将 `本 PR 模板的内容 <https://github.com/volkamerlab/teachopencadd/blob/master/.github/PULL_REQUEST_TEMPLATE/talktorial_review.md>`_ 复制粘贴进去。

11. 通读 PR 描述中的待办事项，如有疑问请与我们沟通。注意：许多条目与我们的维护工作有关（更多细节见 `维护 talktorials`_）。

12. 开始开发你的 talktorials。按照**第 9 步**的流程将你的改动添加到 PR 中。

13. 如需帮助或准备好进行 PR 评审时，请 ping 我们。谢谢！


更新 talktorials
--------------------

这是一份如何更新现有 talktorials 的分步指南。

如果你在某个 talktorial 中发现错误，或希望扩展其中某个 talktorial 的内容，请遵循以下步骤（示例：更新 talktorial ``T002_compound_adme``）：

1. 按照 `提交新 talktorials`_ 中的**第 1-5 步**，fork 并 clone ``teachopencadd`` 仓库，并检出一个新分支，其中**第 2 步**指的是你希望更新的 talktorial 的索引（例如 ``T002_compound_adme``），而你的新分支应取一个描述性名称（例如 ``ab-t002-extend-adme-theory``）。

3. 按照 `提交新 talktorials`_ 中的**第 6 步**设置环境。

2. 将你的新分支推送到你的 GitHub 仓库（将 ``T002_compound_adme`` 和 ``ab-t002-extend-adme-theory`` 替换为你自己的）::

    # Add folder
    git add teachopencadd/talktorials/T002_compound_adme/
    # Commit changes
    git commit -m "T002: Extend ADME theory"
    # Push changes
    git push origin ab-t002-extend-adme-theory

3. 按照 `提交新 talktorials`_ 中的**第 10 和第 11 步**创建 PR。某些 PR 条目可能不适用于你的情况，请使用 ``~``（例如 ``~some bullet point~``）将其删除线标出。

4. 如需帮助或准备好进行 PR 评审时，请 ping 我们。谢谢！


维护 talktorials
-----------------------

这是关于我们 TeachOpenCADD 维护工作的一份概览。

- 我们的`环境文件 <https://github.com/volkamerlab/teachopencadd/tree/master/devtools>`_ 满足所有 TeachOpenCADD talktorials 的依赖。此格式可能会如`此处 <https://github.com/volkamerlab/teachopencadd/discussions/277>`_ 讨论的那样在未来改变。

- 我们的 `GitHub Actions CI 配置文件 <https://github.com/volkamerlab/teachopencadd/blob/master/.github/workflows/ci.yml>`_ 包含：

  - Notebook 测试（``pytest``），检查 notebook 是否能无错运行，以及被 ``# NBVAL_CHECK_OUTPUT`` 标记的单元格在 CI 运行中产生的输出是否与保存在 ``talktorial.ipynb`` 文件中的输出一致。在 ``jobs.test`` 下查看被测的操作系统和 Python 版本。

  - Notebook 格式化（``black-nb``），在 ``jobs.format`` 下查看::

        # Apply formatting to all talktorials
        black-nb -l 99 teachopencadd/talktorials/T*/talktorial.ipynb

  - 自动生成的 README，在 ``jobs.readmes`` 下查看::

        # Autogenerate all talktorials' README
        for path in teachopencadd/talktorials/T*/talktorial.ipynb; do
            python devtools/regenerate_readmes.py --output README.md $path
        done

- 我们的 `TeachOpenCADD 网站 <https://projects.volkamerlab.org/teachopencadd/>`_：

  - 你可以如`我们的文档 README <https://github.com/volkamerlab/teachopencadd/blob/master/docs/README.md>`_ 所述在本地渲染网站（包括你的改动）。

  - 如果你希望添加新内容，请遵循`这些步骤 <https://github.com/volkamerlab/teachopencadd/blob/master/.github/PULL_REQUEST_TEMPLATE/talktorial_review.md#website>`_。

- 我们如本 `讨论帖 <https://github.com/volkamerlab/teachopencadd/discussions/197>`_ 所述发布新的版本。

- 我们的 ``teachopencadd`` 包托管在 ``conda-forge``：https://anaconda.org/conda-forge/teachopencadd

  - 每次我们发布一个新的 GitHub release 时，也需要发布一个新的 ``conda`` release。

  - 关于如何操作的说明，请参考《`"Maintaining packages" <https://conda-forge.org/docs/maintainer/updating_pkgs.html>`_》和`这些笔记 <https://github.com/volkamerlab/teachopencadd/discussions/184>`_，并可向 @dominiquesydow 求助。要发布一个新的 ``conda`` release，你需要更新我们 `teachopencadd feedstock <https://github.com/conda-forge/teachopencadd-feedstock>`_ 中的配方（recipe）。
