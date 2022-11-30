# Scholarly Publications and Dataset Evidence for the Human Reference Atlas

Experts from 17 consortia are collaborating on the Human Reference Atlas (HRA) which aims to map the human body at single cell resolution. To bridge across scales—from the meter size human body to the micrometer size single-cell level—organ experts are constructing anatomical structures, cell types plus biomarkers (ASCT+B) tables and associated spatial reference objects that capture major anatomical structures, the cell types commonly located in these, and the biomarkers (gene, protein, lipid, metabolites) used to characterize cell types. The tables also capture 88 ORCID IDs of expert authors and reviewers and 456 paper DOIs at the organ level and the cell type level. In a parallel effort, high quality single-cell experimental datasets used in the construction of the atlas are linked to the elements in the ASCT+B tables. A total of 620 datasets for 58 organs, with 1,174 unique cell types, and associated gene expression values for the 47,000 genes that have been processed and linked to the 33 organs covered in the ASCT+B tables in November 2022. The scholarly papers and experimental datasets provide scientific evidence for the existence of nodes and linkages in the HRA. We analyze the amount and type of evidence for subgraphs of the HRA, and visualize the network of experts collaborating on the HRA. Study results are important for (1) understanding and communicating the quality (and remaining uncertainty) of the HRA, (2) planning future tissue data collection (e.g., to collect a minimum amount of experimental data that maximally improves HRA coverage and quality), and (3) inviting other leading experts to serve as authors or reviewers of the evolving atlas.

This repository provides easy access to data and code used in the study. 

It is structured in the following way:
* [code](https://github.com/cns-iu/hra-evidence-issi-2023-supporting-information/tree/main/code)
  * wos data queries and data processing
    * [author_per_paper.sql](code/wos_data_queries_and_data_processing/author_per_paper.sql)
    * [clean_funding_name.py](code/wos_data_queries_and_data_processing/clean_funding_name.py)
    * [count_grant_agencies_per_organ.sql](code/wos_data_queries_and_data_processing/count_grant_agencies_per_organ.sql)
    * [country_per_paper.sql](code/wos_data_queries_and_data_processing/country_per_paper.sql)
  * vicky_code
    * [analysis.ipynb](https://github.com/cns-iu/hra-evidence-issi-2023-supporting-information/blob/main/code/vicky_code/analysis.ipynb)
* [data](https://github.com/cns-iu/hra-evidence-issi-2023-supporting-information/tree/main/data)
  * [33_organs.csv](data/33_organs.csv)
  * [grant_agencies.csv](data/grant_agencies.csv)
  * [experimental_data_references.csv](data/experimental_data_references.csv)
  * [Count_of_unique_papers_associated_with_experimental_data_per_organ.csv](data/Count_of_unique_papers_associated_with_experimental_data_per_organ.csv)
  * [HRA_XML](https://github.com/cns-iu/hra-evidence-issi-2023-supporting-information/tree/main/data/HRA_XML)

## Code
In data collection and data preprocessing, CSV data should be downloaded in `Data` and SQL data should be collected based on specific requirements. They should be put into corresponding folders. Use `Clean_funding_name.py` to preprocess funding agencies.

In data analysis, code can be applied to make statistics of data. Use `country_per_paper.sql` to count the number of papers per each country, use `count_grant_agencies_per_organ.sql` to count the number of funding agencies per organ, use `author_per_paper.sql` to count the number of authors per paper. 

In data visualization, the geospatial layout and bimodel network were created by Gephi using the above results csv data. PFnet is applied to Sci2 Tool, freely available at https://sci2.cns.iu.edu.

Code used to compute the number of cells per cell type per organ is available at https://github.com/hubmapconsortium/tissue-bar-graphs. 

## Data
* `33_organs.csv` contains the 33 organs planned for the next HRA release.

* `Grant_agencies.csv` contains the funding agencies which support papers tagged with 33 HRA specific organ tags in 2018-2022 publication year, selected from WoS core collections.

* `experimental_data_references.csv` contains experimental data references, including data, data sources, paper DOIs and organs.

* `Count_of_unique_papers_associated_with_experimental_data_per_organ.csv` contains count of unique papers associated with experimental data per organ.  Experimental datasets cover 57 organs; for 19 of these there exist ASCT+B tables. Note that PBMC corresponds to the Blood ASCT+B table, and several papers are listed for multiple organs, e.g., paper titled “Tabula Sapiens: An Atlas of Single-Cell Gene Expression” is cited for 34 organs.

* `HRA_XML` contains released information for HRA (in XML format), collected from [HuBMAP CCF PORTAL](https://hubmapconsortium.github.io/ccf/index.html)
 Anatomical Structures, Cell Types and Biomarkers (ASCT+B) Tables
  * `2D Reference Functional Tissue Unit (FTU) Library`
  * `3D Reference Object Library`
  * `Organ Mapping Antibody Panels (OMAPs)`

## Data Sources
Web of Science data was retrieved from [CADRE](https://cadre.iu.edu/about-cadre).

Human Reference Atlas data was retrieved from the [CCF Portal](https://hubmapconsortium.github.io/ccf/). 

Azimuth publication data and experimental data were downloaded from the [Azimuth portal](https://azimuth.hubmapconsortium.org).

Experimental data was retrieved from [HuBMAP Portal](https://portal.hubmapconsortium.org), [CxG Portal](https://cellxgene.cziscience.com), [NeMO](https://nemoarchive.org), and [GTEx](https://gtexportal.org). 

## Licenses
All code used here is [MIT licensed](https://opensource.org/licenses/MIT).

The Human Reference Atlas data is [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) licensed. 

## Credits
Kong is funded by the China Scholarship Council. The Human Reference Atlas is research has been funded by the NIH Common Fund through the Office of Strategic Coordination/Office of the NIH Director under awards OT2OD033756 and OT2OD026671, by the Cellular Senescence Network (SenNet) Consortium through the Consortium Organization and Data Coordinating Center (CODCC) under award number U24CA268108, and by the NIDDK Kidney Precision Medicine Project grant U2CDK114886.
