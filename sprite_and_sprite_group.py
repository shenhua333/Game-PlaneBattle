# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 025 17:22
# @Author  : 神话
# @FileName: sprite_and_sprite_group.py
# @Software: PyCharm
import pygame
import random
from 飞机大战 import plane_battle
class Sprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()
        #图像数据
        self.image = pygame.image.load(image_name)

        self.rect = self.image.get_rect()
        self.speed =speed

    def update(self):
        self.rect.y += self.speed


#背景类
class Background(Sprite):
    def __init__(self,is_scend=False):
        super().__init__('images/background.png')
        if is_scend:
            self.rect.y = -self.rect.height




    def update(self):
        super().update()
        if self.rect.y >=700:
            self.rect.y = -self.rect.height

#敌机类
class Enemy(Sprite):
    def __init__(self,image_name):
        super().__init__(image_name)

        self.speed = random.randint(2,4)

        self.rect.x = random.randint(0,480-self.rect.width)
    def update(self):
        super().update()
        if self.rect.y >=700:
            self.kill()


#英雄飞机
class Hero(Sprite):
    def __init__(self,image_name,):
        super().__init__(image_name,0)
        self.up = 0
        #设置初始位置
        self.rect.x = 240-self.rect.width/2
        self.rect.y = 700-self.rect.height-100
        self.bullet_group = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 480:
            self.rect.x = 0
        elif self.rect.x <= -self.rect.width:
            self.rect.x = 480-self.rect.width
        self.rect.y += self.up
        if self.rect.y >= 700-self.rect.height:
            self.rect.y = 700-self.rect.height
        elif self.rect.y <= 0:
            self.rect.y = 0
    def fire(self):
        # if len(plane_battle.PlaneGame.ret2):
        #     for i in range(3):
        #         bullet2 = Bullet('images/bullet_supply.png')
        #         bullet2.rect.centerx = self.hero.rect.centerx
        #         bullet2.rect.y = self.hero.rect.y - i * 60
        #         # self.hero.bullet_group.kill(bullet)
        #         self.hero.bullet_group.add(bullet2)
        for i in range(3):
            bullet = Bullet('images/bullet2.png')
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.y = self.rect.y - i*20

            self.bullet_group.add(bullet)

class Bullet(Sprite):
    def __init__(self,image_name):
        super().__init__(image_name,-3)
    def update(self):
        super().update()
        if self.rect.y <= 0-self.rect.height:
            self.kill()