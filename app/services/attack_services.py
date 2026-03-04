from app.database import neo4j_db

def find_attack_path(entry, target):
    query = """
    MATCH path = (start {name: $entry})-[*1..5]->(end {name: $target})
    RETURN path
    """
    return neo4j_db.execute_query(query, {"entry": entry, "target": target})