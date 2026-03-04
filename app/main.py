from fastapi import FastAPI
from app.database import neo4j_db

app = FastAPI()

@app.get("/test-db")
def test_db():
    query = "RETURN 'Neo4j Connected' AS message"
    return neo4j_db.execute_query(query)

@app.post("/add-device")
def create_device(name: str):
    return add_device(name)
