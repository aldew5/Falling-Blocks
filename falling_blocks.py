import pygame
import random

pygame.init()

win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Falling Blocks")

boulderimg = pygame.image.load('finalboulder.png')
snowballimg = pygame.image.load("betterball.png")
rockimg = pygame.image.load("bestrock.png")
heartimg = pygame.image.load("resizedheart.png")
bg = pygame.image.load("background.jpg")
char = pygame.image.load('standing.png')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]


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

class Heart(object):
    def __init__(self, x):
        self.x = x
        self.y = 635
        self.increase = 1
        self.image = heartimg
        self.time = 270
        self.appear = True
        self.hitbox = (self.x, self.y, 30, 30)

    def draw(self, win):
        if self.appear:
            if self.time > 0:
                win.blit(self.image, (self.x, self.y))
            else:
                self.appear = False
        
            self.time -= 1
            self.hitbox = (self.x, self.y, 30, 30)
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
heart = Heart(400)



objects, powerups = [], []               
run, hit = True, False
max_length, rounds, score, cooldown, interval = 0, 0, 0, 0, 27
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
    x = random.randint(1, 50)
    if score > 50 and x == 25 and len(powerups) == 0:
        xpos = random.randint(0,700)
        newheart = Heart(xpos)
        powerups.append(newheart)

    # check for picking up powerup
    for p in powerups:
        if center_x >= p.hitbox[0] and center_x <= p.hitbox[0] + p.hitbox[2]:
            # check the y
            if center_y >= p.hitbox[1] and center_y <= p.hitbox[1] + p.hitbox[3]:
                if man.health < 10:
                    man.health += 1

                p.appear = False
                
    # draw the scene
    drawWindow()

    
    # increment the cooldown by a tenth of the score after 10 objects
    # so that difficulty increases over time
    if score < 10:
        cooldown += 1
    else:
        cooldown += int(score * 0.1)

    rounds += 1

    # add to the amount of allowed objects as time goes on
    if rounds == 100 and max_length <= 15:
        max_length += 1
        rounds = 0
    interval += 1

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
while run and not(man.alive):

    # screen being closed
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    
    drawWindow()

pygame.quit()
