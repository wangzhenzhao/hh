import pygame,sys
from pygame.locals import *
pygame.init()
#创建一个窗口显示系统的访问
screen=pygame.display.set_mode((600,500))
#标题
pygame.display.set_caption('咸鱼斗地主')

#参数 字体（默认）和字体大小
myfont=pygame.font.Font('宋体',20)
#字体颜色取值范围0-255 红色200 0 0
rad = 200,0,0#字体颜色
blue = 0,0,255#背景颜色
white = 255,255,255

#输出内容
ziti = myfont.render('等你好久了快来体验吧',True,rad)
screen.fill(blue)#窗口背景颜色


pos_x=200
pos_y=50
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
     #把字体绘制到窗口二参数为元祖体现字体的位置
    screen.blit(ziti,(100,100))
    # pygame.display.update()

    #画矩形 颜色  位置 大小 width线宽 0 代表填充
    color = white
    pos = pos_x,pos_y
    daxiao = 100,200
    rect = pos,daxiao#位置大小得用一个参数所以把这两个附上一个变量
    width = 0
    #然后用函数画出来
    pygame.draw.rect(screen,color,rect,width)
    pygame.display.update()
