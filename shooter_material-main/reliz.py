#Створи власний Шутер!

from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((700,500))
display.set_caption("Shooter")

fon = transform.scale(image.load("fon.png"),(700,500))
# menu_fon = transform.scale(image.load("dropper1.png"),(700,500))

finish = False

menu = 1
level_1=0

fps = 60
clock = time.Clock()

font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)
catch = 1


WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)





class Area():
    def __init__(self, x=0, y=0, width=0, height=0):
    #запам'ятовуємо прямокутник:
        self.rect = Rect(x, y, width, height)
      

    def fill(self):
        draw.rect(wn,(5,54,43),self.rect)


    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y) 

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


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
palka = Player("palka.png", 300,0,70,200,0,0)
palka2 = Player("palka2.png", 300,400,70,200,0,0)

palka3 = Player("palka.png", 600,0,70,200,0,0)
palka4 = Player("palka2.png", 600,400,70,200,0,0)
menu = 1 

chiken = Player("chiken.png", 50,170,70,70,0,4)
exit = Player("exit.png", 240,250,200,70,0,4)
start = Player("start.png", 240,100,200,70,0,4)
restart = Player("rest.png", 230,150,220,170,0,4)
exit1 = Area( 240,250,200,70)
start1 = Area( 240,100,200,70)
restart1 = Area(50,170,70,70)

game_over = 0
score = 0     
while game:
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                chiken.rect.y -= 5

        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                x,y = e.pos
                if exit1.collidepoint(x,y) and menu:
                    game = 0
                if start1.collidepoint(x,y) and menu:
                    menu = 0
                    finish = 0  
                    level_1 = 1  

                if restart.rect.collidepoint(x,y) and game_over:
                    finish = 0
                    game_over = 0
                    score = 0
    
                label_catch = font1.render(f"Рахунок:  {catch}",True,(0,0,0)) 
                wn.blit(fon,(0,0))
                palka = Player("palka.png", 300,0,70,200,0,0)
                palka2 = Player("palka2.png", 300,400,70,200,0,0)
                palka3 = Player("palka.png", 600,0,70,200,0,0)
                palka4 = Player("palka2.png", 600,400,70,200,0,0)
                chiken = Player("chiken.png", 50,170,70,70,0,4)

        

                   

    
                        
    if not finish:
        # if menu:
        #     wn.blit(menu_fon,(0,0))
            
        if level_1:
            score += 0.01
            wn.blit(fon,(0,0))
            label_score = font1.render(f'Score: {int(score)}',True,(255,255,255))
            wn.blit(label_score,(10,10))
            chiken.show()
            chiken.move()
            palka.show()  
            palka2.show()
            palka3.show()
            palka4.show(  )
            chiken.rect.y += 2
            palka.rect.x -= 2
            palka2.rect.x -= 2
            palka3.rect.x -=2
            palka4.rect.x -=2      

            if chiken.rect.y > 400:
                chiken.rect.y = 400   

            if palka.rect.x < -200 :
                palka.rect.x = 500
                palka.rect.y = randint(-30,0)

            if palka2.rect.x < -200 :
                palka2.rect.x = 500
                palka2.rect.y = randint(320,380 )
            if palka3.rect.x < -200 :
                palka3.rect.x = 500
                palka3.rect.y = randint(-30,0)

            if palka4.rect.x < -200 :
                palka4.rect.x = 500
                palka4.rect.y = randint(320,380 )          

            if palka.rect.colliderect(chiken.rect):
                finish = 1
                game_over = 1
            if palka2.rect.colliderect(chiken.rect):
                finish = 1
                game_over =1

            if palka3.rect.colliderect(chiken.rect):
                finish = 1
                game_over = 1
            if palka4.rect.colliderect(chiken.rect):
                finish = 1
                game_over =1

            

        if menu:        
               wn.blit(fon,(0,0))
               exit1.fill()
               start1.fill()
               exit1.fill()
               exit.show()
               start.show()

    if game_over:
            wn.blit(fon,(0,0))
            restart.show()
            label_score = font1.render(f'Score: {int(score)}',True,(255,255,255))
            wn.blit(label_score,(10,10))

    
           

  
        
  
          
            
    display.update()
    clock.tick(fps)
 