# main.py
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/api")
def read_root():
    data = ''
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)

    output = {
        "marks": [entry["marks"] for entry in data]
    }
    return json.dumps(output)
