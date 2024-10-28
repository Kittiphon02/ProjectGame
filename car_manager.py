from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_IMAGE = "yy.gif" # ใช้ภาพที่ลดขนาดแล้ว

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

        # ลงทะเบียนภาพรถที่ลดขนาดเพื่อใช้ใน Turtle
        screen = Screen()
        screen.addshape(CAR_IMAGE)

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle(CAR_IMAGE)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def reset(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
