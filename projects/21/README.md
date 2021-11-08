# Project 21: Handling Knowledge graphs subsets

## Abstract

Knowledge graphs like Wikidata are successfully employed to represent and link an overwhelming amount of knowledge. Wikidata is updated continuously and provides a valuable hub of knowledge. This success leads to an ever increasing body of interconnected data which can be difficult to handle. Getting a subset of the contents in a specific domain and at some point in time can be hard to do.
This proposal is a continuation of project 35 from Biohackathon 2020. After that event, we continued working at the SWAT4HCLS and obtained some prototype subsets that were enriched with information from bioschemas. The work seems to thrive during the Biohackathon and we would like to continue at the next edition. Currently, we have various methods to generate subsets from wikidata, which require maturity and better documentation.
The Biohackathon proved to be instrumental in the progress made. We want to continue working on developing knowledge graphs subsetting techniques that enable the creation of snapshots which can be later used by researchers. Having a service that creates knowledge graphs subsets is necessary for scientific reproducibility and to enrich, transform and link the data enabling cross-domain research.

## Topics

Bioschemas
Cancer
Covid-19
Data Platform
Federated Human Data
Machine learning
Plant Sciences
Rare Disease
Tools Platform

**Project Number:** 21



**EasyChair Number:** 37

## Team

### Lead(s)

Jose Emilio Labra Gayo (labra@uniovi.es)
Dan Brickley (danbri@danbri.org)
Lydia Pitschner (lydia.pintscher@wikimedia.de)
Andra Waagmeester (andra@micel.io)

## Expected outcomes

- A wikidata subsetting service that allows users to declare their domain and generates a snapshot of the contents of wikidata from that domain
- Implementation of the slurper technique for Shape Expressions that facilitates the creation of the subset
- Creation of subsets for some domains of interest like the Genewiki, Scholia, Chemistry, etc.
- A transformation/enrichment system that allows the subset data to be linked with other data or transformed during the subset process

## Expected audience

Domain experts who want to define some domain of interest from a knowledge graph
Developers who want to help with the implementation

## Notes

We keep this [hackmd](https://hackmd.io/QI5KK1ecQICgGERmSj981g) for notes as well as this [github repo](https://github.com/kg-subsetting/biohackathon2021) for specific code/scripts/data.


**Number of expected hacking days**: 4

