import pygame
import random
import time
import sys

all_sprites = pygame.sprite.Group()
edge = pygame.sprite.Group()
bullet = pygame.sprite.Group()
playerg = pygame.sprite.Group()
enemy = pygame.sprite.Group()


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
        Bullet(self.x+7, self.y+1)


class Bullet(pygame.sprite.Sprite): 
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
        self.rect = self.rect.move(0, -5)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.Surface((30, 30))
        self.color = pygame.Color((153, 0, 76))
        self.image.fill(self.color)
        self.rect = pygame.Rect(random.randint(10, 650), 0, 30, 30)
        pygame.draw.rect(self.image, self.color, self.rect, 3)
        self.add(enemy)
    
    def update(self):
        global DEFEAT, SCORE
        global enemy_alive
        global HP
        if pygame.sprite.spritecollideany(self, playerg):
            HP -= 1
            self.kill()
            enemy_alive = True
        elif pygame.sprite.spritecollideany(self, bullet):
            self.kill()
            enemy_alive = True
            SCORE += 1
            if SCORE %10 == 0 and SCORE != 0:
                HP+=1
        elif pygame.sprite.spritecollideany(self, edge):
            self.kill()
            enemy_alive = False
            DEFEAT = True
        else:
            self.rect = self.rect.move(0, 1)


class Edge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.Surface((700, 0))
        self.color = pygame.Color((0, 0, 0))
        self.image.fill(self.color)
        self.rect = pygame.Rect(0, 700, 700, 10)
        pygame.draw.rect(self.image, self.color, self.rect, 3)
        pygame.draw.line(screen, (0, 255, 0), (0, 400), (700, 400), 1)
        self.add(edge)


def defeat_sc(screen):
    for i in all_sprites:
        i.kill
    screen.fill((0, 0, 0))
    u = 100
    font = pygame.font.Font(None, u)
    u -= 70
    text = font.render("DEFEAT", True, (153, 0, 76))
    text1 = font.render(f"Score: {SCORE}", True, (0, 102, 204))
    screen.blit(text, (700/len("DEFEAT"), 350))
    screen.blit(text1, (700/len(f"Score: {SCORE}"), 420))


def score(screen):
    font = pygame.font.Font(None, 40)
    text = font.render(f"Score: {SCORE}", True, (0, 102, 204))
    text1 = font.render(f"HP: {HP}", True, (0, 102, 204))
    screen.blit(text, (0, 0))
    screen.blit(text1, (600, 0))


def start_sc(screen):
    font = pygame.font.SysFont('kacstbook', 30)
    j, l = 3, 100
    s_text = [
        "Hello, player!",
        "You're playing my game.",
        "So, you need to know rules, don't you?",
        "Here they are:",
        "You can shoot the red squares.",
        "Five score points and you get one more HP.",
        "You need HP to destroy red squares using your body.",
        "No HP - you're defeated.",
        "If you miss a red square - you're defeated too.",
        "LMB - start game."
    ]
    for i in s_text:
        screen.blit(font.render(i, True, (0, 102, 204)), (j, l))
        l+=40


pygame.init()
size = (700, 700)
BLACK = (0,0,0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chippin' In")
screen.fill(BLACK)
fps = 120
clock = pygame.time.Clock()


player1 = Player(110, 510)
DEFEAT = False
SCORE = 0
HP = 5
START = True


for i in range(random.randint(5, 5)): 
    Enemy()
enemy_spawn = False
enemy_alive = False


while True:
    screen.fill(BLACK)
    while START:
        start_sc(screen)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    START = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        START = False
        pygame.display.flip()
    all_sprites.draw(screen)
        
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION: 
                _x = event.pos[0]
                _y = event.pos[1]
                player1.move(_x, _y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player1.shoot()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
    Edge()
    score(screen)

    if not enemy_spawn:
        Enemy()
        enemy_spawn = True
    if enemy_alive:
        enemy_spawn = False
        enemy_alive = False
    if HP == 0:
        DEFEAT = True
    if DEFEAT:
        defeat_sc(screen)
        pygame.mouse.set_visible(True)

    all_sprites.update()
    clock.tick(fps)
    pygame.display.flip()




