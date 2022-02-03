import pygame
from player import Player

pygame.init()

class ConnectFour:
    def __init__(self, block_size):
        self.layout = [[['O', (j,i)] if i > 0 else [' ', (j,i)] for j in range(10)] for i in range(10)]
        self.turn = 'Red'

        self.red = Player('R', block_size, self.layout)
        self.yellow = Player('Y', block_size, self.layout)

        self.circle_width = 20
        self.cooldown_counter = 0

        self.game_over = False
        self.status = 'Playing'

    def cooldown(self):
        if self.cooldown_counter > 0:
            self.cooldown_counter += 1
        if self.cooldown_counter > 15:
            self.cooldown_counter = 0

    def draw_layout(self, screen, block_size):
        screen.fill((0,128,255))

        for i, row in enumerate(self.layout):
            for j, col in enumerate(row):
                x = j * block_size
                y = i * block_size

                if col[0] == 'O':
                    rect = pygame.Rect(x, y, block_size, block_size)
                    pygame.draw.rect(screen, (0,128,255), rect, 0)

                    pygame.draw.circle(screen, (224,224,224), (x + block_size//2 ,y + block_size/2), self.circle_width)

                if col[0] == 'R':
                    rect = pygame.Rect(x, y, block_size, block_size)
                    pygame.draw.rect(screen, (0,128,255), rect, 0)

                    pygame.draw.circle(screen, (255,0,0), (x + block_size/2,y + block_size/2), self.circle_width)

                if col[0] == 'Y':
                    rect = pygame.Rect(x, y, block_size, block_size)
                    pygame.draw.rect(screen, (0,128,255), rect, 0)

                    pygame.draw.circle(screen, (255,255,51), (x + block_size/2, y + block_size/2), self.circle_width)
                    

        if self.turn == 'Red':
            pygame.draw.circle(screen, (204,0,0), ((self.red.rect.x * block_size) + block_size/2, 
                (self.red.rect.y * block_size) + block_size/2), 25, 5)
        elif self.turn == 'Yellow':
            pygame.draw.circle(screen, (204, 204, 0), ((self.yellow.rect.x * block_size) + block_size/2, 
                (self.yellow.rect.y * block_size) + block_size/2), 25, 5)

    def check_tie(self):
        for row in self.layout:
            for col in row:
                if col[0] == 'O':
                    return
        
        self.game_over = True
        self.status = "It's a tie!"

    def check_win(self):
        for row in self.layout:
            for col in row:
                    try:
                        # row yellow
                        if self.layout[col[1][1]][col[1][0]][0] == 'Y' and self.layout[col[1][1]][col[1][0] + 1][0] == 'Y' \
                            and self.layout[col[1][1]][col[1][0] + 2][0] == 'Y' and self.layout[col[1][1]][col[1][0] + 3][0] == 'Y':
                            self.game_over = True
                            self.status = 'Yellow wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'Y' and self.layout[col[1][1]][col[1][0] - 1][0] == 'Y' \
                            and self.layout[col[1][1]][col[1][0] - 2][0] == 'Y' and self.layout[col[1][1]][col[1][0] - 3][0] == 'Y':
                            self.game_over = True
                            self.status = 'Yellow wins!'
                    except:
                        pass
                    
                    try:
                        # col yellow
                        if self.layout[col[1][1]][col[1][0]][0] == 'Y' and self.layout[col[1][1] + 1][col[1][0]][0] == 'Y' \
                            and self.layout[col[1][1] + 2][col[1][0]][0] == 'Y' and self.layout[col[1][1] + 3][col[1][0]][0] == 'Y':
                            self.game_over = True
                            self.status = 'Yellow wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'Y' and self.layout[col[1][1] - 1][col[1][0]][0] == 'Y' \
                            and self.layout[col[1][1] - 2][col[1][0]][0] == 'Y' and self.layout[col[1][1] - 3][col[1][0]][0] == 'Y':
                            self.game_over = True
                            self.status = 'Yellow wins!'
                    except:
                        pass
                    
                    try:
                        #diagonals yellow
                        if self.layout[col[1][1]][col[1][0]][0] == 'Y' and self.layout[col[1][1] + 1][col[1][0] + 1][0] == 'Y' \
                            and self.layout[col[1][1] + 2][col[1][0] + 2][0] == 'Y' and self.layout[col[1][1] + 3][col[1][0] + 3][0] == 'Y':
                            self.game_over = True
                            self.status = 'Yellow wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'Y' and self.layout[col[1][1] - 1][col[1][0] - 1][0] == 'Y' \
                            and self.layout[col[1][1] - 2][col[1][0] - 2][0] == 'Y' and self.layout[col[1][1] - 3][col[1][0] - 3][0] == 'Y':
                            self.game_over = True
                            self.status = 'Yellow wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'Y' and self.layout[col[1][1] + 1][col[1][0] - 1][0] == 'Y' \
                            and self.layout[col[1][1] + 2][col[1][0] - 2][0] == 'Y' and self.layout[col[1][1] + 3][col[1][0] - 3][0] == 'Y':
                            self.game_over = True
                            self.status = 'Yellow wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'Y' and self.layout[col[1][1] - 1][col[1][0] + 1][0] == 'Y' \
                            and self.layout[col[1][1] - 2][col[1][0] + 2][0] == 'Y' and self.layout[col[1][1] - 3][col[1][0] + 3][0] == 'Y':
                            self.game_over = True
                            self.status = 'Yellow wins!'
                    except:
                        pass
                    
                    try:
                        # row red
                        if self.layout[col[1][1]][col[1][0]][0] == 'R' and self.layout[col[1][1]][col[1][0] + 1][0] == 'R' \
                            and self.layout[col[1][1]][col[1][0] + 2][0] == 'R' and self.layout[col[1][1]][col[1][0] + 3][0] == 'R':
                            self.game_over = True
                            self.status = 'Red wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'R' and self.layout[col[1][1]][col[1][0] - 1][0] == 'R' \
                            and self.layout[col[1][1]][col[1][0] - 2][0] == 'R' and self.layout[col[1][1]][col[1][0] - 3][0] == 'R':
                            self.game_over = True 
                            self.status = 'Red wins!'
                    except:
                        pass
                    
                    try:
                        # col red
                        if self.layout[col[1][1]][col[1][0]][0] == 'R' and self.layout[col[1][1] + 1][col[1][0]][0] == 'R' \
                            and self.layout[col[1][1] + 2][col[1][0]][0] == 'R' and self.layout[col[1][1] + 3][col[1][0]][0] == 'R':
                            self.game_over = True
                            self.status = 'Red wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'R' and self.layout[col[1][1] - 1][col[1][0]][0] == 'R' \
                            and self.layout[col[1][1] - 2][col[1][0]][0] == 'R' and self.layout[col[1][1] - 3][col[1][0]][0] == 'R':
                            self.game_over = True
                            self.status = 'Red wins!'
                    except:
                        pass
                    
                    try:
                        #diagonals red
                        if self.layout[col[1][1]][col[1][0]][0] == 'R' and self.layout[col[1][1] + 1][col[1][0] + 1][0] == 'R' \
                            and self.layout[col[1][1] + 2][col[1][0] + 2][0] == 'R' and self.layout[col[1][1] + 3][col[1][0] + 3][0] == 'R':
                            self.game_over = True
                            self.status = 'Red wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'R' and self.layout[col[1][1] - 1][col[1][0] - 1][0] == 'R' \
                            and self.layout[col[1][1] - 2][col[1][0] - 2][0] == 'R' and self.layout[col[1][1] - 3][col[1][0] - 3][0] == 'R':
                            self.game_over = True
                            self.status = 'Red wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'R' and self.layout[col[1][1] + 1][col[1][0] - 1][0] == 'R' \
                            and self.layout[col[1][1] + 2][col[1][0] - 2][0] == 'R' and self.layout[col[1][1] + 3][col[1][0] - 3][0] == 'R':
                            self.game_over = True
                            self.status = 'Red wins!'

                        if self.layout[col[1][1]][col[1][0]][0] == 'R' and self.layout[col[1][1] - 1][col[1][0] + 1][0] == 'R' \
                            and self.layout[col[1][1] - 2][col[1][0] + 2][0] == 'R' and self.layout[col[1][1] - 3][col[1][0] + 3][0] == 'R':
                            self.game_over = True
                            self.status = 'Red wins!'
                    except:
                        pass
 

    def update_game(self, screen, block_size):
        self.draw_layout(screen, block_size)
        self.cooldown()
        self.check_win()
        self.check_tie()

        if self.turn == 'Red':
            self.red.update(self)
        else:
            self.yellow.update(self)