from beverages.models.schemas import BeverageSchema, BeverageSchemaIn, BeverageSchemaUpdate
from beverages.controllers import BeveragesController

from fastapi import HTTPException, APIRouter


beverage_router = APIRouter(tags=['beverages'], prefix='/api/beverages')


@beverage_router.get("", response_model=list[BeverageSchema], summary='Endpoint for retrieving all beverages',
         response_description='List of available beverages in database')
def get_all_beverages():
    return BeveragesController.get_all_beverages()


@beverage_router.get("/id/{beverage_id}", response_model=BeverageSchema)
def get_beverage_by_id(beverage_id: int):
    return BeveragesController.get_beverage_by_id(beverage_id)


@beverage_router.get("/name", response_model=BeverageSchema)
def find_beverage_by_name(name: str = None):
    if name is None:
        raise HTTPException(status_code=400, detail="No name to look for is provided")
    response = BeveragesController.find_beverage_by_name(name)
    return response


@beverage_router.post("", response_model=BeverageSchema)
def create(beverage: BeverageSchemaIn):
    response = BeveragesController.create(**beverage.__dict__)
    return response


@beverage_router.put("/{id}", response_model=BeverageSchema)
def update(beverage_id: int, update_data: BeverageSchemaUpdate):
    return BeveragesController.update_beverage(update_data.__dict__, beverage_id)


@beverage_router.delete("/{beverage_id}")
def delete(beverage_id: int):
    try:
        BeveragesController.delete_beverage(beverage_id)
        return {"message": "Beverage successfully deleted."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
