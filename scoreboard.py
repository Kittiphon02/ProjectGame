from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 270)  # กำหนดให้คะแนนอยู่ด้านบนระหว่างเล่น
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)  # ให้คะแนนอัปเดตที่ด้านบน
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        self.score = 0
        self.update_scoreboard()

    # ฟังก์ชันแสดงท็อปสกอร์หลังจบเกมที่ด้านล่าง
    def display_top_score(self, text, y_position):
        self.goto(0, y_position)
        self.write(text, align="center", font=("Arial", 18, "normal"))
