# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Kubernetes"}

@app.get("/error")
def raise_error():
    raise Exception("This is a bad error")
    return {"Hello": "Kubernetes"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/health")
async def healthcheck():
    return JSONResponse({
        "ok": True
    })
