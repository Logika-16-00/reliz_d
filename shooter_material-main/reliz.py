#Створи власний Шутер!

from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((700,500))
display.set_caption("Shooter")

fon = transform.scale(image.load("fon.png"),(700,500))
# menu_fon = transform.scale(image.load("dropper1.png"),(700,500))

finish = False

menu = 0
level_1=1

fps = 60
clock = time.Clock()

font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)





class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,life,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life
    
    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))

    def move(self):
        keys = key.get_pressed()

        if keys[K_SPACE] and self.rect.y>0:
            self.rect.y -= self.speed
            
game = 1
palka = Player("palka.png", 300,0,200,200,0,0)
palka2 = Player("palka.png", 300,320,200,200,0,0)


chiken = Player("chiken.png", 50,170,70,70,0,4)
while game:
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                chiken.rect.y -= 5

    
                        
    if not finish:
        # if menu:
        #     wn.blit(menu_fon,(0,0))
            
        if level_1:
            wn.blit(fon,(0,0))
            chiken.show()
            chiken.move()
            palka.show()  
            palka2.show()
            chiken.rect.y += 2
            palka.rect.x -= 2
            palka2.rect.x -= 2      

            if chiken.rect.y > 400:
                chiken.rect.y = 400   

            if palka.rect.x < -200 :
                palka.rect.x = 500
                palka.rect.y = randint(-30,0)

            if palka2.rect.x < -200 :
                palka2.rect.x = 500
                palka2.rect.y = randint(320,370)

          
            
    display.update()
    clock.tick(fps) 
 