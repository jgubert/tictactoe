# TicTacToe
# Made by João Gubert
# github.com/jgubert/tictactoe.git

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.font.init()

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
info_font = pygame.font.SysFont(font_name, 24)
menu_font = pygame.font.SysFont(font_name, 36)

screen = pygame.display.set_mode((640, 480), 0, 32)

# --- Define Functions ---

def someoneWins(list):
	result = False
	# Check Line, Columm and Diagonal for Place 1
	for i in list:
		if i.position == [60,60]:
			for j in list:
				if (j.position == [180,60] or j.position == [60,180] or j.position == [180,180]) and i.player == j.player:
					for k in list:
						if (k.position == [300,60] or k.position == [60,300] or k.position == [300,300]) and j.player == k.player and i.player == k.player:
							result = True
	#Check Line for Place 4
	for i in list:
		if i.position == [60,180]:
			for j in list:
				if j.position == [180,180] and i.player == j.player:
					for k in list:
						if k.position == [300,180] and j.player == k.player:
							result = True
	#Check Line and Diagonal for Place 7
	for i in list:
		if i.position == [60,300]:
			for j in list:
				if (j.position == [180,300] or j.position == [180,180]) and i.player == j.player:
					for k in list:
						if (k.position == [300,300] or k.position == [300,60]) and j.player == k.player and k.player == i.player:
							result = True
	#Check Columm for Place 2
	for i in list:
		if i.position == [180,60]:
			for j in list:
				if j.position == [180,180] and i.player == j.player:
					for k in list:
						if k.position == [180,300] and j.player == k.player:
							result = True
	#Check Columm for Place 3
	for i in list:
		if i.position == [300,60]:
			for j in list:
				if j.position == [300,180] and i.player == j.player:
					for k in list:
						if k.position == [300,300] and j.player == k.player:
							result = True
	return result


def checkPositionFree(list, position):
	result = True
	for i in list:
		if i.position == position:
			result = False
	return result

def putElement(selection, elements):
	if checkPositionFree(elements, selection.position_px):
		if selection.player == 1:
			element_filename = './images/X.png'
			sprite_element = pygame.image.load(element_filename).convert_alpha()
		if selection.player == 2:
			element_filename = './images/O.png'
			sprite_element = pygame.image.load(element_filename).convert_alpha()

		element = Elements(sprite_element, selection.position_px, selection.player)
		elements.append(element)
	else:
		if selection.player == 1:
			selection.player = 2
		else:
			selection.player = 1

def printElements(list):
	print(len(list))
	for i in list:
		print(i.position)
		i.printElement()


# --- Classes ---

class Elements():
	def __init__(self, sprite_element,position, player):
		self.sprite = sprite_element
		self.position = position
		self.player = player

	def printElement(self):
		screen.blit(self.sprite,(self.position))
		

class SelectionSquare():
	def __init__(self, sprite_square):
		self.position = 5
		self.position_px = [180,180]
		self.sprite = sprite_square
		self.player = 1

	def updatePositionPx(self):
		if self.position == 1:
			self.position_px = [60,60]
		if self.position == 2:
			self.position_px = [180,60]
		if self.position == 3:
			self.position_px = [300,60]
		if self.position == 4:
			self.position_px = [60,180]
		if self.position == 5:
			self.position_px = [180,180]
		if self.position == 6:
			self.position_px = [300,180]
		if self.position == 7:
			self.position_px = [60,300]
		if self.position == 8:
			self.position_px = [180,300]
		if self.position == 9:
			self.position_px = [300,300]

	def printSelectionSquare(self):
		self.updatePositionPx()
		screen.blit(self.sprite,(self.position_px))

	
	def moveSelectionSquare(self,key_pressed, key_up, elements):
		if key_up == 1:
			if key_pressed == "up":
				if self.position > 3:
					self.position = self.position - 3
			if key_pressed == "down":
				if self.position < 7:
					self.position = self.position + 3
			if key_pressed == "left":
				if self.position != (1 or 4 or 7):
					self.position = self.position - 1
			if key_pressed == "right":
				if self.position != (3 or 6 or 9):
					self.position = self.position + 1
			if key_pressed == "space":
				putElement(self, elements)
				if self.player == 1:
					self.player = 2
				else:
					self.player = 1
				

# --- Loading Images ---

background_filename = './images/bg.png'
background = pygame.image.load(background_filename).convert()
selection_square_filename = './images/selectionsquare.png'
selection_square_sprite = pygame.image.load(selection_square_filename).convert_alpha()

pygame.display.set_caption('TicTacToe')
clock = pygame.time.Clock()

text_info = menu_font.render(('Press any button to continue.'),1,(0,0,0))
screenLock = 1

while screenLock == 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            screenLock = 0

    screen.blit(background, (0, 0))
    screen.blit(text_info,(20,150))
    pygame.display.update()


background_filename = './images/bg2.png'
background = pygame.image.load(background_filename).convert()

gameInit = 1
selection_square = SelectionSquare(selection_square_sprite)

elements = []



while gameInit == 1:


	key_up = 1
	key_pressed = 0
	ticks_time = 30

	screen.blit(background, (0, 0))
	#pygame.display.update()


	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYUP:
			key_up = 1
		if event.type == KEYDOWN:
			if key_up == 1:
				key_pressed = pygame.key.name(event.key)
				selection_square.moveSelectionSquare(key_pressed, key_up, elements)
		if not ticks_time:
			ticks_time = 30
		else:
			ticks_time -= 1


	selection_square.printSelectionSquare()

	printElements(elements)

	if someoneWins(elements):
		if selection_square.player == 2:
			text_info = menu_font.render(('Player 1 Wins'),1,(0,0,0))
		if selection_square.player == 1:
			text_info = menu_font.render(('Player 2 Wins'),1,(0,0,0))
		
		screenLock = 1

		while screenLock == 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					exit()
				if event.type == KEYDOWN:
					screenLock = 0

			screen.blit(text_info,(20,150))
			pygame.display.update()
	

	time_passed = clock.tick(30)
	pygame.display.update()


exit()



