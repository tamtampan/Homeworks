from pydantic import BaseModel
from typing import Optional
from beverages.models.schemas import BeverageSchema


class DeviceModelSchema(BaseModel):
    device_model_id: int
    model_name: str
    model_number: str
    water_capacity_liters: float
    coffee_capacity_kgs: float
    milk_capacity_kgs: float
    sugar_capacity_kgs: float
    sweetener_capacity_count: int
    cups_capacity_count: int

    class Config:
        orm_mode = True


class DeviceModelSchemaIn(BaseModel):
    model_name: str
    model_number: str
    water_capacity_liters: float
    coffee_capacity_kgs: float
    milk_capacity_kgs: float
    sugar_capacity_kgs: float
    sweetener_capacity_count: int
    cups_capacity_count: int

    class Config:
        orm_mode = True


class DeviceModelSchemaUpdate(BaseModel):
    model_name: Optional[str]
    model_number: Optional[str]
    water_capacity_liters: Optional[float]
    coffee_capacity_kgs: Optional[float]
    milk_capacity_kgs: Optional[float]
    sugar_capacity_kgs: Optional[float]
    sweetener_capacity_count: Optional[int]
    cups_capacity_count: Optional[int]

    class Config:
        orm_mode = True


class DeviceModelSchemaWithBeverages(BaseModel):
    device_model_id: int
    model_name: str
    model_number: str
    water_capacity_liters: float
    coffee_capacity_kgs: float
    milk_capacity_kgs: float
    sugar_capacity_kgs: float
    sweetener_capacity_count: int
    cups_capacity_count: int
    beverages: list[BeverageSchema]

    class Config:
        orm_mode = True
