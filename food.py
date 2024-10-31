# food.py

import pygame
import random

class Food:
    def __init__(self):
        # สร้างพื้นผิวของ Pygame สำหรับไอเท็มอาหาร (เช่น วงกลมขนาด 20x20)
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)  # พื้นหลังโปร่งใส
        self.draw_food()

        # ตั้งค่าตำแหน่งเริ่มต้นแบบสุ่ม
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(600, 800)  # เริ่มอยู่นอกจอทางขวา
        self.rect.y = random.randint(0, 580)

    def draw_food(self):
        # วาดไอเท็มอาหารเป็นวงกลมสีเขียว
        pygame.draw.circle(self.image, (0, 255, 0), (10, 10), 10)  # วงกลมสีเขียวเพื่อแทนอาหาร

    def move_food(self):
        # เลื่อนอาหารไปทางซ้ายของจอ
        self.rect.x -= 5  # ปรับความเร็วตามต้องการ

    def refresh(self):
        # รีเซ็ตตำแหน่งของอาหารให้อยู่นอกจอทางขวา
        self.rect.x = random.randint(600, 800)
        self.rect.y = random.randint(0, 580)
