# main.py
from fastapi import FastAPI, Query
import json
from typing import List

app = FastAPI()

@app.get("/api")
def read_root(filter_names: List[str] = Query(...)):
    data = ''
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)

    output = {
        "marks": [entry["marks"] for entry in data if entry["name"] in filter_names]
    }
    return json.dumps(output)
