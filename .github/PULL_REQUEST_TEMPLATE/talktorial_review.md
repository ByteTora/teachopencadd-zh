<!-- Talktorial 评审模板 -->
<!-- 非常感谢你帮助我们改进/扩展 TeachOpenCADD！ -->

# Talktorial 评审

本 PR 模板适用于添加新 talktorial 以及扩展现有 talktorial（如果你做的是后者，请针对你的扩展内容回答以下各条目）。

## 详情

* Talktorial ID：XXX
* 标题：XXX
* 原作者：XXX
* 评审人：XXX
* 评审日期：DD-MM-YYYY

## 内容

* 一句话摘要：XXX
* 潜在标签或分类（例如机器学习、小分子、在线 API）：XXX
* 执行耗时（约）：
* [ ] 我使用了 [talktorial 模板](https://github.com/volkamerlab/teachopencadd/blob/master/teachopencadd/talktorials/T000_template/talktorial.ipynb)，并遵循了其中的内容与格式建议
* [ ] _包_ 必须是开源的，并且应可从 `conda-forge` 安装。如果你正在向 TeachOpenCADD 环境添加新包，请检查已安装的包是否能实现相同功能；如果不能，请留一句说明为什么需要新增。如果新包不在 `conda-forge` 上，请在此列出它们及其预期用途。
  * `package1`：已在 TeachOpenCADD 中
  * `package2` (conda-forge)：我将其用于 XXX
  * `package3` (仅 pip)：我将其用于 XXX
* [ ] _数据_ 必须可公开访问，最好可通过 webserver 访问或通过 URL 下载。请列出你使用的数据资源及访问方式：
  * 资源 1（链接到资源）：通过 XXX 访问
  * 资源 2（链接到资源）：通过 XXX 访问

## 内容风格

* [ ] 如适用，talktorial 包含对其他 talktorial 的交叉引用
* [ ] 目录反映了 talktorial 的叙事线；#、##、### 标题的顺序正确
* [ ] URL 使用有意义的词进行链接，而不是直接粘贴 URL 或链接诸如 `here`（此处）之类的词。
* [ ] 我已对 notebook 进行拼写检查
* [ ] 图片分辨率足够高质量渲染，同时又不至于_太重_。
* [ ] 所有图形都有描述
* [ ] Markdown 单元格内容与代码单元格输出保持一致（凡是讨论结果之处）
* [ ] 我已检查单元格输出不是异常地长（这也适用于 `DataFrames`）
* [ ] 格式在 Sphinx 渲染下显示正确（粗体、斜体、图形位置）

## 代码风格

* [ ] 变量和函数名遵循 snake_case 规则（例如 `a_variable_name` 而非 `aVariableName`）
* [ ] 间距遵循 PEP8（如有需要，对代码单元格运行 Black）
* [ ] 每行代码不超过 99 个字符（运行 `black-nb -l 99`）
* [ ] 注释有用且位置得当
* [ ] 没有不 Pythonic 的惯用法，如 `for i in range(len(list))`（见讲义）
* [ ] 所有第三方依赖都列在 notebook 顶部
* [ ] 我已将所有在 markdown 单元格中被引用的代码单元格输出标记了 `# NBVAL_CHECK_OUTPUT` 标签
* [ ] 我已识别出代码重构 / 有用函数的潜在候选
* [ ] 所有 `import ...` 行都在顶部的（实践部分）单元格中，按标准库 / 第三方包 / 我们自己的（`teachopencadd.*`）排序
* [ ] 我使用了绝对路径而非相对路径
  ```python
  HERE = Path(_dh[-1])
  DATA = HERE / "data"
  ```

## 网站
我们在 TeachOpenCADD 网站 (https://projects.volkamerlab.org/teachopencadd/) 上展示我们的 talktorial，因此还需要检查该 Jupyter notebook 在那里是否渲染良好。

* [ ] 如果本 PR 添加了一个新 talktorial，请遵循以下步骤：
  * [ ] 将你的 talktorial 添加到 talktorial 完整列表 [这里](https://github.com/volkamerlab/teachopencadd/blob/master/docs/all_talktorials.rst)（末尾）。
  * [ ] 将你的 talktorial 添加到一个或多个集合 [这里](https://github.com/volkamerlab/teachopencadd/blob/master/docs/talktorials.rst)。或者在你的 PR 中提出一个新的集合章节。
  * [ ] 通过在目录 `teachopencadd/docs/talktorials` 内运行 `python generate_nblinks.py` 来添加你 talktorial 的 `nblink` 文件。
  * [ ] 请按照 [这里](https://github.com/volkamerlab/teachopencadd/tree/master/docs) 的说明编译网站。
* [ ] 检查本 PR 的 talktorial 渲染效果。
* [ ] 你的 talktorial 是否列在 [talktorial 列表](https://projects.volkamerlab.org/teachopencadd/all_talktorials.html) 中？
* [ ] 你的 talktorial 是否列在 [talktorial 集合](https://projects.volkamerlab.org/teachopencadd/talktorials.html) 中？
  * [ ] 按照 [这些说明](https://github.com/volkamerlab/teachopencadd/discussions/185) 为集视图中你的 talktorial 添加一张图片。
