# 编译 opencadd 的文档

本项目的文档使用 [Sphinx](http://www.sphinx-doc.org/en/master/) 构建。
编译文档前，请确保已安装 Sphinx 和 ReadTheDocs 主题。


```bash
conda install sphinx sphinx_rtd_theme
```


安装完成后，你可以使用本目录中的 `Makefile` 编译静态 HTML 页面：
```bash
make html
```

编译好的文档位于 `_build` 目录中，通过打开 `index.html` 即可查看（根据所安装的 Sphinx 版本不同，该文件本身可能位于名为 `html/` 的目录内）。
