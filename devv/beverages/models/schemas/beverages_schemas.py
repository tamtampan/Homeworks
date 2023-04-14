from typing import Optional
from pydantic import BaseModel


class BeverageSchema(BaseModel):
    beverage_id: int
    beverage_name: str
    price: float
    water_quantity_milliliters: float
    milk_quantity_grams: float
    cofee_quantity_grams: float

    class Config:
        orm_mode = True


class BeverageSchemaIn(BaseModel):
    beverage_name: str
    price: float
    water_quantity_milliliters: float
    milk_quantity_grams: float
    cofee_quantity_grams: float

    class Config:
        orm_mode = True


class BeverageSchemaUpdate(BaseModel):
    beverage_name: Optional[str]
    price: Optional[float]
    water_quantity_milliliters: Optional[float]
    milk_quantity_grams: Optional[float]
    cofee_quantity_grams: Optional[float]

    class Config:
        orm_mode = True
        
