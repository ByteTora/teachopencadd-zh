# 模板文档目录

在此添加包含模板的任意路径，相对于
`conf.py` 文件所在目录。
它们会在内置模板文件之后被复制，
因此名为 "page.html" 的文件会覆盖内置的 "page.html"。

此文件夹的路径在 Sphinx `conf.py` 文件的以下一行中设置：
```python
html_static_path = ['_templates']
```

## 添加到本目录的文件示例
* 标准页面（如 `page.html` 或 `layout.html`）的 HTML 扩展
