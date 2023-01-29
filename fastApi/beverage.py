from connector import my_cursor


class Beverage:

    def __init__(self, beverage_id: int, name: str, price: float, water_qty: float, milk_qty: float, coffee_qty: float):
        self.beverage_id = beverage_id
        self.name = name
        self.price = price
        self.water_qty = water_qty
        self.milk_qty = milk_qty
        self.coffee_qty = coffee_qty

    def __repr__(self):
        return f"Beverage ID: {self.beverage_id} | {self.name}"

    @staticmethod
    def read_all_beverages():
        sql = """SELECT beverage_id, beverage_name, price, water_quantity_milliliters, milk_quantity_grams, cofee_quantity_grams FROM beverage;"""
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        beverages = []
        for row in result:
            print(row)
            beverages.append(Beverage(*row))
        return beverages

    @staticmethod
    def find_beverage_by_id(beverage_id: int):
        sql = f"""SELECT beverage_id, beverage_name, price, water_quantity_milliliters, milk_quantity_grams, cofee_quantity_grams FROM beverage WHERE beverage_id = %s;"""
        val = (beverage_id, )
        my_cursor.execute(sql, val)
        result = my_cursor.fetchall()
        if result:
            return Beverage(*result[0])
        else:
            raise ValueError(f"Not valid ID: {beverage_id}")

    @staticmethod
    def find_beverage_by_name(name: str):
        sql = f"""SELECT beverage_id, beverage_name, price, water_quantity_milliliters, milk_quantity_grams, cofee_quantity_grams FROM beverage WHERE LOWER(beverage_name) = %s;"""
        val = (name.lower(),)
        my_cursor.execute(sql, val)
        result = my_cursor.fetchall()
        if result:
            return Beverage(*result[0])
        else:
            raise ValueError(f"Not valid name: {name}")

    @staticmethod
    def create_beverage(beverage_name, price, water_quantity_milliliters, milk_quantity_grams, cofee_quantity_grams):
        sql = """INSERT INTO beverage (beverage_name, price, water_quantity_milliliters, milk_quantity_grams, cofee_quantity_grams) VALUES (%s, %s, %s, %s, %s)"""
        vals = (beverage_name, price, water_quantity_milliliters, milk_quantity_grams, cofee_quantity_grams)
        my_cursor.execute(sql, vals)
        beverage_id = my_cursor.lastrowid
        return Beverage(beverage_id=beverage_id, name=beverage_name, price=price, water_qty=water_quantity_milliliters, milk_qty=milk_quantity_grams, coffee_qty=cofee_quantity_grams)

    @staticmethod
    def delete_beverage(beverage_id):
        sql = """DELETE FROM beverage WHERE beverage_id = (%s);"""
        val = (beverage_id, )
        try:
            my_cursor.execute(sql, val)

            return True
        except Exception as e:
            raise Exception(f"Delete failed. Beverage with provided ID: {beverage_id} was not found")
