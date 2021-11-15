from fastapi import FastAPI, APIRouter, Request, Response
from fastapi.responses import JSONResponse
from typing import List, Optional

from SPARQLWrapper import SPARQLWrapper, TURTLE, XML, JSON

# Implementation of the Ranked Search for FDP

router = APIRouter()

METADATA_ENDPOINT = 'https://ejprd.fair-dtls.surf-hosted.nl/triple-store/repositories/bh-2021'

PREFIXES = """PREFIX :<http://www.ontotext.com/graphdb/similarity/>
    PREFIX inst:<http://www.ontotext.com/graphdb/similarity/instance/>
    PREFIX pubo: <http://ontology.ontotext.com/publishing#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX dcat: <http://www.w3.org/ns/dcat#>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>"""


@router.get("/search", name="Ranked search",
    description="Ranked search of SPARQL endpoints",
    response_model=List[dict],
)            
def ranked_search(search: str = "blood") -> List[dict]:

    list_endpoints_query = PREFIXES + """#SELECT DISTINCT ?resource ?label (AVG(?score) AS ?total_score) {
    SELECT DISTINCT ?resource ?label (SUM(?score) AS ?total_score) {
        VALUES ?search_term {'""" + search + """'}
        
        # Search similarity index for input text
        ?search a inst:first-index ;
            :searchTerm ?search_term;
            :documentResult [:value ?documentID; :score ?score].    

        {
            ?documentID a dcat:Resource ;
                rdfs:label|dcterms:title ?label .
            BIND(?documentID AS ?resource)
        } UNION {
            ?documentID a owl:Class .
            # Search FDP with terms URI suggested by similartiy index search
            ?resource a ?resource_type;
            rdfs:label|dcterms:title ?label;
            dcat:theme ?documentID .
            # OPTIONAL {?resource dcterms:description ?resource_description}   
            #FILTER(regex(?resource_name, ?search_term) || regex(?resource_description, ?search_term))    
        }
    } 
    GROUP BY ?resource ?label ORDER BY DESC(?total_score)"""

    sparql = SPARQLWrapper(METADATA_ENDPOINT)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(list_endpoints_query)
    sparqlwrapper_results = sparql.query().convert()
    sparql_results = sparqlwrapper_results["results"]["bindings"]

    dataset_list = []
    for result in sparql_results:
        dataset_list.append({
            'url': result['resource']['value'],
            'title': result['label']['value'],
            'score': result['total_score']['value'],
        })

    return JSONResponse(dataset_list)

