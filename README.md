General information about the CLUS-RM widgets
--------------------------------------------------

This is the repository with the source code of the CLUS-RM widgets for ClowdFlows [5]. This code allows using CLUS-RM algorithm, its extensions and the redescription set optimization procedures through the ClowdFlows tool (available online: http://www.clowdflows.org/ ). 

The package contains the code for three widgets: a) the Generate RM Settings widget, b) the CLUS-RM widget and c) Display redescription file widget.

This package was created with the assistance of dr. Tomislav Lipić to allow easy user access and usage of the CLUS-RM library (https://github.com/matmih/CLUS-RM-library). The CLUS-RM library was developed as a result of scientific work of Matej Mihelčić (matmih1@gmail.com) in the Data Mining field called Redescription mining [7]. 

CLUS-RM widgets for ClowdFlows implementation
----------------------------------------------

- Matej Mihelčić, Ruđer Bošković Institute, Zagreb, Croatia, matmih1@gmail.com
- dr. Tomislav Lipić, Ruđer Bošković Institute, Zagreb, Croatia

About CLUS-RM library
----------------------

The CLUS-RM redescription mining algorithm [1,2], is based on Predictive Clustering Trees [6]. It also contains the following algorithm extensions: a) using random forest of Predictive Clustering Trees [2] to produce redescriptions, b) using conjunctive refinement procedure [3] to increase redescription accuracy, c) use constraint-based redescrition mining [4] which allows adding user-defined constraints on attributes that build redescription queries. The constraint-based setting allows three modes of targeted redescription exploration.

The CLUS-RM library also incorporates two modes of redescription set optimization: a) optimization by redescription exchange [1,2] and b) optimization by redescription extraction [3]. 

The source code of the CLUS-RM library is available online: https://github.com/matmih/CLUS-RM-library


Original publications:
----------------------

1. M. Mihelčić, S. Džeroski, N. Lavrač, and T. Šmuc, “Redescription mining with multi-target
predictive clustering trees,” in Proceedings of the 4th International Workshop, New
Frontiers in Mining Complex Patterns, NFMCP 2015, Held in conjunction with ECMLPKDD
2015, Porto, Portugal, September 7, 2015, Revised Selected Papers, M. Ceci, C.
Loglisci, G. Manco, E. Masciari, and Z. W. Ras, Eds. Cham: Springer International
Publishing, 2016, pp. 125–143, isbn: 978-3-319-39315-5. doi: 10.1007/978-3-319-
39315-5_9. [Online]. Available: http://dx.doi.org/10.1007/978-3-319-39315-5_9.

2. M. Mihelčić, S. Džeroski, N. Lavrač, and T. Šmuc, “Redescription mining augmented with
random forest of multi-target predictive clustering trees,” Journal of Intelligent Information
Systems, pp. 1–34, 2017, In press, issn: 1573-7675. doi: 10.1007/s10844-017-0448-5. [Online]. Available: http://dx.doi.org/10.1007/s10844-017-0448-5.

3. M. Mihelčić, S. Džeroski, N. Lavrač, and T. Šmuc, “A framework for redescription set
construction,” Expert Systems with Applications, vol. 68, pp. 196–215, 2017, issn: 0957-4174. doi: http://doi.org/10.1016/j.
eswa.2016.10.012. [Online]. Available: http://www.sciencedirect.com/science/
article/pii/S0957417416305437.

4. M. Mihelčić, G. Šimić, M. Babić Leko, N. Lavrač, S. Džeroski, T. Šmuc, and for the
Alzheimer’s Disease Neuroimaging Initiative, “Using redescription mining to relate
clinical and biological characteristics of cognitively impaired and alzheimer’s disease
patients,” PLOS ONE, vol. 12, no. 10, pp. 1–35, 2017, doi: 10.1371/journal.pone.0187364. [Online]. Available: https://doi.org/
10.1371/journal.pone.0187364.
--------------------------------------------------------------------------------------

Related publications: 
---------------------
5. J. Kranjc, V. Podpecan, and N. Lavrac, “Clowdflows: A cloud based scientific workflow
platform.,” in ECML/PKDD (2), P. A. Flach, T. D. Bie, and N. Cristianini,
Eds., ser. Lecture Notes in Computer Science, vol. 7524, Springer, 2012, pp. 816–819, isbn: 978-3-642-33485-6.

6. H. Blockeel, “Top-down induction of first order logical decision trees,” PhD thesis,
Katholieke Universiteit Leuven, Belgium, 1998.

7. N. Ramakrishnan, D. Kumar, B. Mishra, M. Potts, and R. F. Helm, “Turning
CARTwheels: An alternating algorithm for mining redescriptions,” in Proceedings
of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and
Data Mining, Seattle, Washington, USA, 2004, pp. 266–275. doi: 10.1145/1014052.1014083. [Online]. Available: http://doi.acm.org/10.1145/1014052.1014083.











