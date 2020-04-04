import pygame
import random
import os

pygame.init()

win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Falling Blocks")


script_dir = os.path.dirname('Obstacles')
rel_path = r"C:\Users\Owner\Desktop\Falling-Blocks\Images\Obstacles"
abs_file_path = os.path.join(script_dir, rel_path)

# loading objects
current_file = r"\finalboulder.png"
boulderimg = pygame.image.load(abs_file_path + current_file)
current_file = r"\betterball.png"
snowballimg = pygame.image.load(abs_file_path + current_file)
current_file = r"\bestrock.png"
rockimg = pygame.image.load(abs_file_path + current_file)

rel_path = r"C:\Users\Owner\Desktop\Falling-Blocks\Images\Powerups"
script_dir = os.path.dirname('Powerups')
abs_file_path = os.path.join(script_dir, rel_path)

# loading powerups
current_file = r"\resizedheart.png"
heartimg = pygame.image.load(abs_file_path + current_file)
current_file = r"\bestgun.png"
gunimg = pygame.image.load(abs_file_path + current_file)
current_file = r'\better_small.png'
side_gun = pygame.image.load(abs_file_path + current_file)

#loading background
abs_file_path = os.path.join('Backgrounds',r"C:\Users\Owner\Desktop\Falling-Blocks\Images\Backgrounds")
bg = pygame.image.load(abs_file_path + r"\background.jpg")


rel_path = r"C:\Users\Owner\Desktop\Falling-Blocks\Images\Player"
script_dir = os.path.dirname('Player')
abs_file_path = os.path.join(script_dir, rel_path)

# character
char = pygame.image.load(abs_file_path + r'\standing.png')

walkRight = [pygame.image.load(abs_file_path + r'\R1.png'), pygame.image.load(abs_file_path + r'\R2.png'), pygame.image.load(abs_file_path + r'\R3.png'), pygame.image.load(abs_file_path + r'\R4.png'),\
             pygame.image.load(abs_file_path + r'\R5.png'), pygame.image.load(abs_file_path + r'\R6.png'), pygame.image.load(abs_file_path + r'\R7.png'), pygame.image.load(abs_file_path + r'\R8.png'), pygame.image.load(abs_file_path + r'\R9.png')]
walkLeft = [pygame.image.load(abs_file_path + r'\L1.png'), pygame.image.load(abs_file_path + r'\L2.png'), pygame.image.load(abs_file_path + r'\L3.png'), pygame.image.load(abs_file_path + r'\L4.png'),\
            pygame.image.load(abs_file_path + r'\L5.png'), pygame.image.load(abs_file_path + r'\L6.png'), pygame.image.load(abs_file_path + r'\L7.png'), pygame.image.load(abs_file_path + r'\L8.png'), pygame.image.load(abs_file_path + r'\L9.png')]


clock = pygame.time.Clock()


class Character(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.v = 5
        self.left, self.right = False, False
        self.standing = True
        self.walkCount = 0
        self.health = 10
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.alive = True
        self.shooting = False

    def draw(self, win):
        if self.alive:
            # reset image cycle
            if self.walkCount + 1 >= 9:
                self.walkCount = 0

            # moving
            if not(self.standing):
                # drawing left walking images 
                if self.left:
                    win.blit(walkLeft[self.walkCount], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount], (self.x, self.y))
                    self.walkCount += 1
            # not moving
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
            #hitbox
            # hitbox[0], hitbox[1] are the coords of the top left of the hitbox
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

            #health bar
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ( 5* (10-self.health)), 10))

            # gun
            if self.shooting:
                win.blit(side_gun, (self.x + 20, self.y + 40))
                

            # circle at start of rect
            # pygame.draw.circle(win, (255,0,0), (self.hitbox[0], self.hitbox[1]), 20)
        else:
            #game over
            font = pygame.font.SysFont('comicsans', 30, True)
            over = font.render('GAME OVER', 1, (0,0,0))
            win.blit(over, (290, 350))

            

# abstract block class
class Block(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = 10
        self.falling = True

    def draw(self, win):
        # not off the screen
        if self.y < 700:
            win.blit(self.image, (self.x, self.y))
            self.y += self.v
        else:
            self.falling = False
    

class Rock(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.v = 10
        self.image = rockimg
        self.hitbox = (self.x, self.y + 10, 90, 60)
        self.id = "rock"

    def draw(self, win):
        Block.draw(self,win)
        
        # hitbox
        self.hitbox = (self.x, self.y + 10, 90, 60)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        

class Snowball(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.v = 20
        self.image = snowballimg
        self.hitbox = (self.x, self.y - 10, 15, 15)
        self.id = "snowball"
    
    def draw(self,win):
        Block.draw(self, win)
        
        self.hitbox = (self.x, self.y - 10, 30, 30)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class Boulder(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.v = 5
        self.image = boulderimg
        self.hitbox = (self.x, self.y - 20, 200 ,200)
        self.id = "boulder"

    def draw(self, win):
        Block.draw(self, win)

        self.hitbox = (self.x, self.y - 5, 135, 135)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class Powerup(object):
    def __init__(self, x):
        self.x = x
        self.y = 635
        self.image = None
        self.time = 270
        self.appear = True

    def draw(self, win):
        if self.appear:
            if self.time > 0:
                win.blit(self.image, (self.x, self.y))
            else:
                self.appear = False
            self.time -= 1

class Heart(Powerup):
    def __init__(self, x):
        Powerup.__init__(self, x)
        self.increase = 1
        self.image = heartimg
        self.id = "heart"
        self.hitbox = (self.x, self.y, 30, 30)

    def draw(self, win):
        Powerup.draw(self, win)
        
        self.hitbox = (self.x, self.y, 30, 30)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class Gun(Powerup):
    def __init__(self, x):
        Powerup.__init__(self, x)
        self.image = gunimg
        self.id = "gun"
        self.hitbox = (self.x, self.y, 30, 30)

    def draw(self, win):
        Powerup.draw(self, win)
            
        self.hitbox = (self.x, self.y, 30, 30)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, 30, 30)
        self.appear = True
        self.v = 8

    def draw(self, win):
        if self.appear:
            pygame.draw.circle(win, (0,0,0), (self.x, self.y), 7)

            self.hitbox = (self.x - 10, self.y - 10, 20, 20)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
            
                        
def drawWindow():
    win.blit(bg, (0,0))
    man.draw(win)

    # drawing falling blocks
    if man.alive:
        for o in objects:
            o.draw(win)
        for p in powerups:
            p.draw(win)
        for b in bullets:
            b.draw(win)

        # displaying score
        font = pygame.font.SysFont('comicsans', 30, True)
        text = font.render('Score: ' + str(score), 1, (0,0,0))
        win.blit(text, (550, 10))
                       
    else:
        # draw the score
        font = pygame.font.SysFont('comicsans', 30, True)
        text = font.render('Score: ' + str(score), 1, (0,0,0))
        win.blit(text, (290, 400))

    # update the display
    pygame.display.update()
                         

man = Character(300, 600, 64, 64)
gun = Gun(400)
print(type(man))

objects, powerups, bullets = [], [gun] , []              
run, hit = True, False
max_length, rounds, score, cooldown, interval = 0, 0, 0, 0, 27
shoot_cooldown, shoot_time = 0, 0
while run and man.alive:
    # set fps
    clock.tick(27)

    # find the center of the man
    center_x = (man.hitbox[0] + (man.hitbox[0] + man.hitbox[2]))//2
    center_y = (man.hitbox[1] + (man.hitbox[1] + man.hitbox[3]))//2

    # screen being closed
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # keys list
    keys = pygame.key.get_pressed()
    
    # moving left
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.v
        man.left, man.right = True, False
        man.standing = False
    # moving right
    elif keys[pygame.K_RIGHT] and man.x < 700 - man.width:
        man.x += man.v
        man.right, man.left = True, False
        man.standing = False
    # standing
    else:
        man.standing = True
        man.walkCount = 0
    
    #shooting controls
    if man.shooting and keys[pygame.K_SPACE] and len(bullets) <= 5 and shoot_cooldown >= 10:
        shoot_cooldown = 0
        new_bullet = Bullet(man.x + 30, man.y)
        bullets.append(new_bullet)

    # change bullet position or delete them
    for bullet in bullets:
        if bullet.y > 0:
            bullet.y -= bullet.v
        else:
            bullets.pop(bullets.index(bullet))

    # check for bullet collisions
    for bullet in bullets:
        for o in objects:
            if bullet.x >= o.hitbox[0] and bullet.x <= o.hitbox[0] + o.hitbox[2]:
                # check the y
                if bullet.y >= o.hitbox[1] and bullet.y <= o.hitbox[1] + o.hitbox[3]:
                    objects.pop(objects.index(o))
                    bullets.pop(bullets.index(bullet))
                
    #check rocks
    for o in objects:
        if o.falling == False:
            objects.pop(objects.index(o))
            score += 1

    # check powerups
    for p in powerups:
        if p.appear == False:
            powerups.pop(powerups.index(p))

            
    #check for a collision
    for r in objects:
        # check the x
        if center_x >= r.hitbox[0] and center_x <= r.hitbox[0] + r.hitbox[2]:
            # check the y
            if center_y >= r.hitbox[1] and center_y <= r.hitbox[1] + r.hitbox[3]:
    
                if r.id == "boulder":
                    if man.health - 2 <= 0:
                        man.alive = False
                    else:
                        print("HIT")
                        r.falling = False
                        man.health -= 2
                # not a boulder       
                elif man.health - 1 == 0:
                        man.alive = False
                else:
                    print('hit')
                    r.falling = False
                    man.health -= 1


    # generate new objects
    x = random.randint(1,10)
    if x >= 5 and len(objects) < 5 + max_length and cooldown >= 20:
        x = random.randint(1, 21)
        xpos = random.randint(0, 700)

        if x == 10 or x == 15:
            new_snowball = Snowball(xpos, 0)
            objects.append(new_snowball) 
        elif x == 20:
            new_boulder = Boulder(xpos, 0)
            objects.append(new_boulder)
        else:
            newrock = Rock(xpos, 0)
            objects.append(newrock)
        cooldown = 0


    # generate new powerups
    x = random.randint(1, 100)
    if score > 50 and x == 25 and len(powerups) == 0:
        choice = random.randint(1, 100)
        xpos = random.randint(0,700)
        if choice >= 50:
            newheart = Heart(xpos)
            powerups.append(newheart)
        else:
            newgun = Gun(xpos)
            powerups.append(newgun)

    # check for picking up powerup
    for p in powerups:
        if center_x >= p.hitbox[0] and center_x <= p.hitbox[0] + p.hitbox[2]:
            # check the y
            if center_y >= p.hitbox[1] and center_y <= p.hitbox[1] + p.hitbox[3]:
                if p.id == "heart":
                    if man.health < 10:
                        man.health += 1
                elif p.id == "gun":
                    man.shooting = True
                    # reset the shoot time
                    shoot_time = 135

                # picked up an powerup
                p.appear = False

    # check for the gun being use up
    if shoot_time == 0:
        man.shooting = False
              
    # draw the scene
    drawWindow()

    # increment the cooldown by a tenth of the score after 10 objects
    # so that difficulty increases over time
    if score < 10:
        cooldown += 1
    else:
        cooldown += int(score * 0.1)

    # add to the amount of allowed objects as time goes on
    if rounds == 100 and max_length <= 10:
        max_length += 1
        rounds = 0

    # increment varaibles
    interval += 1
    shoot_cooldown += 1
    shoot_time -= 1
    rounds += 1

# print higscores
highscores = open('highscores.txt', 'r')
top = int(highscores.read())
print("Current highscore is ", top)
highscores.close()

hs = open('highscores.txt', 'w')
if score > top:
    print("Congratulations! You have the new highscore")
    hs.write(str(score))
hs.close()

run = True
# game over screen
while run and not(man.alive):

    # screen being closed
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    
    drawWindow()

pygame.quit()
