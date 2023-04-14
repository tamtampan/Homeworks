from pydantic import BaseModel

class DeviceModelProducesBeverageSchema(BaseModel):
    device_model_id: int
    beverage_id: int