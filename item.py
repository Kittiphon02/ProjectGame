# item.py

import pygame
import random

class Item:
    def __init__(self):
        # สร้างพื้นผิวของ Pygame สำหรับนาฬิกาให้เล็กลง (เช่น วงกลมขนาด 20x20)
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)  # พื้นหลังโปร่งใส
        self.draw_clock()

        # ตั้งค่าตำแหน่งเริ่มต้นแบบสุ่ม
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(600, 800)  # เริ่มอยู่นอกจอทางขวา
        self.rect.y = random.randint(0, 580)

    def draw_clock(self):
        # วาดขอบวงกลมของนาฬิกาให้เล็กลง
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)  # วงกลมสีขาวเป็นหน้าปัดนาฬิกา
        pygame.draw.circle(self.image, (0, 0, 0), (10, 10), 10, 2)  # ขอบสีดำรอบนอก

        # วาดเข็มนาฬิกา (แบบง่ายๆ ชี้ที่ 12 และ 3 เพื่อให้ดูเหมือนนาฬิกา)
        # เข็มชั่วโมง
        pygame.draw.line(self.image, (0, 0, 0), (10, 10), (10, 5), 2)  # เส้นสั้นสำหรับเข็มชั่วโมง
        # เข็มนาที
        pygame.draw.line(self.image, (0, 0, 0), (10, 10), (15, 10), 1)  # เส้นยาวสำหรับเข็มนาที

    def move_item(self):
        # เลื่อน item ไปทางซ้ายของจอ
        self.rect.x -= 5  # ปรับความเร็วตามต้องการ

    def refresh(self):
        # รีเซ็ตตำแหน่งของ item ให้อยู่นอกจอทางขวา
        self.rect.x = random.randint(600, 800)
        self.rect.y = random.randint(0, 580)
