---
title: 'Bioschemas data validation project report'
tags:
  - FAIR
  - RDF
  - Schema.org
  - Bioschemas
authors:
  - name: Alban Gaignard
    orcid: 0000-0002-3597-8557
    affiliation: 1
  

affiliations:
 - name: Nantes Université, CNRS, INSERM, l’institut du thorax, F-44000 Nantes, France 
   index: 1

date: 11 November 2021
bibliography: paper.bib
authors_short: Bioschemas team
group: Bioschemas team
event: BioHackathon Europe 2021
---

# Introduction

Bioschemas profiles are community agreed standards leveraging Schema.org for Life Sciences. They specify the minimal, recommended, optional metadata as well as cardinality and expected reuse of controlled vocabulary. Conformance to these profiles are vital to support harvesting by initiatives such as OpenAIRE.

However, biologists and bioinformaticians may find annotating their resources to be too technically complex and time-consuming without the availability of user-friendly tools. 
Multiple initiatives are emerging to provide support tools. FAIR-checker is a web-application, supported by Knowledge Graphs, aimed at providing developers with technical hints to better implement FAIR principles, and provide minimal Bioschemas markup for better findability. 

Within the Bioschemas Community, there have been efforts to develop a reusable scraper (BMUSE) to reliably retrieve embedded markup in websites, as well as several validation frameworks to test the conformance of retrieved markup against a stated Bioschemas Profile. These include the TeSS Validator, CTSA/NIH Data Discovery Engine, the ELIXIR JSON Schema validator, and Bioschemas Validata. These frameworks have tried a variety of underlying technologies, including JSON-Schema, ShEx, and SHACL.

The goal of this is project is to leverage Bioschemas community profiles and gather community efforts on metadata validation to provide: scraping and validation tools, basic statistics on live deploys metadata quality (per profile), tools to help the crowd-sourced Bioschemas markup curation.

# Achievements 
### Generic validation tool  
The validation is performed as follows: 
1. RDF data extraction from web pages (both static and dynamic) 
2. For each typed entity (Schema.org or Bioschemas specific types) a SHACL(https://www.w3.org/TR/shacl/) shape is generated based on template. 
3. The SHACL shape is evaluated against the extracted RDF data, producing warnings for missing recommended properties, and errors for missing minimal properties.

Several heterogeneous resources were validated (12  profiles): 
- Scholarly Articles ()
- Computational Workflows
- Computational Tools
- Studies
- Genes
- Molecular Entities
- Protein
- Sequence annotations
- Sequence ranges
- Datasets
- Persons
- Training material

### Improved metadata quality for several data sources
- Bgee (https://bgee.org): issues have been raised in the exposed markup, they will be fixed in the next release
- MetaNetX (https://www.metanetx.org): 1,066,990 compound (MolecularEntity) pages
- PED (https://proteinensemble.org): Adding in links for publications using DOIs/PubMedID 
- Issues identified in both Profiles and Resources for persons, workflows, studies, etc. 


# Future work
1. Generate SHACL constraints from JSON serialization (Data Discovery Engine)
2. Determine the validation profile from dct:conformsTo
3. Suggest a relevent profile 


# Jupyter notebooks, GitHub repositories and data repositories

https://github.com/BioSchemas/bioschemas-validation
This repository hosts a command line tool aimed at validating Bioschemas markup from a web page. 


# Acknowledgements

We wish to thank the organizers and supporters of the Biohackathon Europe 2021 for offering the venue for improving Bioschemas community efforts.

# References

Leave thise section blank, create a paper.bib with all your references.
