import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.transform.scale(pygame.image.load('images/alienblaster.png'), ai_settings.ship_size)
        self.screen_rect = screen.get_rect()


        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def update(self):
        if self.moving_up and self.rect.y > self.screen_rect.y:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom

