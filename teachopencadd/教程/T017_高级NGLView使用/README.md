# T017 · 高级NGLView使用

**注：**此教程是 TeachOpenCADD 的一部分，该平台旨在教授领域特定技能，并提供可作为研究项目起点的流程模板。

作者：

- Jaime Rodríguez-Guerra, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)
- Dominique Sydow, 2021, [Volkamer实验室, 夏里特医学院](https://volkamerlab.org/)


## 本教程的目标

[NGLView](http://nglviewer.org/nglview/latest/) 是一个强大的Jupyter小部件，可让您在笔记本中以3D交互视图展示分子结构！它同时支持单一构象和轨迹，以及丰富的表示形式。在本教程中，我们将介绍如何在不同场景下使用它，从简单案例到更复杂的案例。

### _理论_ 部分内容

* NGL与NGLView
* NGL对象模型与术语

### _实践_ 部分内容

* 第一步：确保一切正常！
    * 尝试交互式控件
* 基本API使用：
    * 使用PDB标识符展示结构
    * 使用本地文件展示结构
    * 保存控件状态为截图以供离线查看
    * 自定义表示形式
    * 通过选择控制表示形式
    * NMR与多模型结构
    * 加载多个结构
    * 显示和隐藏组件
* 高级使用：
    * 自定义配色方案和表示形式
    * 在选定原子上添加几何对象
    * 创建交互式界面
    * 访问JavaScript层
* 故障排除技巧：
    * 检查您正在使用的Jupyter平台
    * 如何正确安装`nglview`

### References

* **NGL manuscript**: Rose *et al.*, <i>Nucl Acids Res.</i> (2015), <b>43</b> (W1), W576-W579 (https://academic.oup.com/nar/article/43/W1/W576/2467902)
* [NGL documentation](http://nglviewer.org/ngl/api/) and [repository](https://github.com/nglviewer/ngl)
* **NGLView manuscript**: Nguyen *et al.*, <i>Bioinformatics</i> (2018), <b>34</b> (7), 1241-1242 (https://academic.oup.com/bioinformatics/article/34/7/1241/4721781)
* [NGLView documentation](http://nglviewer.org/nglview/latest/) and [repository](https://github.com/nglviewer/nglview)
* [NGLView Q&A issues](https://github.com/nglviewer/nglview/issues?q=is%3Aissue+label%3AQ%26A). A lot of hidden knowledge in these conversations!
* [NGLView examples](https://github.com/nglviewer/nglview/tree/master/examples)
* [Jupyter Widgets (IPyWidgets)](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20Basics.html)
