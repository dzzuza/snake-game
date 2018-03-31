import pygame
import time
import random

grey=(120,120,120)
red=(255,0,0)
green=(75,190,75)
black=(0,0,0)
white=(255,255,255)
pygame.init()

x=800
y=600
gameDisplay = pygame.display.set_mode((x,y))
pygame.display.set_caption('game') 

icon=pygame.image.load('head.png')
pygame.display.set_icon(icon)

#pygame.display.update()
img_head=pygame.image.load('head.png')
img_apple = pygame.image.load('apple1.png')
img_apple2 = pygame.image.load('apple(1).png')
img_back=pygame.image.load('background.png')
img_back2=pygame.image.load('background2.png')

thickness=20
block_size=20
clock=pygame.time.Clock()
FPS=10
back=True
multi=False
flag=0

direct="right"
level=1
level_score=5
small_font=pygame.font.SysFont("comicsanssms", 25)
large_font=pygame.font.SysFont("comicsanssms", 70)


def snake(block_size, snake_list):
	if direct=="right":
		head=pygame.transform.rotate(img_head,270)
#		body=pygame.transform.rotate(img_body,270)
	if direct=="left":
		head=pygame.transform.rotate(img_head,90)
#		body=pygame.transform.rotate(img_body,90)
	if direct=="up":
		head=pygame.transform.rotate(img_head,0)
#		body=pygame.transform.rotate(img_body,0)
	if direct=="down":
		head=pygame.transform.rotate(img_head,180)
#		body=pygame.transform.rotate(img_body,180)

#	ii=-1m
	gameDisplay.blit(head,(snake_list[-1][0],snake_list[-1][1]))	
	
	for element in snake_list[:-1]:
		pygame.draw.rect(gameDisplay,green,[element[0],element[1],block_size, block_size])


def snake2(block_size, snake_list):
	if direct2=="right":
		head=pygame.transform.rotate(img_head,270)
#		body=pygame.transform.rotate(img_body,270)
	if direct2=="left":
		head=pygame.transform.rotate(img_head,90)
#		body=pygame.transform.rotate(img_body,90)
	if direct2=="up":
		head=pygame.transform.rotate(img_head,0)
#		body=pygame.transform.rotate(img_body,0)
	if direct2=="down":
		head=pygame.transform.rotate(img_head,180)
#		body=pygame.transform.rotate(img_body,180)

	ii=-1
	gameDisplay.blit(head,(snake_list[-1][0],snake_list[-1][1]))	
	
	for element in snake_list[:-1]:
		pygame.draw.rect(gameDisplay,green,[element[0],element[1],block_size, block_size])
#		ii+=1
#		snake_x=snake_list[ii][0]
#		snake_y=snake_list[ii][1]
#		gameDisplay.blit(body,(snake_x,snake_y))

def pause():
	paused=True
	message_to_screen("Paused",green,-100,"large")
	message_to_screen("Press C to continue",black,0,"small")
	pygame.display.update()
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key ==pygame.K_c:
					paused = False
				elif event.key ==pygame.K_q:
					pygame.quit()
					quit()	
				elif event.key ==pygame.K_b:
					game_intro()
		#gameDisplay.fill(white)

def text_surf(text,color,size):
	if size == "small":
		text_Surface = small_font.render(text, True, color)
	if size == "large":
		text_Surface = large_font.render(text, True, color)
	return text_Surface

def message_to_screen(msg,color,y_displace,size):
	text_Surface = text_surf(msg, color,size)
	text_Rect=text_Surface.get_rect()
#	screen_text= font.render(msg, True, color)
#	gameDisplay.blit(screen_text,[x/2,y/2])
	text_Rect.center = (x/2),(y/2)+y_displace
	gameDisplay.blit(text_Surface, text_Rect)
		
def score(score,place):
	text=small_font.render("Score: "+str(score),True,grey)
	gameDisplay.blit(text,[0+place,0])
	

def food_gen():
	rand_food_x =round (random.randrange(0,x-thickness)/10)*10
	rand_food_y = round (random.randrange(0,y-thickness)/10)*10
	return rand_food_x,rand_food_y


def bomb_gen():
	rand_bomb_x =round (random.randrange(0,x-thickness)/10)*10
	rand_bomb_y = round (random.randrange(0,y-thickness)/10)*10
	return rand_bomb_x,rand_bomb_y

def multi_game_loop():
	global direct
	global direct2
	global FPS
	global level
	global level_score
	global back
	global flag

#	FPS=5
	direct="right"
	direct2="right"
	gameExit = False
	gameOver = False


	lead_x = x/2+100
	lead_y = y/2+100

	lead_x2 = x/2-100
	lead_y2 = y/2-100

	lead_x_change=block_size
	lead_y_change=0

	lead_x_change2=block_size
	lead_y_change2=0

	snake_list =[]
	snake_length=1

	snake_list2 =[]
	snake_length2=1

	rand_food_x,rand_food_y=food_gen()
	rand_bomb_x,rand_bomb_y=bomb_gen()

	while not gameExit:
		if gameOver==True:
			if flag==1:
				message_to_screen("The winner is player 1",green,-50,size="large")
				message_to_screen("Press 'c' to contnue or press 'q' to quit",green,150,size="small")
				pygame.display.update()
			if flag==2:
				message_to_screen("The winner is player 2",green,-50,size="large")
				message_to_screen("Press 'c' to contnue or press 'q' to quit",green,150,size="small")
				pygame.display.update()
			if flag==3:
				message_to_screen("Game Over",green,-50,size="large")
				message_to_screen("Press 'c' to contnue or press 'q' to quit",green,150,size="small")
				pygame.display.update()

		while gameOver==True:
			#gameDisplay.fill(white)
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = False
						gameExit = True
						print(gameOver)
					elif event.key == pygame.K_c:
						level=1
						FPS=10
						back=True
						level_score=5
						game_intro()
				elif event.type == pygame.QUIT:
					gameOver = False
					gameExit = True


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
#				if event.key == pygame.K_q:
				gameExit = True
#					print('zamknij')
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
					direct="left"
				if event.key == pygame.K_a:
					lead_x_change2 = -block_size
					lead_y_change2 = 0
					direct2="left"
				if event.key == pygame.K_RIGHT:
					lead_x_change =block_size
					lead_y_change = 0
					direct = "right"
				if event.key == pygame.K_s:
					lead_x_change2 =block_size
					lead_y_change2 = 0
					direct2 = "right"
				if event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
					direct="up"
				if event.key == pygame.K_w:
					lead_y_change2 = -block_size
					lead_x_change2 = 0
					direct2="up"
				if event.key == pygame.K_DOWN:
					lead_y_change =block_size 
					lead_x_change = 0
					direct="down"
				if event.key == pygame.K_z:
					lead_y_change2 =block_size 
					lead_x_change2 = 0
					direct2="down"
				if event.key == pygame.K_p:
					pause()
#background

		if back==True:
			gameDisplay.blit(img_back,(0,0))
		else:
			gameDisplay.blit(img_back2,(0,0))
#dodatki
		gameDisplay.blit(img_apple,(rand_food_x,rand_food_y,thickness,thickness))
		gameDisplay.blit(img_apple2,(rand_bomb_x,rand_bomb_y,thickness,thickness))

#waz 1
		if lead_x>=x or lead_x<= 0 or lead_y>=y or lead_y<=0:
			gameOver = True
			flag=2

		snake_head =[]
		snake_head.append(lead_x)
		snake_head.append(lead_y)
		snake_list.append(snake_head)

		if len(snake_list)>snake_length:
			del snake_list[0]

		for segment in snake_list[:-1]:
			if segment==snake_head:
				gameOver=True
				flag=1

		lead_x += lead_x_change
		lead_y += lead_y_change

		for segment in snake_list[:-1]:
			if segment==snake_head2:
				gameOver=True
				flag=1

#waz 2

		if lead_x2>=x or lead_x2<= 0 or lead_y2>=y or lead_y2<=0:
			gameOver = True
			flag=1

		lead_x2 += lead_x_change2
		lead_y2 += lead_y_change2

		snake_head2 =[]
		snake_head2.append(lead_x2)
		snake_head2.append(lead_y2)
		snake_list2.append(snake_head2)

	
		if len(snake_list2)>snake_length2:
			del snake_list2[0]

		for segment in snake_list2[:-1]:
			if segment==snake_head2:
				gameOver=True
				flag=2

		for segment in snake_list2[:-1]:
			if segment==snake_head:
				gameOver=True
				flag=2

		if snake_head==snake_head2:
			gameOver=True
			flag=3

#wywolanie wezy
		snake(block_size,snake_list)
		snake2(block_size,snake_list2)
#		snake(block_size,snake_list)

#punktacje
		score(snake_length-1,0)
		score(snake_length2-1,100)
#		text=small_font.render("Level: "+str(level),True,grey)
#		gameDisplay.blit(text,[0,30])
		pygame.display.update()


		if lead_x2 >= rand_food_x and lead_x2 <= rand_food_x+thickness or lead_x2+block_size >= rand_food_x and lead_x2 + block_size <= rand_food_x+thickness:
			if lead_y2 >= rand_food_y and lead_y2 <= rand_food_y+thickness or lead_y2+block_size >= rand_food_y and lead_y2 + block_size <= rand_food_y+thickness:
					rand_food_x,rand_food_y=food_gen()
					rand_bomb_x,rand_bomb_y=bomb_gen()
					snake_length2 +=1
	
		if lead_x2 >= rand_bomb_x and lead_x2 <= rand_bomb_x+thickness or lead_x2+block_size >= rand_bomb_x and lead_x2 + block_size <= rand_bomb_x+thickness:
			if lead_y2 >= rand_bomb_y and lead_y2 <= rand_bomb_y+thickness or lead_y2+block_size >= rand_bomb_y and lead_y2 + block_size <= rand_bomb_y+thickness:
				gameOver=True
				flag=1
	
		if snake_length2>2:
			gameOver=True
			message_to_screen("The winner is player 1",green,-50,size="large")
			message_to_screen("Press 'c' to contnue or press 'q' to quit",green,150,size="small")
			pygame.display.update()

		elif snake_length>2:
			gameOver=True
			message_to_screen("The winner is player 2",green,-50,size="large")
			message_to_screen("Press 'c' to contnue or press 'q' to quit",green,150,size="small")
			pygame.display.update()
#		snake(lead_x,lead_y,block_size)
#		pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size, block_size])

		if lead_x >= rand_food_x and lead_x <= rand_food_x+thickness or lead_x+block_size >= rand_food_x and lead_x + block_size <= rand_food_x+thickness:
			if lead_y >= rand_food_y and lead_y <= rand_food_y+thickness or lead_y+block_size >= rand_food_y and lead_y + block_size <= rand_food_y+thickness:
					rand_food_x,rand_food_y=food_gen()
					rand_bomb_x,rand_bomb_y=bomb_gen()
					snake_length +=1

		if lead_x >= rand_bomb_x and lead_x <= rand_bomb_x+thickness or lead_x+block_size >= rand_bomb_x and lead_x + block_size <= rand_bomb_x+thickness:
			if lead_y >= rand_bomb_y and lead_y <= rand_bomb_y+thickness or lead_y+block_size >= rand_bomb_y and lead_y + block_size <= rand_bomb_y+thickness:
				gameOver=True

		clock.tick(FPS)

	pygame.quit()
	quit()

def game_loop():
	global direct
	global FPS
	global level
	global level_score
	global back
	global flag
	direct="right"
	gameExit = False
	gameOver = False

#pozycja x i y snakea
	lead_x = x/2+100
	lead_y = y/2+100

	lead_x_change=block_size
	lead_y_change=0

	snake_list =[]
	snake_length=1

#losowanie pozycji foodow i bomb + generowanie
	rand_food_x,rand_food_y=food_gen()
	rand_bomb_x,rand_bomb_y=bomb_gen()

#exit koniec programu
#over koniec pojedynczej rozgrywki

	while not gameExit:
		if gameOver==True:
			message_to_screen("Game Over",green,-50,size="large")
			message_to_screen("Press 'c' to continue or press 'q' to quit",green,150,size="small")
			pygame.display.update()

		while gameOver==True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = False
						gameExit = True
						print(gameOver)
					elif event.key == pygame.K_c:
						level=1
						FPS=10
						back=True
						level_score=5
						game_intro()
				elif event.type == pygame.QUIT:
					gameOver = False
					gameExit = True

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
#				if event.key == pygame.K_q:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
					direct="left"
				if event.key == pygame.K_a:
					lead_x_change2 = -block_size
					lead_y_change2 = 0
					direct2="left"
				if event.key == pygame.K_RIGHT:
					lead_x_change =block_size
					lead_y_change = 0
					direct = "right"
				if event.key == pygame.K_s:
					lead_x_change2 =block_size
					lead_y_change2 = 0
					direct2 = "right"
				if event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
					direct="up"
				if event.key == pygame.K_w:
					lead_y_change2 = -block_size
					lead_x_change2 = 0
					direct2="up"
				if event.key == pygame.K_DOWN:
					lead_y_change =block_size 
					lead_x_change = 0
					direct="down"
				if event.key == pygame.K_z:
					lead_y_change2 =block_size 
					lead_x_change2 = 0
					direct2="down"
				if event.key == pygame.K_p:
					pause()

#kolizja ze scianami
		if lead_x>=x+1 or lead_x<=(-1) or lead_y>=y+1 or lead_y<=(-1):
			gameOver = True
#przemieszczenie
		lead_x += lead_x_change
		lead_y += lead_y_change
#tlo
		if back==True:
			gameDisplay.blit(img_back,(0,0))
		else:
			gameDisplay.blit(img_back2,(0,0))
#wyswietlanie dodatkow
		gameDisplay.blit(img_apple,(rand_food_x,rand_food_y,thickness,thickness))
		gameDisplay.blit(img_apple2,(rand_bomb_x,rand_bomb_y,thickness,thickness))
#dzialanie weza
		snake_head =[]
		snake_head.append(lead_x)
		snake_head.append(lead_y)
		snake_list.append(snake_head)

		if len(snake_list)>snake_length:
			del snake_list[0]

		for segment in snake_list[:-1]:
			if segment==snake_head:
				gameOver=True

		snake(block_size,snake_list)
		
#punktacje
		score(snake_length-1,0)
#levele

		if snake_length-1>level_score:
			level_up()
			level_score+=3
			FPS+=3
			level+=1
			if back==True:
				back=False
			else:
				back=True
			game_loop()

		text=small_font.render("Level: "+str(level),True,grey)
		gameDisplay.blit(text,[0,30])
#		pygame.display.update()
		pygame.display.update()
#zjadanie jablek wpadanie na bomby
		if lead_x >= rand_food_x and lead_x <= rand_food_x+thickness or lead_x+block_size >= rand_food_x and lead_x + block_size <= rand_food_x+thickness:
			if lead_y >= rand_food_y and lead_y <= rand_food_y+thickness or lead_y+block_size >= rand_food_y and lead_y + block_size <= rand_food_y+thickness:
					rand_food_x,rand_food_y=food_gen()
					rand_bomb_x,rand_bomb_y=bomb_gen()
					snake_length +=1

		if lead_x >= rand_bomb_x and lead_x <= rand_bomb_x+thickness or lead_x+block_size >= rand_bomb_x and lead_x + block_size <= rand_bomb_x+thickness:
			if lead_y >= rand_bomb_y and lead_y <= rand_bomb_y+thickness or lead_y+block_size >= rand_bomb_y and lead_y + block_size <= rand_bomb_y+thickness:
				gameOver=True

		clock.tick(FPS)

	pygame.quit()
	quit()

def level_up():
	level=True
	while level:
		if back==True:
			gameDisplay.blit(img_back,(0,0))
		else:
			gameDisplay.blit(img_back2,(0,0))
		message_to_screen("Level_up",green,-100,"large")
		message_to_screen("Press C to continue",black,0,"small")
		pygame.display.update()		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					level=False


def game_intro():
	intro = True
	while intro:
		gameDisplay.blit(img_back,(0,0))
		message_to_screen("Menu",green,-150,"large")
		message_to_screen("Press 'P' to play the game",black,-100,"small")
		message_to_screen("Press 'I' to see instructions",black,-50,"small")
		message_to_screen("Press 'Q' to Quit",black,0,"small")
		message_to_screen("Press 'M' to play multiplayer game",black,50,"small")
		pygame.display.update()
	
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					game_loop()
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_i:
					instructions()
				if event.key == pygame.K_m:
					multi_game_loop()
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
#		clock.tick(15)


def instructions():
	gameDisplay.fill(white)
	message_to_screen("Singleplayer instructions",green,-150,"large")
	message_to_screen("The objective of the game is to eat apples",black,-100,"small")
	message_to_screen("The more apples you eat, the longer you get",black,-50,"small")
	message_to_screen("Multiplayer instructions",green,0,"large")
	message_to_screen("To win multiplayer you need to be the first who eats 3 apples",black, 50,"small")
	message_to_screen("If you kill yourself before, you lose",black, 100,"small")
	message_to_screen("Press 'B' to go back to MENU",black, 200,"small")
	
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_b:
					game_intro()


game_intro()