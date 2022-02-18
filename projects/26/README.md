# Project 26: Ranking Algorithm for Dataset Search Platforms

## Abstract

With the fast Increasing volumes of dataset being generated, routines for searching and discovering datasets are becoming more and more important and essential components for open science and efficient reuse of data.

Although different paradigms exist to encourage dataset sharing and searching, for example FAIR Data Point and Google Dataset Search, it is still by far not as advanced as document search, particularly considering the lack of semantics during search and poor ranking due to very limited clues for ranking in the metadata. Within the European Joint Programme on Rare Diseases (EJP-RD) the FAIR Data Point is a key technology that will be used for discovery of appropriate clinical resources.  As such, it is important to address this critical limitation.

To address the challenge of enabling more effective ranking, we propose developing a ranking algorithm to help users more easily find the most relevant dataset to their query. We plan to implement and exercise this algorithm on a FAIR Data Point instance as it is open sourced.

## Topics

Compute Platfrom
Containers
Data Platform
industry
Machine learning
Metabolomics
Rare Disease
EJP-RD
Tools Platform

**Project Number:** 26



**EasyChair Number:** 43

## Team

**EJP-RD Team Members:**  
   * Peter-Bram ‘t Hoen
   * Mark Wilkinson
   * Rajaram Kaliyaperumal
   * Pablo Alarcon Moreno

### Lead(s)

Peter-Bram ‘t Hoen, Peter-Bram.tHoen@radboudumc.nl

XiaoFeng Liao, xiaofeng.liao@radboudumc.nl

### Members
Mark Wilkinson, mark.wilkinson@upm.es

Michel Dumontier, michel.dumontier@maastrichtuniversity.nl

Rajaram Kaliyaperumal, r.kaliyaperumal@lumc.nl

Vincent Emonet, vincent.emonet@maastrichtuniversity.nl

Pablo Alarcon Moreno, pabloalarconmoreno@gmail.com

## Expected outcomes

Form an interest group.
Develop an initial algorithm.
Deploy a prototype.

## Expected audience

Machine Learning
Semantic Web Technology
RDF
Script
Life Science

**Number of expected hacking days**: 4

## Documentation

### Scripts

Install the dependencies:

```bash
pip install -r requirements.txt
```

Example script to get HCLS metadata for the Bio2RDF SPARQL endpoint from the Shapes of You triplestore:

```bash
python3 scripts/get_metadata.py
```

Example script to compute HCLS metadata for the Drugbank graph in the Bio2RDF SPARQL endpoint :

```bash
python3 scripts/construct_metadata.py
```

### API

Start the API locally after installing the dependencies:

```bash
uvicorn api.main:app --reload
```

Or start it with docker:

```bash
docker-compose up
```

Access it on http://localhost:8000/docs

