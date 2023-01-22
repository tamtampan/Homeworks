from database_connector import my_cursor


class DeviceModel:
    def __init__(self, device_model_id: int, model_name: str, model_number: str, water_capacity_liters: float,
                 coffee_capacity_kgs: float, milk_capacity_kgs: float, sugar_capacity_kgs: float,
                 sweetener_capacity_count: int, cups_capacity_count: int):
        self.device_model_id = device_model_id
        self.model_name = model_name
        self.model_number = model_number
        self.water_capacity_liters = water_capacity_liters
        self.coffee_capacity_kgs = coffee_capacity_kgs
        self.milk_capacity_kgs = milk_capacity_kgs
        self.sugar_capacity_kgs = sugar_capacity_kgs
        self.sweetener_capacity_count = sweetener_capacity_count
        self.cups_capacity_count = cups_capacity_count

    @staticmethod
    def read_all() -> list:
        """ Returns all device models from database as list of objects. """

        sql = "SELECT device_model_id, model_name, model_number, water_capacity_liters, coffee_capacity_kgs, " \
              "milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count " \
              "FROM device_model LIMIT 1000;"
        my_cursor.execute(sql)
        results = my_cursor.fetchall()
        device_models = []
        for row in results:
            device_models.append(DeviceModel(device_model_id=row[0], model_name=row[1], model_number=row[2],
                                             water_capacity_liters=row[3], coffee_capacity_kgs=row[4],
                                             milk_capacity_kgs=row[5], sugar_capacity_kgs=row[6],
                                             sweetener_capacity_count=row[7], cups_capacity_count=row[8]))
        return device_models

    @staticmethod
    def get_by_id(device_model_id: int) -> "DeviceModel":
        """ Returns device model with specific id from database as object. """

        sql = "SELECT device_model_id, model_name, model_number, water_capacity_liters, coffee_capacity_kgs, " \
              "milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count " \
              "FROM device_model WHERE device_model_id = (%s);"
        val = (device_model_id,)
        my_cursor.execute(sql, val)
        result = my_cursor.fetchone()
        if result:
            return DeviceModel(device_model_id=result[0], model_name=result[1], model_number=result[2],
                               water_capacity_liters=result[3], coffee_capacity_kgs=result[4],
                               milk_capacity_kgs=result[5], sugar_capacity_kgs=result[6],
                               sweetener_capacity_count=result[7], cups_capacity_count=result[8])
        else:
            raise Exception(F"There is no model with {device_model_id} id.")

    @staticmethod
    def create(model_name: str, model_number: str, water_capacity_liters: float, coffee_capacity_kgs: float,
               milk_capacity_kgs: float, sugar_capacity_kgs: float, sweetener_capacity_count: int,
               cups_capacity_count: int) -> "DeviceModel":
        """ Inserts new device model into database and returns new device model as object. """

        sql = "INSERT INTO device_model (model_name, model_number, water_capacity_liters, coffee_capacity_kgs, " \
              "milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count) VALUES (%s, %s," \
              " %s, %s, %s, %s, %s, %s);"
        vals = (model_name, model_number, water_capacity_liters, coffee_capacity_kgs, milk_capacity_kgs,
                sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count)
        my_cursor.execute(sql, vals)
        device_model_id = my_cursor.lastrowid
        return DeviceModel(device_model_id=device_model_id, model_name=model_name, model_number=model_number,
                           water_capacity_liters=water_capacity_liters, coffee_capacity_kgs=coffee_capacity_kgs,
                           milk_capacity_kgs=milk_capacity_kgs, sugar_capacity_kgs=sugar_capacity_kgs,
                           sweetener_capacity_count=sweetener_capacity_count, cups_capacity_count=cups_capacity_count)

    @staticmethod
    def delete(device_model_id: int) -> bool:
        """ Deletes device model in database by id, returns True if deleted. """

        sql = "DELETE FROM device_model WHERE device_model_id = (%s)"
        val = (device_model_id,)
        try:
            my_cursor.execute(sql, val)
            return True
        except Exception as e:
            raise Exception(f"Delete failed. Device model with provided ID {device_model_id} was not found.")

    def update(self, attributes_dict) -> "DeviceModel":
        """ Updates device model values in database and returns device model as object if exists. """

        string_with_attributes = ""
        for attribute in attributes_dict:
            string_with_attributes += f'{attribute} = "{attributes_dict[attribute]}",'
        string_with_attributes = string_with_attributes[:-1]
        sql = "UPDATE device_model SET " + string_with_attributes + f" WHERE device_model_id = {self.device_model_id}"
        my_cursor.execute(sql)
        if my_cursor.rowcount == 0:
            raise Exception("Not updated.")
        elif my_cursor.rowcount == 1:
            return DeviceModel.get_by_id(self.device_model_id)

    def __str__(self) -> str:
        return f"{self.device_model_id} - name: {self.model_name}, number: {self.model_number}, water: " \
               f"{self.water_capacity_liters}l, coffee: {self.coffee_capacity_kgs}kg, milk: {self.milk_capacity_kgs}" \
               f"kg, sugar: {self.sugar_capacity_kgs}kg, sweetener capacity: {self.sweetener_capacity_count}, cups: " \
               f"{self.cups_capacity_count}"
