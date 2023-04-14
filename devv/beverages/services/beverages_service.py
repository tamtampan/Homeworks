from beverages.repositories import BeveragesRepository
from database_connector import mydb


class BeverageServices:

    @staticmethod
    def get_all_beverages():
        my_cursor = mydb.cursor()
        beverage_repository = BeveragesRepository(my_cursor=my_cursor)
        result = beverage_repository.read_all_beverages()
        my_cursor.close()
        return result

    @staticmethod
    def get_beverage_by_id(beverage_id: int):
        my_cursor = mydb.cursor()
        beverage_repository = BeveragesRepository(my_cursor=my_cursor)
        result = beverage_repository.find_beverage_by_id(beverage_id)
        my_cursor.close()
        return result

    @staticmethod
    def find_beverage_by_name(name: str):
        my_cursor = mydb.cursor()
        beverage_repository = BeveragesRepository(my_cursor=my_cursor)
        result = beverage_repository.find_beverage_by_name(name)
        my_cursor.close()
        return result

    @staticmethod
    def create(beverage_name, price, water_quantity_milliliters, milk_quantity_grams,
               cofee_quantity_grams):
        my_cursor = mydb.cursor()
        beverage_repository = BeveragesRepository(my_cursor=my_cursor)
        result = beverage_repository.create_beverage(beverage_name, price, water_quantity_milliliters,
                                                     milk_quantity_grams,
                                                     cofee_quantity_grams)
        my_cursor.close()
        return result

    @staticmethod
    def delete_beverage(beverage_id: int):
        my_cursor = None
        try:
            my_cursor = mydb.cursor()
            beverage_repository = BeveragesRepository(my_cursor=my_cursor)
            beverage_repository.delete_beverage(beverage_id)
        except Exception as e:
            raise e
        finally:
            if my_cursor:
                my_cursor.close()

    @staticmethod
    def update_beverage(attributes_dict, beverage_id):
        my_cursor = mydb.cursor()
        beverage_repository = BeveragesRepository(my_cursor=my_cursor)
        result = beverage_repository.update_beverage(attributes_dict, beverage_id)
        my_cursor.close()
        return result
