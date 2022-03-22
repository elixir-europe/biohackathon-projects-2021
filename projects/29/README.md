# Project 29: Facilitating life science metadata curation through Bioschemas Validators

## Abstract

Bioschemas is a community effort to specify the minimal, recommended, optional Life Science metadata. Conformance to these profiles is vital to support harvesting by initiatives such as OpenAIRE.
However, biologists and bioinformaticians may find annotating their resources to be too technically complex and time-consuming without the availability of user-friendly tools.
Multiple initiatives are emerging to provide support tools. FAIR-checker is a web-application, supported by Knowledge Graphs, aimed at providing developers with technical hints to better implement FAIR principles, and provide minimal Bioschemas markup for better findability.
Within the Bioschemas Community, there have been efforts to develop a reusable scraper (BMUSE) to reliably retrieve embedded markup in websites, as well as several validation frameworks to test the conformance of retrieved markup against a stated Bioschemas Profile. These include the TeSS Validator, CTSA/NIH Data Discovery Engine, the ELIXIR JSON Schema validator, and Bioschemas Validata. These frameworks have tried a variety of underlying technologies, including JSON-Schema, ShEx, and SHACL.
The goal of this is project is to leverage Bioschemas community profiles and gather community efforts on metadata validation to provide: scraping and validation tools, basic statistics on live deploys metadata quality (per profile), tools to help the crowd-sourced Bioschemas markup curation.

## Topics

Bioschemas
Data Platform
Interoperability Platform
Tools Platform

**Project Number:** 29



**EasyChair Number:** 48

## Team

### Lead(s)

Alban Gaignard, alban.gaignard@univ-nantes.fr
Alasdair J. G. Gray, A.J.G.Gray@hw.ac.uk
Leyla Jael Garcia Castro, ljgarcia@zbmed.de

## Expected outcomes

- Tools consuming (machine readable) Bioschemas profiles and producing validation implementations. This will help to validate Bioschemas Live deployments, and compute basic statistics on metadata quality per profiles.
- Tools helping the curation of Bioschemas annotated resources:  (i) ranking resources based on Bioschemas profiles, (ii) randomly picking some resources with urgent curation needs
- Incorporating the validation into the data ingestion workflow of OpenAIRE

## Expected audience

- Chris Child (TeSS portal)
- Ginger Tsueng (Data Discovery Engine)
- Thomas Rosnet (FAIR-checker)
- Alan Williams (WorkflowHub)
- Alessia Bardi (CNR/OpenAIRE)
- Claudio Atzori (CNR/OpenAIRE)
- Nick Juty (Bioschemas)

and anyone knowledge-able in Knowledge Graphs, Schema.org, metadata validation technologies

**Number of expected hacking days**: 4

