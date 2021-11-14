from pygame import *
from random import *
window=display.set_mode((700,500))
display.set_caption("догонялки")

background =transform.scale(image.load("background.png"),(700,500))
window.blit(background,(0,0))
game=True

clock=time.Clock()
FPS=60
clock.tick(FPS)

x1=0
x2=600
y1=100
y2=200

right=True

sprite1=transform.scale(image.load("sprite1.png"),(100,100))
sprite2=transform.scale(image.load("sprite2.png"),(100,100))

class GameSprite(sprite.Sprite):
    def __init__(self, image_1, xx, yy, speed_):
        super().__init__()
        self.image=transform.scale(image.load(image_1),(100,100))
        self.rect=self.image.get_rect()
        self.rect.x=xx
        self.rect.y=yy
        self.speed=speed_
        mvmnt=0
        global mvmnt
    def reset(self):
        global mvmnt
        if right==True:
            self.rect.x+=2
            self.rect+=mvmnt
            if self.rect.y==490:
                mvmnt=5
            if self.rect.y==10:
                mvmnt=-5
        
        if right==False:
            self.rect.x-=2
            self.rect+=mvmnt
            if self.rect.y==490:
                mvmnt=5
            if self.rect.y==10:
                mvmnt=-5

        window.blit(self.image, (self.rect.x, self.rect.y))

ball1=GameSprite("мяч.png",200,200,5)

while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    ball1.reset()
    keys_pressed=key.get_pressed()
    if keys_pressed[K_UP] and y1>1:
        y1-=5
    if keys_pressed[K_DOWN] and y1<400:
        y1+=5
    if keys_pressed[K_w] and y2>1:
        y2-=5
    if keys_pressed[K_s] and y2<400:
        y2+=5
        
    for e in event.get():
        if e.type==QUIT:
            game=False
    display.update()