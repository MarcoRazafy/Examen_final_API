

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


# 3
# a. 
@app.get("/ping")
def ping():
    return "pong"

# b. 
app = FastAPI()

class Characteristics(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristics

cars_db: List[Car] = []
@app.post("/cars", status_code=201)
def create_car(car: Car):
    cars_db.append(car)
    return car

# c. 
@app.get("/cars", response_model=List[Car])
def get_cars():
    return cars_db

# d. 
@app.get("/cars/{id}", response_model=Car)
def get_car(id: str):
    for car in cars_db:
        if car.identifier == id:
            return car
    raise HTTPException(
        status_code=404,
        detail=f"Car with id '{id}' not found"
    )

# e.
@app.put("/cars/{id}/characteristics", response_model=Car)
def update_characteristics(id: str, new_characteristics: Characteristics):
    for car in cars_db:
        if car.identifier == id:
            car.characteristics = new_characteristics
            return car
    raise HTTPException(status_code=404, detail=f"Car with id '{id}' not found")

