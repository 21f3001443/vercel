from fastapi import FastAPI, Query, Response
import json

app = FastAPI()

@app.get("/api")
def read_root(name: list[str] = Query(...)):
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)

    marks = []
    for n in name:
        for entry in data:
            if entry["name"] == n:
                marks.append(entry["marks"])
                break
    out = {
        "marks": marks
    }
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
        "Access-Control-Allow-Credentials": "true",
    }
    return Response(content=json.dumps(out), media_type="application/json", status_code=200, headers=headers)
