from settings import *
import pygame
import math


bullets1 = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
sh = pygame.sprite.Group()
sv = pygame.sprite.Group()
ba = pygame.sprite.Group()
powerUp = pygame.sprite.Group()
targets = pygame.sprite.Group()
players = pygame.sprite.Group()
wall = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


class originaltank():
    def __init__(self, x, y):
        self.posx = x * tile
        self.posy = y * tile
        self.vel = 5
        self.velbal = 10
        self.escudo = 1

    def getposx(self):
            return self.posx

    def getposy(self):
            return self.posy

    def getvel(self):
            return self.vel

    def getvelbal(self):
            return self.velbal

    def getescudo(self):
            return self.escudo

class Player(pygame.sprite.Sprite, originaltank):
    def __init__(self, x, y, img, j):
        pygame.sprite.Sprite.__init__(self)
        originaltank.__init__(self, x, y)
        self.jugador = j
        self.image_orig = pygame.transform.scale(img, (60, 60))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 0
        self.speedy = 0
        self.rot = 0
        self.rot_speed = 22.5
        self.last_update_rot = pygame.time.get_ticks()
        self.score = 0
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tile
        self.rect.y = y * tile
        self.vel = 5
        self.escudo = 1
        self.vel_bala = 10

    def res(self):
        self.rect.x = super(Player, self).getposx()
        self.rect.y = super(Player, self).getposy()
        self.vel = super(Player, self).getvel()
        self.vel_bala =  super(Player, self).getvelbal()
        self.escudo =  super(Player, self).getescudo()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        if now - self.last_update_rot > 50:
            self.last_update_rot = now
            if self.jugador == 2:
                if keystate[pygame.K_LEFT]:
                    avanzarsnd.play()
                    self.rot = (self.rot + self.rot_speed) % 360
                    new_image = pygame.transform.rotate(self.image_orig, self.rot)
                    old_center = self.rect.center
                    self.image = new_image
                    self.image = new_image
                    self.rect = self.image.get_rect()
                    self.rect.center = old_center
                if keystate[pygame.K_RIGHT]:
                    avanzarsnd.play()
                    self.rot = (self.rot - self.rot_speed) % 360
                    new_image = pygame.transform.rotate(self.image_orig, self.rot)
                    old_center = self.rect.center
                    self.image = new_image
                    self.image = new_image
                    self.rect = self.image.get_rect()
                    self.rect.center = old_center
                if keystate[pygame.K_UP]:
                    avanzarsnd.play()
                    self.speedx = self.vel * math.cos(self.rot * math.pi / 180)
                    self.speedy = self.vel * -math.sin(self.rot * math.pi / 180)
                if keystate[pygame.K_DOWN]:
                    avanzarsnd.play()
                    self.speedx = -self.vel * math.cos(self.rot * math.pi / 180)
                    self.speedy = self.vel * math.sin(self.rot * math.pi / 180)

            if self.jugador == 1:
                if keystate[pygame.K_a]:
                    avanzarsnd.play()
                    self.rot = (self.rot + self.rot_speed) % 360
                    new_image = pygame.transform.rotate(self.image_orig, self.rot)
                    old_center = self.rect.center
                    self.image = new_image
                    self.image = new_image
                    self.rect = self.image.get_rect()
                    self.rect.center = old_center
                if keystate[pygame.K_d]:
                    avanzarsnd.play()
                    self.rot = (self.rot - self.rot_speed) % 360
                    new_image = pygame.transform.rotate(self.image_orig, self.rot)
                    old_center = self.rect.center
                    self.image = new_image
                    self.image = new_image
                    self.rect = self.image.get_rect()
                    self.rect.center = old_center
                if keystate[pygame.K_w]:
                    avanzarsnd.play()
                    self.speedx = self.vel * math.cos(self.rot * math.pi / 180)
                    self.speedy = self.vel * -math.sin(self.rot * math.pi / 180)
                if keystate[pygame.K_s]:
                    avanzarsnd.play()
                    self.speedx = -self.vel * math.cos(self.rot * math.pi / 180)
                    self.speedy = self.vel * math.sin(self.rot * math.pi / 180)

        self.tx = self.rect.x
        self.rect.x += self.speedx
        hits = pygame.sprite.spritecollide(self, wall, False)
        if hits:
            if self.speedx > 0:
                self.x = self.tx #hits[0].rect.left - self.rect.width
            if self.speedx < 0:
                self.x = hits[0].rect.right
            self.speedx = 0
            self.rect.x = self.x

        self.ty = self.rect.y
        self.rect.y += self.speedy
        hits = pygame.sprite.spritecollide(self, wall, False)
        if hits:
            if self.speedy > 0:
                self.y = self.ty #hits[0].rect.top - self.rect.height
            if self.speedy < 0:
                self.y = hits[0].rect.bottom
            self.speedy = 0
            self.rect.y = self.y

        if self.rect.right > largo:
            self.rect.right = largo
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > alto:
            self.rect.bottom = alto

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.rot, self.vel_bala)
        all_sprites.add(bullet)
        if self.jugador == 1:
            bullets1.add(bullet)
        else:
            bullets2.add(bullet)

#para break the targets
class target(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(tar, (30, 30))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tile
        self.rect.y = y * tile

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, ang, vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rot = ang
        self.rect.centery = y + 25 * -math.sin(self.rot * math.pi / 180)
        self.rect.centerx = x + 25 * math.cos(self.rot * math.pi / 180)
        self.speed = vel


    def update(self):
        self.rect.y += self.speed * -math.sin(self.rot * math.pi / 180)
        self.rect.x += self.speed * math.cos(self.rot * math.pi / 180)
        if (self.rect.bottom > alto) or (self.rect.top < 0) or (self.rect.left > largo) or (self.rect.right < 0):
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(wa, (tile, tile))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tile
        self.rect.y = y * tile

class velup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(S, (tile, tile))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tile
        self.rect.y = y * tile

class velBup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet, (tile, tile))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tile
        self.rect.y = y * tile

class defup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(shield, (tile, tile))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tile
        self.rect.y = y * tile