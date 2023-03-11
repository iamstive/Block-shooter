import pygame
import random
import sys

all_sprites = pygame.sprite.Group()
enemy = pygame.sprite.Group()
bullet = pygame.sprite.Group()
playerg = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20))
        self.color = pygame.Color((102, 178, 255))
        self.image.fill(self.color)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(self.image, self.color, self.rect, 1)
        self.add(playerg)
    
    def move(self, evx, evy):
        if 1:
            x = evx
            y = evy
            while self.x < x and x <= 685:
                self.x += 1
                self.rect = self.rect.move(1, 0)
            while self.x > x and x <= 685:
                self.x -= 1
                self.rect = self.rect.move(-1, 0)
            while self.y < y and y <= 685 and y >= 400:
                self.y += 1
                self.rect = self.rect.move(0, 1)
            while self.y > y and y <= 685 and y >= 400:
                self.y -= 1
                self.rect = self.rect.move(0, -1)
    def shoot(self):
        Bullet(self.x, self.y)
    

class Bullet(pygame.sprite.Sprite): # падающий объект
    def __init__(self, x: int, y: int):
        super().__init__(all_sprites)
        self.image = pygame.Surface((5, 15))
        self.color = pygame.Color((204, 0, 102))
        self.image.fill(self.color)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 5, 15)
        pygame.draw.rect(self.image, self.color, self.rect, 3)
        self.add(bullet)

    def update(self):
        self.rect = self.rect.move(0, -5) # иначе продолжает падать


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.Surface((30, 30))
        self.color = pygame.Color((153, 0, 76))
        self.image.fill(self.color)
        self.rect = pygame.Rect(random.randint(10, 650), 0, 30, 30)
        pygame.draw.rect(self.image, self.color, self.rect, 3)
    
    def update(self):
        if pygame.sprite.spritecollideany(self, playerg):
            self.kill()
        elif pygame.sprite.spritecollideany(self, bullet):
            self.kill()
        else:
            self.rect = self.rect.move(0, 1)


pygame.init()
size = (700, 700)
BLACK = (0,0,0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chippin' In")
screen.fill(BLACK)
fps = 120
clock = pygame.time.Clock()

player1 = Player(110, 510)


while True:
    screen.fill("black")
    all_sprites.draw(screen)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEMOTION: # двигаем мышь - двигаем платформу
                _x = event.pos[0]
                _y = event.pos[1]
                player1.move(_x, _y)
                #print(event.pos[0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player1.shoot()
    Enemy()
    all_sprites.update()
    clock.tick(fps)
    pygame.display.flip()


