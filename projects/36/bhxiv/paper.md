---
title: 'Mapping GA4GH Phenopackets and OHDSI OMOP for COVID-19 disease epidemics and analytics'
title_short: 'OMOP to Phenopackets for COVID-19 analytics'
tags:
  - FAIR
authors:
  - name: Núria Queralt-Rosinach
    orcid: 0000-0003-0169-8159
    affiliation: 1
  - name: Giovanni Delussu 
    orcid: 0000-0002-1023-2257
    affiliation: 2
  - name: Danielle Welter
    orcid: 0000-0003-1058-2668
    affiliation: 3
affiliations:
  - name: Human Genetics, Leiden University Medical Center, Leiden, Netherlands
    index: 1
  - name: Digital Health Group, CRS4 Center for Advanced Studies, Research and Development in Sardinia, Pula, Italy
    index: 2
  - name: Luxembourg Centre for Systems Biomedicine, University of Luxembourg, Esch-sur-Alzette, Luxembourg
    index: 3
date: 11 November 2021
cito-bibliography: paper.bib
event: Barcelona2021
biohackathon_name: "BioHackathon-Europe"
biohackathon_url:   "https://biohackathon-europe.org/index.html"
biohackathon_location: "Barcelona, Spain, 2021"
group: Project 36
# URL to project git repo --- should contain paper.md
git_url: https://github.com/elixir-europe/biohackathon-projects-2021/tree/main/projects/36/bhxiv
# This is the short authors description that is used at the
# bottom of the generated paper.
authors_short: Núria Queralt-Rosinach \emph{et al.}
---
<!--

The paper.md, bibtex and figure file can be found in this repo:

  https://github.com/journal-of-research-objects/Example-BioHackrXiv-Paper

To modify, please clone the repo. You can generate PDF of the paper by
pasting above link (or yours) in

  http://biohackrxiv.genenetwork.org/

-->

# Introduction

The  COVID-19 crisis demonstrates a critical requirement for rapid and efficient sharing of data to facilitate the global response to this and future pandemics. We can address this challenge by making viral genomic and patient phenomic data FAIR, and formalising it to permit seamless data integration for analysis. Phenopackets is a standard file format for sharing phenotypic information that facilitates communication within the research and clinical genomics communities. The OMOP model allows for large-scale analysis of distributed data to generate evidence for research that promotes better health decisions and better care. This gathered data is used by epidemiologists to monitor the infection, model it and make outbreak analysis and predictions to evaluate policy interventions. To harness machine-learning and AI approaches to discover meaningful patterns in epidemic outbreaks, we need to ensure that data are FAIR. To leverage data for federated learning/analytics, datasets can be discovered in FAIR Data Points; FAIR data repositories that publish human- and machine-readable metadata for data resources. This project aims to enhance interoperability between health and research data by mapping Phenopackets and OMOP and representing COVID-19 metadata using the FAIR principles to enable discovery, integration and analysis of  genotypic and phenotypic data.


<!--
# Results
-->

## OMOP to Phenopackets
In order to accomplish the mapping between OMOP CDR and Phenopackets the availability of data in OMOP CDR format is extremely useful. However, due to the extreme sensitivity of real patients data, artificial data have been preferred over real ones. 
### Population of OMOP CDR tables with synthetic patients data
The process of populating the OMOP CDR tables of a database can roughly be divided into four step: 
1. Creation of patients data
2. Database deployment
3. Vocabularies retrieval
5. Transfer of patients data and vocabularies to DB

The choice of the tools needed to accomplish these tasks was facilitated by the familiarity of some group member with Synthea[^1], an open-source, synthetic patient generator. In fact, Synthea has an extension called ETL-Synthea[^2] that loads the data created by the former into a PostgreSQL database, set with OMOP CDR schema. 

The first step makes use of Synthea version 2.7[^3]. Once downloaded the jar and the source from the link, a csv file with 1000 patients can be created with:
```
java -jar synthea-with-dependencies.jar -p 1000 -c /pathtosynthea/src/main/resources/synthea.properties
```
where synthea.properties, located in the source code in /pathtosynthea/synthea/src/main/resources/, must be edited in order to export data in csv format.
```
exporter.csv.export = true
```
More recent versions of synthea yield data that can not be ingested by the ETL-Synthea tool only after some columns cutting and editing. 

The next step is to set up a Postgres db. Probably the easiest way is to create a docker container. After installing docker and docker-compose a yaml file like the following can be used:
```
version: "3"
services:
  db:
    image: postgres:12.2
    restart: "no"
    shm_size: 256m
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: lollipop
      PGDATA: /var/lib/postgresql/data
    volumes:
      - db-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
 
  pgadmin:
    image: dpage/pgadmin4:4.18
    restart: "no"
    environment:
      PGADMIN_DEFAULT_EMAIL: youremail@yourdomain.com
      PGADMIN_DEFAULT_PASSWORD: yourpassword
      PGADMIN_LISTEN_PORT: 80
    ports:
      - "8081:80"
    volumes:
      - pgadmin-data:/var/lib/pgadmin
    links:
      - "db:pgsql-server"
volumes:
  db-data:
  pgadmin-data:
```
The yaml contains the instructions to create the postgres container and a tool for administration connected to it. In order to generate the container:
```
docker-compose up
```
Then after logging in to the administrattion tool at http://localhost:8081 it must be created a db called "synthea10" and inside it two schema named "cdm_synthea10" and "native".

In the third step we chose the athena site[^4] to donwload the vocabularies. Accepting all the default vocabularies resulted in a zip file of over 4 GB and an error later in the fourth step. Reducing the vocabularies zip file dimension under 3 GB solved the issue.

The next step is the actual population of the postgresql db just created with the synthetic data generated in the first step. The command to execute is:
```
Rscript loader_all_master.r
```

where "loader_all_master.r" is similar to:
```
devtools::install_github("OHDSI/ETL-Synthea")
library(ETLSyntheaBuilder)
devtools::install_github("OHDSI/CommonDataModel", "v5.4")
cd <- DatabaseConnector::createConnectionDetails(
  dbms     = "postgresql", 
  server   = "172.23.0.2/synthea10", 
  pathToDriver = "/tmp/",
  user     = "postgres", 
  password = "lollipop", 
  port     = 5432
)
cdmSchema      <- "cdm_synthea10"
cdmVersion     <- "5.4"
syntheaVersion <- "2.7.0"
syntheaSchema  <- "native"
syntheaFileLoc <- "/tmp/output/csv"
vocabFileLoc   <- "/tmp/Vocabulary_restricted"

ETLSyntheaBuilder::CreateCDMTables(connectionDetails = cd, cdmSchema = cdmSchema, cdmVersion = cdmVersion)
                                     
ETLSyntheaBuilder::CreateSyntheaTables(connectionDetails = cd, syntheaSchema = syntheaSchema, syntheaVersion = syntheaVersion)
                                       
ETLSyntheaBuilder::LoadSyntheaTables(connectionDetails = cd, syntheaSchema = syntheaSchema, syntheaFileLoc = syntheaFileLoc)
                                     
ETLSyntheaBuilder::LoadVocabFromCsv(connectionDetails = cd, cdmSchema = cdmSchema, vocabFileLoc = vocabFileLoc)
                                    
ETLSyntheaBuilder::LoadEventTables(connectionDetails = cd, cdmSchema = cdmSchema, syntheaSchema = syntheaSchema, cdmVersion = cdmVersion, syntheaVersion = syntheaVersion)
```

The actual server address in the server line must be replaced with the ip address of your db container. Some commands to retrieve it are:
```
docker ps #get the db container name e.g. 6cd32142e88c
docker inspect 6cd32142e88c | grep -i IPADD
```
"pathToDriver" have to filled with the path to the postgresql java driver. For the version included in the yaml shown postgresql-42.3.1.jar is the right choice and can be downloaded from https://jdbc.postgresql.org/download.html
"user" and "password" are the same set in the yaml by the name of "POSTGRES_USER" and "POSTGRES_PASSWORD". 
"syntheaFileLoc" is the path to the directory containing the synthetic data created with Synthea whereas "vocabFileLoc" points to the path of the directory with the vocabularies. 


[^1]:[https://synthetichealth.github.io/synthea/](https://synthetichealth.github.io/synthea/)
[^2]: [https://github.com/OHDSI/ETL-Synthea]( https://github.com/OHDSI/ETL-Synthea )
[^3]:[https://github.com/synthetichealth/synthea/releases/tag/v2.7.0](https://github.com/synthetichealth/synthea/releases/tag/v2.7.0)
[^4]:https://athena.ohdsi.org/vocabulary/

### Mapping Omop to Phenopackets

In order to create reusable mappings between OMOP and Phenopackets, we first identified the appropriate tables in the OMOP schema for each relevant Phenopacket entity (or "building block"). A number of Phenopacket entities are outside the scope of OMOP, in particular in the area of "Genomic Interpretation". We also excluded the top-level elements of "Family" and "Cohort" as again, these are not within the OMOP scope, which is focused on healthcare data of individual patients.

After an initial review of the two domains, we found that no Phenopacket concept has a direct one-to-one mapping to a single entity in the OMOP CDM. While there are many fields that have a direct equivalence between the two, fields within one Phenopacket entity are usually spread across multiple OMOP tables and vice-versa. In addition, some Phenopackets fields need to be derived or inferred from one or more OMOP fields, especially for time- and date-related fields. For example, Phenopacket's Individual.date\_of\_birth is a concatenation of OMOP's Person.year\_of\_birth, Person.month\_of\_birth and Person.day\_of\_birth if Person.birth\_datetime is not available, while Phenopacket's Treatment.interval.end is derived from OMOP's DrugEra.drug\_exposure\_start\_date and DrugExposure.days\_supply if DrugEra.drug\_exposure\_end\_date is not available. Equally, concepts such as Disease.primary\_site and Disease.laterality need to be derived from multiple entries in the ConditionOccurrence table linked via specific concept relationships. 

Differentiating between PhenotypicFeature and Disease posed another mapping challenge as a lot of concept in OMOP ConditionOccurrence are more aligned with the concept of phenotypic feature than disease (eg cerebrovasuclar accident, atrial fibrillation). We were faced with either having to declare a set equivalence between ConditionOccurrence and one of the Phenopacket entities or using query refinements to assess each ConditionOccurrence against ontologies such as HPO and MONDO in order to determine the correct Phenopackets concept for each mapping.

Table 1 shows an overview of the Phenopacket entity to OMOP table mappings. The full list of mappings in available in appendix 1.

| Phenopacket Entity | OMOP Tables |
| ------------------ | ----------- |
| Individual | Person, VisitOccurrence, Death |
| VitalStatus | Death, Person, ConditionOccurrence |
| PhenotypicFeature| Observation, ConditionOccurrence, ConditionEra |
| Measurement| Measurement, (ProcedureOccurrence) |
| Disease | ConditionOccurrence |
| MedicalAction | DrugEra, EpisodeEvent, DrugExposure |
| Procedure | ProcedureOccurrence, Person |
| Treatment | DrugExposure, DrugStrength, DrugEra |
| RadiationTherapy | ConditionOccurrence, DrugExposure, DrugEra |
| TherapeuticRegimen | DoseEra, DrugExposure |




### SQL script creation

### Omop to Phenopackets in Python
During the hackaton an example of Python code that leverages the mapping and the SQL scripts was created. The code can be found at https://github.com/sasurfer/PyPhenoFromOmop
and it connects to the Postgres database where it retrieves the data for the chosen patient id. Then the data are serialized into a phenopacket which is written in a file.  The phenopacket fields are limited to the subject and measurements fields, i.e. the mappings present at the time of coding.


## OMOP to Phenopackets for the Semantic Web
Semantic web technologies are being extensively used in the modeling of clinical data resources to fulfill the FAIR criterias. This is the case in the Swiss Personalized Health Network (SPHN) project that builds a whole semantic web based ecosystem with defined semantics and schemas for “FAIRyfing” and sharing health-related data across data providers in Switzerland to fit the needs of researchers [Österle et al. 2021]. The phenopackets is a standard built for representing disease and phenotype information. The European Joint Programme on Rare Diseases (EJP RD) is an EU funded research program aimed at accelerating research in the rare disease field. One of the goals of this programme is to FAIRify heterogeneous rare diseases resources by applying FAIR principles. In the EJP RD programme a semantic model of phenopackets [https://github.com/LUMC-BioSemantics/phenopackets-rdf-schema/wiki] has been created to FAIRify phenotypic data. The phenopackets semantic model is created based on design patterns proposed in the Semanticscience Integrated Ontology (SIO). 
During the biohackathon, the idea came to join forces between these two projects by comparing and mapping the concepts defined in the SPHN consortium with the phenopackets concepts to ease the integration of data coming from one or the other data type and therefore, in the longer term, improve data interoperability across these alternative platforms. The common thread between these two has been the semantic web framework which largely facilitated the mapping exercise. Today, the measurement concept has been mapped between the two data representations and collaboration is now in place to further continue the developments.


## FAIR federated Machine Learning


Future work includes:

1. documenting the generation of synthetic OMOP database for the community;
2. extracting and mapping COVID-19 relevant OMOP terms to open bio-ontologies;
3. modelling and evaluating FAIR federated machine learning.

# Discussion

XXX

## Acknowledgements

We thank the organizers of the BioHackathon-Europe 2021 for
travel support for some of the authors.

## References
