import pygame

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, comp, altura, scale, colour):
		image = pygame.Surface((comp, altura)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * comp), 0, comp, altura))
		image = pygame.transform.scale(image, (int(comp * scale), int(altura * scale)))
		image.set_colorkey(colour)

		return image