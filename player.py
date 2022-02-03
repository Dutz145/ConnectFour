import pygame

pygame.init()

class Player:
    def __init__(self, color, block_size, layout):
        self.image = pygame.Surface((block_size, block_size))
        self.rect = self.image.get_rect(topleft = (0,len(layout) - 1))
        self.color = color

    def move(self, game_obj):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.rect.x < len(game_obj.layout[0]) - 1 and game_obj.cooldown_counter == 0:
            game_obj.cooldown_counter = 1
            self.rect.x += 1

        if keys[pygame.K_LEFT] and self.rect.x > 0 and game_obj.cooldown_counter == 0:
            game_obj.cooldown_counter = 1
            self.rect.x -= 1

        if keys[pygame.K_UP] and self.rect.y > 1 and game_obj.cooldown_counter == 0:
            game_obj.cooldown_counter = 1
            self.rect.y -= 1

        if keys[pygame.K_DOWN] and self.rect.y < len(game_obj.layout) - 1 and game_obj.cooldown_counter == 0:
            game_obj.cooldown_counter = 1
            self.rect.y += 1


        if keys[pygame.K_SPACE] and game_obj.cooldown_counter == 0:
            game_obj.cooldown_counter = 1

            changed = False
            for row in game_obj.layout:
                for col in row:
                    if col[1] == (self.rect.x, self.rect.y) and col[0] == 'O':
                        if col[1][1] == len(game_obj.layout) - 1 or game_obj.layout[self.rect.y + 1][self.rect.x][0] != 'O':
                            col[0] = self.color
                            changed = True
                            break

    
            if changed:
                if self.color == 'R':
                    game_obj.turn = 'Yellow'
                    
                elif self.color == 'Y':
                    game_obj.turn = 'Red'


    def update(self, game_obj):
        self.move(game_obj)