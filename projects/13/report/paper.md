---
title: 'Integration of visualisation tools for disease mechanisms and their annotations: UniProt, Nightingale and the MINERVA Platform'
title_short: 'Integration of UniProt, Nightingale and Disease Maps'
tags:
  - visualisation
  - protein databases
  - UniProt
  - Nightingale
  - Disease Maps
authors:
  - name: Thijs van Beek
    orcid: 0000-0000-0000-0000
    affiliation: 1
  - name: David Hoksza
    orcid: 0000-0003-4679-0557
    affiliation: 2
  - name: Piotr Gawron
    orcid: 0000-0002-9328-8052
    affiliation: 1
  - name: Marek Ostaszewski
    affiliation: 1
    orcid: 0000-0003-1473-370X
  - name: Xavier Watkins
    orcid: 0000-0001-9327-5887
    affiliation: 3
affiliations:
  - name: LCSB, University of Luxembourg, Luxembourg
    index: 1
  - name: Charles University, Prague, Czech Republic
    index: 2
  - name: European Bioinformatics Institute, Canbridge, UK
    index: 3
date: 11 November 2021
bibliography: paper.bib
event: lamola2021
biohackathon_name: "BioHackathon Europe"
biohackathon_url:   "https://biohackathon-europe.org"
biohackathon_location: "La Mola, Spain 2021"
group: Logic programming group
---

# Abstract

We will integrate resources enabling the visual exploration of the mechanisms of diseases across different levels - gene/protein annotation, 
protein-protein interaction, pathways and genomic variation. Disease maps (disease-maps.org) provide a standardised, diagrammatic way to encode mechanisms of 
human diseases (https://biohackrxiv.org/gmbjv/), with COVID-19 as a prime example (https://fairdomhub.org/projects/190). 
We aim to integrate these maps with data from the recently developed UniProt Alzheimer’s disease portal and COVID-19 platform (https://diseases.uniprot.org, https://covid-19.uniprot.org).

We will work with UniProt and the MINERVA Platform (minerva-web.lcsb.uni.lu), ELIXIR resources which we have already started 
to bring together (https://github.com/xwatkins/disease-map-portal). In this project, we will use the 
Nightingale library (https://ebi-webcomponents.github.io/nightingale/#/), a suite of standardised modular data visualisation components, 
including the protein feature annotation viewer ProtVista, a protein interaction visualisation and a 3D viewer Mol* (https://molstar.org). 
We will embed diagrams visualised by MINERVA with corresponding protein-level visualisations, and explore the sequence annotation visualisation 
to MINERVA via its plugin architecture. Finally, this will allow us to define standards for the data exchange for Nightingale components, 
to make them easily usable by other ELIXIR resources.
