import random
import sys
import pygame


def Wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                return
    
def Collided(catRect,Cucumbers):
    for c in Cucumbers:
        if catRect.colliderect(c['rect']):
            return True
    return False
    
#Set up
pygame.init()
catChara = pygame.image.load('cat.jpg')
catChara = pygame.transform.scale(catChara,(30,30))
catRect = catChara.get_rect()
cucumberChara = pygame.image.load('cucumber.jpg')

AddCucumberRate = 20
screen = pygame.display.set_mode((800,600))

pygame.display.update()
Wait()

while True:
    Cucumbers = []
    score = 0
    cucumberAddCounter = 0
    catRect.topleft = (400,550)
    catmoving_right = False
    catmoving_left = False
    catmoving_up = False
    catmoving_down = False
    
    
    while True:
        score += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    catmoving_right = True
                elif event.key == pygame.K_LEFT:
                    catmoving_left = True
                elif event.key == pygame.K_UP:
                    catmoving_up = True
                elif event.key == pygame.K_DOWN:
                    catmoving_down = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    catmoving_right = False
                elif event.key == pygame.K_LEFT:
                    catmoving_left = False
                elif event.key == pygame.K_UP:
                    catmoving_up = False
                elif event.key == pygame.K_DOWN:
                    catmoving_down = False
        
        cucumberAddCounter += 1
        if cucumberAddCounter == AddCucumberRate:
            cucumberAddCounter = 0
            newCucumber = {'rect': pygame.Rect(random.randint(0, 800-20), 0 - 20, 20, 20),
                         'speed': 1,
                         'surface': pygame.transform.scale(cucumberChara, (20, 20)),
                         }
            Cucumbers.append(newCucumber)
                
        if catmoving_right and catRect.right <= 800:
            catRect.x += 1
        elif catmoving_left and catRect.left >= 0:
            catRect.x -= 1
        elif catmoving_up and catRect.top >= 0:
            catRect.y -= 1
        elif catmoving_down and catRect.bottom <= 600:
            catRect.y += 1
            

        
    
        #Cucumbers
        for c in Cucumbers:
            c['rect'].move_ip(0,c['speed'])
            
        for c in Cucumbers[:]:
            if c['rect'].top > 600:
                Cucumbers.remove(c)
                
        screen.fill((0,0,40)) 
        screen.blit(catChara,catRect)
        for c in Cucumbers:
            screen.blit(c['surface'],c['rect'])
            
        if Collided(catRect,Cucumbers):
            
            break
        pygame.display.update()
        
    pygame.display.update()
    Wait()
    
    
        