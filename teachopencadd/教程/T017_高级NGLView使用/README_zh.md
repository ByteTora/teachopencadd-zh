# T017 ·高级NGLview使用

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Jaime Rodríguez-Guerra，2021年，[Amsteramer Lab，Charité] (https：//volkamerab.org/） - Dominique Sydow，2021年，[Amplamer Lab，Charité]（https：//volkamerab.org/)

 ## 本期脱口秀的目标

[NGLView] (http：//nglviewer.org/nglview/latest/)是一个功能强大的Inflyter小部件，允许您以3D交互式视图在笔记本中显示分子结构！它支持单一的形态和轨迹，以及大量的表示。在这篇谈话文章中，我们将讨论如何在不同的场景中使用它，从简单的情况到更复杂的情况。

 # * 理论 * 内容

* NGL和NGL View * NGL对象模型和术语

 # * 实用 * 中的内容

* 第一步：确保一切正常！ * 尝试交互式控件 * 基本API使用： * 使用其DBC标识符显示结构 * 使用本地文件显示结构 * 将小部件状态保存为屏幕截图以供离线查看 * 自定义表示 * 通过选择控制表示 * 核磁共振和多模型结构 * 加载多个结构 * 显示和隐藏组件 * 高级使用： * 自定义着色方案和表示 * 在选定原子处添加几何对象 * 创建交互式界面 * 访问JavaScript层 * 故障排除提示： * 检查您正在哪个Deliveryter平台工作 * 如何安装“nglview”，正确的方法

 # 参考文献

* **NGL手稿 **：Rose * 等人 *，<i>核酸资源</i>（2015），<b>43</b>（W1），W576-W579（https：//academic.oup.com/nar/article/43/W1/W576/2467902） * [NGL文档] (http：//nglviewer.org/ngl/api/）和[存储库]（https：//github.com/nglviewer/ngl） * ** NGL查看手稿 **：Nguyen * 等人 *，<i>生物信息学</i>（2018），<b>34</b>（7），1241-1242（https：//academic.oup.com/bioinformatics/article/34/7/1241/4721781） * [NGLView文档]（http：//nglviewer.org/nglview/latest/）和[存储库]（https：//github.com/nglviewer/nglview） * [NGL查看问答问题]（https：github.com/nglviewer/nglview/issues? q=is%3Aissue+label%3AQ%26A）。这些对话中隐藏了很多知识！ * [NGLView示例]（https：//github.com/nglviewer/nglview/Tree/master/examples） * [Deliveryter Widgets（IPyWidgets）]（https：//ipyWidgets.readthedocs.io/en/stable/examples/Widget%20Basics.html) 