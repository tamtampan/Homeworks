from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from device_model import DeviceModel

app = FastAPI()


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


@app.get("/api/devices", response_model=list[DeviceModelSchema])
def get_all_devices():
    """Returns all device models from database."""
    all_devices = DeviceModel.read_all()
    return all_devices


@app.get("/api/devices/{device_model_id}", response_model=DeviceModelSchema)
def get_device_by_id(device_model_id: int):
    """Returns device model by id from database."""
    try:
        return DeviceModel.get_by_id(device_model_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Device model with provided ID not found.")


@app.post("/api/devices", response_model=DeviceModelSchema)
def create_device_model(device_model: DeviceModelSchemaIn):
    """Creates new device model in database."""
    return DeviceModel.create(model_name=device_model.model_name, model_number=device_model.model_number,
                              water_capacity_liters=device_model.water_capacity_liters,
                              coffee_capacity_kgs=device_model.coffee_capacity_kgs,
                              milk_capacity_kgs=device_model.milk_capacity_kgs,
                              sugar_capacity_kgs=device_model.sugar_capacity_kgs,
                              sweetener_capacity_count=device_model.sweetener_capacity_count,
                              cups_capacity_count=device_model.cups_capacity_count)


@app.put("/api/devices/{device_model_id}", response_model=DeviceModelSchema)
def update_device_model(device_model_id: int, update_device: DeviceModelSchemaUpdate):
    """Updates device model in database."""
    try:
        device = DeviceModel.get_by_id(device_model_id=device_model_id)
        update_device_dict = update_device.__dict__
        for key in update_device_dict.copy():
            if update_device_dict[key] is None:
                del update_device_dict[key]

        return device.update(attributes_dict=update_device_dict)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Input not valid.")


@app.delete("/api/devices/{device_model_id}")
def delete_device(device_model_id: int):
    """Deletes device model from database."""
    try:
        flag = DeviceModel.delete(device_model_id=device_model_id)
        if flag:
            raise HTTPException(status_code=200, detail="Successful delete.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.__str__())
