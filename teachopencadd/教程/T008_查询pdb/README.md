# T008 ·蛋白质数据表集：蛋白质数据库（DBC）



## 这次音乐节的目的

 在这个基座中，我们为下一个基座确定了基础，我们将为 EGFR 生成基础的综合疗效团。因此，我们： (i)从DBC数据库中获取足够特定条款的所有 EGFR DBC ID（例如，高比例的配体结合结构）， (ii)There is the best of the best， (iii)调整所有结构，以及 (iv)提取并保存配体以用于下一次课程。

 # 理论内容

- 蛋白数据表（） - 使用 Python 包咨询ZB ' biotite '和' pypDB ' 

 # 实用内容

* 选择查询蛋白 * 获取查询蛋白质的DBC条目数 * 寻找足够的特定条款的DBC条款 * 选择有最高比例的DBC条目 * 从顶部结构中获取配体的元数据 * 绘制顶部配体分子 * 创建蛋白质-配体 ID 对 * 对DBC结构并提出分配体



* * 注：** 此基座是 TeachOpenCADD 的一部分，该平台在教学特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Anja Georgi，CADD研讨会，2017年，Charité/FU柏林 - Majid Vafadar，CADD研讨会，2018年，Charité/FU柏林 - Jaime Rodríguez-Guerra，[Amsteramer Lab，Charité] (https：//volkamerab.org/） - Dominique Sydow，[Amsteramer Lab，Charité]（https：//volkamerab.org/)

 __Talkorial T008__：本次演讲是第一篇 TeachOpenCADD 出版物（[_J. Cheminform._（2019），**11**，1-7] (https：//jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0351-x）)中描述的 TeachOpenCADD 管道的一部分，由演讲 T001-T010 组成。

 # 引用

* 蛋白质数据库 ([PDB网站] (http：//www.rcsb.org/） * ' pypDB ' Python包 （[_Bioinformatics_（2016），**1**，159-60]（https：//academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv543）; [文档]（http：//www.wgilpin.com/pypdb_docs/html/）） * ' biotite ' Python包（[_BMC Bioinformatics_（2018），**19**]（https：//bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2367-z）; [documination]（https：//www.biotite-python.org/）） * 与Python包“opencadd”进行分子叠加（[repository]（https：//github.com/volkamerlab/opencadd）) 