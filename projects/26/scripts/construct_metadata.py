from SPARQLWrapper import SPARQLWrapper, TURTLE, XML, JSON

# Compute HCLS metadata for the Drugbank graph in the Bio2RDF SPARQL endpoint 
# Run a CONSTRUCT query to build RDF for subject type - predicate - object type summary

analyze_endpoint = 'https://bio2rdf.org/sparql'

sparql_query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dqv: <http://www.w3.org/ns/dqv#>
PREFIX hcls: <http://www.w3.org/hcls#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dctypes: <http://purl.org/dc/dcmitype/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX void-ext: <http://ldf.fi/void-ext#>

CONSTRUCT {
  <http://bio2rdf.org/drugbank_resource:bio2rdf.dataset.drugbank.R3> a void:Dataset ;
    void:propertyPartition [
      void:property ?p ;
      void:classPartition [
        void:class ?stype ;
        void:distinctSubjects ?scount ;
      ];
      void-ext:objectClassPartition [
        void:class ?otype ;
        void:distinctObjects ?ocount ;
      ];
    ] .
  ?stype rdfs:label ?slabel .
  ?otype rdfs:label ?olabel .
} WHERE { 
  graph <http://bio2rdf.org/drugbank_resource:bio2rdf.dataset.drugbank.R3> {
    SELECT (COUNT(DISTINCT ?s) AS ?scount) ?stype ?p ?otype  (COUNT(DISTINCT ?o) AS ?ocount)
    { 
      ?s ?p ?o . 
      ?s a ?stype .
      ?o a ?otype .
    } GROUP BY ?p ?stype ?otype 
}
  OPTIONAL { ?stype rdfs:label ?slabel}
  OPTIONAL { ?otype rdfs:label ?olabel}
}
"""

print(f'Getting HCLS metadata for {analyze_endpoint}')
print(sparql_query)

sparql = SPARQLWrapper(analyze_endpoint)
sparql.setReturnFormat(TURTLE)
sparql.setQuery(sparql_query)

results = sparql.query().convert().decode('utf-8')

# Write RDF to file
with open('metadata.ttl', 'w') as f:
    f.write(results)
