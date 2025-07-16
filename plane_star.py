# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 026 18:58
# @Author  : 神话
# @FileName: plane_star.py
# @Software: PyCharm
import pygame
from 飞机大战 import plane_battle
pygame.init()
if __name__ == '__main__':
    game = plane_battle.PlaneGame()
    game.star_game()
    print(f'恭喜您得到{game.sum}积分'*10)
pygame.quit()



