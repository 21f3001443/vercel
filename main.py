from fastapi import FastAPI, Query
import json

app = FastAPI()

@app.get("/api")
def read_root(name: list[str] = Query(...)):
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)

    out = {
        "marks": [entry["marks"] for entry in data if entry["name"] in name]
    }
    return out
