import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()

    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 将事件循环替换为对函数check_events()的调用
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()

            # 每次循环时都要重绘屏幕
            # 调用screen.fill()方法,用背景色填充屏幕,该方法只接受一个实参:一个中颜色
            # screen.fill(ai_settings.bg_color)
            # ship.blitme()

            # 让最近绘制的屏幕可见
            # pygame.display.flip()
            # 将alien_invasion.py的while循环中更新的代码替换为对函数update_screen()的调用
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
