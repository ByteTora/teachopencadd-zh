# 静态文档目录

在此添加包含自定义静态文件（例如样式表）的任意路径，
相对于 `conf.py` 文件所在目录。
它们会在内置静态文件之后被复制，
因此名为 "default.css" 的文件会覆盖内置的 "default.css"。

此文件夹的路径在 Sphinx `conf.py` 文件的以下一行中设置：
```python
templates_path = ['_static']
```

## 添加到本目录的文件示例
* 自定义级联样式表（CSS）
* 自定义 JavaScript 代码
* 静态 logo 图片
