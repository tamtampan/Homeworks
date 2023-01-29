from device_models.models.dao import DeviceModel


class DeviceModelsRepository:
    def __init__(self, my_cursor):
        self.my_cursor = my_cursor

    def read_all(self) -> list:
        """ Returns all device models from database as list of objects. """

        sql = "SELECT device_model_id, model_name, model_number, water_capacity_liters, coffee_capacity_kgs, " \
              "milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count " \
              "FROM device_model LIMIT 1000;"
        self.my_cursor.execute(sql)
        results = self.my_cursor.fetchall()
        device_models = []
        for row in results:
            device_models.append(DeviceModel(device_model_id=row[0], model_name=row[1], model_number=row[2],
                                             water_capacity_liters=row[3], coffee_capacity_kgs=row[4],
                                             milk_capacity_kgs=row[5], sugar_capacity_kgs=row[6],
                                             sweetener_capacity_count=row[7], cups_capacity_count=row[8]))
        return device_models

    def get_by_id(self, device_model_id: int) -> "DeviceModel":
        """ Returns device model with specific id from database as object. """

        sql = "SELECT device_model_id, model_name, model_number, water_capacity_liters, coffee_capacity_kgs, " \
              "milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count " \
              "FROM device_model WHERE device_model_id = (%s);"
        val = (device_model_id,)
        self.my_cursor.execute(sql, val)
        result = self.my_cursor.fetchone()
        if result:
            return DeviceModel(device_model_id=result[0], model_name=result[1], model_number=result[2],
                               water_capacity_liters=result[3], coffee_capacity_kgs=result[4],
                               milk_capacity_kgs=result[5], sugar_capacity_kgs=result[6],
                               sweetener_capacity_count=result[7], cups_capacity_count=result[8])
        else:
            raise Exception(F"There is no model with {device_model_id} id.")

    def create(self, model_name: str, model_number: str, water_capacity_liters: float, coffee_capacity_kgs: float,
               milk_capacity_kgs: float, sugar_capacity_kgs: float, sweetener_capacity_count: int,
               cups_capacity_count: int) -> "DeviceModel":
        """ Inserts new device model into database and returns new device model as object. """

        sql = "INSERT INTO device_model (model_name, model_number, water_capacity_liters, coffee_capacity_kgs, " \
              "milk_capacity_kgs, sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count) VALUES (%s, %s," \
              " %s, %s, %s, %s, %s, %s);"
        vals = (model_name, model_number, water_capacity_liters, coffee_capacity_kgs, milk_capacity_kgs,
                sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count)
        self.my_cursor.execute(sql, vals)
        device_model_id = self.my_cursor.lastrowid
        return DeviceModel(device_model_id=device_model_id, model_name=model_name, model_number=model_number,
                           water_capacity_liters=water_capacity_liters, coffee_capacity_kgs=coffee_capacity_kgs,
                           milk_capacity_kgs=milk_capacity_kgs, sugar_capacity_kgs=sugar_capacity_kgs,
                           sweetener_capacity_count=sweetener_capacity_count, cups_capacity_count=cups_capacity_count)

    def delete(self, device_model_id: int) -> bool:
        """ Deletes device model in database by id, returns True if deleted. """

        sql = "DELETE FROM device_model WHERE device_model_id = (%s)"
        val = (device_model_id,)
        try:
            self.my_cursor.execute(sql, val)
            return True
        except Exception:
            raise Exception(f"Delete failed. Device model with provided ID {device_model_id} was not found.")

    def update(self, attributes_dict, device_model_id) -> "DeviceModel":
        """ Updates device model values in database and returns device model as object if exists. """

        string_with_attributes = ""
        for attribute in attributes_dict:
            string_with_attributes += f'{attribute} = "{attributes_dict[attribute]}",'
        string_with_attributes = string_with_attributes[:-1]
        sql = "UPDATE device_model SET " + string_with_attributes + f" WHERE device_model_id = {device_model_id}"
        self.my_cursor.execute(sql)
        if self.my_cursor.rowcount == 0:
            raise Exception("Not updated.")
        elif self.my_cursor.rowcount == 1:
            return self.get_by_id(device_model_id)

