import pytest
from Model import Car
from Flow import car_flow, task_get_a_car

def test_car_flow():
    speed = car_flow()
    assert speed == 10

def test_car_task():
    assert isinstance(task_get_a_car.fn('3BodyProblem', 'RedCar', 2015, 0), Car)

