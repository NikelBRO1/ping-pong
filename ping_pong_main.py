from pygame import * 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y, player_speed,wight,height):
        super().__init__()
        self.image = trans.form.scale(image.load(player_image), (weight, height))
        self.speed - player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.imahe, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.player_speed
        if keys [K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.player_speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.u += self.speed
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
clock = time.Clock()
FPS = 60
while game:
    display.update()
    clock.tick(FPS)
