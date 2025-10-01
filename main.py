from fastapi import FastAPI  #framework
from pydantic import BaseModel 
from typing import List


app = FastAPI()

class Home_Class(BaseModel):
    id: int
    name: str
    origin: str
    
data: List[Home_Class] = [] # The type is defined and it will hold the data defined above


@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

@app.get("/about")
def get_data():
    return data

@app.post("/about")
def add_tea(tea: Home_Class):
    data.append(data)
    return tea
@app.put("/about/{home_id}")
def update_tea(home_id: int, updated_home: Home_Class):
    for index, home in enumerate(data):
        if home.id == home_id:
            data[index] = updated_home
            return updated_home
    return {"error": "home not found"}

@app.delete("/about/{home_id}")
def delete_tea(home_id: int):
    for index, home in enumerate(data):
        if home.id == home_id:
            del data[index]
            return {"message": "home deleted"}
    return {"error": "home not found"}