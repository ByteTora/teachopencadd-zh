安装
==========

.. note::

    我们假设你的电脑上已有一个可用的 ``mamba`` 安装。
    如果并非如此，请参阅其`官方文档 <https://mamba.readthedocs.io/en/latest/installation.html#mamba>`_。

    如果你把 ``mamba`` 安装到了已有的 ``conda`` 环境中，请运行 ``conda config --add channels conda-forge`` 确保已配置 ``conda-forge`` 频道。

    如果你更习惯使用 ``conda``，请在下方说明中用 ``conda`` 替换 ``mamba``。
    请注意，用 ``conda`` 设置 TeachOpenCADD 比用 ``mamba`` 耗时更长。


从 conda 包安装
------------------------------
.. note::

    conda 包目前尚未包含运行深度学习版 talktorials（T033-T038）所需的全部包。

    我们正在处理，新包可用后会尽快发布更新。

1. 为 TeachOpenCADD 创建一个新的 conda 环境::

    # Linux / MacOS
    mamba create -n teachopencadd teachopencadd

    # Windows
    mamba create -n teachopencadd teachopencadd -c conda-forge -c defaults

    # 如果你使用的是搭载 M1 芯片的 MacBook Air 12.4，可能需要：
    CONDA_SUBDIR=osx-64 mamba create -n teachopencadd teachopencadd

2. 激活新环境::

    conda activate teachopencadd

3. 运行 ``teachopencadd -h`` 测试其是否可用。
4. 运行 ``teachopencadd start .`` 用一个包含 TeachOpenCADD 材料的新工作区进行设置。按照终端中打印的说明用 Jupyter Lab 打开材料（Jupyter notebooks）。
   在此示例命令中，你在当前目录 ``.`` 设置工作区；你也可以使用其他任意路径。

你可以随时用 ``jupyter lab /path/to/your/teachopencadd/workspace`` 返回你的 TeachOpenCADD 材料。
如果你需要 Jupyter notebook 的入门介绍，请查看 :ref:`此处推荐的资源 <jupyter_tutorial>`。

从最新开发快照安装
--------------------------------------------

1. 创建一个新的 conda 环境并激活它::

    mamba env create -f https://raw.githubusercontent.com/volkamerlab/TeachOpenCADD/master/devtools/test_env.yml
    conda activate teachopencadd

   注意：如果你在搭载 M1 芯片的 MacOS 上工作且上述命令无法运行（例如出现 "The environment can't be solved, aborting the operation"），请在命令前加上 ``CONDA_SUBDIR=osx-64`` 后重试::

    CONDA_SUBDIR=osx-64 mamba env create -f https://raw.githubusercontent.com/volkamerlab/TeachOpenCADD/master/devtools/test_env.yml
    conda activate teachopencadd

2. 使用`此链接 <https://github.com/volkamerlab/teachopencadd/archive/master.zip>`_ 下载仓库的压缩包。
3. 解压到你选择的位置。
4. 进入该位置。
5. 启动 Jupyter Lab。
6. 双击你想开始的那一课。

第 2 到第 5 步汇总如下。

.. Unix instructions

.. raw:: html

    <details>
    <summary>Linux / MacOS 说明</summary>

.. code-block:: bash

    wget https://github.com/volkamerlab/teachopencadd/archive/master.zip -O teachopencadd.zip
    mkdir -p ~/Documents
    unzip teachopencadd.zip -d ~/Documents
    cd ~/Documents/teachopencadd-master/teachopencadd/talktorials
    jupyter lab

.. raw:: html

    </details>

.. Windows instructions

.. raw:: html

    <details>
    <summary>Windows（PowerShell）说明</summary>

.. code-block::

    wget https://github.com/volkamerlab/teachopencadd/archive/master.zip -O teachopencadd.zip
    mkdir ~/Documents/
    Expand-Archive teachopencadd.zip -d ~/Documents
    cd ~/Documents/teachopencadd-master/teachopencadd/talktorials
    jupyter lab

.. raw:: html

    </details>
