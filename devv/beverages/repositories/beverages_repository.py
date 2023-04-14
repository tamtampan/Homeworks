from beverages.models.dao import Beverage


class BeveragesRepository:
    def __init__(self, my_cursor):
        self.my_cursor = my_cursor

    def read_all_beverages(self):
        sql = """SELECT beverage_id, beverage_name, price, water_quantity_milliliters, milk_quantity_grams, 
        cofee_quantity_grams FROM beverage;"""
        self.my_cursor.execute(sql)
        result = self.my_cursor.fetchall()
        beverages = []
        for row in result:
            print(row)
            beverages.append(Beverage(*row))
        return beverages

    def find_beverage_by_id(self, beverage_id: int):
        sql = f"""SELECT beverage_id, beverage_name, price, water_quantity_milliliters, milk_quantity_grams, 
        cofee_quantity_grams FROM beverage WHERE beverage_id = %s;"""
        val = (beverage_id,)
        self.my_cursor.execute(sql, val)
        result = self.my_cursor.fetchall()
        if result:
            return Beverage(*result[0])
        else:
            raise ValueError(f"Not valid ID: {beverage_id}")

    def find_beverage_by_name(self, name: str):
        sql = f"""SELECT beverage_id, beverage_name, price, water_quantity_milliliters, milk_quantity_grams, 
        cofee_quantity_grams FROM beverage WHERE LOWER(beverage_name) = %s;"""
        val = (name.lower(),)
        self.my_cursor.execute(sql, val)
        result = self.my_cursor.fetchall()
        if result:
            return Beverage(*result[0])
        else:
            raise ValueError(f"Not valid name: {name}")

    def create_beverage(self, beverage_name, price, water_quantity_milliliters, milk_quantity_grams,
                        cofee_quantity_grams):
        sql = """INSERT INTO beverage (beverage_name, price, water_quantity_milliliters, milk_quantity_grams, 
        cofee_quantity_grams) VALUES (%s, %s, %s, %s, %s)"""
        values = [beverage_name, price, water_quantity_milliliters, milk_quantity_grams, cofee_quantity_grams]
        self.my_cursor.execute(sql, values)
        beverage_id = self.my_cursor.lastrowid
        return Beverage(*([beverage_id]+values))

    def delete_beverage(self, beverage_id):
        sql = """DELETE FROM beverage WHERE beverage_id = (%s);"""
        val = (beverage_id,)
        try:
            self.my_cursor.execute(sql, val)
            if self.my_cursor.rowcount == 0:
                raise ValueError('Beverage with provided ID is not found in database.')
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Database error occurred while deleting beverage") from e

    def update_beverage(self, attributes_dict, beverage_id):
        string_with_attributes = " "
        for attribute in attributes_dict:
            string_with_attributes += f"{attribute} = '{attributes_dict[attribute]}',"
        string_with_attributes = string_with_attributes[:-1]
        sql = "UPDATE beverage SET " + string_with_attributes + f" WHERE beverage_id = {beverage_id}"
        self.my_cursor.execute(sql)
        if self.my_cursor.rowcount == 0:
            raise Exception("Error during update")
        elif self.my_cursor.rowcount == 1:
            return self.find_beverage_by_id(beverage_id)
