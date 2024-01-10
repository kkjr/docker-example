from fastapi import FastAPI
from pydantic import BaseModel

class MyModel(BaseModel):
    name: str

app = FastAPI()

@app.post("/hello")
def hello(data: MyModel):
    print(f"Hello, {data.name}")
    return {"message": f"Hello, {data.name}"}