import pygame,sys
from pygame.locals import *
from  math import pi
#初始化pygame
pygame.init()
#设置窗口大小
screen = pygame.display.set_mode((1080,720))
#设置窗口标题
pygame.display.set_caption("斗地主")

#设置背景颜色插入图片
# screen.fill(WHITE)
#my_tupian=pygame.image.load('./122.png')

#让主程序循环
while True:
    #screen.blit(my_tupian,(0,0))
    # pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #获得鼠标位置
    # x,y = pygame.mouse.get_pos()
    # x=mouse_cursor.get_width()
    # y=mouse_cursor.get_height()
    # screen.blit(mouse_cursor(x,y))
    #绘制屏幕内容
    pygame.display.update()
