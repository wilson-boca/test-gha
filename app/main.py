# Just to run CD 1.0.7
from fastapi import FastAPI
 

app = FastAPI()
 
 
@app.get("/")
async def hello_world():
    return {"message": "Hello World"}
 