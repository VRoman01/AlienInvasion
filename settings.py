class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (30, 230, 230)

        # Ship settings
        self.ship_speed_factor = 0.5
        self.ship_size = (50, 70)
        self.ship_limit = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
