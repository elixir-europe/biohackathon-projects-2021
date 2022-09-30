---
title: 'FAIR Lipids: Biohackathon-Europe-2021'
tags:
  - lipid
  - FAIR
  - RDF
authors:
  - name: Jerven Bolleman
    orcid: 0000-0002-7449-1266
    affiliation: 1
  - name: Jakub Galgonek 
    orcid: 0000-0002-7038-544X
    affiliation: 2
  - name: Robert Andrews
    orcid: 0000-0002-3491-2361
    affiliation: 3
  - name: Karla Mendvelso
    orcid: 0000-0002-5282-3995
    affiliation: 3
  - name: Caroline Gaud
    orcid: 0000-0002-0453-9260
    affiliation: 4
  - name: Dominik Martinát
    orcid: 0000-0001-6611-7883
    affiliation: 5
  - name: Nils Hoffmann
    orcid: 0000-0002-6540-6875
    affiliation: 6
  - name: Anne Morgat
    orcid: 0000-0002-1216-2969
    affiliation: 1
  - name: Parit Bansal
    orcid: 0000-0002-0875-1680
    affiliation: 1
  - name: Lucila Aimo
    orcid: 0000-0003-0943-6401
    affiliation: 1
  - name: Venkatesh Muthukrishnan
    orcid: 0000-0003-0943-6401
    affiliation: 1
  - name: Maksim Kolchin
    orcid: 0000-0002-3851-9874
    affiliation: 7

affiliations:
 - name: Swiss-Prot Group, Swiss Institute of Bioinformatics, rue Michel Servet 1, CH 1211 Geneva 4, Switzerland
   index: 1
 - name: Institute of Organic Chemistry and Biochemistry of the CAS, Flemingovo náměstí 2, 166 10, Prague 6, Czech Republic
   index: 2
 - name: LIPID MAPS, Systems Immunity Research Institute, Cardiff Univeristy, Cardiff, UK
   index: 3
 - name: LIPID MAPS, Bioinformatics Group, Babraham Institute, Babraham Research Campus, Cambridge, UK
   index: 4  
 - name: Center for Biotechnology, Bielefeld University, Universitätsstraße 27, 33615 Bielefeld, Germany
   index: 6
 - name: Department of Biochemistry, Faculty of Science, Palacký University Olomouc, 17. listopadu 1192/12, 779 00, Olomouc, Czech Republic
   index: 5
 - name: Boehringer Ingelheim España S.A., Sant Cugat del Vallès, Spain
   index: 7
date: 11 November 2021
bibliography: paper.bib
authors_short: FAIR Lipids team
group: FAIR Lipids team
event: BioHackathon Europe 2021
---

# Introduction

Data in the lipid world, while free to access suffers from a number of technical barriers 
to being truly Interoperable and Accessible in the FAIR sense. This makes it harder
to Reuse these resources.

Team members of SwissLipids, IDSM, MolMedDB, Rhea, UniProt, LIPID MAPS joined by volunteers
met virtually at the BioHackathon Europe 2021 to challenge these technical barriers.
Critically we implemented W3C standards to enable interoperability of these public databases using SPARQL 
and prior existing ontologies and schemas such as ChEBI and the Biological Assay Ontology.

# RDFying databases

## MolMeDB

Bit about MolMeDB. Feel free to edit or move it too

The mapping of the MolMeDB database into the RDF dataset has been created mostly relying on the BioAssay Ontology (BAO) and the Chemical Information Ontology (CHEMINF). Substances present in the MolMeDB database have been linked into PubChem, ChEBI, ChEMBL and PDB databases via the skos:exactMatch property. Some membrane models have been linked to their components in the ChEBI database via the bao:BAO_0090004 (has part) property. Linking of transporter assay targets to the UniProt database has been made directly by using UniProt IRIs. All these mentioned links allow for easy federated querying across all the mentioned databases.

The prototype of the MolMeDB SPARQL endpoint has been implemented using the IDSM SPARQL engine, and it is available at https://idsm.elixir-czech.cz/sparql/endpoint/molmedb.

## LIPID MAPS

The LIPID MAPS® Structure Database (LMSD) [1] is a relational database encompassing structures 
and annotations of biologically relevant lipids. As of today, LMSD contains 46430 unique lipid structures, 
making it the largest public lipid-only database in the world.

The decision to follow the approach based on the RDF Mapping Language (RML) [2] was chosen because:

- LIPID MAPS database is hosted as a relational database, therefore it can be queried directly without 
an intermediate step that does ETLing of data into a CSV file, for example, 
- some LIPID MAPS data isn't the format that can be used as it is, therefore some transformations using SQL functions 
were required, e.g. SwissLipid identifiers are stored as strings in `SLM:000000` format, although they need to be IRIs 
in RDF data, therefore `REGEXP_REPLACE` was used to extract only digits after the colon (i.e. `:`) symbol.  

An example RDF representing the `C10H19NO4` lipid (in RDF 1.1 Turtle format):

```turtle
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix chebi: <http://purl.obolibrary.org/obo/chebi/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix lmontology: <https://www.lipidmaps.org/ontology/> .

<https://www.lipidmaps.org/rdf/LMFA07070005> a owl:Class;
    chebi:formula "C10H19NO4";
    chebi:inchi "InChI=1S/C10H19NO4/c1-5-10(14)15-8(6-9(12)13)7-11(2,3)4/h8H,5-7H2,1-4H3/t8-/m1/s1";
    chebi:inchikey "UFAHZIUFPNSHSL-MRVPVSSYSA-N";
    chebi:monoisotopicmass 2.17131409E2;
    rdfs:label "O-propanoyl-carnitine"@en;
    rdfs:subClassOf <https://www.lipidmaps.org/rdf/category/10707>;
    owl:equivalentClass <http://purl.obolibrary.org/obo/CHEBI_53210>, <https://swisslipids.org/rdf/SLM_000390084> ;
    lmontology:abbrev "CAR 3:0" .
```

In addition to the lipids itself, we've RDFied the Lipids Categories as `owl:Class`es 
and used `rdfs:subClassOf` relations to reproduce the hierarchy. 

The RDF data is available through a SPARQL endpoint at https://www.lipidmaps.org/sparql. We employ Apache Fuseki here 
to provide the SPARQL endpoint. 

## Tables, figures and so on

Please remember to introduce tables (see Table 1) before they appear on the document. We recommend to center tables, formulas and figure but not the corresponding captions. Feel free to modify the table style as it better suits to your data.

Table 1
| Header 1 | Header 2 |
| -------- | -------- |
| item 1 | item 2 |
| item 3 | item 4 |

Remember to introduce figures (see Figure 1) before they appear on the document. 

![BioHackrXiv logo](./biohackrxiv.png)
 
Figure 1. A figure corresponding to the logo of our BioHackrXiv preprint.

# Other main section on your manuscript level 1

Feel free to use numbered lists or bullet points as you need.
* Item 1
* Item 2

# Discussion and/or Conclusion

We recommend to include some discussion or conclusion about your work. Feel free to modify the section title as it fits better to your manuscript.

# Future work

And maybe you want to add a sentence or two on how you plan to continue. Please keep reading to learn about citations and references.

For citations of references, we prefer the use of parenthesis, last name and year. If you use a citation manager, Elsevier – Harvard or American Psychological Association (APA) will work. If you are referencing web pages, software or so, please do so in the same way. Whenever possible, add authors and year. We have included a couple of citations along this document for you to get the idea. Please remember to always add DOI whenever available, if not possible, please provide alternative URLs. You will end up with an alphabetical order list by authors’ last name.


Bit about future of MolMeDB RDF. Feel free to edit or move it too. Or even to scrapt it if it won't fit.

The MolMeDB RDF dataset and the related SPARQL endpoint introduced as result of BioHackaton Europe 21 is at a prototype stage. It will be further developed to encompass a wider variety of data present in MolMeDB and to facilitate more possibilities of query federation.

# Jupyter notebooks, GitHub repositories and data repositories

* https://github.com/lifs-tools/goslin-sparql/

* https://github.com/DominikMartinat/rdf-mmdb

# Acknowledgements

We wish to thank the organizers and supporters of the Biohackathon Europe 2021 for offering the venue for improving the Lipid information landscape.

The SwissLipids team was funded by the Swiss State Secretariat for Education, Research and Innovation through the Swiss Institute of Bioinformatics.

The Rhea contribution was funded by the Swiss State Secretariat for Education, Research and Innovation through the Swiss Institute of Bioinformatics.

The LIPID MAPS team was funded by the Wellcome Trust, UK.

The UniProt contribution was supported by UniProt by the National Eye Institute (NEI), National Human Genome Research Institute (NHGRI), National Heart, Lung, and Blood Institute (NHLBI), National Institute on Aging (NIA), National Institute of Allergy and Infectious Diseases (NIAID), National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK), National Institute of General Medical Sciences (NIGMS), National Institute of Mental Health (NIMH), and National Cancer Institute (NCI) of the National Institutes of Health (NIH) under grant U24HG007822. Additional support for the EMBL-EBI's involvement in UniProt comes from European Molecular Biology Laboratory (EMBL) core funds, the Alzheimer's Research UK (ARUK) grant ARUK-NAS2017A-1, the Biotechnology and Biological Sciences Research Council (BBSRC) [BB/T010541/1] and Open Targets. UniProt activities at the SIB are additionally supported by the Swiss Federal Government through the State Secretariat for Education, Research and Innovation SERI. PIR's UniProt activities are also supported by the NIH grants R01GM080646, G08LM010720, and P20GM103446, and the National Science Foundation (NSF) grant DBI-1062520.

N. H. acknowledges funding from the Federal Ministry of Education and Research in Germany (BMBF) (grant number: FKZ 031A532B).

# References

Leave this section blank, create a paper.bib with all your references.

1. LIPID MAPS® Structure Database (LMSD)
LMSD: LIPID MAPS® structure database. Sud M., Fahy E., Cotter D., Brown A., Dennis E., Glass C., Murphy R., Raetz C., Russell D., and Subramaniam S., Nucleic Acids Research 35, D527-32 (2006)
2. Dimou, A., Vander Sande, M., Colpaert, P., Verborgh, R., Mannens, E., & Van de Walle, R. (2014, January). RML: a generic language for integrated RDF mappings of heterogeneous data. In Ldow.

