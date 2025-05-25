from fastapi import FastAPI, Query, Response
import json

app = FastAPI()

@app.get("/api")
def read_root(name: list[str] = Query(...)):
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)

    out = {
        "marks": [entry["marks"] for entry in data if entry["name"] in name]
    }
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
        "Access-Control-Allow-Credentials": "true",
    }
    return Response(content=out, status_code=200, headers=headers)
