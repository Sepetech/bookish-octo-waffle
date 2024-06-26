class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def get_model(self):
        return self.model

    def set_model(self, new_model):
        self.model = new_model

    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, new_manufacturer):
        self.manufacturer = new_manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def set_engine_capacity(self, new_engine_capacity):
        self.engine_capacity = new_engine_capacity

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"{self.model} ({self.year}) by {self.manufacturer}, {self.engine_capacity}L, {self.color}, ${self.price:.2f}"
