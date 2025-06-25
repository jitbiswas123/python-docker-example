from fastapi import FastAPI
import numpy

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
