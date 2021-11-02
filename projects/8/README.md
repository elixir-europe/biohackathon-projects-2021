# Project 8: Executing workflows in the cloud with WESkit

## Abstract

Sending the analysis and processing workflows to the data will be essential to cope with growing amounts of genomic data in healthcare and may increase efficiency and data security. The Global Alliance for Genomics and Health (GA4GH) defines several standards for processing data in a cloud framework. Specifically, the GA4GH Workflow Execution Service (WES) defines an interface for transmitting workflows and their configuration to a computing platform. Thus, GA4GH WES can also serve as a general interface between data management software and data processing software within an HPC environment.

Our tool WESkit implements the GA4GH WES standard and is developed with high data throughput, stability, and security in mind. Currently, WESkit supports the workflow systems Nextflow and Snakemake. Furthermore, it can be easily deployed for an application in a cloud environment or in an HPC environment. The software is used for processing whole-genome cancer data at the Deutsches Krebsforschungszentrum and Charité Universitätsmedizin Berlin. We also support its deployment as a service in the German de.NBI cloud for building up a workflow execution framework.

## Topics

Compute Platform
GA4GH partnership

**Project Number:** 8

**EasyChair Number:** 12

## Team

### Lead(s)

 * sven.twardziok@charite.de
 * p.kensche@dkfz-heidelberg.de

## Expected outcomes

During the ELIXIR Biohackathon, we will improve WESkit on several aspects to improve its usability, interoperability, and integration. Open topics are 1.) implementing additional GA4GH standards such as Data Repository Service (DRS) and Tool Registry Service (TRS), 2.) closer integration of WESkit into the ELIXIR cloud framework, e.g. by using ELIXIR AAI for user management, and 3.) supporting additional workflow languages such as CWL, Luigi or WDL.

## Expected audience

ELIXIR-AAI experts, GA4GH DRS and TRS user and developer, workflow developer, python programmer

**Number of expected hacking days**: 4

## Further project information

Code development will be done in the WESkit Gitlab Repositories. The [Gitlab project group](https://gitlab.com/one-touch-pipeline/weskit) contains repositories specifically for the [WES-API service](https://gitlab.com/one-touch-pipeline/weskit/api), [Documentation](https://gitlab.com/one-touch-pipeline/weskit/documentation), and [deployment](https://gitlab.com/one-touch-pipeline/weskit/deployment).

During the Biohackathon we will collect and manage our work with a dedicated [project board](https://gitlab.com/one-touch-pipeline/weskit/api/-/boards/3460290?milestone_title=Elixir%20Biohackathon%202021).
