from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from beverage import Beverage
from typing import Optional

app = FastAPI()


class BeverageSchema(BaseModel):
    beverage_id: int
    name: str
    price: float
    water_qty: float
    milk_qty: float
    coffee_qty: float

    class Config:
        orm_mode = True


class BeverageSchemaIn(BaseModel):
    name: str
    price: float
    water_qty: float
    milk_qty: float
    coffee_qty: float

    class Config:
        orm_mode = True


class BeverageSchemaUpdate(BaseModel):
    name: Optional[str]
    price: Optional[float]
    water_qty: Optional[float]
    milk_qty: Optional[float]
    coffee_qty: Optional[float]

    class Config:
        orm_mode = True


@app.get("/api/beverages", response_model=list[BeverageSchema])
def get_all_beverages():
    all_beverages = Beverage.read_all_beverages()
    # all_beverages_lst = []
    # for beverage in all_beverages:
    #     all_beverages_lst.append(BeverageSchema(**beverage.__dict__))
    return all_beverages


@app.get("/api/beverages/{beverage_id}", response_model=BeverageSchema)
def get_beverage_by_id(beverage_id: int):
    """Ova funkcija trba da nam vrati beverage po id-ju."""
    try:
        return Beverage.find_beverage_by_id(beverage_id)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Beverage with provided id not found.")


@app.post("/api/beverages", response_model=BeverageSchema)
def create_beverage(beverage: BeverageSchemaIn):
    return Beverage.create_beverage(beverage_name=beverage.name, price=beverage.price,
                                    water_quantity_milliliters=beverage.water_qty,
                                    milk_quantity_grams=beverage.milk_qty,
                                    cofee_quantity_grams=beverage.coffee_qty)

#
# @app.put("/api/beverages/{beverage_id}", response_model=BeverageSchema)
# def update_beverage(beverage_id: int, update_beverage: BeverageSchemaUpdate):
#     beverage = Beverage.find_beverage_by_id(beverage_id)
#     return beverage.update_beverage
