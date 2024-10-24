#import libraries
import pygame
import random
import os
from pygame import mixer
from spritesheet import SpriteSheet

#inicializar jogo e a musica
mixer.init()
pygame.init()

#tamanho da tela 
COMP_TELA = 400
ALTURA_TELA = 600

#criar a tela
tela = pygame.display.set_mode((COMP_TELA, ALTURA_TELA))
pygame.display.set_caption('Jumpy')

#definir game rate
clock = pygame.time.Clock()
FPS = 60

#carregar musica e sons
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0.0)
pulo_fx = pygame.mixer.Sound('assets/jump.mp3')
pulo_fx.set_volume(0.5)
morte_fx = pygame.mixer.Sound('assets/death.mp3')
morte_fx.set_volume(0.5)


#variaveis
SCROLL_THRESH = 200
GRAVIDADE = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0

if os.path.exists('score.txt'):
	with open('score.txt', 'r') as file:
		high_score = int(file.read())
else:
	high_score = 0

#definir cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
PANEL = (153, 217, 234)

#definir fontes
font_pequena = pygame.font.SysFont('Lucida Sans', 20)
font_grande = pygame.font.SysFont('Lucida Sans', 24)

#Carregar imagens
imageog = pygame.image.load('assets/pulo.png').convert_alpha()
jumpy_image = pygame.transform.scale_by(imageog,4)
bg_image = pygame.image.load('assets/bg.png').convert_alpha()
platform_image = pygame.image.load('assets/tronco.png').convert_alpha()
gameoverOG = pygame.image.load ("assets/gameover.png").convert_alpha()
gameover = pygame.transform.scale( gameoverOG, (COMP_TELA, ALTURA_TELA))
menuOg = pygame.image.load ("assets/menu.png").convert_alpha()
imgMenu = pygame.transform.scale (menuOg, (COMP_TELA, ALTURA_TELA))
#funcoes pra colocar texto na tela
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	tela.blit(img, (x, y))

#funcao pra colocar as infos na tela
def draw_panel():
	pygame.draw.rect(tela, PANEL, (0, 0, COMP_TELA, 30))
	pygame.draw.line(tela, BRANCO, (0, 30), (COMP_TELA, 30), 2)
	draw_text('SCORE: ' + str(score), font_pequena, BRANCO, 0, 0)


#funcao pra desenhar o background
def draw_bg(bg_scroll):
	tela.blit(bg_image, (0, 0 + bg_scroll))
	tela.blit(bg_image, (0, -600 + bg_scroll))

#classe do player
class Player():
	def __init__(self, x, y):
		self.image = pygame.transform.scale(jumpy_image, (45, 45))
		self.comp = 25
		self.altura = 40
		self.rect = pygame.Rect(0, 0, self.comp, self.altura)
		self.rect.center = (x, y)
		self.vel_y = 0
		self.flip = False

	def move(self):
		#resetar as variaveis
		scroll = 0
		dx = 0
		dy = 0

		#processar teclas
		key = pygame.key.get_pressed()
		if key[pygame.K_a]:
			dx = -10
			self.flip = True
		if key[pygame.K_d]:
			dx = 10
			self.flip = False

		#GRAVIDADE
		self.vel_y += GRAVIDADE
		dy += self.vel_y

		# fazer com que o player nao saia da tela
		if self.rect.left + dx < 0:
			dx = -self.rect.left
		if self.rect.right + dx > COMP_TELA:
			dx = COMP_TELA - self.rect.right


		#colisoes com a plataforma
		for platform in platform_group:
			#colisoes no eixo y
			if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.comp, self.altura):
				#checkar se está acima da plataforma
				if self.rect.bottom < platform.rect.centery:
					if self.vel_y > 0:
						self.rect.bottom = platform.rect.top
						dy = 0
						self.vel_y = -20
						pulo_fx.play()

		#checkar se o player foi pra cima da tela
		if self.rect.top <= SCROLL_THRESH:
			#se o player esta pulando
			if self.vel_y < 0:
				scroll = -dy

		#atualizar a posiçao do retangulo
		self.rect.x += dx
		self.rect.y += dy + scroll

		#atualizar mask
		self.mask = pygame.mask.from_surface(self.image)

		return scroll

	def draw(self):
		tela.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))

#platforma classe
class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, comp, moving):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(platform_image, (comp, 10))
		self.moving = moving
		self.move_counter = random.randint(0, 50)
		self.direction = random.choice([-1, 1])
		self.speed = random.randint(1, 2)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self, scroll):
		#movimentar a plataforma
		if self.moving == True:
			self.move_counter += 1
			self.rect.x += self.direction * self.speed

		#mudar a plataforma de lado
		if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > COMP_TELA:
			self.direction *= -1
			self.move_counter = 0

		#atualizar a posicao 
		self.rect.y += scroll

		#verificar se a plataforma saiu da tela
		if self.rect.top > ALTURA_TELA:
			self.kill()

#player instancia
jumpy = Player(COMP_TELA // 2, ALTURA_TELA - 150)

#criar grupos
platform_group = pygame.sprite.Group()

#criar plataforma inicial
platform = Platform(COMP_TELA // 2 - 50, ALTURA_TELA - 50, 100, False)
platform_group.add(platform)

#game loop
run = True
menu = True

score = 0
scroll = 0
fade_counter = 0
platform_group.empty()
while run:

	clock.tick(FPS)
	if menu == True:
		tela.blit(imgMenu,(0,0))
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
					#reposition jumpy
					jumpy.rect.center = (COMP_TELA // 2, ALTURA_TELA - 150)
					#create starting platform
					platform = Platform(COMP_TELA // 2 - 50, ALTURA_TELA - 50, 100, False)
					platform_group.add(platform)
					menu = False
					print(game_over)
					 
	else:
		if game_over == False:
			scroll = jumpy.move()

			#desenhar background
			bg_scroll += scroll
			if bg_scroll >= 600:
				bg_scroll = 0
			draw_bg(bg_scroll)

			#generar platformas
			if len(platform_group) < MAX_PLATFORMS:
				p_w = random.randint(40, 60)
				p_x = random.randint(0, COMP_TELA - p_w)
				p_y = platform.rect.y - random.randint(80, 120)
				p_type = random.randint(1, 2)
				if p_type == 1 and score > 500:
					p_moving = True
				else:
					p_moving = False
				platform = Platform(p_x, p_y, p_w, p_moving)
				platform_group.add(platform)

			#atualizar platforms
			platform_group.update(scroll)

			#atualizar score
			if scroll > 0:
				score += scroll

			#desenhar linha no record anterior
			pygame.draw.line(tela, BRANCO, (0, score - high_score + SCROLL_THRESH), (COMP_TELA, score - high_score + SCROLL_THRESH), 3)
			draw_text('HIGH SCORE', font_pequena, BRANCO, COMP_TELA - 130, score - high_score + SCROLL_THRESH)

			#desenhar sprites
			platform_group.draw(tela)
			jumpy.draw()

			#desenhar panel
			draw_panel()

			#checkar game over
			if jumpy.rect.top > ALTURA_TELA:
				game_over = True
				morte_fx.play()

		else:
			if fade_counter < COMP_TELA:
				fade_counter += 5
				for y in range(0, 6, 2):
					pygame.draw.rect(tela, PRETO, (0, y * 100, fade_counter, 100))
					pygame.draw.rect(tela, PRETO, (COMP_TELA - fade_counter, (y + 1) * 100, COMP_TELA, 100))
			else:
				
				tela.blit(gameover,(0,0))
				draw_text('SCORE: ' + str(score), font_grande, BRANCO, 130, 110)
				#atualizar high score
				if score > high_score:
					high_score = score
					with open('score.txt', 'w') as file:
						file.write(str(high_score))
				key = pygame.key.get_pressed()
				if key[pygame.K_SPACE]:
					#resetar variaveis
					game_over = False
					score = 0
					scroll = 0
					fade_counter = 0
					#reposition jumpy
					jumpy.rect.center = (COMP_TELA // 2, ALTURA_TELA - 150)
			
					#reset platforms
					platform_group.empty()
					#create starting platform
					platform = Platform(COMP_TELA // 2 - 50, ALTURA_TELA - 50, 100, False)
					platform_group.add(platform)


	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#update high score
			if score > high_score:
				high_score = score
				with open('score.txt', 'w') as file:
					file.write(str(high_score))
			run = False


	#update display window
	pygame.display.update()



pygame.quit()

