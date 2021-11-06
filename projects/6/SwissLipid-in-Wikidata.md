# Swiss Lipid IDs in Wikidata

Previously, we already proposed a [Swiss Lipid property for Wikidata](https://www.wikidata.org/wiki/Wikidata:Property_proposal/SwissLipids_identifier)
which was approved and created in [just before the 2020 BioHackathon Europe](https://www.wikidata.org/w/index.php?title=Property:P8691&oldid=1287579005).
But populating Wikidata with identifiers got stuck.

The intention for this BioHackathon is the add them, using SwissLipid ID <> InChIKey tuples and Bacting code. This page will describe the process.

## Step 1: getting the data

The data is CC-BY but it was agreed that adding the SwissLipid identifiers to Wikidata (CCZero) is okay.

* Download `lipids.tsv` from the [Downloads](https://www.swisslipids.org/#/downloads) page
* Gunzip the file

## Step 2: extract Swiss Lipid ID <> InChIKey tuples

For this step I use `csvtool` (`apt get install csvtool`):

```shell
csvtool -t TAB col 1,11 swisslipids.tsv
```

The output needs some further clean up, like removing lines without InChIKeys or "none" and "-" as value. Also,
the "InChIKey=" prefix is removed in preparation for the next step. The full used code is:

```shell
csvtool -t TAB col 1,11 swisslipids.tsv  | sed 's/InChIKey=//' | grep -v "none" | grep -v ",-$" | grep -v ",$" | tee swisslipids_ids.tsv
```

This results in almost 600k tuples:

```shell
$ wc -l swiss*tsv
   592412 swisslipids_ids.tsv
   777957 swisslipids.tsv
```
