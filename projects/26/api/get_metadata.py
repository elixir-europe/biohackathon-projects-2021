from fastapi import FastAPI, APIRouter, Request, Response
from fastapi.responses import JSONResponse
from typing import List, Optional
from pydantic import BaseModel, Field

from SPARQLWrapper import SPARQLWrapper, TURTLE, XML, JSON

# API calls to retrieve metadata from the Shapes of You SPARQL endpoint

router = APIRouter()

PREFIXES = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX bl: <http://w3id.org/biolink/vocab/>
PREFIX dctypes: <http://purl.org/dc/dcmitype/>
PREFIX idot: <http://identifiers.org/idot/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX void-ext: <http://ldf.fi/void-ext#>

PREFIX dcat-ext: <http://purl.org/biosemantics-lumc/ontologies/dcat-extension/>
PREFIX dcterm: <http://purl.org/dc/terms/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fdo: <http://rdf.biosemantics.org/ontologies/fdp-o#>
"""

# METADATA_ENDPOINT = 'https://graphdb.dumontierlab.com/repositories/shapes-registry'

# METADATA_ENDPOINT = 'http://ejprd.fair-dtls.surf-hosted.nl:7200/repositories/ordo-catalog-fdp'


class Dataset(BaseModel):
    url: str = Field(...)
    keywords: List[str] = Field(...)
    graph_count: int = Field(...)
    # id: str = Field(..., alias="@id")
    # context: str = Field(..., alias="@context")


@router.get("/datasets", name="List datasets available for Ranked Search",
    description="List the datasets available for Ranked Search",
    response_model=List[Dataset],
)            
def list_datasets() -> List[Dataset]:

    list_endpoints_query = PREFIXES + """#SELECT DISTINCT ?resource ?title ?description ?homepage ?resourceType ?theme ?keyword WHERE { 
    SELECT * {  
    ?resource a ?resourceType ;
                dcat:theme ?theme;
    #             dcat:theme [ rdfs:label ?theme ];
                dcat:keyword ?keyword;
                dcterm:description ?description;
                dcterm:title ?title; 
                dcat:landingPage ?homepage;                                                                                  
    #             fdo:metadataIdentifier [ dcterm:identifier ?id].
    }"""

    # list_endpoints_query = PREFIXES + """SELECT DISTINCT ?endpoint (count(distinct ?graph) AS ?datasets_graph_count)
    # WHERE {
    #     GRAPH ?endpoint {
    #         # ?graph a void:Dataset .
    #         ?graph void:propertyPartition ?propertyPartition . 
    #         # ?propertyPartition void:property ?predicate ;
    #     }
    # } GROUP BY ?endpoint ORDER BY DESC(?datasets_graph_count)
    # """

    sparql = SPARQLWrapper(METADATA_ENDPOINT)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(list_endpoints_query)
    sparqlwrapper_results = sparql.query().convert()
    sparql_results = sparqlwrapper_results["results"]["bindings"]

    dataset_list = []
    for result in sparql_results:
        dataset_list.append({
            'url': result['endpoint']['value'],
            'graph_count': result['datasets_graph_count']['value'],
        })

    return JSONResponse(dataset_list)



@router.get("/get-dataset-classes", name="Get dataset classes",
    description="Retrieve the list of classes in a SPARQL endpoint indexed in Shapes of You",
    response_model=dict,
)            
def get_dataset_classes(dataset: str = "https://bio2rdf.org/sparql") -> dict:
    results = {'classes': [], 'predicates': []}
    sparql = SPARQLWrapper(METADATA_ENDPOINT)
    sparql.setReturnFormat(JSON)

    get_properties_query = PREFIXES + """
    SELECT DISTINCT ?predicate (SUM(?partitionTriples) AS ?triplesCount)
    WHERE {
    GRAPH <""" + dataset + """> {
        ?graph void:propertyPartition ?propertyPartition . 
        ?propertyPartition void:property ?predicate .
        ?propertyPartition void:triples ?partitionTriples .
    } } GROUP BY ?predicate ORDER BY DESC(?triplesCount)"""

    sparql.setQuery(get_properties_query)
    sparqlwrapper_results = sparql.query().convert()
    sparql_results = sparqlwrapper_results["results"]["bindings"]

    for result in sparql_results:
        results['predicates'].append({
            'uri': result['predicate']['value'],
            'triples_count': result['triplesCount']['value'],
        })


    get_classes_query = PREFIXES + """
    SELECT DISTINCT ?class (SUM(?partitionCount) AS ?triplesCount)
    WHERE {
    {
    GRAPH <""" + dataset + """> {
        ?graph void:propertyPartition ?propertyPartition . 
        ?propertyPartition void:property ?predicate .
        {
            ?propertyPartition void:classPartition [
            void:class ?class ;
            void:distinctSubjects ?partitionCount ;
            ] .
        } UNION {
            ?propertyPartition void-ext:objectClassPartition [
                void:class ?class ;
                void:distinctObjects ?partitionCount ;
            ] .
        }
    }
    } UNION {
      ?dataset dct:hasPart ?class .
  	  	FILTER(?dataset = <""" + dataset + """>)
    }
    } GROUP BY ?class ORDER BY DESC(?triplesCount)
    """

    sparql.setQuery(get_classes_query)
    sparqlwrapper_results = sparql.query().convert()
    sparql_results = sparqlwrapper_results["results"]["bindings"]

    for result in sparql_results:
        results['classes'].append({
            'uri': result['class']['value'],
            'triples_count': result['triplesCount']['value'],
        })

    return JSONResponse(results)



detailed_metadata_query = PREFIXES + """
SELECT DISTINCT ?endpoint ?graph ?subjectCount ?subject ?predicate ?objectCount ?object
WHERE {
GRAPH ?endpoint {
    # ?graph a void:Dataset .
    ?graph void:propertyPartition ?propertyPartition . 
    ?propertyPartition void:property ?predicate ;
    void:classPartition [
        void:class ?subject ;
        void:distinctSubjects ?subjectCount ;
    ] .
    
    OPTIONAL {
    ?propertyPartition void-ext:objectClassPartition [
    void:class ?object ;
    void:distinctObjects ?objectCount ;
    ]
    }
}
# FILTER (?sparql_endpoint = ?_sparqlendpoint_iri)
} ORDER BY DESC(?subjectCount)
"""
