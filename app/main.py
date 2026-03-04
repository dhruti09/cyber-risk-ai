from fastapi import FastAPI
from app.graph_builder import add_device
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Cyber Risk AI System Running"}


@app.post("/add-device")
def create_device(name: str):
    return add_device(name)
