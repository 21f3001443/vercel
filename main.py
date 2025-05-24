# main.py
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    data = ''
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)
    return json.dumps(data)
