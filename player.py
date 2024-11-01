import pygame

class Player:
    def __init__(self):
        # โหลดรูปภาพเต๋าสำหรับตัวผู้เล่น
        self.image = pygame.image.load("bttt.png")  # สมมุติว่าชื่อไฟล์คือ bttt.png
        self.image = pygame.transform.scale(self.image, (40, 40))  # ปรับขนาดเป็น 40x40
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 300, 580  # ตำแหน่งเริ่มต้นของผู้เล่น

    def go_up(self):
        self.rect.y -= 20

    def go_down(self):
        self.rect.y += 20

    def go_left(self):
        self.rect.x -= 20

    def go_right(self):
        self.rect.x += 20

    def go_to_start(self):
        self.rect.y = 580  # รีเซ็ตตำแหน่งเมื่อกลับไปเริ่มต้น
        self.rect.x = 300  # รีเซ็ตตำแหน่งเริ่มต้นทางแนวนอน

    def is_at_finish_line(self):
        return self.rect.y <= 0
