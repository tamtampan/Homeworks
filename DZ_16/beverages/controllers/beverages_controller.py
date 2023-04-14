from beverages.services import BeverageServices
from beverages.models.schemas import BeverageSchema


class BeveragesController:

    @staticmethod
    def get_all_beverages():
        all_beverages = BeverageServices.get_all_beverages()
        all_beverages_schemas = []
        for beverage in all_beverages:
            all_beverages_schemas.append(BeverageSchema(**beverage.__dict__))
        return all_beverages_schemas

    @staticmethod
    def get_beverage_by_id(beverage_id: int):
        return BeverageServices.get_beverage_by_id(beverage_id)

    @staticmethod
    def find_beverage_by_name(name: str):
        return BeverageServices.find_beverage_by_name(name)

    @staticmethod
    def create(beverage_name, price, water_quantity_milliliters, milk_quantity_grams,
               cofee_quantity_grams):
        return BeverageServices.create(beverage_name, price, water_quantity_milliliters, milk_quantity_grams,
                                       cofee_quantity_grams)

    @staticmethod
    def delete_beverage(beverage_id: int):
        try:
            BeverageServices.delete_beverage(beverage_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_beverage(attributes_dict: dict, beverage_id: int):
        return BeverageServices.update_beverage(attributes_dict, beverage_id)
