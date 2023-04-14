class Beverage:

    def __init__(self, beverage_id: int, beverage_name: str, price: float,
                 water_quantity_milliliters: float, milk_quantity_grams: float, cofee_quantity_grams: float):
        self.beverage_id = beverage_id
        self.beverage_name = beverage_name
        self.price = price
        self.water_quantity_milliliters = water_quantity_milliliters
        self.milk_quantity_grams = milk_quantity_grams
        self.cofee_quantity_grams = cofee_quantity_grams

    def __repr__(self):
        return f"Beverage ID: {self.beverage_id} | {self.beverage_name}"
