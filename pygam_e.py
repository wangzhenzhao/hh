#-*- coding: utf-8 -*
import pygame,sys
from pygame.locals import *
from multiprocessing import Process
# import os
class jiem1:
    def __init__(self): 
        self.init=pygame.init()
        #创建一个窗口显示系统的访问
        self.screen = pygame.display.set_mode([1080,720])
        self.title = pygame.display.set_caption('咸鱼斗地主')
        #以下是所需要的一系列图片
        # self.tu1 = pygame.image.load('./bg2.jpg')
        self.my_tupian = pygame.image.load('./bg1.png')
        self.myimage = pygame.image.load('./an.png')
        self.back = pygame.image.load('./back.png')
        self.yinliang = pygame.image.load('./音量.png')
        self.jingyin = pygame.image.load('./静音.png')
        self.buguan = pygame.image.load('./aa/不管.png')
        self.buqiang = pygame.image.load('./aa/不抢.png')
        self.jiaodizhu = pygame.image.load('./aa/jiao.png')
        self.qiangdizhu = pygame.image.load('./aa/login.png')
        self.color = (200,0,0)
        self.color1 = (243,238,39)
        #音效属性
        # self.zhuyinyue = /home/tarena/音乐/bg_game.ogg

    def yinyue(self):
        pygame.mixer.init()
        pygame.mixer.music.load('/home/tarena/音乐/bg_game.ogg')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1,0.0)
        print('正在播放')

    def button(self,msg,x,y,ic,ac,action=None):
        pressed=pygame.mouse.get_pressed()
        mouse_x,mouse_y=pygame.mouse.get_pos()
        if 415<=mouse_x<=594 and 473<=mouse_y<=533:
            fon_t=pygame.font.Font("./SIMSUN.TTC",40)
            text1=fon_t.render(msg,True,ac)
            self.screen.blit(text1,(x,y))
            if pressed[0]==1:
                action()
        else:
            fon_t=pygame.font.Font("./SIMSUN.TTC",40)
            text1=fon_t.render(msg,True,ic)
            self.screen.blit(text1,(x,y))

    def sb(self,x1,x2,y1,y2,x,y,p,hs):
        pressed=pygame.mouse.get_pressed()
        mouse_x,mouse_y=pygame.mouse.get_pos()
        #print(mouse_x,mouse_y)
        if x1<=mouse_x<=x2 and y1<=mouse_y<=y2:
            
            self.screen.blit(p,(x+3,y+3))
            if pressed[0]==1:
                hs()
        else:
            self.screen.blit(p,(x,y))

    def yaobuqi(self):
        
        # pygame.mixer.init()
        # print('正在打开文件')
        pygame.mixer.Sound('/home/tarena/音乐/语音/要不起.wav').play()
        # if sb[6]==self.buguan:
        #     erfen.play()

    def qdz(self):
        pygame.mixer.Sound('/home/tarena/音乐/语音/抢地主.wav').play()

    def jdz(self):
        pygame.mixer.Sound('/home/tarena/音乐/语音/叫地主.wav').play()
        self.jiemia_n()

    def bq(self):
        pygame.mixer.Sound('/home/tarena/音乐/语音/不抢.wav').play()


    def zxh(self):
        
        while True:
            self.screen.blit(self.my_tupian,(0,0))#背景图片 底层
            self.screen.blit(self.myimage,(380,450))#按钮图片第二层
            # self.screen.blit((self.ziti()),(430,475))#字体最上层(表面层)
            self.button('开始游戏',430,475,self.color,self.color1,self.game_loop)
            #获得所有事件
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                # pressed=pygame.mouse.get_pressed()
                # mouse_x,mouse_y=pygame.mouse.get_pos()
                # if pressed[0] == 1 and 415<=mouse_x<=594 and 473<=mouse_y<=533:
                #     print('正在进入游戏')
                #     self.game_loop()

        
            pygame.display.update()

    def game_loop(self):
        myimage2 = pygame.image.load('./bg2.jpg')
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type==KEYDOWN:
                    if event.key==K_F9:
                        pygame.mixer.music.stop()
                    elif event.key==K_F10:
                        pygame.mixer.music.play()
            self.screen.blit(myimage2,(0,0))
            # self.screen.blit(self.back,(10,0))
            self.sb(5,70,5,45,10,0,self.back,self.zxh)
            self.sb(330,406,440,488,330,440,self.buguan,self.yaobuqi)
            self.sb(299,427,370,428,299,370,self.qiangdizhu,self.qdz)
            self.sb(488,620,370,428,488,370,self.jiaodizhu,self.jdz)
            self.sb(660,775,370,428,660,370,self.buqiang,self.bq)
            
            pygame.display.update()

    def jiemia_n(self):
        myimage2 = pygame.image.load('./bg2.jpg')
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.zxh()
            self.screen.blit(myimage2,(0,0))
            pygame.display.update()


j=jiem1()
j.yinyue()
j.zxh()
