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

font.init()
font1 = font.SysFont('Times New Roman',80)
win = font1.render('WIN!',True , (0,150,0))
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
    def __init__(self, wall_image, wall_x, wall_y, wall_width, wall_height, wall_speed):
        super().__init__()
        self.image = transform.scale(image.load(wall_image), (wall_width, wall_height))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.width = wall_width
        self.height = wall_height
        self.speed = wall_speed

    def update(self):
        self.rect.x -=self.speed 
        global lost 
        if self.rect.x > win_width:
            self.rect.x = randint(500, win_height-20)
            self.rect.x = 0
            lost +=1
        

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    


hero = Player('cat.png', 5, 375, 150, 117, 10)

walls = sprite.Group()
fish_ = sprite.Group()

for i in range(1, 7):

    wall = Wall('ice.png', randint(777, win_width-20), randint(0, win_height-30), 80, 50, randint(1, 3))
    walls.add(wall)



for i in range(1, 15):

    fish = Wall('fish.png', randint(777, win_width-20), randint(0, win_height-30), 80, 50, randint(1, 3))
    fish_.add(fish)

finish = False
run = True
rel_time = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if hero.rect.bottom > 100:
                    hero.fall_y = 10 



            

    if not finish:
        window.blit(background, (0, 0))
        fish_.update()
        walls.update()
        hero.update()
        hero.reset()

        walls.draw(window)
        fish_.draw(window)



        if sprite.spritecollide(hero, walls, False):
            sprite.spritecollide(hero, walls, True)
            life = life - 1
            wall = Wall('ice.png', randint(777, win_width-20), randint(0, win_height-30), 80, 50, randint(1, 3))
            walls.add(wall)

        if sprite.spritecollide(hero, fish_, False):
            sprite.spritecollide(hero, fish_, True)
            score += 1
            fish = Wall('fish.png', randint(777, win_width-20), randint(0, win_height-30), 80, 50, randint(1, 3))
            fish_.add(fish)

            




        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)

        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (828, 10))


        text_score = font1.render(str(score), 1, (0,0,0))
        window.blit(text_score, (20, 10))

        
    
        

        if life == 0:
            finish = True
            window.blit(lose, (320, 200))


        if score >= goal:
            finish = True
            window.blit(win, (320, 200))


        display.update()

    time.delay(50)
    clock.tick(FPS)