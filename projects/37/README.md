# Project 37: Support for the Common Workflow Language version 1.2 in Galaxy

# Chat room

https://matrix.to/#/#galaxy-cwl:matrix.org

## Abstract

Computational pipelines have become ubiquitous in bioinformatics, with an increasing need for sharing them among researchers in portable formats like the Common Workflow Language (CWL).

Galaxy has been involved in the development of the CWL standard from the start,
and native support for CWL in Galaxy has been developed in a fork of the Galaxy codebase created by John Chilton.

The first three European BioHackathons allowed several different contributors to work together on this project and discuss with the wider communities. This resulted in major progress in the CWL support in Galaxy, and in large portions of the CWL branch of Galaxy making their way into the core repository.

In particular, an initial Galaxy implementation of a major feature of the v1.2 version of the CWL specification was developed during the 2020 BioHackathon Europe: conditional execution of a workflow step. We plan to finish this work and merge the pull request ( https://github.com/common-workflow-language/galaxy/pull/123 ) in the Galaxy fork.

Other goals for the 2021 BioHackathon will be to fix the remaining required CWL 1.2 conformance tests, work on the other open issues ( tracked at https://github.com/common-workflow-language/galaxy/issues ), and continue the merge of the separate CWL branch into the upstream Galaxy repository.

## Topics

Galaxy
Interoperability Platform
Tools Platform

**Project Number:** 37



**EasyChair Number:** 66

## Team

### Lead(s)

Nicola Soranzo <nicola.soranzo@earlham.ac.uk>

## Expected outcomes

- Complete the implementation CWL 1.2 conditionals in Galaxy
- Fix remaining CWL conformance tests
- Advance the merge of the separate branch into the upstream Galaxy repository to be part of future Galaxy releases

## Expected audience

Software developers with either Python or Web Frontend development skills (especially JavaScript/Vue.js), with or without an initial experience of development in Galaxy and/or CWL.

**Number of expected hacking days**: 4

