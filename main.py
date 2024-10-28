import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from item import Item  # นำเข้า Item
import pygame
import random

# ตั้งค่าเสียง
pygame.mixer.init()
jump_sound = pygame.mixer.Sound("woosh-230554.mp3")
crash_sound = pygame.mixer.Sound("sword-hit-7160.mp3")

# ตั้งค่า Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgpic("water.gif")

# สร้างวัตถุต่างๆ ของเกม
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
items = [Item() for _ in range(5)]  # สร้างไอเท็มหลายชิ้น

# ฟังก์ชันดึงคะแนนสูงสุดจากไฟล์
def get_top_score():
    try:
        with open("scores.txt") as file:
            scores = [int(score.strip()) for score in file.readlines()]
        top_score = max(scores) if scores else 0
        return top_score
    except FileNotFoundError:
        return 0

# ฟังก์ชันบันทึกคะแนน
def save_score(score):
    with open("scores.txt", mode="a") as file:
        file.write(f"{score}\n")
    
    with open("scores.txt") as file:
        scores = [int(line.strip()) for line in file]
    
    top_score = max(scores)
    scores = [s for s in scores if s >= top_score]

    with open("scores.txt", "w") as file:
        for s in scores:
            file.write(f"{s}\n")

# ฟังก์ชันแสดงท็อปสกอร์และคะแนนล่าสุดที่ด้านล่างของหน้าจอหลังจบเกม
def display_scores(latest_score):
    top_score = get_top_score()
    y_position = -250  # แสดงที่ด้านล่าง
    screen.tracer(0)
    scoreboard.display_top_score(f"Top Score: {top_score}", y_position)
    y_position -= 30
    scoreboard.display_top_score(f"Latest Score: {latest_score}", y_position)
    screen.update()

# สร้างตัวแปรปุ่มเป็น global
go_button = None
end_button = None

# ฟังก์ชันแสดงปุ่ม "Go" และ "End" เมื่อจบเกม
def display_buttons():
    global go_button, end_button
    go_button = Turtle()
    go_button.shape("square")
    go_button.color("green")
    go_button.penup()
    go_button.goto(-50, -200)
    go_button.write("Go", align="center", font=("Arial", 16, "bold"))
    go_button.onclick(start_game)

    end_button = Turtle()
    end_button.shape("square")
    end_button.color("red")
    end_button.penup()
    end_button.goto(50, -200)
    end_button.write("End", align="center", font=("Arial", 16, "bold"))
    end_button.onclick(exit_game)

# ฟังก์ชันซ่อนปุ่ม "Go" และ "End"
def hide_buttons():
    global go_button, end_button
    if go_button is not None:
        go_button.hideturtle()
        go_button.clear()
    if end_button is not None:
        end_button.hideturtle()
        end_button.clear()

# ฟังก์ชันเริ่มเกมใหม่
def start_game(x=None, y=None):
    global game_is_on
    hide_buttons()  # ซ่อนปุ่มเมื่อเริ่มเกมใหม่
    player.go_to_start()
    car_manager.reset()
    scoreboard.reset()
    for item in items:
        item.refresh()  # ย้ายไอเท็มทั้งหมดไปที่ตำแหน่งใหม่
    game_is_on = True

# ฟังก์ชันออกจากเกม
def exit_game(x=None, y=None):
    screen.bye()

# ฟังก์ชันให้เต่าเคลื่อนที่ขึ้นและเล่นเสียง jump_sound
def go_up_with_sound():
    jump_sound.play()
    player.go_up()

# ตั้งค่าการควบคุม
screen.listen()
screen.onkey(go_up_with_sound, "Up")

# เริ่มเกม
game_is_on = True
slow_duration = 5
slow_effect_end_time = 0

while True:
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        
        # ตรวจสอบเอฟเฟกต์การชะลอความเร็ว
        current_time = time.time()
        if current_time > slow_effect_end_time:
            car_manager.move_cars()
        else:
            for car in car_manager.all_cars:
                car.backward(car_manager.car_speed / 2)

        # เคลื่อนที่ไอเท็มจากขวาไปซ้าย
        for item in items:
            item.move_item()

            # ตรวจจับการเก็บไอเท็ม
            if player.distance(item) < 20:
                item.refresh()  # ย้ายไอเท็มไปที่ใหม่
                slow_effect_end_time = current_time + slow_duration

            # ถ้าไอเท็มถึงขอบซ้าย ให้รีเซ็ตตำแหน่ง
            if item.xcor() < -300:
                item.refresh()

        # ตรวจจับการชนกับรถ
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                crash_sound.play()
                scoreboard.game_over()
                latest_score = scoreboard.score
                save_score(latest_score)
                display_scores(latest_score)
                display_buttons()  # แสดงปุ่ม "Go" และ "End" ที่จบเกม

        # ตรวจสอบว่าผู้เล่นถึงเส้นชัย
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()  # อัปเดตคะแนนที่ด้านบนขณะเล่นเกม

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
