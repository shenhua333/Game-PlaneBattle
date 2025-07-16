# -*- coding: utf-8 -*-
# @Time    : 2023/10/24 024 19:56
# @Author  : 神话
# @FileName: 6.py
# @Software: PyCharm
import pygame
from 飞机大战 import sprite_and_sprite_group
import random
#敌机出场事件代号
ENEMY_EVENT = pygame.USEREVENT
#子弹出现
FIRE = pygame.USEREVENT+1
class PlaneGame:
    def __init__(self):
        print('游戏初始化中...')
        #创建游戏窗口
        self.screen = pygame.display.set_mode((480,700))
        #创建时钟对象
        self.clock = pygame.time.Clock()
        #调用私有方法，创建精灵和精灵组
        self.__create_sprites()
        #定时器
        pygame.time.set_timer(ENEMY_EVENT,1000)
        pygame.time.set_timer(FIRE,500)
        self.sum = 0
    # 创建精灵和精灵组
    def __create_sprites(self):
        #背景精灵和精灵组
        # self.bg1 = sprite_and_sprite_group.Background('images/background.png')
        # self.bg2 = sprite_and_sprite_group.Background('images/background.png')
        # self.bg2.rect.y = -self.bg2.rect.height
        self.bg1 = sprite_and_sprite_group.Background()
        self.bg2 = sprite_and_sprite_group.Background(True)
        self.bg_group = pygame.sprite.Group()
        self.bg_group.add(self.bg1,self.bg2)
        #敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        #英雄飞机精灵组
        self.hero = sprite_and_sprite_group.Hero('images/me1.png')
        self.hero_group = pygame.sprite.Group()
        self.hero_group.add(self.hero)
        self.hero_group2 = pygame.sprite.Group()
    #事件监听
    def __event_handler(self):
        #获取按键
        keypressed = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        if keypressed[pygame.K_RIGHT] or keypressed[pygame.K_d]:#右方向键
            self.hero.speed = 2
        elif keypressed[pygame.K_LEFT] or keypressed[pygame.K_a]:#左方向键
            self.hero.speed = -2
        elif keypressed[pygame.K_UP] or keypressed[pygame.K_w]:
            self.hero.up = -2
        elif keypressed[pygame.K_DOWN] or keypressed[pygame.K_s]:
            self.hero.up = 2
        else:
            self.hero.speed = 0
            self.hero.up = 0
        if  mouse_buttons[2]:
            self.hero.up = -3
        # elif mouse_buttons[0]:
        #     self.hero.fire()


        for evnet in pygame.event.get():
            if evnet.type == ENEMY_EVENT:
                # print('diji')
                #创建敌机精灵，添加到精灵组
                enemy1 = sprite_and_sprite_group.Enemy('images/enemy1.png')
                self.enemy_group.add(enemy1)
                if self.sum >= 1e3:
                    enemy2 = sprite_and_sprite_group.Enemy('images/enemy2.png')
                    enemy2.speed = random.randint(3,8)
                    self.enemy_group.add(enemy2, )
                    hero2 = sprite_and_sprite_group.Enemy('images/me2.png')
                    self.hero_group2.add(hero2)

                elif self.sum >= 2e3:
                    enemy3 = sprite_and_sprite_group.Enemy('images/enemy3_n2.png')
                    enemy3.speed = random.randint(5,15)
                    self.enemy_group.add(enemy3)
                    # hero2 = sprite_and_sprite_group.Enemy('images/enemy2.png')
                    # self.hero_group2.add(hero2)
            elif evnet.type == FIRE:
                self.hero.fire()
            elif evnet.type == pygame.QUIT:
                pygame.quit()

    #碰撞检测
    def __check_coolide(self):
        #子弹和敌机
        pygame.sprite.groupcollide(self.hero.bullet_group,
                                   self.enemy_group,True,True)
        #print(ret1)
        #敌机和英雄
        ret1 = pygame.sprite.groupcollide(self.hero_group,
                                   self.enemy_group,True,True)
        if ret1:
            print(f'恭喜您获得{self.sum}积分')
            pygame.quit()

        self.ret2 = pygame.sprite.groupcollide(self.hero_group, self.hero_group2, False, True)
        if len(self.ret2):
            for i in range(3):
                bullet = sprite_and_sprite_group.Bullet('images/bullet_supply.png')
                bullet.rect.centerx = self.hero.rect.centerx
                bullet.rect.y = self.hero.rect.y - i * 60
                self.hero.bullet_group.remove()
                self.hero.bullet_group.add(bullet)

    #更新/绘制精灵组
    def __update_sprite(self):
        #背景
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.hero_group2.update()
        self.hero_group2.draw(self.screen)
        #敌机
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        #英雄飞机
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        #子弹
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
    def star_game(self):
        print('游戏开始')
        while 1:

            #刷新帧率
            self.clock.tick(60)
            self.sum += random.randint(1,5)
            #事件监听
            self.__event_handler()

            #碰撞检测
            self.__check_coolide()
            #更新/绘制精灵组
            self.__update_sprite()
            #更新屏幕显示
            pygame.display.update()























