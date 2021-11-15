# Project 5: From FAIR plant research data capture to integration based on MIAPPE, ISA, and knowledge graphs

## Abstract

By leveraging interoperability platform tools and expertise such as Bioschemas, the ELIXIR Plant Sciences Community sees opportunities to contribute to tasks T1 (data standards development and dissemination), T2 (data collection), T4 (data integration), and T7 (tools and workflows) of its roadmap [https://doi.org/10.7490/f1000research.1118482.1] through the following activities.
The MIAPPE standard [https://doi.org/10.1111/nph.16544] provides a biologist-friendly guide to capture phenotyping data in the best reusable way and expose it in the standard ISA format. To feature a RDM process from data acquisition to data integration, we propose to work on two aspects here.

The first aspect enables MIAPPE 1.1 in ISA4J library to generate compliant ISA formatted data files [ https://doi.org/10.12688/f1000research.27188.1 ], hence allowing plant scientists to store phenotyping metadata in a reusable way. The software will be designed as a library for developers to use in their data publishing workflows, and will include a graphical and/or command line interface as time permits. The results can be integrated in a ready-to-use data warehouse, relying on Zendro(https://zendro-dev.github.io). It would expose an intuitive web interface backed by a GraphQL API, linking data processing scripts to the knowledge hub and be capable of seamlessly connecting to other instances from a data cloud.

The second aspect enables data integration through Knowledge Graphs (KG) based tools and models for plant omics (e.g., ISA, MIAPPE, BrAPI, Knetminer) to be aligned with other ontologies/models (e.g., Bioschemas, Dublin Core, or BioLink). An effort will be made to develop and extend shared ETL tools based on existing attendees’ toolboxes to feed KG with new sources of data, possibly reusing work from the first aspect and leveraging distributed queries over public SPARQL endpoints.

## Topics

Biodiversity
Bioschemas
Data Platform
Interoperability Platform
Plant Sciences
Tools Platform

**Project Number:** 5



**EasyChair Number:** 7

## Team

### Lead(s)

Dennis Psaroudakis <psaroudakis@ipk-gatersleben.de>, Flores Raphaël <raphael.flores@inrae.fr>

## Expected outcomes

Main outcome: to create a proof-of-concept endpoint based on integrated public data to prototype applications, such as a simple MIAPPE-compliant data warehouse to host and query data
Aspect #1:
- create an extension to isa4j that translates the abstract ISA notions into more palpable biological concepts
- provide ready to use plug and play ISA Model data warehouse
Aspect #2:
- Alignment between several data models (ISA/MIAPPE, KG specific models with more general ontologies bioschemas, Dublin Core
- New and extended ETL tools allowing to feed partners’ knowledge graphs with publicly available data
- Creation of several federated queries over SPARQL and/or GraphQL endpoints

One goal would be to combine both aspects and present as a proof of concept a complete research data management workflow from data acquisition to data analysis. Primary data from plant phenotyping can be described and exported in a MIAPPE-compliant manner using isa4j and serve as a source for a data warehouse infrastructure accessible through a BrAPI endpoint. The provided endpoint can be used by tools (such as KnetMiner, AgroLD or Plaza) for graphical representation and integrative data analysis.

In an effort to combine the above tools and approaches, a ready to use fully featured ISA / MIAPPE data warehouse will be set up and filled with scientific data obtained from tabular data. Several such warehouses can be connected to form a distributed data cloud. The features and functions of two interfaces are explored, one intuitive browser based interface front end capable of including scientific plots and the  GraphQL based API backend (zendro-dev.github.io).

## Expected audience

We are planning to attend with 6-7 people and would be happy to welcome 2-3 more people during the hackathon. Experience with knowledge graph data integration and/or coding in Java, Javascript (Node.js), Python, or shell scripting and using git for versioning would be good since there will be little time to learn these things (unless you’re looking for a challenge). Knowledge about the ISA-Tab format and MIAPPE standard are not really necessary as long as you are willing to learn about it during the first two days of the hackathon.

**Number of expected hacking days**: We'll take the full 4 days.

## Resources

- repository for isa4j: https://github.com/IPK-BIT/isa4j . The extension is being developed in the [miappe](https://github.com/IPK-BIT/isa4j/tree/miappe) branch

