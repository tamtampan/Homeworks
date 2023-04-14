from fastapi import HTTPException, APIRouter

from device_models.controllers.device_model_controller import DeviceModelsController
from device_models.models.schemas import DeviceModelSchema, DeviceModelSchemaIn, DeviceModelSchemaUpdate, \
    DeviceModelProducesBeverageSchema, DeviceModelSchemaWithBeverages

device_model_router = APIRouter(tags=['device models'], prefix='/api/device-models')


@device_model_router.get("", response_model=list[DeviceModelSchema])
def get_all_device_models():
    return DeviceModelsController.get_all_device_models()


@device_model_router.get("/{device_model_id}", response_model=DeviceModelSchema)
def get_device_model_by_id(device_model_id: int):
    return DeviceModelsController.get_device_model_by_id(device_model_id)


@device_model_router.post("", response_model=DeviceModelSchema)
def create_device_model(device_model: DeviceModelSchemaIn):
    response = DeviceModelsController.create_device_model(**device_model.__dict__)
    return response


@device_model_router.put("/{id}", response_model=DeviceModelSchema)
def update_device_model(beverage_id: int, update_data: DeviceModelSchemaUpdate):
    return DeviceModelsController.update_device_model(update_data.__dict__, beverage_id)


@device_model_router.delete("/{device_model_is}")
def delete_device_model(device_model_id: int):
    try:
        DeviceModelsController.delete_device_model(device_model_id)
        return {"message": "Device model successfully deleted."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@device_model_router.post("/add-beverage-to-device-model", status_code=201, response_model=DeviceModelSchemaWithBeverages)
def add_new_beverage_to_device_model(dev_model_produces_bev: DeviceModelProducesBeverageSchema):
    try:
        DeviceModelsController.add_new_beverage_to_device_model(dev_model_produces_bev.device_model_id,
                                                                   dev_model_produces_bev.beverage_id)
        return DeviceModelsController.get_device_with_list_of_beverages(dev_model_produces_bev.device_model_id)
    except HTTPException as e:
        raise e


@device_model_router.get("/get-device-models-with-beverages/{dev_model_id}", response_model=DeviceModelSchemaWithBeverages)
def get_device_with_list_of_beverages(dev_model_id: int):
    return DeviceModelsController.get_device_with_list_of_beverages(dev_model_id=dev_model_id)

