from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/test_endpoint")
async def test_endpoint(data: dict):
    try:
        return {"message": data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
