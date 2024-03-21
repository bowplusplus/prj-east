from prefect import task

class Car():
    def __init__(self, make, model, year, initioal_speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = initioal_speed
    
    def accelerate(self, increase):
        self.speed += increase
        return self.speed
