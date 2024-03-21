from prefect import flow, task
from Model import Car

@task
def task_get_a_car(make, model, year, initioal_speed):
    car = Car(make, model, year, initioal_speed)
    return car

@flow
def car_flow():
    red_car = task_get_a_car('3BodyProblem', 'RedCar', 2015, 0)
    speed = red_car.accelerate(10)
    return speed

if __name__ == '__main__':
    speed = car_flow()
    print(speed)