# Just to run CD 02
from fastapi import FastAPI
 

app = FastAPI()
 
 
@app.get("/")
async def hello_world():
    return {"message": "Hello World"}
 