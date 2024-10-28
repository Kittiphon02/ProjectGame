from turtle import Turtle
import random

class Item(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.move_speed = 5
        self.refresh()

    def refresh(self):
        """สุ่มตำแหน่งเริ่มต้นของไอเท็มด้านขวาของหน้าจอ"""
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)

    def move_item(self):
        """เคลื่อนที่ไอเท็มจากขวาไปซ้าย"""
        self.setx(self.xcor() - self.move_speed)
