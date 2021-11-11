# Project 13: Integration of visualisation tools for disease mechanisms and their annotations

## Abstract

We will integrate resources enabling the visual exploration of the mechanisms of diseases across different levels - gene/protein annotation, protein-protein interaction, pathways and genomic variation. Disease maps (disease-maps.org) provide a standardised, diagrammatic way to encode mechanisms of human diseases (https://biohackrxiv.org/gmbjv/), with COVID-19 as a prime example (https://fairdomhub.org/projects/190). We aim to integrate these maps with data from the recently developed UniProt Alzheimer’s disease portal and COVID-19 platform (https://diseases.uniprot.org, https://covid-19.uniprot.org).

We will work with UniProt and the MINERVA Platform (minerva-web.lcsb.uni.lu), ELIXIR resources which we have already started to bring together (https://github.com/xwatkins/disease-map-portal). In this project, we will use the Nightingale library (https://ebi-webcomponents.github.io/nightingale/#/), a suite of standardised modular data visualisation components, including the protein feature annotation viewer ProtVista, a protein interaction visualisation and a 3D viewer Mol* (https://molstar.org). We will embed diagrams visualised by MINERVA with corresponding protein-level visualisations, and explore the sequence annotation visualisation to MINERVA via its plugin architecture. Finally, this will allow us to define standards for the data exchange for Nightingale components, to make them easily usable by other ELIXIR resources.

## Topics

Covid-19
Data Platform
Interoperability Platform
Rare Disease
Tools Platform

**Project Number:** 13

**EasyChair Number:** 20

The active paper.md report as a BioHackrXiv draft publication can be found [here](https://github.com/mjostaszewski/BH21-BioHAckrXiv-paper/blob/main/report/paper.md)

## Team

### Lead(s)

Xavier Watkins, xwatkins@ebi.ac.uk, corresponding author
Marek Ostaszewski, marek.ostaszewski@uni.lu

## Expected outcomes

- A MINERVA-based disease map visualisation embedded in the Disease Maps portal (during the BioHackathon)
- Protein structure visualisation coupled to the visualised diagram (during the BioHackathon)
- Protein sequence visualisation for the MINERVA Platform as a plugin (draft: during the BioHackathon, stable version: 3 months later)
- Standardised representation of information exchange between the components (draft: during the BioHackathon, stable version: 6 months later)

## Expected audience

We invite participants in the knowledge of:
- web development, in particular JavaScript/TypeScript
- graphics design and/or visual analytics

We expect to have at least six people participating from ELIXIR-Hub (3), ELIXIR-LU (2) and ELIXIR-CZ (1).

**Number of expected hacking days**: 4

