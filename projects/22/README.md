# Project 22: Making bio.tools Fit for Workflows

## Abstract

With 20.000+ entries, bio.tools is a major registry of computational tools in the life sciences. In this BioHackathon project we will address two urgent needs of the platform:

1. Slicing the bio.tools content through specialisation and categorisation, to improve exposure to communities and to present useful content for the users. The main challenge is to summarise relevant information from the wealth of annotation categories in bio.tools and metrics from external sources. Therefore we aim to enrich tools, communities and collections with statistics and metrics that summarise functionality, impact and annotation quality. These metrics and statistics are valuable resources for tool-building communities, scientific domains, individual scientific tool repositories and groups specialising in technical features. With that information, we can identify, calculate and integrate metrics relevant for the bio.tools registry. In addition we will devise a mock-up / alpha version summary stats page within bio.tools.

2. Improving the quality of functional tool annotations, to enable automated composition of individual tools into multi-step computational pipelines or workflows. Currently, tool annotations are often incomplete or imprecise, hampering plug&play workflow composition. We will develop a protocol for improving functional tool annotations in bio.tools. It will be based on 1) selecting reference workflows from workflow repositories and literature, 2) trying to recreate them using bio.tools and the Automated Pipeline Explorer, 3) comparing automatically created and reference workflows, and 4) if necessary revising the tool annotations until recreation succeeds. Workshop participants will perform this process and concurrently develop the tooling and documentation to enable its application to additional workflows after the hackathon.

The outcomes of this project will make software more findable and provide a solid basis for iteratively improving the quality of functional annotations in bio.tools, making it an increasingly powerful source of new fit-for-purpose workflows.

## Topics

Cancer
Containers
Covid-19
Human Copy Number Variation
Intrinsically Disordered Community
Machine learning
Marine Metagenomics
Metabolomics
Microbial Biotechnology
Plant Sciences
Proteomics
Rare Disease
Tools Platform

**Project Number:** 22



**EasyChair Number:** 38

## Team

### Lead(s)

Veit Schwämmle (veits@bmb.sdu.dk)
Hans Ienasescu (hans@bio.tools)
Anna-Lena Lamprecht (a.l.lamprecht@uu.nl)
Magnus Palmblad (n.m.palmblad@lumc.nl)

## Expected outcomes

We expect the following outcomes for subtopic 1 of the project:
* Set of metrics and statistics describing a tool collection, defined in collaboration with CHAOSS and OpenEBench (immediately)
* Overview of annotation quality within specific communities (immediately)
* Overview of variety in terms of tool functionality (immediately)
* Mockup summary stats page (immediately)
* Clear visibility of tools in most prominent scientific fields and categories (1-2 months after workshop)
* Identify relevant areas (domains/communities) lacking tools/annotations/EDAM concepts (3 months after workshop)
* Motivate potential curators by presenting statistics of software in their field (open)
* Manuscript about specialised views in bio.tools (6-12 months after workshop)

We expect the following outcomes for subtopic 2 of the project:
* Improved annotations in bio.tools (immediately)
* Tooling to support the iterative, automated workflow exploration-based annotation revision process (immediately)
* Tooling to create and visualize a bio.tools “compatibility graph” (immediately)
* BioHackrXiv manuscript (3 months after project)
* Journal manuscript (6 months after project)

The code developed during the BioHackathon will reside in a publicly accessible GitHub repository (e.g. under the organisation https://github.com/bio-tools or directly integrated in the source code of https://github.com/bio-tools/biotoolsRegistry).

## Expected audience

Researchers developing software metrics
Statistics experts
OpenEBench developers / data experts
CHAOSS community members
Domain experts in different areas of bioinformatics
Ontology and metadata experts
Developers

**Number of expected hacking days**: 4

## Literature

[Perspectives on automated composition of workflows in the life sciences](https://doi.org/10.12688/f1000research.54159.1)

[APE in the Wild: Automated Exploration of Proteomics Workflows in the bio.tools Registry](https://doi.org/10.1021/acs.jproteome.0c00983)

[Proteomics Software in bio.tools: Coverage and Annotations](https://doi.org/10.1021/acs.jproteome.0c00978)

[Automated workflow composition in mass spectrometry-based proteomics](https://doi.org/10.1093/bioinformatics/bty646)

[One Thousand and One Software for Proteomics: Tales of the Toolmakers of Science](https://doi.org/10.1021/acs.jproteome.9b00219)
