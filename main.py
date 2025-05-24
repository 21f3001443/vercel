from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

@app.get("/api")
def read_root(name: List[str] = Query(...)):
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)

    output = {
        "marks": [entry["marks"] for entry in data if entry["name"] in name]
    }
    return output
