from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "CyberRiskneo4j"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def run_query(query, parameters=None):
    with driver.session() as session:
        result = session.run(query, parameters)
        return [record.data() for record in result]
