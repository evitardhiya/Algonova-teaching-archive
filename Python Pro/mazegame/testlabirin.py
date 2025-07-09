from pygame import *
class gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) # type: ignore

class Player(gamesprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        gamesprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if char.rect.x <= win_width-80 and char.x_speed > 0 or char.rect.x >= 0 and char.x_speed < 0:
            self.rect.x += self.x_speed
        
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        if char.rect.y <= win_width- 80 and char.y_speed > 0 or char.rect.y >= 0 and char.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)

win_width = 700
win_height = 500
display.set_caption("Maze")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load('back.jpg'), (700, 700))

w1 = gamesprite('platform2.png', win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = gamesprite('platform2_v.png', 370, 100, 50, 400)

barriers = sprite.Group()
barriers.add(w1)
barriers.add(w2)

char = Player('hero.png', 5, win_height - 80, 80, 80, 0, 0)
monster = gamesprite('pac-1.png', win_width - 80, 180, 80, 80)
final_sprite = gamesprite('cyborg.png', win_width - 85, win_height - 100, 80, 80)

finish=False
run=True
while run:
    time.delay(50)
    window.blit(back, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                char.speed_x = -10
            elif e.key == K_RIGHT:
                char.speed_x = 10
            elif e.key == K_UP:
                char.speed_y = -10
            elif e.key == K_DOWN:
                char.speed_y = 10
        elif e.type == KEYUP:
            if e.key== K_LEFT:
                char.speed_x = 0
            elif e.key == K_RIGHT:
                char.speed_x = 0
            elif e.key == K_UP:
                char.speed_y = 0
            elif e.key == K_DOWN:
                char.speed_y = 0

    if not finish:
        window.blit(back, (0, 0))
        barriers.draw(window)

        monster.reset()
        final_sprite.reset()
        char.reset()
        char.update()

        if sprite.collide_rect(char, monster):
            finish = True
            img = image.load('gameover.png')
            d = img.get_width() / img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

        if sprite.collide_rect(char, final_sprite):
            finish = True
            img = image.load('thumb.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

    display.update()