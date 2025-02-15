from pygame import *
from random import randint
from time import time as timer
wn = display.set_mode((700,500))
display.set_caption("shooter")

fps = 60
fon = transform.scale( image.load("background.png"),(700,500))
finish = 0
clock = time.Clock()
mixer.init()
mixer.music.load("snake.ogg")
mixer.music.play()
fire_s = mixer.Sound("ukus.ogg")
font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)
global lose,catch
lose = 0
catch = 0
label_lose = font1.render(f'Пропущені: {lose}',True,(255,255,255))
label_catch = font1.render(f'Збито: {catch}',True,(255,255,255))
text_win = font2.render('You win!',True,(25,255,2))
text_lose = font2.render('You lose!',True,(255,25,2))
text_wait = font1.render("Wait",True,(255,255,255))

class Player(sprite.Sprite):
    def __init__(self,x,y,image_p,size_x,size_y,speed,life):
        super().__init__()
        self.image = transform.scale(image.load(image_p),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life

    def draw(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x<600:
            self.rect.x += 5
        if keys[K_a] and self.rect.x>0:
            self.rect.x -= 5
        
    def fire(self):
        bullet = Bullet(self.rect.x+20,self.rect.y,"bullet.png",15,20,15,0)
        bullets.add(bullet)


bullets = sprite.Group()        
class Enemy(Player):
    def update(self):
        global lose
        self.rect.y += self.speed
        if self.rect.y>500:
            self.rect.y = -10
            self.rect.x = randint(0,635)
            lose += 1


class Bullet(Player):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y >500:
            self.rect.y = -10
            lose += 1
game = 1





rocket = Player(310,360,"rocket.png",60,120,45,5)
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy(randint(0,650),0,'ufo.png',65,60,randint(1,5),0)
    monsters.add(enemy)


asteroids = sprite.Group() 
for i in range(3):
    asteroid = Enemy(randint(0,650),0,'asteroid.png',65,60,randint(1,5),0)
    asteroids.add(asteroid)

level_boss = 0
boss = Enemy(230,60,'boss.png',260,200,8,50)

num_fire =0
rel_time = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = 0
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <= 15 and rel_time == False:
                    fire_s.play() 
                    rocket.fire()
                    num_fire += 1
                elif num_fire >= 15 and rel_time == False:
                    rel_time = True
                    rel_timer = timer()
    if rel_time:
        if timer() - rel_timer > 3:
            rel_time = False
            num_fire =0
        time_to_fire = 3-int(timer()-rel_time)
        label_rel = font1.render(f"Почекай ще: {time_to_fire}",True,(255,255,255))
        wn.blit(label_rel,(550,15))
    if not finish:
        label_lose = font1.render(f'Пропущені: {lose}',True,(255,255,255))
        label_catch = font1.render(f'Збито: {catch}',True,(255,255,255))
        wn.blit(fon,(0,0))
        rocket.draw()
        rocket.update()
        bullets.draw(wn)
        bullets.update()
        monsters.draw(wn)
        monsters.update()
        asteroids.draw(wn)
        asteroids.update()
        wn.blit(label_catch,(10,10))
        wn.blit(label_lose,(10,40))
        if rel_time:
            if timer() - rel_timer > 3:
                rel_time = False
                num_fire =0
            time_to_fire = 3-int(timer()-rel_timer)
            label_rel = font1.render(f"Почекай ще: {time_to_fire}",True,(255,255,255))
            wn.blit(label_rel,(550,15))

        colides = sprite.groupcollide(monsters,bullets,True,True)
        for c in colides:
            catch+=1
            enemy = Enemy(randint(0,650),0,'ufo.png',65,60,randint(1,5),0)
            monsters.add(enemy)
        colides_a = sprite.groupcollide(asteroids,bullets,True,True)
        for c in colides_a:
            catch+=1
            asteroid = Enemy(randint(0,650),0,'asteroid.png',65,60,randint(1,5),0)
            asteroids.add(asteroid)
        
        if catch >= 10:
            finish = True
            level_boss = True
            for a in asteroids:
                a.kill()
            for a in monsters:
                a.kill()
            
    elif level_boss:
        wn.blit(fon,(0,0))
        label_boss_live = font1.render(f"Життя боса: {boss.life}",True,(255,255,255))
        wn.blit(label_boss_live,(10,10))
        label_live = font1.render(f"Життя: {rocket.life}",True,(255,255,255))
        wn.blit(label_live,(10,50))
        rocket.update()
        rocket.draw()
        bullets.draw(wn)
        bullets.update()
        boss.draw()
        boss.rect.x += boss.speed
        if boss.rect.x < 0 or boss.rect.x >470:
            boss.speed *=-1
        if sprite.spritecollide(boss, bullets,True):
            boss.life -= 1

        if rel_time:
            if timer() - rel_timer > 3:
                rel_time = False
                num_fire =0
            time_to_fire = 3- int(timer()-rel_timer)
            label_rel = font1.render(f"Почекай ще: {time_to_fire}",True,(255,255,255))
            wn.blit(label_rel,(550,15))
    if boss.life <= 0:
            level_boss = False
            label_lose = font2.render("Перемога",True,(13,197,11))
            wn.blit(label_lose,(240,240))
            boss.life = 0
    if lose >= 10 or sprite.spritecollide(rocket,monsters,False):
            wn.blit(text_lose,(220,230))
            finish = 1