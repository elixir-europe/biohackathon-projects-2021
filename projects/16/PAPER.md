# Wine Ontology 2021 - Reworking structured wine metadata into Food Ontology
Sirarat Sarntivijai[^1], Damion Dooley[^2], Robert Warren[^3] --- calling for co-authors

[^1]:ELIXIR Hub, Wellcome Genome Campus, Hinxton, Cambridge, CB10 1SD, UK
[^2]:Centre for Infectious Disease Genomics and One Health, Simon Fraser University, 8888 University Drive, Burnaby, BC, V5A 1S6, Canada
[^3]:Glengarry Agriculture and Forestry, Ottawa, Canada


## Abstract
Biohackathon Europe lent an opportunity to explore an area of critical collaboration for global food industry to the topic 
[_Wine (Ontology) Tasting: testing technicality in practicality for the food industry_](https://github.com/elixir-europe/bioHackathon-projects-2021/tree/master/projects/16). Previous works on examination of structural data of wine making process, taste profile, and labeling legal requirement were investigated for reuse with an inventory dataset donated by a wine merchant to test for reusability of the metadata model generated in this study. Design patterns were designed based on three use-case drivers from the perspectives of wine makers, business merchants, and wine consumers. Challenges of fit-for-purposeness for different drivers confirmed the needs for wine data classification by ontology representation as the approach that allows for flexibility in rendering different indexing inferences for different querying use cases. On-going efforts to classify wine product and wine manufacturing data exist globally. Entry point-of-contacts were initiated with potential collaborations across North American and European Partners. (Author's note: can name specific partners if agreed by all partners)

## Motivation
- estimated investment & value of global wine market
- complex data that do not lose value of knowledge but structuring of data for future reuse is VERY difficult (shifting technology framework with no backward compatibility in the previous works,
no sustainability plan defined previously)
- data gathering has been done based on siloed view of metadata modeling


## Challenges
- Previous works could not be easily reused
- Wine data were collected based on different use cases, combining of findings had to be performed carefully with a lot of manual investigation/curation
- No standardised criteria on how to define the process e.g., maceration/pre-maceration, primary fermentation vs normal fermentation, secondary fermentation vs double fermentation, does secondary fermentation imply any modification done to the first-step fermentationL?
- Implication pf Domain of Origin and Appellation classification. Some countries do this purely on geographical location, some countries is a combination of methods & geographical location of the process and/or origin of the raw materials (grapes). Definition is fussy.
- SubclassOf relation of appellation classification is not straigt-forward. By technical definition, a French AOP is a SubClassof French IGP... BUT!!!! when querying data with the ontology, do we want to see AOP listing returned with IGP which in turn implies differently level of _superiority_ (abstraction by human opinion). Is this the resut the querying user wants to see?
- Grape (genetic) varieties - should it be associated with the location? How should we model it?


**The top-level expansion of FoodON grape wine class**
![FoodOn Wine](https://github.com/elixir-europe/biohackathon-projects-2021/blob/a8645808e84000119a6af6e7468a3bf406bf2b94/projects/16/images/foodOnWine.jpeg)


**Example of challenges in modeling maceration...with disagreement of grape part from two different renderings of the same study....joy...lol...**
![grapes-maceration](https://github.com/elixir-europe/biohackathon-projects-2021/blob/a8645808e84000119a6af6e7468a3bf406bf2b94/projects/16/images/FoodOn_macerationprocessGrapes.jpeg)



## Results
- a propose extension of wine classification in FoodON
- a curator's datasheet for data harmonisation to class creation/mapping in FoodON
- ...


## Discussion
- complex data
- needs collaboration
- needs global sustaining and uptake of harmonised/synchroised metadata structure for wine by all key stakeholders

