from fastapi import FastAPI, Query
import json

app = FastAPI()

@app.get("/")
def read_root(name = list[str] = Query(...)):
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)

    _ = {
        "marks": [entry["marks"] for entry in data if entry["name"] in ['tpQ', '2UOWSLOtV1']]
    }
    return name
