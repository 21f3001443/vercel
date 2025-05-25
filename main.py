from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)

    output = {
        "marks": [entry["marks"] for entry in data if entry["name"] in ['tpQ', '2UOWSLOtV1']]
    }
    return output
