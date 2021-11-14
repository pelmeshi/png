from pygame import *
from random import *
window=display.set_mode((700,500))
display.set_caption("понг")

background =transform.scale(image.load("background.png"),(700,500))
window.blit(background,(0,0))
game=True

clock=time.Clock()

x1=0
x2=600
y1=100
y2=200

right=True
#sprite1=transform.scale(image.load("sprite1.png"),(100,100))
#sprite2=transform.scale(image.load("sprite2.png"),(100,100))



class GameSprite_player(sprite.Sprite):
    def __init__(self, image_1, xx, yy, speed_):
        super().__init__()
        self.image=transform.scale(image.load(image_1),(100,100))
        self.rect=self.image.get_rect()
        self.rect.x=xx
        self.rect.y=yy
        self.speed=speed_
    def move1(self):
        global keys_pressed    
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>1:
            self.rect.y-=5
        if keys_pressed[K_DOWN] and y1<400:
            self.rect.y+=5
    def move2(self):
        if keys_pressed[K_w] and self.rect.y>1:
            self.rect.y-=5
        if keys_pressed[K_s] and self.rect.y<400:
            self.rect.y+=5

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite(sprite.Sprite):
    def __init__(self, image_1, xx, yy, speed_):
        super().__init__()
        self.image=transform.scale(image.load(image_1),(100,100))
        self.rect=self.image.get_rect()
        self.rect.x=xx
        self.rect.y=yy
        self.speed=speed_

    def move_right(self,movement_speed):    
        self.rect.x+=5
        self.rect.y+=movement_speed
            

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball1=GameSprite("мяч.png",200,200,5)
sprite1=GameSprite_player("sprite1.png",0,100,5)
sprite2=GameSprite_player("sprite2.png",600,100,5)

speeed=5

while game:
    window.blit(background,(0,0))
    sprite1.reset()
    sprite1.move1()
    sprite2.reset()
    sprite2.move2()
    ball1.reset()
    keys_pressed=key.get_pressed()


    if ball1.rect.y>=400 and speeed>=0:
        speeed=speeed*(-1)
    if ball1.rect.y<=0 and speeed<=0:
        speeed=speeed*(-1)
    ball1.move_right(speeed)

    if sprite1.rect.x-ball1.rect.x<=50 and sprite1.rect.x-ball1.rect.x>=0:
        if ball1.rect.y-sprite1.rect.y<=50 and ball1.rect.y-sprite1.rect.y>=0:
            print("ДА НУ ОНО РАБОТАЕТ??!!")

    for e in event.get():
        if e.type==QUIT:
            game=False
    clock.tick(75)
    display.update()