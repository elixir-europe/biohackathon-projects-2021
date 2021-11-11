---
title: 'Bioschemas data harvesting project report'
tags:
  - FAIR
  - RDF
  - Schema.org
  - Bioschemas
authors:
  - name: Alasdair Gray
    orcid: 0000-0002-5711-4872
    affiliation: 1
  - name: Petros Papadopoulos
    orcid: 0000-0002-8110-7576
    affiliation: 1

affiliations:
 - name: Heriot-Watt University, Edinburgh, UK
   index: 1

date: 11 November 2021
bibliography: paper.bib
authors_short: Bioschemas team
group: Bioschemas team
event: BioHackathon Europe 2021
---

# Introduction

# Data Harvesting

Prior to the BioHackathon, we set about harvesting data from as many of the Bioschemas [live deploy sites](https://bioschemas.org/liveDeploys) as possible. At the time of the BioHackathon, there were 70 sites listed, and 137 profile deployments (a site can deploy multiple profiles, e.g. Dataset and DataCatalog). Not all deployments could be harvested since they do not provide sitemaps listing the pages within the site. At the time of the BioHackathon there were 25 sites with sitemaps. Several of these do not list the pages containing data, limiting the amount that could be harvested. 

The list of sites to be harvested were gathered in a GitHub [project board](https://github.com/BioSchemas/bioschemas-data-harvesting/projects/1) so that progress could be tracked. The cards in this board were annotated to state whether the source was known to use a static site deployment (i.e. the markup is embedded in the page source by the server) or dynamic single page application (i.e. the page content is generated client side using Javascript), and also whether they were known to have data content or limited content of Dataset and DataCatalog.

The Bioschemas Markup Scraper and Extractor ([BMUSE](https://github.com/HW-SWeL/BMUSE)) was used for the harvesting of the data. During the harvesting we found a two key issues with BMUSE which arose due to the scale of the data harvest. The first was that errors in the JSON-LD were not correctly identified and logged. The second was a memory limit relating to JSoup which meant that about 24,104 pages were scraped out of the 50,000 in the sitemap file ([BMUSE #82](https://github.com/HW-SWeL/BMUSE/issues/82)). Fixes to these issues were applied resulting in BMUSE v0.5.2 being used for most of the harvesting.

The data harvesting workflow consisted of the following steps:
1. Pick one of the sites to be harvested: priority was given to static sites with data content.
2. For each sitemap in the sitemap index, harvest the content from the source pages.
3. Merge the individual nquad files for each page in the (sub)sitemap into a single nquad file.
4. Load the merged nquad file into the triplestore.
5. Make the merged nquad file available on the web.
6. Update the project [README](https://github.com/BioSchemas/bioschemas-data-harvesting) with details of what had been harvested.

Where issues were found with the source site, these were fedback to the data provider to allow them to revise their markup. For example, it was found that MassBank were including characters in their string values such as `"` that need to be escaped to generate valid JSON-LD ([MassBank-Web #316](https://github.com/MassBank/MassBank-web/issues/316)). 


# Data Analysis


# Discussion and/or Conclusion


# Future work


# Jupyter notebooks, GitHub repositories and data repositories

* GitHub repository: https://github.com/BioSchemas/bioschemas-data-harvesting
* Jupyter Notebooks: https://github.com/BioSchemas/bioschemas-data-harvesting/blob/main/AnalysisQueries.ipynb

# Acknowledgements

We wish to thank the organizers and supporters of the Biohackathon Europe 2021 for offering the venue for improving Bioschemas community efforts.

# References

Leave thise section blank, create a paper.bib with all your references.
