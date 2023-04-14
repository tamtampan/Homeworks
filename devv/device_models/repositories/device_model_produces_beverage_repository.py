from mysql.connector.cursor import MySQLCursor

from device_models.models.dao import DeviceModelProducesBeverage


class DeviceModelProducesBeverageRepository:
    def __init__(self, my_cursor: MySQLCursor):
        self.my_cursor = my_cursor

    def add_new_beverage_for_device_model(self, device_model_id: int, beverage_id: int):

        sql = """INSERT INTO device_model_produces_beverage (device_model_id, beverage_id) VALUES (%s, %s)"""
        val = (device_model_id, beverage_id)
        self.my_cursor.execute(sql, val)
        # result = self.my_cursor.fetchall()
        if self.my_cursor.rowcount == 1:
            return True
        else:
            return False

    def get_all_beverages_ids_for_device_model(self, device_model_id: int):
        sql = """SELECT beverage_id FROM device_model_produces_beverage WHERE device_model_id = %s """
        val = (device_model_id,)
        self.my_cursor.execute(sql, val)
        result = self.my_cursor.fetchall()
        beverage_ids = []
        for beverage_id_tuple in result:
            beverage_ids.append(DeviceModelProducesBeverage(device_model_id, beverage_id_tuple[0]))
        return beverage_ids
