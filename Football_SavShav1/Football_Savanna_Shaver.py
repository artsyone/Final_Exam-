
# Imports
import pygame
import random

# Initialize game engine
pygame.init()



# Window
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "FOOTBALL!!!!"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

     
# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_LG = pygame.font.Font("fonts/score.ttf", 64)
FONT_MD = pygame.font.Font(None, 64)
FONT_XL = pygame.font.Font("fonts/sports.ttf", 96)

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)
DARKGREEN = (1,63,30)

# Images
ship_img = pygame.image.load('images/p1backp.png')
enemy = pygame.image.load('images/p1fronty.png')
laser_img = pygame.image.load('images/bullet.png')
field = pygame.image.load("images/footballfield1.png")
bomb_img  = pygame.image.load("images/p1fronty.png")
enemy_img = pygame.image.load('images/p1back.png')
crowds = pygame.image.load('images/watchfootball.jpg')
winner = pygame.image.load('images/winner.png')
win = pygame.image.load('images/fanshappy.jpg')
#sounds

theme = pygame.mixer.music.load("sounds/theme.ogg")
sad = pygame.mixer.Sound("sounds/sad.ogg")
theme = pygame.mixer.Sound("sounds/theme.ogg")

run = False


START = 0
PLAYING = 1
END = 2        

# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 5
        self.shield = 5

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    def shoot(self):
        laser = Laser(laser_img)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        lasers.add(laser)    

    def update(self, bombs,mobs):
        hit_list = pygame.sprite.spritecollide(self, bombs, True)
        hits = pygame.sprite.spritecollide(self, mobs, True)

        for hit in hit_list:
            pygame.mixer.music.pause()
            sad.play()
            self.shield -= 1    

        for h in hits:
            
            stage = END
            
        if self.shield == 0:
            #EXPLOSION.play()
            self.kill()

       
    
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0 :
            self.kill()
    
class Mob(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
        

    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)
        hit = pygame.sprite.spritecollide(self, lasers, True)
        if len(hit_list) > 0:
           # EXPLOSION.play()
            player.score += 1
            for e in  team:
                e.rect.y += 50
                self.kill()
        if len(hit) == 0:
            stage = END
class Team(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 5
                      
    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)
    
        if len(hit_list) > 0:
             
            
            for e in  team:
                e.rect.y -= 300
                # e.rect.y -= self.speed

        else:
            pass

    def has_scored(self):
        return self.rect.y <= 0


class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 3

    def update(self,lasers,player):
        self.rect.y += self.speed

        
        hit_list = pygame.sprite.spritecollide(self, lasers, True)

        if len(hit_list) > 0:
           # EXPLOSION.play()
            player.score += 1
            self.kill()

        #if self.rect.top >= HEIGHT :
            #self.kill()

class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.bomb_rate = 60

        self.speed = 3
        self.moving_right = True
        
    def move(self):
       
        reverse = False
        if self.moving_right:
            
            for m in  mobs:
                m.rect.x += self.speed
                
                
                if m.rect.right >= WIDTH:
                    reverse = True

        else:
               
            for m in  mobs:
                m.rect.x -= self.speed
                if m.rect.left <= 0:
                    reverse = True

        if reverse:  
                self.moving_right = not self.moving_right
                
                for m in mobs:
                    m.rect.y += 100

            
                    
    def choose_bomber(self):
            rand = random.randrange(0, self.bomb_rate)
            all_mobs = mobs.sprites()
            
            if len(all_mobs) > 0 and rand == 0:
                return random.choice(all_mobs)
            else:
                return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()

        run == []
        
            
              
class FleetT:
    def __init__(self, team):
        self.team = team
        self.speed = 3
        self.moving_right = True
        
    def move(self):
        
            reverse = False
        
            if self.moving_right:
            
                for e in  team:
                    e.rect.x += self.speed
                
                
                    if e.rect.right >= WIDTH:
                        reverse = True

            else:
           
                for e in  team:
                    e.rect.x -= self.speed
                    if e.rect.left <= 0:
                        reverse = True
        
            
            if reverse:  
                self.moving_right = not self.moving_right
                
                for e in team:
                    e.rect.x += 0
          
        
    def update(self):
        self.move()


     

    
# Make game objects
ship = Ship(384, 636, ship_img)
mob1 = Mob (123,-65,enemy)
mob2 = Mob (223,-65,enemy)
mob3 = Mob (323,-65,enemy)
mob4 = Mob (423,-65,enemy)

mob5 = Mob (0,-165,enemy)
mob6 = Mob (250,-165,enemy)
mob7 = Mob (500,-165,enemy)



team1 = Team (123,564,enemy_img)
team2 = Team (256,564,enemy_img)
team3 = Team  (364,564,enemy_img)
  
# Make sprite groups
player = pygame.sprite.GroupSingle()
player.add(ship)
player.score = 0

lasers = pygame.sprite.Group()
mobs = pygame.sprite.Group()
mobs.add(mob1,mob2,mob3,mob4,mob5,mob6,mob7)

team = pygame.sprite.Group()
team.add(team1,team2,team3)

bombs = pygame.sprite.Group()

# Make fleet
fleet = Fleet(mobs)
fleetT = FleetT(team)

# set stage
stage = START

# Game helper functions
def show_title_screen():
    screen.blit(crowds,(0,0))
    title_text = FONT_XL.render("FOOTBALL!", 1, RED)
    screen.blit(title_text, [208, 350])

def show_stats(player):
    score_text = FONT_LG.render(str(player.score), 1, DARKGREEN)
    screen.blit(score_text, [32, 32])


def show_end_screen():
    screen.fill(BLACK)
    screen.blit(winner,(125,150))
    title_text = FONT_XL.render("FOOTBALL!", 1, RED)
    score_text = FONT_LG.render(str(player.score), 1, RED)
    screen.blit(score_text, [32, 32])


# Game loop



done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    ship.shoot()
            if event.key == pygame.K_x:
                    done = True
                    
    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            ship.move_left()
        elif pressed[pygame.K_RIGHT]:
            ship.move_right()

        if stage == END:
            if event.key == pygame.K_SPACE:
                        stage = START
        
    
    # Game logic (Check for collisions, update points, etc.)
   
    player.update(bombs,mobs)
    lasers.update()
    bombs.update(lasers,player)
    mobs.update(lasers)
    team.update(lasers)
    fleet.update()
    fleetT.update()

    for t in team: 
        if t.has_scored():
            stage = END     
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(field,(0,0))
    lasers.draw(screen)
    bombs.draw(screen)
    player.draw(screen)
    mobs.draw(screen)
    team.draw(screen)

    
    show_stats(player)

    if stage == START:
        
        theme.play()
       
        show_title_screen()


    if stage == END:
       
        show_end_screen()


    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
