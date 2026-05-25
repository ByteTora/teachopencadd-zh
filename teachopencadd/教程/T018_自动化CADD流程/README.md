# T018 ·用于潜在客户优化的自动化管道

* * 注意：** 这篇谈话文章是TeachOpenCADD的一部分，该平台旨在教授特定领域的技能并提供管道模板作为研究项目的起点。

作者：

- Armin Ariamajd，2021年，CADD 2021年研讨会，Charité/Freie University Berlin - 梅兰妮·沃格尔（Melanie Vogel），2021年，CADD研讨会2021年，Charité/Freie University柏林 - Andrea Thomamer，2021年，[Thomamer实验室，Charité] (https：//volkamerab.org/） - Dominique Sydow，2021年，[Amplamer Lab，Charité]（https：//volkamerab.org/） - Corey Taylor，2021年，[Amsteramer Lab，Charité]（https：//volkamerab.org/)

 ## 本期脱口秀的目标

在本期谈话中，我们将学习如何开发 ** 自动化的基于结构的虚拟筛选管道 **。 该管道 ** 特别适合药物发现项目的命中扩展和先导优化 ** 阶段，其中有前途的配体（即初始命中或先导化合物）需要进行结构修饰，以提高其对目标蛋白的结合亲和力和选择性。因此，管道的一般架构可以总结如下（图1）。

* ** 输入 ** * 目标蛋白结构和有前途的配体（例如铅或命中化合物），以及需要执行的过程的规范。 * ** 流程 ** * 检测给定蛋白质结构的最可药物结合位点。 * 寻找配体的衍生物和结构类似物，并根据药物相似性对其进行过滤。 * 使用所选类似物对检测到的蛋白质结合位点进行对接计算。 * 分析和虚拟化每种类似物的预测蛋白质-配体相互作用和结合模式。 * ** 输出 ** * 针对亲和力、选择性和药物相似性进行了优化的新配体结构。

 ! [管道概述] (images/sb_vs_pipeline.png)

* 图1*：基于自动结构的虚拟筛选管道的一般架构。

 <a id='#Contents-in-Theory'></a>

# [*Theory*]中的内容（#Theory）

- [药物设计管道] (#药物设计管道） - [蛋白质结合位点]（#蛋白质结合位点） - [化学相似性搜索]（#Chemical-similarity-search） - [分子对接]（#分子对接） - [蛋白质配体相互作用]（#蛋白质配体相互作用） - [对接结果的目视检查]（#对接结果的目视检查)

[评论]：<>（如果您更改标题，则必须更新目录标签，以使交叉引用在我们的网站上发挥作用！）

 <a id='Contents-in-Practical'></a>

# [*Practical*]中的内容（#Practical）

- [虚拟筛选管道轮廓] (#虚拟筛选管道轮廓） - [创建新项目]（#创建新项目） - [输入数据]（#The-put-data） - [处理输入蛋白质数据]（#处理输入蛋白质数据） - [处理输入配体数据]（#处理输入配体数据） - [结合点检测]（#结合点检测） - [配体相似性搜索]（#配体相似性-搜索） - [对接计算]（#对接计算） - [蛋白质配体相互作用分析]（#蛋白质配体相互作用分析） - [选择最佳模拟物]（#选择最佳模拟物） - [将碎片放在一起：一个全自动化的管道]（#将碎片放在一起：-A-完全自动化的管道)

[评论]：<>（如果您更改标题，则必须更新目录标签，以使交叉引用在我们的网站上发挥作用！）

 # 参考文献

* 注意：* 由于每个类别中都有大量引用，默认情况下详细信息是隐藏的。

<details>

<summary>单击此处查看完整的参考文献列表。</summary>

* **TeachOpenCADD教学平台 ** 1.关于 *TeachOpenCADD* 计算机辅助药物设计教学平台的期刊文章：[D. Sydow * 等人 *，*J. Cheminform。* **2019年 **，11，29。] (https：//doi.org/10.1186/s13321-019-0351-x） 2. [*TeachOpenCADD* 网站]（https：//projects.volkamerab.org/teachopencadd/index.html），位于[Amsteramer Lab]（https：//volkamerab.org/) 3.这篇脱口秀的灵感来自 *TeachOpenCADD* 脱口秀T013-T017

* 药物设计流程** 4.药物设计书籍：[*G.Klebe*，*Drug Design*，Springer，**2013**.](https://doi.org/10.1007/978-3-642-17907-5) 5.关于药物发现早期阶段的综述文章：[J.P.Hughes*等人*，*Br.J.Pharmacol.*2011**，162.1239-1249.](https://doi.org/10.1111/j.1476-5381.2010.01127.x) 6.关于计算药物设计的综述文章：[G.Sliwoski*等人*，*Pharmacol。Rev.*2014**，66,334-395.](https://doi.org/10.1124/pr.112.007336) 7.关于计算药物发现的综述文章：[S.P.Leelananda*等人*，*Beilstein J.Org.化学.*2016**，12,2694-2718.](https://doi.org/10.3762/bjoc.12.267) 8.审查关于建立虚拟筛选管道的自由软件的文章：[E.Glaab，*Brief。生物信息。*2016**，17352-366.](https://doi.org/10.1093/bib/bbv037) 9.评论关于自动药物发现的文章：[G.Schneider，*NAT。药品发现版本*2018**，17，97-113.](https://doi.org/10.1038/nrd.2017.232) 10.关于基于结构的药物发现的综述文章：[M.Batool*等人*，*Int.J.Mol.科学*2019**，20,2783.](https://doi.org/10.3390/ijms20112783)

* 结合部位检测** 11.关于结合位点的预测和分析的书的章节：[A.Volkamer*等人*，*应用化学信息学*，威利，**2018**，283-311.](https://doi.org/10.1002/9783527806539.ch6g)页 12.使用*DoGSiteScorer*进行结合部位和可药性预测的期刊文章：[A.Volkamer*et al.*，*J.Chem.信息型号。*2012**，*52*，360-372.](https://doi.org/10.1021/ci200454v) 13.描述*ProteinsPlus*门户网站的期刊文章：[R.Fahrroll fes*et al.*，*Nucleic Res.*2017**，45，W337-W343.](https://doi.org/10.1093/nar/gkx333) 14.[*ProteinsPlus*网站](https://proteins.plus/)，及其*DoGSiteScorer*[REST-API](https://proteins.plus/help/dogsite_rest)的使用信息 15.*TeachOpenCADD*结合位点检测讲师：[讲师T014](https://projects.volkamerlab.org/teachopencadd/talktorials/T014_binding_site_detection.html) 16.*TeachOpenCADD*关于查询在线api网络服务的讲解：[讲解T011](https://projects.volkamerlab.org/teachopencadd/talktorials/T011_query_online_api_webservices.html)

* 化学相似性搜索与分子指纹** 17.关于药物化学中分子相似性的综述文章：[G.Maggiora*等人*，*J.Med.化学。*2014**，57岁，3186-3204.](https://doi.org/10.1021/jm401411z) 18.关于分子指纹相似性搜索的综述文章：[A.Cereto-Massague*et al.*，*方法*2015**，71，58-63.](https://doi.org/10.1016/j.ymeth.2014.08.005) 19.回顾关于虚拟筛选中的分子指纹的文章：[I.Muegge*等人*，*Expert Opin。毒品迪斯科。**2016**，11,137-148.](https://doi.org/10.1517/17460441.2016.1117070) 20.关于扩展连接指纹(ECFP)的期刊文章：[D.Rogers*et al.*，*J.Chem.信息型号。*2010**，50742-754.](https://doi.org/10.1021/ci100050t) 21.关于*Morgan*算法的期刊文章：[H.L.Morgan，*J.Chem.文档.*2002**，5,107-113.](https://doi.org/10.1021/c160017a018) 22.关于分子接入系统(MACCS)密钥指纹的期刊文章：[J.L.杜兰特*等人*，J.信息电脑。SCI。**2002**，42,1273-1280.](https://doi.org/10.1021/ci010132r) 23.描述*PubChem*网络服务的最新发展的期刊文章：[S.Kim*et al.*，*Nucleic Res.*2019**，47，D1102-D1109.](https://doi.org/10.1093/nar/gky1033) 24.[*PubChem*网站](https://pubchem.ncbi.nlm.nih.gov/)，及其[APIs](https://pubchemdocs.ncbi.nlm.nih.gov/programmatic-access)使用信息 25.描述*PubChem*‘S[自定义子结构fingerprint](https://ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem_fingerprints.pdf)和[*田本*相似性measure](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-016-0163-1)]在其相似性搜索引擎中使用。 26.*TeachOpenCADD*关于化合物相似性的谈话指南：[Talktal T004](https://projects.volkamerlab.org/teachopencadd/talktorials/T004_compound_similarity.html) 27.*TeachOpEnCADD*从*PubChem*获取数据的讲演指南：[Talktal T013](https://projects.volkamerlab.org/teachopencadd/talktorials/T013_query_pubchem.html) * 化学类毒品** 28.关于类药物的综述文章：[O.Ursu*et al.，*Wiley Interativep.牧师：电脑。摩尔。科学文献*2011**，1760-781.](https://doi.org/10.1002/wcms.52) 29.关于类毒品的社论评论文章：[*NAT。药品发现修订版*2007**，6853.](https://doi.org/10.1038/nrd2460) 30.关于类药物背后的物理和化学概念的综述文章：[M.Athar*等人*，*Phys.SCI。版本*2019**，4,20180101.](https://doi.org/10.1515/psr-2018-0101) 31.关于可用于评估药物相似性的在线工具的综述文章：[C.Y.Jia*等人*，*Drug Discov.今天*2020**，25,248-258.](https://doi.org/10.1016/j.drudis.2019.10.014) 32.关于利平斯基规则5的期刊文章：[C.A.利平斯基*等人*，*药物递送高级版本*，23，3-25.](https://doi.org/10.1016/S0169-409X(96)00423-1) 33.20年后重新评估5规则的简短回顾：[A·穆拉德，*NAT。药品发现版本。*2018**，17,777。](https://doi.org/10.1038/nrd.2018.197) 34.关于Druglike(QED)方法的定量估计的期刊文章：[G.Bickerton*等人*，*NAT.化学*2012**，4(2)，90-98.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3524573/) 35.[*RDKit*documentations](https://www.rdkit.org/docs/source/rdkit.Chem.QED.html)关于计算QED. 

* 分子对接** 36.分子对接算法综述：[X.Y.Meng*et al.*，*Curr.电脑。辅助药物说明书*2011**，7,146-157.](https://doi.org/10.2174/157340911795677602) 37.关于用于分子对接的不同软件的评论文章：[N.S.Pagadala*et al.*，*BiPhys.版本*2017**，9，91-102.](https://doi.org/10.1007/s12551-016-0247-1) 38.关于不同对接计划和评分功能的评估和比较的综述文章：[G.L.Warren*et al*，*J.Med.化学.*2006**，49,5912-5931.](https://doi.org/10.1021/jm050362n) 39.关于评估一组不同的蛋白质-配体复合体上的十个对接计划的综述文章：[Z.Wang*et al.*，*Phys.化学。化学。Phys.*2016**，18,12964-12975.](https://doi.org/10.1039/C6CP01555G) 40.描述Smina对接计划及其评分功能的期刊文章：[D.R.Kos*et al.*，*J.Chem.信息型号。*2013**，53,1893-1904.](https://doi.org/10.1021/ci300604z) 41.[*OpenBabel*documentation](http://openbabel.org/wiki/Main_Page) 42.[*smina*documentation](https://sourceforge.net/projects/smina/) 43.*TeachOpenCADD*关于蛋白质-配体对接的讲演指南：[讲演指南T015](https://projects.volkamerlab.org/teachopencadd/talktorials/T015_protein_ligand_docking.html) * 蛋白质-配体相互作用** 44.关于蛋白质-配体相互作用的综述文章：[X.Du*et al.*，*Int.J.Mol.科学*2016**，17,144.](https://doi.org/10.3390/ijms17020144) 45.分析可用的蛋白质-配体复合体结构中不同蛋白质-配体相互作用的类型和频率的期刊文章：[R.Ferreira de Freitas*et al.*，*Med.化学。逗号。*2017**，8,1970-1981.](https://doi.org/10.1039/C7MD00381A) 46.描述*plip*算法的期刊文章：[S.Salentin*et al.*，*Nucic Ids Res.*2015**，43，W443-447.](https://doi.org/10.1093/nar/gkv315) 47. [*PLIP* 网站] (https：//plip-tool.biotec.tu-dresden.de/plip-web/plip/index） 48. [*PLIP* 文档]（https：//github.com/pharmai/plip） 49. *TeachOpenCADD* 关于蛋白质-配体相互作用的谈话：[谈话T016]（https：//projects.volkamerab.org/teachopencadd/talktorials/T016_蛋白质_ligand_interactions.html)

* ** 对接结果目视检查 ** 50.描述NGLView程序的期刊文章：[H. Nguyen * 等人 *，* 生物信息学 *2018**，34，1241-1242。] (https：//doi.org/10.1093/bioinformatics/btx789） 51. [*NGLView* 文档]（http：//nglviewer.org/nglview/latest/api.html） 52. *TeachOpenCADD* 关于高级NGL查看使用的谈话版：[谈话版T017]（https：//projects.volkamerab.org/teachopencadd/talktorials/T017_advanced_nglview_usage.html) </details> 