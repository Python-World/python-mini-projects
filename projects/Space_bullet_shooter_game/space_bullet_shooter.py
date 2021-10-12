"""
 @Author : TheKnight
 Date : 6/09/2020

 copyright  © TheKight All Right Reserved



"""

import pygame
import random
import math
import time

from pygame import mixer




pygame.init()

clock = pygame.time.Clock()
# bg sound
mixer.music.load("bg.wav")
mixer.music.play(-1)


score_value = 0


# setting the display
screen = pygame.display.set_mode((800,600))

# background
bg = pygame.image.load("img2.png")

icon = pygame.image.load("icond.png")
pygame.display.set_caption("Space Bullet Shooter")
# display the icon
pygame.display.set_icon(icon)




# showing the bird imageo
playeimg = pygame.image.load("pl4.png")
playerx = 370
playery = 460

playerx_change = 0

def player(x,y):
	screen.blit(playeimg,(x,y))







 # moving the playerimag
 # for this we will use cordinate movement 
 # we will pass arugument to the function 


# for enemy
enemyimg =[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

number_of_enemy = 6
for i in range(number_of_enemy):


	enemyimg.append(pygame.image.load("ens.png"))

	enemyX.append(random.randint(0,736))
	enemyY.append(random.randint(50,150))
	enemyX_change.append(4)
	enemyY_change.append(30)


# bullet
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"
# function for enemy

def enemy(x,y,i):
	screen.blit(enemyimg[i],(x,y))


# function for fire bullet

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletimg,(x+53,y+10))



# checking if collision
def is_collision(enemyX,enemyY,playerx,playery):

	distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
	if distance < 27:
		return True

	else:
		return False



# showing score

font = pygame.font.Font("freesansbold.ttf",35)
score_cordinate_X = 10
Score_cordinate_Y=10
def showscore(x,y):
	score = font.render("Score : " + str(score_value),True,(255,255,255))
	screen.blit(score,(x,y))



OVER = pygame.font.Font("freesansbold.ttf",60)
# game over 
def game_over():
	over = OVER.render("GAME OVER   " 
	 ,True,(0,0,255))
	screen.blit(over,(250,250))


final = pygame.font.Font("freesansbold.ttf",50)
def final_score():
	finalscore = final.render("Total Score : " +str(score_value) ,True,(0,255,0))
	screen.blit(finalscore,(280,350))
	 

author = pygame.font.Font("freesansbold.ttf",16)
# showing author name

def author_name():
	subject = author.render("Copyright ©2020 TheKnight All Right Reseved By TheKnight " 
	 ,True,(0,255,0)) 
	screen.blit(subject,(170,580))


# game loop
running = True

while running:
	screen.fill((0,0,0))
	screen.blit(bg,(0,0))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# controlling the bird by arrow keys

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerx_change = -5

			if event.key == pygame.K_RIGHT:
				playerx_change = 5

			if event.key == pygame.K_SPACE:
				if bullet_state == "ready":
					bulletX = playerx
					bulletsound = mixer.Sound("bulletout.wav")
					bulletsound.play()
				
					fire_bullet(bulletX,bulletY)

			

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_LEFT:
				playerx_change = 0



	for i in range(number_of_enemy):

		# game over
		if enemyY[i] >440:

			for j in range(number_of_enemy):
				enemyY[j] =2000
			game_over()
			time.sleep(2)

			final_score()
			
			break





			
		enemyX[i] += enemyX_change[i]
		if enemyX[i] <=0:
			enemyX_change[i]= 4
			enemyY[i] += enemyY_change[i]

		elif enemyX[i]>=736:
			enemyX_change[i] = -4
			enemyY[i] += enemyY_change[i]


		# collision

		collision = is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
		if collision:
			bulletsound = mixer.Sound("bulletshoot.wav")
			bulletsound.play()
			bulletY = 480
			bullet_state = "ready"

			score_value +=1

		
			enemyX[i] = random.randint(0,736)
			enemyY[i] = random.randint(50,150)


		enemy(enemyX[i],enemyY[i],i)




			


			
			

			
			
			
			



			





















	

	# checking boundries of spacechip
	playerx+=playerx_change

	if playerx <=0:
		playerx = 0
	elif playerx>=730:
		playerx = 730
	

	
	# playerx -=0.2
	# playery -=.2

	

	# bullet movement
	if bulletY <=0:
		bulletY=480
		bullet_state = "ready"
	if bullet_state == "fire":
		fire_bullet(bulletX,bulletY)
		bulletY -= bulletY_change
	
	player(playerx,playery)
	showscore(score_cordinate_X,Score_cordinate_Y)

	author_name()
	





	pygame.display.update()

