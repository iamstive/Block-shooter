import os
import sys
import pygame
from screeninfo import get_monitors
import time
from random import randint
from DataBase import Map


class Wall1(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 30))
        self.image.fill('cyan')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])

    def update(self, xy, ox, colligecar, t=False, d_mode=False):
        global cox, coy, gx, gy, chpx, chpy, delete_mode, sprites_xy, oriental_xy
        if not d_mode:
            self.rect.center = (self.rect.center[0] - xy[0], self.rect.center[1] - xy[1])
            collide = self.rect.colliderect(collidecar)
            if collide and not t and not d_mode:
                self.rect.center = (self.rect.center[0] + xy[0], self.rect.center[1])
                collide = self.rect.colliderect(colligecar)
                if collide:
                    coy = True
                self.rect.center = (self.rect.center[0] - xy[0], self.rect.center[1] + xy[1])
                collide = self.rect.colliderect(colligecar)
                if collide:
                    cox = True
                self.rect.center = (self.rect.center[0], self.rect.center[1] - xy[1])
                if not cox and not coy:
                    cox = True
                    coy = True
        if cox and t:
            gx = 0
            chpx = 0
        if coy and t:
            gy = 0
            chpy = 0

        if d_mode:
            collide = self.rect.collidepoint(ox)
            if collide:
                q = self.rect.center
                try:
                    sprites_xy.remove((1, *q))
                except:
                    try:
                        sprites_xy.remove((2, *q))
                    except:
                        print(1, *q)
                self.kill()
                delete_mode = False


class Wall2(Wall1):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 100))
        self.image.fill('cyan')
        self.rect = self.image.get_rect()
        self.rect.center = (xy[0], xy[1])


class Money(pygame.sprite.Sprite):
    def __init__(self, limit):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.center = (randint(limit[0], limit[1]), randint(limit[2], limit[3]))

    def update(self, xy, ox, colligecar, t=False, d_mode=False):
        global money_limit, money_count, ice_xy, oriental_xy
        if not d_mode:
            ice_xy = (ice_xy[0] - xy[0], ice_xy[1] - xy[1])
            money_limit[0] -= xy[0] + oriental_xy[0] % 5
            money_limit[1] -= xy[0] + oriental_xy[0] % 5
            money_limit[2] -= xy[1] + oriental_xy[1] % 5
            money_limit[3] -= xy[1] + oriental_xy[0] % 5
            self.rect.center = (self.rect.center[0] - xy[0], self.rect.center[1] - xy[1])
            collide = collide = self.rect.colliderect(collidecar)
            if collide:
                self.kill()
                money_count += 1
                all_sprites.add(Money(money_limit))


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def mobileobgadd(last):
    screen.fill((0, 0, 0))
    screen.blit(ice_fon, (ice_xy[0] % (ex + 1), ice_xy[1] % (ey + 1)))
    screen.blit(ice_fon, (ice_xy[0] % (ex + 1) - ex, ice_xy[1] % (ey + 1) - ey))
    screen.blit(ice_fon, (ice_xy[0] % (ex + 1), ice_xy[1] % (ey + 1) - ey))
    screen.blit(ice_fon, (ice_xy[0] % (ex + 1) - ex, ice_xy[1] % (ey + 1)))
    if last == car90 or last == car270:
        screen.blit(last, (px, py))
    elif last == car0 or last == car180:
        screen.blit(last, (px + 50, py - 50))
    else:
        screen.blit(last, (px, py - 50))


xy = [0, 0]
ox = [0, 0]
s = str(get_monitors())
running = True
chpx = 0
chpy = 0
ex = int(s[25:29])
ey = int(s[38:42])
gx = 0.0
gy = 0.0
px = ex // 2 - 100
py = ey // 2 - 50
collidecar = pygame.Rect(0, 0, ex // 27, ey // 15)
collidecar.center = (ex // 2, ey // 2)
car = load_image('lada0.png')
car = pygame.transform.scale(car, (ex//19.2, ey//5.4))
car0 = car
car45 = pygame.transform.rotate(car, 45)
car90 = pygame.transform.rotate(car, 90)
car135 = pygame.transform.rotate(car, 135)
car180 = pygame.transform.rotate(car, 180)
car225 = pygame.transform.rotate(car, 225)
car270 = pygame.transform.rotate(car, 270)
car315 = pygame.transform.rotate(car, 315)
ice_fon = load_image('ice_main.png')
ice_fon = pygame.transform.scale(ice_fon, (ex, ey))
db = Map()
ice_xy = [0, 0]
last = car90
all_sprites = pygame.sprite.Group()
delete_mode = False
horisont = True
vertical = False
up = False
down = False
left = False
right = False
render1 = False
render2 = True
t1 = 0.005
colision = list()
oriental_xy = [0, 0]
money_limit = [30, 3450, 30, 2760]
all_sprites.add(Money(money_limit))
time_start = time.time()
money_count = 0
count = 0
sprites_xy = []
enemylist = []

screen = pygame.display.set_mode((ex, ey))
clock = pygame.time.Clock()
pygame.init()
font1 = pygame.font.Font(pygame.font.get_default_font(), 36)
font2 = pygame.font.Font(pygame.font.get_default_font(), 36)
font3 = pygame.font.Font(pygame.font.get_default_font(), 36)
pygame.display.set_caption('Cold Road')

for i in db.out_all_blocks():
    if i[0] == 1:
        wall = Wall1((i[1], i[2]))
        all_sprites.add(wall)

    if i[0] == 2:
        wall = Wall2((i[1], i[2]))
        all_sprites.add(wall)
    sprites_xy.append((i[0], i[1], i[2]))
count = len(sprites_xy)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] - mpos[0] % 5, mpos[1] - mpos[1] % 5)
        if event.type == pygame.QUIT:
            for i in range(len(sprites_xy)):
                sprites_xy[i] = (sprites_xy[i][0], sprites_xy[i][1] + oriental_xy[0], sprites_xy[i][2] + oriental_xy[1])
            db.delete_blocks()
            for i in sprites_xy:
                db.add_block(*i, count)
                count += 1
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_1:
                if vertical:
                    vertical = False
                    horisont = True
                    render2 = True
                    render1 = False
            if event.key == pygame.K_2:
                if horisont:
                    horisont = False
                    vertical = True
                    render2 = False
                    render1 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_s:
                down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ox = mpos
                if vertical:
                    wall = Wall2((ox[0] - oriental_xy[0] % 5, ox[1] - oriental_xy[1] % 5))
                    all_sprites.add(wall)
                    sprites_xy.append((2, ox[0] - oriental_xy[0] % 5 + oriental_xy[0], ox[1] - oriental_xy[1] % 5 +
                                       oriental_xy[1], count))
                    count += 1
                if horisont:
                    wall = Wall1((ox[0] - oriental_xy[0] % 5, ox[1] - oriental_xy[1] % 5))
                    all_sprites.add(wall)
                    sprites_xy.append((1, ox[0] - oriental_xy[0] % 5 + oriental_xy[0], ox[1] - oriental_xy[1] % 5 +
                                       oriental_xy[1], count))
                    count += 1
            if event.button == 3:
                delete_mode = True
                ox = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                delete_mode = False

    t2 = time.time()
    chpx += abs(t1 - t2)*50*(int(right)-int(left))
    gx += (int(right)-int(left))*abs(t1 - t2)*10
    chpy += abs(t1 - t2)*(int(down)-int(up))
    gy += (int(down)-int(up))*abs(t1 - t2)*10
    t1 = time.time()
    if chpx > 0 and chpy > 0:
        last = car45
        mobileobgadd(last)
    elif chpx > 0 and chpy == 0:
        last = car90
        mobileobgadd(last)

    elif chpy < 0 < chpx:
        last = car135
        mobileobgadd(last)

    elif chpx == 0 and chpy < 0:
        last = car180
        mobileobgadd(last)

    elif chpx < 0 and chpy < 0:
        last = car225
        mobileobgadd(last)

    elif chpx < 0 and chpy == 0:
        last = car270
        mobileobgadd(last)

    elif chpx < 0 < chpy:
        last = car315
        mobileobgadd(last)

    elif chpx == 0 and chpy > 0:
        last = car
        mobileobgadd(last)
    else:
        mobileobgadd(last)
    if (chpx + gx)*ex/1920 >= 1 or (chpx + gx)*ex/1920 <= -1:
        xy[0] = int(chpx + gx)
        chpx = 0

    if (chpy + gy)*ey/1080 >= 1 or (chpy + gy)*ey/1080 <= -1:
        xy[1] = int(chpy + gy)
        chpy = 0
    if not up and not down:
        chpy = 0
    if not left and not right:
        chpx = 0

    if gx > 0.05:
        gx -= 0.04*ex/1920
    elif gx < -0.05:
        gx += 0.04*ex/1920
    else:
        gx *= 0.95*ex/1920

    if gy > 0.05:
        gy -= 0.04*ey/1080
    elif gy < -0.05:
        gy += 0.04*ey/1080
    else:
        gy *= 0.95*ey/1080

    if delete_mode:
        all_sprites.update(xy, ox, collidecar, False, True)
    all_sprites.draw(screen)
    cox = False
    coy = False
    all_sprites.update(xy, ox, collidecar)
    if cox:
        all_sprites.update((xy[0]*-1, 0), ox, collidecar, True)
    if coy:
        all_sprites.update((0, xy[1]*-1), ox, collidecar, True)
    if render2:
        sqrt_vert = pygame.Surface((100, 30))
        sqrt_vert.fill((0, 255, 255))
        sqrt_vert.set_alpha(150)
        screen.blit(sqrt_vert, ((mpos[0] - oriental_xy[0] % 5) - 50, (mpos[1] - oriental_xy[1] % 5) - 15))
    if render1:
        sqrt_vert = pygame.Surface((30, 100))
        sqrt_vert.fill((0, 255, 255))
        sqrt_vert.set_alpha(150)
        screen.blit(sqrt_vert, ((mpos[0] - oriental_xy[0] % 5) - 15, (mpos[1] - oriental_xy[1] % 5) - 50))

    time_now = time.time()
    t = font1.render(f'Time: {round(time_now - time_start)}', True, 'red')
    screen.blit(t, dest=(10, 10))
    m = font2.render(f'Money collected: {money_count}', True, 'yellow')
    screen.blit(m, dest=(300, 10))
    oxoy = font3.render(f'{ice_xy}', True, 'yellow')
    screen.blit(oxoy, dest=(800, 10))

    oriental_xy[0] += xy[0]
    oriental_xy[1] += xy[1]
    for i in range(len(sprites_xy)):
        sprites_xy[i] = (sprites_xy[i][0], sprites_xy[i][1] - xy[0], sprites_xy[i][2] - xy[1])
    xy = [0, 0]
    pygame.display.flip()
    pygame.display.update()
print(*sprites_xy)
