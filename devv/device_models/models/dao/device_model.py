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

    def __str__(self) -> str:
        return f"{self.device_model_id} - name: {self.model_name}, number: {self.model_number}, water: " \
               f"{self.water_capacity_liters}l, coffee: {self.coffee_capacity_kgs}kg, milk: {self.milk_capacity_kgs}" \
               f"kg, sugar: {self.sugar_capacity_kgs}kg, sweetener capacity: {self.sweetener_capacity_count}, cups: " \
               f"{self.cups_capacity_count}"