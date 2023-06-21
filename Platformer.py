from pygame import *
from random import randint 
from time import time as timer

win_width = 888
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Platformer')
background = transform.scale(image.load('lake.jpg'), (win_width, win_height))

clock = time.Clock()
FPS = 60

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')

font.init()
font1 = font.SysFont('Times New Roman',80)
win = font1.render('WIN!',True , (255,255,255))
lose = font1.render('LOSE',True, (180,0,0))

score = 0
lost = 0
max_lost = 20
goal = 10
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.fall_y = 0
        self.jumped = False

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        elif keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        elif keys[K_SPACE] and self.rect.y > 5:
            self.fall_y = -15
            self.jumped = True
        elif keys[K_SPACE] == False:
            self.jumped = False

        
        self.fall_y += 2
        if self.fall_y > 10:
            self.fall_y = 10
        self.rect.y += self.fall_y

        if self.rect.bottom > win_height:
            self.rect.bottom = win_height
            
class Wall(sprite.Sprite):
    def __init__(self, wall_image, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.image = transform.scale(image.load(wall_image), (wall_width, wall_height))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.width = wall_width
        self.height = wall_height
        

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# w1 = Wall(204, 204, 255, 200, 480, 200, 30)

# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y +=self.speed 
#         global lost 
#         if self.rect.y > win_height:
#             self.rect.x = randint(80, win_width-80)
#             self.rect.y = 0
#             lost +=1


hero = Player('cat.png', 5, 375, 150, 117, 10)

walls = sprite.Group()
wall_1 = Wall('ice.png', 700, 300, 100, 100)
wall_2 = Wall('ice.png', 200, 400, 100, 100)
wall_3 = Wall('ice.png', 450, 350, 100, 100)


# monsters = sprite.Group()
# for i in range(1,15):
    # monster = Enemy(img_enemy, randint(80, win_width-80), -40, 80, 50, randint(1,5))
    # monsters.add(monster)

finish = False
run = True
rel_time = False
num_fire = 0

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        # elif e.type == KEYDOWN:
            

    if not finish:
        window.blit(background, (0, 0))
        
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()

        hero.update()
        hero.reset()

        display.update()

        if sprite.spritecollide(hero, walls, False):
            self.rect.bottom = wall_height

    #     if life == 3:
    #         life_color = (0, 150, 0)
    #     if life == 2:
    #         life_color = (150, 150, 0)
    #     if life == 1:
    #         life_color = (150, 0, 0)

    #     text_life = font1.render(str(life), 1, life_color)
    #     window.blit(text_life, (650, 10))


    #     if rel_time == True:
    #         now_time = timer()
    #         if now_time - last_time < 3:
    #             reload = font2.render('Wait, reload...', 1, (150, 0, 0))
    #             window.blit(reload, (260, 460))
    #         else:
    #             num_fire = 0
    #             rel_time = False
        
        
    #     collides = sprite.groupcollide(monsters, bullets, True, True)
    #     for c in collides:
    #         score += 1
    #         monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
    #         monsters.add(monster)

    #     if sprite.spritecollide(ship, monsters, False) or lost >= max_lost or sprite.spritecollide(ship, asteroids, False):
    #         sprite.spritecollide(ship, monsters, True)
    #         sprite.spritecollide(ship, asteroids, True)
    #         life = life - 1

    #     if life == 0 or lost >= max_lost:
    #         finish = True
    #         window.blit(lose, (200, 200))


    #     if score >= goal:
    #         finish = True
    #         window.blit(win, (200, 200))
    #     display.update()

    # else: 
    #     finish = False
    #     score = 0
    #     lost = 0
    #     for b in bullets:
    #         b.kill()
    #     for i in monsters:
    #         i.kill()

    #     for m in asteroids:
    #         m.kill()


    #     for i in range(1,15):
    #         monster = Enemy(img_enemy, randint(80, win_width-80), -40, 80, 50, randint(1,5))
    #         monsters.add(monster)

    #     for i in range(1,2):
    #         asteroid = Enemy(img_asteroid, randint(80, win_width-80), -40, 80, 80, randint(1,5))
    #         asteroids.add(asteroid)

    #     life = 3

    time.delay(50)
    clock.tick(FPS)