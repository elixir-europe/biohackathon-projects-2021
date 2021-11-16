from SPARQLWrapper import SPARQLWrapper, TURTLE, XML, JSON

# Get HCLS metadata for the Bio2RDF SPARQL endpoint from the Shapes of You triplestore

shapesofyou_endpoint = 'https://graphdb.dumontierlab.com/repositories/shapes-registry'

analyze_endpoint = 'https://bio2rdf.org/sparql'

sparql_query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX bl: <http://w3id.org/biolink/vocab/>
PREFIX dctypes: <http://purl.org/dc/dcmitype/>
PREFIX idot: <http://identifiers.org/idot/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX void-ext: <http://ldf.fi/void-ext#>
SELECT DISTINCT ?graph ?subjectCount ?subject ?predicate ?objectCount ?object
WHERE {
  GRAPH <""" + analyze_endpoint + """> {
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

print(f'Getting HCLS metadata for {analyze_endpoint}')
print(sparql_query)

sparql = SPARQLWrapper(shapesofyou_endpoint)
sparql.setReturnFormat(JSON)
sparql.setQuery(sparql_query)
sparqlwrapper_results = sparql.query().convert()

sparql_results = sparqlwrapper_results["results"]["bindings"]
for result in sparql_results:
    graph = result['graph']['value']
    subject = result['subject']['value']
    subjectCount = result['subjectCount']['value']
    predicate = result['predicate']['value']
    if 'object' in result.keys():
        object = result['object']['value']
        objectCount = result['objectCount']['value']

        # Only print when more than 1 subject/object count
        if int(subjectCount) > 1 and int(objectCount) > 1:
            print(f'In {graph} : {subjectCount} {subject} - {predicate} - {objectCount} {object}')
            print('')