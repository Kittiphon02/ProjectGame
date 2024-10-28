from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)  # ตั้งให้เต่าหันหน้าไปด้านบน
        self.go_to_start()

    def go_up(self):
        print("Moving up")  # ตรวจสอบการเคลื่อนไหว
        self.forward(MOVE_DISTANCE)  # เคลื่อนที่ไปข้างหน้าในทิศทางด้านบน

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)  # ตั้งให้หันไปทางด้านบนเมื่อเริ่มใหม่
